# Smart-Attendance-System-Using-Facial-Recognition
This is a smart attendance system that uses facial recognition to automate and secure the process of taking attendance. It was developed using Python, OpenCV, and Firebase, and is designed to run efficiently on a Raspberry Pi with a connected camera module.

The system detects and recognizes student faces in real-time, matches them with pre-encoded face data, and records their attendance with a timestamp in a Firebase Realtime Database. Student details such as name, registration number, department, level, and starting year are also displayed upon successful recognition.

To maintain privacy, the system avoids storing raw face images and instead uses feature vectors generated from the facial data. It also ensures that duplicate entries are avoided by checking the time interval between consecutive recognitions.

Overall, the project combines machine learning, cloud integration, and edge computing to offer a modern solution for managing attendance in academic environments.
