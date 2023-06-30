import PIL.Image
import argparse
import os

def resize(image, reduction_factor=0.1):
    old_width, old_height = image.size
    new_width = int(old_width * reduction_factor)
    new_height = int(old_height * reduction_factor)
    return image.resize((new_width, new_height))

def convert_to_fdf(image, encode_color_rgb=True):
    width, height = image.size
    hex_string = ""
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            brightness = (r + g + b) // 3
            if encode_color_rgb:
                color = (r << 16) + (g << 8) + b
            else:
                color = (b << 16) + (g << 8) + r
            hex_string += f"{brightness},0x{color:08X} "
        hex_string += "\n"
    return hex_string

def main(args):
    image_path = args.image_path
    if not os.path.isfile(image_path):
        print(f"Unable to find image at path: {image_path}")
        return

    encode_color_rgb = args.rgb
    reduction_factor = args.reduction_factor

    try:
        image = PIL.Image.open(image_path).convert("RGB")
    except:
        print(f"Failed to open or convert the image at path: {image_path}")
        return

    resized_image = resize(image, reduction_factor)
    fdf_string = convert_to_fdf(resized_image, encode_color_rgb)

    output_file = os.path.splitext(image_path)[0] + ".fdf"
    with open(output_file, "w") as f:
        f.write(fdf_string)

    print(f"Image converted and saved as: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image to FDF Converter")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("-rgb", action="store_true", help="Encode color in RGB format (default: BGR)")
    parser.add_argument("-r", "--reduction-factor", type=float, default=0.1, help="Reduction factor for image resizing (default: 0.1)")

    args = parser.parse_args()
    main(args)

