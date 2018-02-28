import sys
import os
from PIL import Image

uniquePics = []

def myFunc(file1, file2):
    pic1 = Image.open(file1)
    pic2 = Image.open(file2)
    answer = True
    if pic1.size[0] == pic2.size[0] and pic2.size[1] == pic1.size[1]:
        size = pic1.size
        for i in range(0, size[0]):
            for j in range(0, size[1]):
                if(pic1.getpixel((i, j))) != pic2.getpixel((i, j)):
                    answer = False
    else:
        answer = False

    if answer == True:
        uniquePics.append(file1)
    print(answer)

folders = []
path = "/Users/skyleguy/Desktop/"
for arg in sys.argv:
    folders.append(arg)
folders = folders[1:]
os.chdir(path)
pictures = []

for arg in folders:
    os.chdir(path + arg)
    for file in os.listdir(path + arg):
        pictures.append(file)

for i in range (0, len(pictures)):
    for j in range(i + 1, len(pictures)):
        print("Comparing " + pictures[i] + " to " + pictures[j])
        if pictures[i] != ".DS_Store" and pictures[j] != ".DS_Store":
            myFunc(pictures[i], pictures[j])
print(uniquePics)
if not os.path.exists(path + "uniques"):
    os.makedirs(path + "uniques")
os.chdir(path + "uniques")
for image in uniquePics:
    with open(os.path.join(path + "uniques", image), 'wb') as temp_file:
        temp_file.write(image)

