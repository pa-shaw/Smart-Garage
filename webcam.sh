fswebcam -r 1280x720 --no-banner /home/pi/webcam/plate.JPG
/home/pi/openalpr/src/alpr -n 5 -j /home/pi/webcam/plate.JPG > /home/pi/webcam/results.json
