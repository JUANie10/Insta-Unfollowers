# Programs runs 11/19/2020. If the front-end of instagram changes, this script might not work.

from Web_automation import InstaAnalyzer
from App import GUI
import tkinter as tk

#Main Function
def main():
    tkWindow = tk.Tk()
    Screen = GUI(tkWindow)
    print("made it")
    tkWindow.mainloop()

if __name__ == "__main__":
    main()