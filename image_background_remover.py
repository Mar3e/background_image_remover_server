from rembg import remove
from PIL import Image


def remove_background(img:str):
    # read the image from file
    input_image = Image.open(img)
    # remove the background
    output_image = remove(input_image)
    # save the modified image
    output_name = modify_image_name(img)
    print("the name is " + output_name)
    output_image.save(output_name)


def modify_image_name(image_path):
    # Extract the directory, file name, and extension
    directory, filename = image_path.split('/')
    name = filename.split('.')[0]
    # Modify the file name
    new_name = f"{name}_no_background.png"
    # Join the new file name with the directory
    new_image_path = f"{directory}/{new_name}"
    return new_image_path