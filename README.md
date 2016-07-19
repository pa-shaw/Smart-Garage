# Smart-Garage
This contains the code for our smart garage and instructions on how to install the software needed for the project

For this project we used some different open source software.  We used OpenCv, Tesseract-OCR, Leptonica, and openALPR. The first step in our project was getting all of this software installed on the pi. This was particularly difficult, as all of the software had to be compiled from the ground up, not just installed. 

The first step was to install all of the dependent libraries. The steps are in the "Instructions to Compile..." file.
The next step would be to copy the other files (MotionSensor.py, Launcher.sh, webcam.sh) onto the raspberry pi.
Then you will copy the code in "crontab" into your crontab to launch on startup of the pi.

Please take note of how you save the files and what directories you place them in as this will affect various aspects of the code. For the most part, if you save things as they are written here, you won't have many errors.
