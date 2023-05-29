import os

def write_to_css_file(cssData, filename):
    if not os.path.exists(filename):
        # File does not exist, create it and write CSS data
        with open(filename, 'w') as f:
            f.write(cssData)
    else:
        # File exists, append CSS data to the end of the file
        with open(filename, 'a') as f:
            f.write(cssData)
