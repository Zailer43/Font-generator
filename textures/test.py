import os
from PIL import Image

def crop_images(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                image = Image.open(file_path)
                cropped_image = image.crop((0, 0, 32, 16))
                cropped_image.save(file_path)
                print(f"Cropped image: {file_name}")
            except Exception as e:
                print(f"Error cropping image: {file_name}")
                print(str(e))

def main():
    folder_path = "./font/"  # Reemplaza con la ruta de tu carpeta
    crop_images(folder_path)

if __name__ == "__main__":
    main()
