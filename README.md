# PatternBruteForce
This repository contains Python scripts designed for the recovery of a forgotten pattern lock on a 3x3 grid interface (e.g., a web security challenge).

.
.
.
.
.

Prerequisites
You must have Python installed on your system. Install the required library via pip:

Bash

pip pip install pyautogui
Step 1: Run the Coordinate Finder
Before running the main script, you must define the location of the pattern lock elements on your screen.

Open the target webpage in your browser and adjust the window so the pattern grid and Clear button are fully visible. DO NOT move or resize the window after this step.

Run the coordinate finder script in your terminal: python find_coord.py

When the 5-second countdown starts, quickly move your mouse cursor over the first element (e.g., Dot 1, Top Left) and keep it still until the coordinates are printed.

Repeat this process 10 times to record the X and Y coordinates for all 9 dots and the Clear button. 
(The lock I was trying to unlock had a clear button after every failed attempt, edit it or delete it or whatevr)

Element	Example Coordinates
Dot 1 (Top Left)	(1177, 489)
Dot 5 (Center)	(1303, 615)
Clear Button	(1032, 838) 

Step 2: Configure the Main Script
Open the bruteforce_web_final.py file and update the DOT_COORDINATES and CLEAR_BUTTON_COORD variables with the 10 sets of coordinates you collected in Step 1.

Step 3: Execute the Brute-Force
Ensure the target webpage is the focused window and is positioned exactly where it was during coordinate capture.

Run the main script from your terminal: python bruteforce_web_final.py

Step 4: The script will pause for 10 seconds before starting. After it begins, DO NOT touch your mouse or keyboard. Watch the screen and be prepared to immediately press Ctrl + C in your terminal the moment the correct pattern is found and the lock is bypassed. The script will be stopped, and the last pattern sequence printed in the terminal is your solution.
