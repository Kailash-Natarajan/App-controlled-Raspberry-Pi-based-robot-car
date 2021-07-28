# App-controlled-Raspberry-Pi-based-robot-car

This project is a robot car with camera that can be controlled via a mobile app. The video stream from the camera is also visible on the app. This project requires Raspberry Pi with the Pi Camera. The app is designed using MIT App Inventor. 

Raspberry Pi is required to have motion library installed or have an equivalent setup to enable it to stream the video to a specific port on its IP address. The port and IP address have to be specified on the app inventor side.

On the Raspberry Pi, the server code must be running along with motion before opening the app.

The control buttons are named as W,A,S and D for forward, left, reverse and right respectively.

The bot moves as long as a button is pressed.
