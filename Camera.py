import cv2

# Try different camera indices (0, 1, 2, ...)
cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not access the camera.")
else:
    print("Camera successfully opened!")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Camera Test", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

