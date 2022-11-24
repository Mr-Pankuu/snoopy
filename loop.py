import pyautogui as pg
import time
print("Starting in 10 sec:")
time.sleep(10)
for i in range(999):
    pg.write("Pahuch gaya hu:")
    pg.press("Enter")