import win32api,win32con
from time import sleep
  
def get_keys(): # Get all the keys pressed since last loop iteration    
    global keypresses 
    keypresses = win32api.GetKeyState() # Store current state of keyboard in a list variable        
      
# Define how often to save keystrokes
interval=10  
for i in range(5):
    with open('keyboard_activity.txt', 'a') as f: 
        for j in keypresses[i]: # Store each pressed keys into a list variable        
            print (j, end=' ')# Print all the keystrokes to screen    
      
sleep(interval)
