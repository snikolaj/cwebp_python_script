import sys
import subprocess

# these extensions can be converted, special exception is animated PNGs
# you can change this for the extension you want
image_extensions = ["jpg", "jpeg", "png", "tiff"]

# CHANGE THIS TO YOUR CWEBP LOCATION
cwebp_location = "C:\\Users\\Stefan\\Desktop\\Skripte\\python_cwebp\\cwebp.exe"
# CHANGE THIS IF YOU WANT A DIFFERENT QUALITY NUMBER, GOES FROM 0 TO 100
quality = "80"

def run_script(full_filepath):
    # the following two lines remove the file location from the filename
    # can be used for other stuff
    file_location_split = full_filepath.split("\\")[0:-1]
    file_location = "\\".join(file_location_split)
    # recreate the filename and location and add a webp extension
    filename_webp = file_location + "\\" + arg.split("\\")[-1].split(".")[0] + ".webp"
    #print(cwebp_location)
    #print(full_filepath)
    #print(filename_webp)
    # the arguments need to be in an array to run
    cwebp_args = [cwebp_location, "-q", quality, full_filepath, "-o", filename_webp]
    subprocess.run(cwebp_args)

for arg in sys.argv:
    # run the script for all image extensions, doesn't cost a lot in performance
    for extension in image_extensions:
        # does the file extension match any of the given ones
        if arg.split(".")[-1].lower() == extension:
            # run the function with the full filename and filepath
            run_script(arg)
