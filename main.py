from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2
import tkinter.messagebox

root = Tk()
root.title("OpenCV Filters")
root.geometry("650x230")
root.configure(background='#020003')

image=""
address =StringVar()
def mfileopen():
    global address,image
    file1 = filedialog.askopenfilename()
    global text
    text = open(file1, 'r')
    address= (str(file1))
    image = cv2.imread(address)
    tkinter.messagebox.showinfo("OpenCVFilters", 'Image is selected !')



def GB():
    Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imshow('Gaussian Blurring', Gaussian)
    cv2.waitKey(0)

def MB():
    median = cv2.medianBlur(image, 5)
    cv2.imshow('Median Blurring', median)
    cv2.waitKey(0)

def BB():
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)
    cv2.imshow('Bilateral Blurring', bilateral)
    cv2.waitKey(0)
def Dial():
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(image, kernel, iterations=1)
    img_dilation = cv2.dilate(image, kernel, iterations=1)

    cv2.imshow('Input', image)
    cv2.imshow('Erosion', img_erosion)
    cv2.imshow('Dilation', img_dilation)
    cv2.waitKey(0)

def Threshold():
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)

    thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 5)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)
    cv2.imshow('Adaptive Mean', thresh1)
    cv2.imshow('Adaptive Gaussian', thresh2)
    cv2.imshow('Otsu Threshold', thresh3)

def TT2():
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Binary Threshold Inverted', thresh2)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.imshow('Set to 0', thresh4)
    cv2.imshow('Set to 0 Inverted', thresh5)

button = Button(root, text="Select an Image", command=mfileopen, bg='powder blue',font="Times 12", width=25)
button.place(x=210, y=10)

button1 = Button(root, text="Gaussian Blurring", command=GB,bg='#22ba4a', font="Times 12", width=25)
button1.place(x=70, y=60)

button2 = Button(root, text="Median Blur", command=MB, bg='#22ba4a',font="Times 12", width=25)
button2.place(x=330, y=60)

button3 = Button(root, text="Bilateral Blur", command=BB, bg='#22ba4a',font="Times 12", width=25)
button3.place(x=70, y=100)

button4 = Button(root, text="Dialation", command=Dial, bg='#22ba4a',font="Times 12", width=25)
button4.place(x=330, y=100)

button5 = Button(root, text="Thresholding Techniques", command=Threshold, bg='#22ba4a',font="Times 12", width=25)
button5.place(x=70, y=140)

button6 = Button(root, text="Thresholding Techniques 2", command=TT2, bg='#22ba4a',font="Times 12", width=25)
button6.place(x=330, y=140)

root.mainloop()
