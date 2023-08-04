import cv2
from pytube import YouTube

# Replace 'your_video_url' with the actual YouTube video URL.
video_url = 'https://www.youtube.com/watch?v=zY0X-9tN7OU'

# Create a YouTube object
yt = YouTube(video_url)

# Get the best video stream available (usually the highest resolution)
video_stream = yt.streams.filter(file_extension='mp4').first()

# Get the frame rate of the video
frame_rate = int(video_stream.fps)

# Create a VideoCapture object to read video stream
video_capture = cv2.VideoCapture(video_stream.url)

# Check if the video stream was opened successfully
if not video_capture.isOpened():
    print("Error opening video stream.")
    exit()

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Show the frame using OpenCV
    cv2.imshow('YouTube Video', frame)

    # Set the frame rate (time delay in milliseconds between frames)
    delay = int(1000 / frame_rate)

    # Press 'q' to quit the video
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
video_capture.release()
cv2.destroyAllWindows()