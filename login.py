from tkinter import*
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #====All images=====


root = Tk()
obj = Login_System(root)
root.mainloop()