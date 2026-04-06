import cv2 as cv

camera = cv.VideoCapture(0)
frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')
record = cv.VideoWriter('record.avi', codec, 30, (frame_width, frame_height))

while True:
    success , image = camera.read()

    if not success:
        print("Failed to grab frame")
        break
    record.write(image)
    cv.imshow("Recording", image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

camera.release()
record.release()
cv.destroyAllWindows()