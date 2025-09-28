import pyautogui
import time

def get_position():
    """Prints the current mouse cursor position after a 5-second delay."""
    print('\nStarting countdown...')
    print('Move your mouse over the desired element (dot or button) NOW.')
    time.sleep(5)
    
    x, y = pyautogui.position()
    print(f"--- 🎯 Found Coordinate: X={x}, Y={y} ---")
    return x, y

if __name__ == "__main__":
    print("Welcome to the Coordinate Finder.")
    print("You need to run this script 10 times (9 dots + 1 Clear Button).")
    
    get_position()