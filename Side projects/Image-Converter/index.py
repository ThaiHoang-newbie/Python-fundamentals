from PIL import Image
import os

def process_image(image, operation, **other_params):
    width, height = image.size
    pixels = list(image.getdata())
    processed_pixels = [operation(pixel, **other_params) for pixel in pixels]
    
    new_image = Image.new("RGB", (width, height))
    new_image.putdata(processed_pixels)
    return new_image

def to_grayscale(pixel):
    gray = sum(pixel) // 3
    return (gray, gray, gray)

def invert_colors(pixel):
    return tuple(255 - value for value in pixel)

def adjust_brightness(pixel, level):
    return tuple(min(max(int(value + level * value), 0), 255) for value in pixel)

def save_image(image, operation_name):
    os.makedirs("assets", exist_ok=True)
    filename = f"assets/{operation_name}.jpg"
    image.save(filename)
    # image.show()

def main():
    base_image = Image.open("assets/cat.jpg").convert("RGB")

    grayscale_image = process_image(base_image, to_grayscale)
    save_image(grayscale_image, "grayscale")

    inverted_image = process_image(base_image, invert_colors)
    save_image(inverted_image, "color-inversion")

    brightness_image = process_image(base_image, adjust_brightness, level=1.5)
    save_image(brightness_image, "brightness-adjustment")

if __name__ == "__main__":
    main()