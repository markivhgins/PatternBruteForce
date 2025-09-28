import pyautogui
import time
import itertools


DOT_COORDINATES = {
    1: (1177, 489),
    2: (1306, 488),
    3: (1436, 484),
    4: (1174, 620),
    5: (1303, 615),
    6: (1434, 618),
    7: (1175, 749),
    8: (1306, 746),
    9: (1434, 749),
}

# Coordinate for the "Clear" or "Erase" button
CLEAR_BUTTON_COORD = (1032, 838)

# Configuration settings (You can adjust these if needed)
DRAWING_SPEED = 0.05       # Speed the mouse moves between dots (Lower is faster)
DELAY_AFTER_CLEAR = 0.5    # Pause after clicking the clear button
DELAY_AFTER_SUBMIT = 1.5   # Pause to allow the webpage to process the pattern


ALL_PATTERNS = []

def generate_patterns():
    """Generates all unique pattern sequences from 4 to 9 dots long."""
    print("Generating all patterns (4 to 9 dots)...")
    
    # Generates all unique sequences (permutations) of dots for lengths 4 through 9.
    for length in range(4, 10):
        for pattern in itertools.permutations(range(1, 10), length):
            ALL_PATTERNS.append(list(pattern))
    
    print(f"Generated {len(ALL_PATTERNS)} total patterns.")

def draw_pattern(pattern_list):
    """Uses PyAutoGUI to simulate a mouse drag for a single pattern."""
    
    # 1. Move to the first dot and press the mouse button
    first_x, first_y = DOT_COORDINATES[pattern_list[0]]
    pyautogui.moveTo(first_x, first_y, duration=0.1)
    pyautogui.mouseDown()
    
    # 2. Drag to the remaining dots
    for dot_index in pattern_list[1:]:
        x, y = DOT_COORDINATES[dot_index]
        pyautogui.moveTo(x, y, duration=DRAWING_SPEED)
        
    # 3. Release the mouse button to submit
    pyautogui.mouseUp()

def run_bruteforce():
    generate_patterns()
    

    print("\nStarting in 10 seconds.")
    print("POSITION THE WEBPAGE CORRECTLY and DO NOT MOVE YOUR MOUSE OR RESIZE THE WINDOW.")
    time.sleep(10)
    
    clear_x, clear_y = CLEAR_BUTTON_COORD

    for i, pattern in enumerate(ALL_PATTERNS):
        print(f"Attempt {i+1} of {len(ALL_PATTERNS)}: Pattern {pattern}")

        draw_pattern(pattern)

        # Wait for the webpage to process the input
        time.sleep(DELAY_AFTER_SUBMIT) 

        # 4. Click the Clear Button
        pyautogui.click(clear_x, clear_y)
        
        # Pause before the next attempt
        time.sleep(DELAY_AFTER_CLEAR) 
        
        

if __name__ == "__main__":
    # IMPORTANT: You must press Ctrl+C in the terminal immediately when the page unlocks!
    run_bruteforce()