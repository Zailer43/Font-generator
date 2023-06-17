import os
import random
from PIL import Image
from tqdm import tqdm


def load_textures(path, x_expected=64, y_expected=64):
    textures = []
    for file in os.listdir(path):
        if file.endswith(".png"):
            texture = Image.open(os.path.join(path, file))
            if texture.size != (x_expected, y_expected):
                print(f"Warning: {file} has an invalid size. Expected {x_expected}x{y_expected}.")
            textures.append(texture)
    return textures


def apply_font_texture(texture, font, font_texture, offset_x=0):
    for x in range(32):
        for y in range(16):
            pixel = font.getpixel((x, y))
            if pixel[3] != 0:  # Non-transparent pixel
                texture.putpixel((x + offset_x, y), font_texture.getpixel((x + offset_x, y)))


def erase_font_shape(texture, font, offset_x=0):
    for x in range(32):
        for y in range(16):
            pixel = font.getpixel((x, y))
            if pixel[3] != 0:  # Non-transparent pixel
                texture.putpixel((x + offset_x, y), (0, 0, 0, 0))  # Set pixel to fully transparent


results_path = "./results/"

def process_fonts(fonts, font_textures, base_texture, watermark, user_option):
    for font in tqdm(fonts, desc="Processing Fonts"):
        font_texture = random.choice(font_textures)
        font_result = Image.new(mode="RGBA", size=(64, 64))

        if user_option == 1 or user_option == 4:
            apply_font_texture(font_result, font, font_texture)
        if user_option == 2:
            apply_font_texture(font_result, font, font_texture, offset_x=32)

        result = base_texture.copy()
        result.paste(watermark, (0, 0), watermark)
        result.paste(font_result, (0, 0), font_result)

        if user_option == 3 or user_option == 4:
            erase_font_shape(result, font, offset_x=32)

        result.save(f"{results_path}{os.path.basename(font.filename)}")

def main():
    textures_path = "./textures"
    font_path = f"{textures_path}/font/"
    font_textures_path = f"{textures_path}/font_texture/"
    base_texture_path = f"{textures_path}/base_texture.png"
    watermark_path = f"{textures_path}/watermark.png"

    if not os.path.exists(f"{textures_path}/"):
        os.mkdir(f"{textures_path}/")

    if not os.path.exists(font_path):
        os.mkdir(font_path)

    if not os.path.exists(font_textures_path):
        os.mkdir(font_textures_path)

    # Load textures
    fonts = load_textures(font_path, 32, 16)
    font_textures = load_textures(font_textures_path)
    base_texture = Image.open(base_texture_path)
    watermark = Image.open(watermark_path)

    # User prompt
    user_option = int(input("Choose the desired result:\n1: Use texture on the first layer\n2: Use texture on the second layer\n3: Erase letter on the second layer\n4: Texture on the first layer and erase letter on the second layer\n"))

    if not os.path.exists(results_path):
        os.mkdir(results_path)

    # Process fonts
    process_fonts(fonts, font_textures, base_texture, watermark, user_option)


if __name__ == "__main__":
    main()
