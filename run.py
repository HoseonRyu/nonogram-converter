from util.File import convert_path, load, save
from util.Image import transf
from util.Convert import result
import argparse
import os

PATH_IMG = "./img/"
PATH_OUTPUT = "./output/"
H = 30



def main():
    dir_list = os.listdir(PATH_IMG)
    for i, d in enumerate(dir_list):
        print(f"[{i}] : {d}")

    idx = int(input("Choose the image to convert : "))
    file = dir_list[idx]

    PATH_SAVE = convert_path(file,PATH_OUTPUT)

    img = load(PATH_IMG+file)
    rows, cols = transf(img, H, 2)
    arr = result(rows, cols)
    save(PATH_SAVE, arr)

if __name__ == "__main__":
    main()