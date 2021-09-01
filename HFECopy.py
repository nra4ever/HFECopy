from shutil import copy2
import glob
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    parser.add_argument('-n', '--newdisks')
    parser.add_argument('-c', '--copyfrom')
    args = parser.parse_args()

def findzero(index):
    if index <= 99:
        zero = "00"
    if index > 99:
        zero = "0"
    return zero


if args.dir:
    fileDir = args.dir
else:
    fileDir = input("Location of images: ")
end = len(glob.glob1(fileDir, "*.HFE"))
print(str(end) + " images currently on drive.")
endCurrent = end - 1


if args.newdisks:
    floppies = int(args.newdisks)
else:
    floppies = int(input("How Many Disks Would you like to make?: "))
if args.copyfrom:
    cpnum = int(args.copyfrom)
else:
    cpnum = input("Specify which floppy image number you would like to copy. Default is " + findzero(endCurrent)
              + str(endCurrent) + ": ").lstrip()


if not cpnum:
    cpnum = endCurrent


highfile = "DSKA" + findzero(int(cpnum)) + str(cpnum) + ".HFE"


if floppies + endCurrent > 999:
    raise ValueError

for i in range(floppies + endCurrent + 1):
    if i > endCurrent:
        print("Writing DSKA" + findzero(i) + str(i) + ".HFE")
        copy2(fileDir + "\\" + highfile, fileDir + "\\" + "DSKA" + findzero(i) + str(i) + ".HFE")

print("Operation Complete")
