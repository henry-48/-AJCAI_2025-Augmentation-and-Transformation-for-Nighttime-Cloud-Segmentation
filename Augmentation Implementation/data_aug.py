import os
import random
from gimpfu import *

def apply_data_aug_to_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)

            # change output

            if "_GT" in filename:
                name, after = filename.split("_GT")
                name = name + "_aug"
                filename = name + "." + after
            else:
                name,suffix = filename.split(".")
                name = name + "_aug"
                filename = name + "." + suffix
            
            output_path = os.path.join(output_folder, filename)

            # Open the image
            image = pdb.gimp_file_load(input_path, input_path)
            layer = image.active_layer

            # Apply a random glow effect
            blur_radius = random.uniform(50, 70)
            opacity = random.uniform(60,100)
            add_glow(image, layer, blur_radius, opacity)

            # Ensure the layer is valid before saving
            layer = image.active_layer

            # Save the image
            pdb.gimp_file_save(image, layer, output_path, output_path)
            pdb.gimp_image_delete(image)


            # fish eye transform
            # Open the image
            image = pdb.gimp_file_load(output_path, output_path)
            layer = image.active_layer
            apply_fisheye(image, layer)
            # Ensure the layer is valid before saving
            layer = image.active_layer

            # Save the image
            pdb.gimp_file_save(image, layer, output_path, output_path)
            pdb.gimp_image_delete(image)


            # Apply lens flare effect at a random position
            # Open the image
            image = pdb.gimp_file_load(output_path, output_path)
            layer = image.active_layer
            apply_lens_flare(image, layer)

            # Ensure the layer is valid before saving
            layer = image.active_layer

            # Save the image
            pdb.gimp_file_save(image, layer, output_path, output_path)
            pdb.gimp_image_delete(image)

def add_glow(image, layer, blur_radius, opacity):
    # Start an undo group, so the operation can be undone in one step
    pdb.gimp_image_undo_group_start(image)
    
    # Duplicate the original layer
    glow_layer = pdb.gimp_layer_copy(layer, True)
    pdb.gimp_image_insert_layer(image, glow_layer, None, -1)

    # Apply Gaussian blur to the duplicated layer
    pdb.plug_in_gauss(image, glow_layer, blur_radius, blur_radius, 0)
    
    # Set the glow layer's mode to 'Screen' and adjust opacity
    pdb.gimp_layer_set_mode(glow_layer, SCREEN_MODE)
    pdb.gimp_layer_set_opacity(glow_layer, opacity)
    
    # Merge down the glow layer and set the result as the active layer
    merged_layer = pdb.gimp_image_merge_down(image, glow_layer, CLIP_TO_BOTTOM_LAYER)
    pdb.gimp_image_set_active_layer(image, merged_layer)

    # End the undo group
    pdb.gimp_image_undo_group_end(image)
    
    # Update the display
    pdb.gimp_displays_flush()

def apply_fisheye(image, layer):
    # Start an undo group, so the operation can be undone in one step
    pdb.gimp_image_undo_group_start(image)
    
    # Apply lens distortion effect (Fisheye effect)
    pdb.plug_in_applylens(image, layer, 1.7, False, False,False)

    # End the undo group
    pdb.gimp_image_undo_group_end(image)
    
    # Update the display
    pdb.gimp_displays_flush()

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
    "python_fu_apply_data_aug_to_folder",
    "Apply random glow effect/fish eye transform/lens flare to all images in a folder",
    "Loads each image in the specified folder, applies a random glow effect/fish eye transform/lens flare, and saves the result in the output folder",
    "Name", "Name", "2024",
    "<Toolbox>/Xtns/Languages/Python-Fu/Apply data_aug",
    "",
    [
        (PF_DIRNAME, "input_folder", "Input Folder", ""),
        (PF_DIRNAME, "output_folder", "Output Folder", "")
    ],
    [],
    apply_data_aug_to_folder
)

main()