# grayscale_conversion_code

import cv2  # OpenCV for image processing
import os   # For file and folder operations

def process_real_world_vegetation(image_path, output_folder, original_crop_size=(350, 350), final_size=(50, 50)):
    os.makedirs(output_folder, exist_ok=True)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"❌ Error: Could not load image {image_path}")
        return

    h, w = image.shape
    crop_w, crop_h = min(w, original_crop_size[0]), min(h, original_crop_size[1])
    crop_x = (w - crop_w) // 2
    crop_y = (h - crop_h) // 2
    cropped = image[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]
    resized = cv2.resize(cropped, final_size, interpolation=cv2.INTER_LINEAR)

    original_name = os.path.splitext(os.path.basename(image_path))[0]
    output_filename = f"{original_name}_processed_50x50.png"
    output_path = os.path.join(output_folder, output_filename)

    cv2.imwrite(output_path, resized)
    print(f"✅ Saved: {output_path}")

def process_all_images_in_folder(input_folder, output_folder, original_crop_size=(350, 350), final_size=(50, 50)):
    if not os.path.exists(input_folder):
        print(f"❌ Error: Input folder not found: {input_folder}")
        return

    processed_count = 0
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif')):
            image_path = os.path.join(input_folder, file_name)
            print(f"🔍 Processing: {file_name}")
            process_real_world_vegetation(image_path, output_folder, original_crop_size, final_size)
            processed_count += 1

    print(f"🎉 Done! Total images processed: {processed_count}")

# Example usage:
if __name__ == "__main__":
    # Set your paths here
    input_folder = "path/to/your/input/folder"
    output_folder = "path/to/your/output/folder"

    # Run processing
    process_all_images_in_folder(input_folder, output_folder)