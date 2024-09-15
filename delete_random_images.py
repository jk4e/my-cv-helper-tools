import os
import random
import argparse

def delete_random_images(folder_path, remaining_count):

    # Get all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter for image files (you can add more extensions if needed)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [f for f in all_files if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Calculate how many images to delete
    total_images = len(image_files)
    images_to_delete = max(0, total_images - remaining_count)
    
    if images_to_delete == 0:
        print(f"There are {total_images} images in the folder, which is less than or equal to the requested remaining count. No images will be deleted.")
        return
    
    # Randomly select images to delete
    images_to_delete = random.sample(image_files, images_to_delete)
    
    # Delete the selected images
    for image in images_to_delete:
        os.remove(os.path.join(folder_path, image))
        print(f"Deleted: {image}")
    
    print(f"Deleted {len(images_to_delete)} images. {remaining_count} images remain in the folder.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete random images from a folder.")
    parser.add_argument("folder_path", help="Path to the folder containing images")
    parser.add_argument("remaining_count", type=int, help="Number of images to keep in the folder")
    
    args = parser.parse_args()
    
    delete_random_images(args.folder_path, args.remaining_count)