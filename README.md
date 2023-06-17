# Font generator

This script processes fonts by applying a texture to them, adding a watermark, and saving the resulting images. It simplifies the process of creating font textures for Minecraft player heads.

## Usage

1. Install Python: 
   - Visit the [Python website](https://www.python.org/) and download the latest version of Python.
   - Follow the installation instructions for your operating system.

2. Install Required Dependencies:
   - Open a terminal or command prompt.
   - Run the following command to install the necessary dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Prepare the Image Files:
   - Create the following directories in the same location as the script:
     - `textures/font/` (Place all font textures with a size of 32x16 in this directory.)
     - `textures/font_texture/` (Place all font textures with a size of 64x64 in this directory.)
     - `textures/base_texture.png` (Place the base texture image file in this directory.)
     - `textures/watermark.png` (Place the watermark image file in this directory.)

4. Run the Script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```
     python script.py
     ```
   - The script will process the fonts, generate new images, and save them in the `result` directory.

5. View the Results:
   - Open the `result` directory to find the processed images.