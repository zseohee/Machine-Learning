# -*- coding: utf-8 -*-
"""Seohee Activity 4: Machine Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DZeNojc923X4n-seSt5R3s7inCjI-eNZ

# Seohee Machine Learning

**Pioneer Research, 2022**

(be sure to update the `sampleImPath` and `sampleDataPath` below to match your system)
"""

# This connects Colab to your Google Drive space
from google.colab import drive
drive.mount('/content/drive')

from google.colab.patches import cv2_imshow

# Import statements

import os
import random
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Store the long path to access the SampleImages and SampleData folders
sampleImPath = "/content/drive/MyDrive/Pioneer/PioneerData/SampleImages/"
sampleDataPath = "/content/drive/MyDrive/Pioneer/PioneerData/SampleData/"

# Uncomment this to see the contents of the sampleImPath folder
print(os.listdir(sampleImPath))
print(os.listdir(sampleDataPath))

from google.colab import drive
drive.mount('/content/drive')

"""---
## K-Nearest Neighbor

### KNN for Random Generated Data
The code below, adapted from the OpenCV Machine Learning tutorial, generates random data, and assigns half of them to one category and the other half to a second category. It then generates a new random value. It plots this data as a scatterplot (note: you must close the plot window for the program to go on).

Line by line:
* Generate an array that has 25 rows and 2 columns, filled with random values between 0 and 99; the data is stored as a 32-bit floating point number, because the `KNearest` algorithm expects that kind of data
* For each of the 25 rows, randomly assign the data to category 0 or category 1
* Plot the data as Cartesian coordinates, using a scatterplot where x is the horizontal axis and y is the vertical axis
* Select the category 0 items from the data array
* Draw the category 0 items on the scatterplot colored in red
* Select the category 1 items from the data array
* Draw the category 1 items on the scatterplot colored in blue
* Generate a new random point: this represents a new item we want to categorize as 0 or 1, based on its proximity to other 0 or 1 data points
* Plot the new point on the same scatterplot, in green
* Display the scatterplot
"""

def plotDataAndPoint(data, responses, newPoint):
    # call data where response is 0 "red"
    red = data[responses==0]
    plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
    # call data where response is 1 "blue"
    blue = data[responses==1]
    plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

    # Plot a new point in green
    plt.scatter(newPoint[:, 0], newPoint[:, 1], 80, 'g', 'o')
    plt.show()

trainData = np.random.randint(0, 100, (40, 2)).astype(np.float32)
responses = np.random.randint(0, 2, 40).astype(np.float32)

# Generate a new point
newPoint = np.random.randint(0, 100, (1, 2)).astype(np.float32)

# Plot random data, and new (random) point
plotDataAndPoint(trainData, responses, newPoint)

"""### Building and Training a KNN Object

Next, we want to set up the KNN algorithm, and then train it on our dataset. Note that the second input to the train method tells it whether the data is organized in rows or columns.

"""

# Create KNN object and train on data
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

"""### Classifying New Points

Finally, we can classify our new point by asking it to find the K nearest data points. This prints the category that is the majority, and then the individual categories of the nearest data, and then their distances from the new point.

Try varying the number of neighbors the KNN algorithm uses to determine the new point's category. What effect does that have?

Run the whole notebook up to this point several times, to generate several sets of random data. How much does the behavior vary?
"""

# Generate a new point
newPoint = np.random.randint(0, 100, (1, 2)).astype(np.float32)

# Plot random data, and new (random) point
plotDataAndPoint(trainData, responses, newPoint)

# Report category of new point (based on k=3)
ret, result, neighbors, dist = knn.findNearest(newPoint, 3)
print("result:", result)
print("neighbors:", neighbors)
print("distances:", dist)

"""---
##Milestone 1: Playing with more realistic random data

**Part 1:** The code above randomly assigns points to category 0 or category 1. Suppose we want to experiment with randomly-created data, but we want something a bit less arbitrary.

**You are going to copy the code from the code blocks above, starting with the block that defines `trainData` and modifying it as you go.**

**Step 1:** Copy the code block that defines `trainData` and `responses` and then plots them so we can see them. We are going to add some steps to change how points are assigned to 1 or 0: we want to assign response 1 to points where the smaller of their x or y values is between 25 and 75, and response 0 to any other points:
* Assign a new variable, `mins`, to hold the smaller of the x and y values for each of the 25 points: `trainData.min(axis=1)` will do what you want; it returns a new array. For instance, if one of the pairs was (51, 33) then the corresponding value should be 33.
* Print `trainData`, and also `mins` so you can see how they relate.
* If you use a boolean operation on a Numpy array, the result is a new Numpy array the same size, filled with booleans. Define a variable `atLeast25` to hold the result of `mins >= 25`. Print it, to see what it looks like
* Do the same for a variable `atMost60` where you compare `mins` to 60.
* Combine these two boolean arrays together using the Numpy command `logical_and`: `inBounds = np.logical_and(atLeast25, atMost60)`.
* Define `responses` to be the result of converting the logical-anded-ed array to a 32-bit float (the original code also did this conversion, just on different data: use the Numpy `astype` method to convert the boolean array to 32-bit floats).
** Plot the data, there should now be a pattern to it

**Step 2:** Copy the next block of code, that sets up the KNN object and trains it on the training data (no changes required).

**Step 3:** Copy the final block of code, that tests the `newPoint` to see how it is categorized.


**Part 2:** In the code above, we generate just one test point. The `findNearest` method can also take an array of points, similar in shape to the training data, and will report all their results at once. Use the `randint` function to generate 10 random points, and pass the array to `findNearest`. Print the results just as before, and examine how they differ from a single point.
"""

# Put any new Milestone code here
trainData = np.random.randint(0, 100, (40, 2)).astype(np.float32)

mins = trainData.min(axis=1)
atLeast25 = mins>=25
atMost60 = mins<=60
inBounds = np.logical_and(atLeast25, atMost60)

responses = inBounds.astype(np.float32)

# Plot random data, and new (random) point
plotDataAndPoint(trainData, responses, newPoint)

# Create KNN object and train on data
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)

# Generate a new point
newPoint = np.random.randint(0, 100, (10, 2)).astype(np.float32)

# Plot random data, and new (random) point
plotDataAndPoint(trainData, responses, newPoint)

# Report category of new point (based on k=3)
ret, result, neighbors, dist = knn.findNearest(newPoint, 3)
for i in range (10):
  print("point: {}".format(i))
  print("result: {}".format(result[i]))
  print("neighbours: {}".format(neighbors[i]))
  print("distance: {}".format(dist[i]))
  print("\n")

"""---
##Classifying Hand-written Digits

We are going to work with a very simple, small dataset of hand-written digits. The data is stored, in this case, in one image: `digits.png`, which is in the SampleData folder. This data consists of 5000 images of digits, each just 20 pixels by 20 pixels in size. There are 500 images for each digit.

The image is 2000 pixels wide and 1000 pixels tall. Each digit has 5 20x20 rows of images, with 100 images per row.

###Data Wrangling

The first step in any machine learning task is data wrangling, or finding, storing, loading, and manipulating the data to be in the form that we need for the ML algorithm. We have to process the big image and break it up into the small images, attach the right label (0 through 9) to each image, and then convert the images so that they are one-dimensional arrays (400-long, rather than 20 by 20) of floating point numbers. Then they will be suitable for training the `KNearest` algorithm.

**Step 1: Break up the big picture**

The code below reads in the digits image, converts it to grayscale, and then breaks it up into 20x20 chunks. The `vsplit` and `hsplit` functions from Numpy divide an array into the given number of sub-arrays: vsplit splits up the rows of the array, and hsplit splits up the columns. This code combines them using a list comprehension, producing a list of arrays of 20x20 grayscale images. The final step converts that list back into a Numpy array, with 50 rows, 100 columns, and each value within that is a small image.

"""

digitDataIm = cv2.imread(sampleDataPath + "digits.png")
gray = cv2.cvtColor(digitDataIm, cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Make it into a Numpy array: its size will be (50,100,20,20)
x = np.array(cells)
print(x.shape)

"""**Step 2: Separate training from testing data**

For this example, we will just have training data and testing/validation data (we won’t break the dataset into three parts). We’re going to assume that, within each digit, the individual pictures are randomized. So we can create training and testing data by using some columns of the x array for training, and the rest for testing.  Initially, we will split the data in half (in the milestone you’ll experiment with other splits).

Remember that the x array has 100 columns. We will take the first 50 for training, and the second 50 for testing. I am recording how many training images I have per digit with the third line below, so that I can generate the correct categories for each training example later.
"""

trainCols = 50
train = x[:, :trainCols]
test = x[:, trainCols:100]
trainPerDigit = 500 / (100 / trainCols)
testPerDigit = 500 / (100 / (100 - trainCols))

"""**Step 3: Flatten the data**

The next step is to turn this data into a 2d array, with one row for each image. We will convert it to 32-bit floats at the same time.

"""

train = train.reshape(-1, 400).astype(np.float32)
test = test.reshape(-1, 400).astype(np.float32)
print(train.shape, test.shape)

"""**Step 4: Generate the correct output categories**

We know from earlier that each digit has `trainPerDigit` rows in our training data. We want to generate the responses we expect, by repeating the digit for each set of rows the correct number of times (so the array will have 250 0’s, followed by 250 1’s, etc, in this case). The final piece is to adjust the shape of the array (a common requirement for data wrangling!) so that, instead of being (2500,) it is (2500,1) so that it matches the format that the `KNearest` algorithm will report back to us. The `np.newaxis` option adds a second axis with just one value in it.

"""

digitCats = np.arange(10)
train_labels = np.repeat(digitCats,trainPerDigit)[:, np.newaxis]
test_labels = np.repeat(digitCats, testPerDigit)[:, np.newaxis]

"""---
##Milestone 2: Finish the digits program

**Complete the KNN training and testing**

The steps above end with data that is in the correct format for the `KNearest` object. Using the earlier program that ran on artificial data as a model, set up a `KNearest` object, and train it on the training data above. Call `findNearest` on the testing data above.  Put your new code before the code in the block below. The code I've provided below computes the percentage of the test examples where KNN gave the correct answer.

**Experiment!**

After you get the KNN algorithm working on the data, try some experimentation.

A major component of working with machine learning is experimenting with how changing the parameters of the problem changes the outcomes. Try the experiments here, and be prepared to report on your findings!
* Dig into the raw results a bit more. Compute the accuracy for each digit. Is KNN equally accurate on all categories, or does it do better on some than on others? Are there patterns to when it is right or wrong?
* Try changing the number of neighbors. For which number of neighbors was the resulting accuracy the best?
* Try changing the number of columns allocated to training versus testing. How does that affect the performance of the algorithm on the test data?

"""

# Put your code for Milestone 2 here
# Create KNN object and train on data
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

# Report category of new point (based on k=3)
ret, result, neighbors, dist = knn.findNearest(test, 10)
#1=92.0, 2=91.24, 3=91.64, 4=91.92 5=91.76, 10=91.16

# Put your code above this point!
matches = result == test_labels

correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size
print(accuracy)

"""---
##Face detection with Haar Cascades

Haar cascades are an ensemble machine learning technique that combines many smaller classifiers that operate one after the other (hence the word "cascade" to describe them). Each classifier uses Haar-like features (See the Activity 4 PDF document for more details) to try to determine whether a rectangular region contains a face.

Haar cascades are trained on datasets with thousands of images in them.

We will not have to train a Haar cascade ourselves. OpenCV provided a set of trained cascades for faces, eyes, and so forth. A folder of trained cascades is in the SampleData folder, inside a folder called haarcascades. We create a classifier, reading its specifications from a file, and then apply it to images.

**Get some images/videos with faces in them:** Some of the pictures in SampleImages have my face in them. I have also included a video called `myface.avi` in the `SampleData` folder, and the `BallFinding` images and videos have my face as well. In addition, I have added a folder called `faces` that is a dataset of five celebrities. If you want to upload to your own space other images or videos of faces, feel free.

The code block below reads three images from the `faces` folder and uses a trained Haar cascade to detect faces in them.

Line by line:
* Loads the trained Haar cascade for front-facing faces
* Reads in the three faces from the faces training set
* Loops over the three images
* Converts the image to grayscale
* Runs the Haar cascade on the current image, which returns a rectangular box where every detected face is
* For each rectangle, draw a green rectangle on the original image
* Display the marked-up image

**Modify this code block** so that you loop over the first five images in each subfolder, and apply the face detector to each of them, displaying the results. Examine which faces are not detected.
"""

faceCascade = cv2.CascadeClassifier(sampleDataPath + "haarcascades/haarcascade_frontalface_alt0.xml")

img1 = cv2.imread(sampleDataPath + "faces/train/madonna/madonna2.jpg")
img2 = cv2.imread(sampleDataPath + "faces/train/mindy_kaling/mindy_kaling4.jpg")
img3 = cv2.imread(sampleDataPath + "faces/train/ben_affleck/ben_affleck7.jpg")

for img in [img1, img2, img3]:
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rects:
       cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2_imshow(img)

"""###Face detection on videos

The script below applies the same method as the previous, but to the frames of a video, saving the result in a new video.

Read this through and make sense of what it is doing.
"""

faceCascade = cv2.CascadeClassifier(sampleDataPath + "haarcascades/haarcascade_frontalface_alt0.xml")

vCap = cv2.VideoCapture(sampleDataPath + "myface.avi")
fps = int(vCap.get(cv2.CAP_PROP_FPS))
fWid = int(vCap.get(cv2.CAP_PROP_FRAME_WIDTH))
fHgt = int(vCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter(sampleImPath + "../faceDetect1.avi", fourcc, fps, (fWid, fHgt), True)
while True:
    res, frame = vCap.read()
    if not res:
        break
    # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rects:
       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    writer.write(frame)
vCap.release()
writer.release()

"""---
##Milestone 3: Finding Eyes

**Part one:** Once we have found faces, we can apply an eye detector to just the ROI where the face appears.
* Add an eye detector to one of the programs above. Create the detector right after the face detector you already have.
* Then, for each face that is found, create a ROI of that region.
* Run the eye detector on it, and for every eye that is detected, draw a circle or rectangle to mark it. Note that the eye detector, like the face detector, returns the (x, y) coordinate of the upper left corner and the width and height. Also, remember that positions in the ROI will start with (0,0) in the corner of the ROI.

**Part two:** Now we will replace the detected eyes by a "googley eye".
* Load the `GoogleyEye.png` file from the SampleImages folder.
* For each detected eye, use `resize` to change the size/shape of the googley eye image to match the size of the eye rectangle.

Even within the bounds of a detected face, the eye detector may find false eyes. Can you think of methods to find the "best" eyes, either by their position in the face, or some other measure.


"""

# Put your code for Milestone 3 here
faceCascade = cv2.CascadeClassifier(sampleDataPath + "haarcascades/haarcascade_frontalface_alt1.xml")
eyeCascade = cv2.CascadeClassifier(sampleDataPath + "haarcascades/haarcascade_eye1.xml")
img = cv2.imread(sampleDataPath + "faces/train/ben_affleck/ben_affleck13.jpg")
googleEye=cv2.imread(sampleImPath+"GoogleyEye.png")

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)

if face_rects is ():
  print("FACE NOT AVAILABLE IN IMAGE")

for (x, y, w, h) in face_rects:
  eye_roi= img[y:y+h,x:x+w]
  roi_gray= cv2.cvtColor(eye_roi, cv2.COLOR_RGB2GRAY)
  eye_rects=eyeCascade.detectMultiScale(roi_gray, 1.05, 2)

  for (ex, ey, ew, eh) in eye_rects:
    cv2.rectangle(eye_roi, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
    googleEye=cv2.resize(googleEye, (eh,ew), interpolation=cv2.INTER_LINEAR)
    eye_roi[ey:ey+eh,ex:ex+ew]=googleEye

cv2_imshow(img)

"""---
## Using dlib to detect faces and facial features

The dlib library has support for more sophisticated machine learning techniques, including deep learning. The shape predictor below uses a HOG-SVM system to detect faces, and then places face landmarks to mark the location of eyes, nose, mouth, etc.


"""

import dlib
shapeDetect = sampleDataPath + "shape_predictor_68_face_landmarks.dat"

def rect_to_bb(rect):
    """Takes a bounding box predicted by dlib, given by upper left corner and
    lower right corner, and converts it to the format (x, y, w, h) as we would
    normally expect from OpenCV"""
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    # return a tuple of (x, y, w, h)
    return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
    """Given a dlib shape object, convert it to a Numpy array of the (x, y)
    coordinates of the facial landmarks"""
    coords = np.zeros((68, 2), dtype=dtype)
    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shapeDetect)

vidCap = cv2.VideoCapture(sampleDataPath + "myface.avi")

for fNum in range(60):
    # load the input image, resize it, and convert it to grayscale
    didIt, image = vidCap.read()
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 1)

    # for each detected face...
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        (x, y, w, h) = rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # show the face number
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
    # show the output image with the face detections + facial landmarks
    cv2_imshow(image)

vidCap.release()
# cv2.destroyAllWindows()

"""---
##Milestone 4: Using Facial Landmarks

Take the program above, and convert it to work on a single still image, for simplicity. Look at the [Adrian Rosebock web page](https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/), which includes a diagram that shows the ordering of the 68 facial landmarks in the array that is generated.

Using that information, choose one of these options to complete:
* Draw line segments in fantastical colors across the person's eyebrows
* Compare the distance between upper and lower lip points to determine if the person's mouth is open or closed
* Computer the convex hull of the set of points, and mask the image so that only the part inside the facial landmakrs is visible.
"""

# Put your Milestone 4 code here
import dlib
shapeDetect = sampleDataPath + "shape_predictor_68_face_landmarks.dat"

def rect_to_bb(rect):
    """Takes a bounding box predicted by dlib, given by upper left corner and
    lower right corner, and converts it to the format (x, y, w, h) as we would
    normally expect from OpenCV"""
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    # return a tuple of (x, y, w, h)
    return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
    """Given a dlib shape object, convert it to a Numpy array of the (x, y)
    coordinates of the facial landmarks"""
    coords = np.zeros((68, 2), dtype=dtype)
    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
      coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shapeDetect)

img = cv2.imread(sampleDataPath + "faces/train/jerry_seinfeld/jerry_seinfeld18.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)

# for each detected face...
for (i, rect) in enumerate(rects):
  # determine the facial landmarks for the face region, then
  # convert the facial landmark (x, y)-coordinates to a NumPy
  # array
  shape = predictor(gray, rect)
  shape = shape_to_np(shape)
  # convert dlib's rectangle to a OpenCV-style bounding box
  # [i.e., (x, y, w, h)], then draw the face bounding box
  (x, y, w, h) = rect_to_bb(rect)
  cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
  # show the face number
  cv2.putText(img, "Face #{}".format(i + 1), (x - 10, y - 10),
  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
  # loop over the (x, y)-coordinates for the facial landmarks
  # and draw them on the image
  for i in range(18,21):
    cv2.line(img,(shape[i][0],shape[i][1]),(shape[i+1][0],shape[i+1][1]),[255,255,0],2)
  for i in range(23,26):
    cv2.line(img,(shape[i][0],shape[i][1]),(shape[i+1][0],shape[i+1][1]),[255,255,0],2)

# show the output image with the face detections + facial landmarks
cv2_imshow(img)