# Virtual Calculator

## Overview

This project features a virtual calculator with a user-friendly interface, utilizing Python's tkinter library for the UI and OpenCV for hand tracking to simulate button clicks. Users can perform basic arithmetic operations using intuitive hand gestures.

## Features

- **User Interface:** The calculator's graphical interface, built with the tkinter library, provides a visually appealing and interactive experience.

- **Virtual Calculator:** Implemented in a separate module (`VirtualCal.py`), this functionality uses the OpenCV library to track hand gestures and simulate button clicks.

- **Instructions:** The application includes a dedicated instruction window to guide users on efficiently using the virtual calculator.

## Usage

1. Run the `User Interface` script to open the main window.
2. Navigate through the options:
   - Click on **"View Instructions"** to learn how to use the virtual calculator.
   - Click on **"Go to the Calculator"** to launch the virtual calculator.
   - Click on **"Exit"** to close the application.

3. In the virtual calculator:
   - Perform hand gestures to simulate button clicks.
   - Use fingers to interact with the calculator buttons.

4. Press **'c'** on the keyboard to stop the calculator and close the window.

## Dependencies

- **tkinter:** Python's standard GUI (Graphical User Interface) package.
- **PIL:** Python Imaging Library for working with images.
- **cv2 (OpenCV):** Open Source Computer Vision library for hand tracking and gesture recognition.
- **cvzone:** A computer vision library used for additional hand tracking functionalities.


