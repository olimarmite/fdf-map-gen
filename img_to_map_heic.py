import pyheif
import PIL.Image
import argparse
import os


def resize(image, reduction_factor=0.1):
    old_width, old_height = image.size
    new_width = int(old_width * reduction_factor)
    new_height = int(old_height * reduction_factor)
    return image.resize((new_width, new_height))

def pixel_to_fdf_depth(image, depth_img, encode_rgb=True):
    width, height = image.size
    depth_width, depth_height = depth_img.size
    hex_string = ""
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            depth_x = int(x * (depth_width / width))
            depth_y = int(y * (depth_height / height))
            brightness = depth_img.getpixel((depth_x, depth_y))
            if encode_rgb:
                color = (r << 16) + (g << 8) + b  # RGB encoding
            else:
                color = (b << 16) + (g << 8) + r  # BGR encoding
            hex_string += f"{brightness},0x{color:08X} "
        hex_string += "\n"
    return hex_string

def main(args):
    heif_file = pyheif.open_container(args.image_path)
    primary_image = heif_file.primary_image
    col_img = primary_image.image.load()
    depth_img = primary_image.depth_image.image.load()
    col_pil_img = PIL.Image.frombytes(
        col_img.mode,
        col_img.size,
        col_img.data,
        "raw",
        col_img.mode,
        col_img.stride,
    )
    depth_pil_img = PIL.Image.frombytes(
        depth_img.mode,
        depth_img.size,
        depth_img.data,
        "raw",
        depth_img.mode,
        depth_img.stride,
    )
    col_pil_img = col_pil_img.convert("RGB")
    col_pil_img = resize(col_pil_img, args.reduction_factor)
    depth_pil_img = depth_pil_img.convert("L")
    depth_pil_img = resize(depth_pil_img, args.reduction_factor)
    hex_string = pixel_to_fdf_depth(col_pil_img, depth_pil_img, encode_rgb=args.rgb)

    output_file = os.path.splitext(args.image_path)[0] + ".fdf"
    with open(output_file, "w") as f:
        f.write(hex_string)

    print(f"Image converted and saved as: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HEIF to FDF Converter")
    parser.add_argument("image_path", help="Path to the HEIF image file")
    parser.add_argument(
        "-r",
        "--reduction-factor",
        type=float,
        default=0.1,
        help="Reduction factor for image resizing (default: 0.1)",
    )
    parser.add_argument(
        "-rgb",
        action="store_true",
        help="Encode color in RGB format (default: BGR)",
    )

    args = parser.parse_args()
    main(args)

