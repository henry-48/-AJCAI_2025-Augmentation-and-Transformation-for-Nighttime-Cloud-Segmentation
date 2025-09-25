#!/usr/bin/env python
# Apply Lens Flare effect to images in a folder using GIMP and GimpFu

import os
import random
from gimpfu import *

def apply_lens_flare_to_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)

            # Change output name
            if "_GT" in filename:
                name, after = filename.split("_GT")
                name = name + "_l_aug"
                filename = name + "_GT" + after
            else:
                name,suffix = filename.split(".")
                name = name + "_l_aug"
                filename = name + "." + suffix
                
            output_path = os.path.join(output_folder, filename)

            # Open the image
            image = pdb.gimp_file_load(input_path, input_path)
            layer = image.active_layer

            # Apply lens flare effect at a random position
            if "_GT" not in filename:
                apply_lens_flare(image, layer)

            # Ensure the layer is valid before saving
            layer = image.active_layer

            # Save the image
            pdb.gimp_file_save(image, layer, output_path, output_path)
            pdb.gimp_image_delete(image)

def apply_lens_flare(image, layer):
    # Start an undo group, so the operation can be undone in one step
    pdb.gimp_image_undo_group_start(image)
    
    # Get random coordinates for the lens flare
    width = layer.width
    height = layer.height
    random_x = random.randint(0, width)
    random_y = random.randint(0, height)

    # Apply the lens flare effect
    # Parameters: image, drawable, source-x, source-y, lens-type
    pdb.plug_in_flarefx(image, layer, random_x, random_y)

    # End the undo group
    pdb.gimp_image_undo_group_end(image)
    
    # Update the display
    pdb.gimp_displays_flush()

register(
    "python_fu_apply_lens_flare",
    "Apply lens flare effect to all images in a folder",
    "Applies a lens flare effect to all images in the specified input folder and saves them to the specified output folder",
    "Your Name", "Your Name", "2024",
    "<Toolbox>/Xtns/Languages/Python-Fu/Apply Lens Flare to Folder",
    "",
    [
        (PF_DIRNAME, "input_folder", "Input Folder", ""),
        (PF_DIRNAME, "output_folder", "Output Folder", "")
    ],
    [],
    apply_lens_flare_to_folder
)

main()
