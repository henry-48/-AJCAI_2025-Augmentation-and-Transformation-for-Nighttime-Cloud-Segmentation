import shutil
import os
import cv2
import matplotlib.pyplot as plt
DESTINATION = "F:\\Cloud segment models\\Pytorch-UNet-day-ver\\data"


night = "F:\\ANU\Research Project\\Dataset\\swinseg"
day = "F:\\ANU\Research Project\\Dataset\\swimseg"


def copy_and_rename(des,target,is_day = False):
    tar_img = target + "/images"
    tar_GT = target + "/GTmaps"

    # copy img
    for _,_,f_ls in os.walk(tar_img):

        for f in f_ls:
            path, suffix = f.split(".")
            if is_day:
                path += "_day"
            else:
                path += "_night"
            
            new_file = path + "." + suffix
            new_path = DESTINATION + "/imgs/" + new_file
            original = tar_img + "/" + f

            image = cv2.imread(original)
            if not is_day:
                padding = 50
                padded_image = cv2.copyMakeBorder(
                    image,
                    top=padding,
                    bottom=padding,
                    left=padding,
                    right=padding,
                    borderType=cv2.BORDER_CONSTANT
                )

                
                cv2.imwrite(new_path, padded_image)
            else:
                shutil.copy(original, new_path)
    
    # copy GT map
    for _,_,f_ls in os.walk(tar_GT):

        for f in f_ls:
            name, GT_suffix = f.split("_")
            if is_day:
                name += "_day"
            else:
                name += "_night"
            
            new_file = name + "_" + GT_suffix
            new_path = DESTINATION + "/masks/" + new_file
            original = tar_GT + "/" + f

            if "jpg" in new_path:
                new_path = new_path.replace(".jpg",".png")

            image = cv2.imread(original, cv2.IMREAD_GRAYSCALE)

            if not is_day:
                padding = 50
                padded_image = cv2.copyMakeBorder(
                    image,
                    top=padding,
                    bottom=padding,
                    left=padding,
                    right=padding,
                    borderType=cv2.BORDER_CONSTANT
                )
                _, binary_image = cv2.threshold(padded_image, 127, 255, cv2.THRESH_BINARY)
                binary_image = binary_image.astype("uint8")
                cv2.imwrite(new_path, binary_image)
            else:
                _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
                binary_image = binary_image.astype("uint8")
                cv2.imwrite(new_path, binary_image)
    
if __name__ == "__main__":
    copy_and_rename(DESTINATION,day,is_day=True)
    copy_and_rename(DESTINATION,night)