import os
import cv2


def load(path):
    return cv2.imread(path)

# file, path_out -> csv_path
def convert_path(file, out):
    filename, file_ext = os.path.splitext(file)
    return out+filename+".csv"

def save(path, arr):
    output = ""
    for l in arr:
        for c in l:
            if c != 0:
                output += str(c)
            output += '\t'
        output = output[:-1]
        output += "\n"
    output = output[:-1]

    with open(path, 'w') as f:
        f.write(output)

    print(f"Saved in {path}!")