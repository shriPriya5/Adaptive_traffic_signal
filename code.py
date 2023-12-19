import cv2
print(cv2.__version__)

cascade_src='vehicle.xml'
video_src='video1.avi'

# Create a VideoCapture object to capture video from the webcam or a video file
cap = cv2.VideoCapture('video1.avi')  # You can also use 0 for the default camera
car_cascade=cv2.CascadeClassifier(cascade_src)

while True:
    # Read a frame from the video source
    ret, frame = cap.read()
    
    if not ret:
        break  # If no frame is captured, exit the loop

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform vehicle detection
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around detected vehicles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(len(cars))

    # Display the frame with vehicle detection
    cv2.imshow('Video', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(33) == 27:
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
