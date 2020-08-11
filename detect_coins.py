# todo: try classification using one-dimensional data clustering of radii
# http://journal.r-project.org/archive/2011-2/RJournal_2011-2_Wang+Song.pdf


import argparse
import glob
import math

import cv2
import numpy as np
from skimage.transform import resize
from sklearn.model_selection import train_test_split
# import classifier
from sklearn.neural_network import MLPClassifier

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# resize image while retaining aspect ratio
d = 1024 / image.shape[1]
dim = (1024, int(image.shape[0] * d))
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# create a copy of the image to display results
output = image.copy()

# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# improve contrast accounting for differences in lighting conditions:
# create a CLAHE object to apply contrast limiting adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
gray = clahe.apply(gray)


def calcHistogram(img):
    # create mask
    m = np.zeros(img.shape[:2], dtype="uint8")
    (w, h) = (int(img.shape[1] / 2), int(img.shape[0] / 2))
    cv2.circle(m, (w, h), 60, 255, -1)

    # calcHist expects a list of images, color channels, mask, bins, ranges
    h = cv2.calcHist([img], [0, 1, 2], m, [8, 8, 8], [0, 256, 0, 256, 0, 256])

    # return normalized "flattened" histogram
    return cv2.normalize(h, h).flatten()


def calcHistFromFile(file):
    img = cv2.imread(file)
    return calcHistogram(img)


# define Enum class
class Enum(tuple): __getattr__ = tuple.index


# Enumerate material types for use in classifier
Material = Enum(('agorot10', 'agorot50', 'sheakel1', 'Euro2'))

# locate sample image files
sample_images_agorot10 = glob.glob("sample_images/agorot10/*")
sample_images_agorot50 = glob.glob("sample_images/agorot50/*")
sample_images_shekel1 = glob.glob("sample_images/sheakel1/*")
# sample_images_euro2 = glob.glob("sample_images/euro2/*")

# define training data and labels
X = []
y = []

# compute and store training data and labels
for i in sample_images_agorot10:
    X.append(calcHistFromFile(i))
    y.append(Material.agorot10)
for i in sample_images_agorot50:
    X.append(calcHistFromFile(i))
    y.append(Material.agorot50)
for i in sample_images_shekel1:
    X.append(calcHistFromFile(i))
    y.append(Material.sheakel1)
# for i in sample_images_euro2:
#     X.append(calcHistFromFile(i))
#     y.append(Material.Euro2)

# instantiate classifier
# Multi-layer Perceptron
# score: 0.974137931034
clf = MLPClassifier(solver="lbfgs")

# split samples into training and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.2)

# train and score classifier
clf.fit(X_train, y_train)
score = int(clf.score(X_test, y_test) * 100)
print("Classifier mean accuracy: ", score)

# blur the image using Gaussian blurring, where pixels closer to the center
# contribute more "weight" to the average, first argument is the source image,
# second argument is kernel size, third one is sigma (0 for autodetect)
# we use a 7x7 kernel and let OpenCV detect sigma
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# circles: A vector that stores x, y, r for each detected circle.
# src_gray: Input image (grayscale)
# CV_HOUGH_GRADIENT: Defines the detection method.
# dp = 2.2: The inverse ratio of resolution
# min_dist = 100: Minimum distance between detected centers
# param_1 = 200: Upper threshold for the internal Canny edge detector
# param_2 = 100*: Threshold for center detection.
# min_radius = 50: Minimum radius to be detected.
# max_radius = 120: Maximum radius to be detected.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.5, minDist=105, param1=200, param2=100, minRadius=50,
                           maxRadius=100)
print("num of circle: ", len(circles[0]))


def predictMaterial(roi):
    # calculate feature vector for region of interest
    hist = calcHistogram(roi)

    # predict material type
    s = clf.predict([hist])

    # return predicted material type
    return Material[int(s)]


# todo: refactor
diameter = []
materials = []
coordinates = []

count = 0
if circles is not None:
    # append radius to list of diameters (we don't bother to multiply by 2)
    for (x, y, r) in circles[0, :]:
        diameter.append(r)

    # convert coordinates and radii to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over coordinates and radii of the circles
    for (x, y, d) in circles:
        count += 1

        # add coordinates to list
        coordinates.append((x, y))

        # extract region of interest
        space = 10
        roi = image[y - d - space:y + d + space, x - d - space:x + d + space]
        # cv2.imshow('bla', roi)
        # cv2.waitKey(0)
        # try recognition of material type and add result to list
        material = predictMaterial(roi)
        materials.append(material)

        # write masked coin to file
        if False:
            m = np.zeros(roi.shape[:2], dtype="uint8")
            w = int(roi.shape[1] / 2)
            h = int(roi.shape[0] / 2)
            cv2.circle(m, (w, h), d, (255), -1)
            maskedCoin = cv2.bitwise_and(roi, roi, mask=m)
            cv2.imwrite("extracted/01coin{}.png".format(count), maskedCoin)

        # draw contour and results in the output image
        cv2.circle(output, (x, y), d, (0, 255, 0), 2)
        cv2.putText(output, material,
                    (x - 40, y), cv2.FONT_HERSHEY_PLAIN,
                    1.5, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# get biggest diameter
biggest = max(diameter)
i = diameter.index(biggest)

# scale everything according to maximum diameter
# todo: this should be chosen by the user
print("materials[i]", materials[i])
if materials[i] == "agorot50":
    diameter = [x / biggest * 25.75 for x in diameter]
    scaledTo = "Scaled to agorot50"
elif materials[i] == "agorot10":
    diameter = [x / biggest * 24.25 for x in diameter]
    scaledTo = "Scaled to 10 agorot"
# elif materials[i] == "Euro1":
#     diameter = [x / biggest * 23.25 for x in diameter]
#     scaledTo = "Scaled to 1 Euro"
# elif materials[i] == "Copper":
#     diameter = [x / biggest * 21.25 for x in diameter]
#     scaledTo = "Scaled to 5 Cent"
else:
    scaledTo = "unable to scale.."

i = 0
total = 0
while i < len(diameter):
    d = diameter[i]
    m = materials[i]
    (x, y) = coordinates[i]
    t = "Unknown"

    print(d, m)
    # compare to known diameters with some margin for error
    if math.isclose(d, 22.75, abs_tol=1.25) and m == "agorot10":
        t = "0.1 agorot"
        total += 0.1
    elif math.isclose(d, 22.0, abs_tol=1.25) and m == "agorot50":
        t = "0.1 agorot"
        total += 0.1
    elif math.isclose(d, 18.5, abs_tol=1.5) and m == "sheakel1":
        t = "1 sheakel"
        total += 1
    elif math.isclose(d, 26.0, abs_tol=2.5) and m == "agorot50":
        t = "0.5 agorot"
        total += 0.5
    else:
        t = str(round(d))

    # write result on output image
    cv2.putText(output, t,
                (x - 40, y + 22), cv2.FONT_HERSHEY_PLAIN,
                1.5, (255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
    i += 1

# resize output image while retaining aspect ratio
d = 768 / output.shape[1]
dim = (768, int(output.shape[0] * d))
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
output = cv2.resize(output, dim, interpolation=cv2.INTER_AREA)

# write summary on output image
cv2.putText(output, scaledTo,
            (5, output.shape[0] - 40), cv2.FONT_HERSHEY_PLAIN,
            1.0, (0, 0, 255), lineType=cv2.LINE_AA)
cv2.putText(output, "Coins detected: {}, Shekel {:2}".format(count, total),
            (5, output.shape[0] - 24), cv2.FONT_HERSHEY_PLAIN,
            1.0, (0, 0, 255), lineType=cv2.LINE_AA)
cv2.putText(output, "Classifier mean accuracy: {}%".format(score),
            (5, output.shape[0] - 8), cv2.FONT_HERSHEY_PLAIN,
            1.0, (0, 0, 255), lineType=cv2.LINE_AA)

# show output and wait for key to terminate program
cv2.imshow("Output", resize(np.hstack([image, output]), (800, 1000)))
cv2.waitKey(0)

if __name__ == "__main__":
    print("main")
