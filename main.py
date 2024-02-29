from PIL import Image
import os
import random


def generate_path():
    path = {}

    path["faces"] = random.randint(1, 8)
    if random.uniform(0, 1) < 0.9:
        path["tops"] = random.randint(1, 7)
    if random.uniform(0, 1) < 0.75:
        path["eyewear"] = random.randint(1, 4)
    if random.uniform(0, 1) < 0.3:
        path["mouth"] = random.randint(1, 2)
    if random.uniform(0, 1) < 0.5:
        path["accessories"] = random.randint(1, 2)

    return path


def combine_layers(layers, bg_path, output_path):
    combined = Image.open(bg_path).convert("RGBA")
    for layer, val in layers.items():
        image = Image.open(f"images/{layer}/{val}.png").convert("RGBA")
        combined = Image.alpha_composite(combined, image)
    combined.save(output_path)


def combine_images():
    im_width, im_heigth = 48, 48
    columns, rows = 60, 40

    width = columns * im_width
    height = rows * im_heigth
    combined_images = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    for i in range(1, columns * rows + 1):
        c = (i - 1) % columns
        r = (i - 1) // columns
        paste_position = (c * im_width, r * im_heigth)

        image = Image.open(f"outputs/PixelMan_{i}.png").convert("RGBA")
        combined_images.paste(image, paste_position, image)
    combined_images.save("PixelMan-Collection.png")


def resize_image(image_path, multiplyer=2):
    image = Image.open(image_path)
    width, height = image.size

    new_width = width * multiplyer
    new_height = height * multiplyer

    resize_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resize_image.save(image_path)


def main():
    layers_combinations = []

    while len(layers_combinations) < 2880:
        layers = generate_path()
        if layers in layers_combinations:
            continue

        layers_combinations.append(layers)
        bg_path = "images/background.png"  # random.randint(1, 5)
        combine_layers(
            layers, bg_path, f"outputs/PixelMan_{len(layers_combinations)}.png"
        )
    combine_images()
    resize_image("PixelMan-Collection.png")


if __name__ == "__main__":
    main()
