import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break
    cv.imshow("Webcam Feed", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv.destroyAllWindows()