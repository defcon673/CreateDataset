import cv2
import os
import sys
import csv
import numpy
import pandas

folder_positive = "../dataset_all" #sys.argv[1]

images_positive = []#numpy.array([])
labels = []
for filename in os.listdir(folder_positive):
    img = cv2.imread(os.path.join(folder_positive, filename), 1)
    img = cv2.resize(img, (32, 32))
    gray_image = img  #cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if img is not None:
        images_positive.append(gray_image)
        if "neg" in filename:
            labels.append([0, 1])
        else:
            labels.append([1, 0])

first_positive = numpy.array(images_positive)
first_labels = numpy.vstack(labels)

#first3 = numpy.concatenate(images, axis=0 )
#first3 = numpy.vstack(images)
#Binary data
numpy.save('dataset', first_positive)
numpy.save('labels', first_labels)
#numpy.savetxt('dataset.csv', first3, delimiter=',')

# with open('dataset.csv', 'w') as f:
#    csvwriter = csv.writer(f, delimiter=',')
#    csvwriter.writerows(first3)

#not nesessary, bur it manual for reading previously saved data
#dataframe = pandas.read_csv("dataset.csv", header=None)
#dataset = dataframe.values

#if (dataset == first3):
#    print("1")
#
# with open('dataset.csv') as csvfile:
#     reader = csv.reader(csvfile)
#
#
# print(reader)