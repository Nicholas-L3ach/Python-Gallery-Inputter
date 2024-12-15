import fileinput
import sys

gallery = input("Input t for traditional, g for graphic design, u for unique projects")

indexfile = 'indexcopy.html'

def insertgallery():
    if gallery == "t":
        filename = input("Enter file name")
        for line in fileinput.FileInput(indexfile, inplace=True):
            if 'pythongalleryt' in line:
                line = line.rstrip()
                line = line.rstrip("];")
                line = line + ', "<img src=\'Gallery/Traditional/' + filename + '.png\'>"];' + '\n'
            sys.stdout.write(line)
    if gallery == "g":
        filename = input("Enter file name")
        for line in fileinput.FileInput(indexfile, inplace=True):
            if 'pythongalleryg' in line:
                line = line.rstrip()
                line = line.rstrip("];")
                line = line + ', "<img src=\'Gallery/Graphic/' + filename + '.png\'>"];' + '\n'
            sys.stdout.write(line)
    if gallery == "u":
        filename = input("Enter file name")
        for line in fileinput.FileInput(indexfile, inplace=True):
            if 'pythongalleryu' in line:
                line = line.rstrip()
                line = line.rstrip("];")
                line = line + ', "<img src=\'Gallery/Unique/' + filename + '.png\'>"];' + '\n'
            sys.stdout.write(line)
    another = input("Insert another file? yes/no")
    if another == "yes":
        insertgallery()

insertgallery()