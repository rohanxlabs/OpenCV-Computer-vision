import cv2 as cv

image = cv.imread('Photos/park.jpg')

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Image not loaded. Please check the file path.")