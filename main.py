from PIL import Image  
import os
import random

def generate_path():
    path = {}

    path["faces"] = random.randint(1, 8)
    if random.uniform(0, 1) < 0.9:
        path["tops"] = random.randint(1, 7)
    if random.uniform(0, 1) < 0.75:
        path["eyewears"] = random.randint(1, 4) 
    if random.uniform(0, 1) < 0.3:
        path["mouth"] = random.randint(1, 2)
    if random.uniform(0, 1) < 0.5:
        path["accessories"] = random.randint(1, 2)

    return path

def main():
    im_paths = generate_path()
    combined = Image.open("images/background/1.png").convert("RGBA")
    for layer, val in im_paths.items():
        im = Image.open(f"images/{layer}/{val}.png").convert("RGBA")
        combined = Image.alpha_composite(combined, im)
    combined.save("output/output.png")

if __name__ == "__main__":
    main()