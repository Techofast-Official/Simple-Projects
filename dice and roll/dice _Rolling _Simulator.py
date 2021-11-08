import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title("Roll the Dice")
dice = [r'C:/Users/mrperfect/Desktop/dice and roll/pic/1.png', 'C:/Users/mrperfect/Desktop/dice and roll/pic/2.png',
        'C:/Users/mrperfect/Desktop/dice and roll/pic/3.png', 'C:/Users/mrperfect/Desktop/dice and roll/pic/4.png',
        'C:/Users/mrperfect/Desktop/dice and roll/pic/5.png', 'C:/Users/mrperfect/Desktop/dice and roll/pic/6.png', ]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tkinter.Label(root, image=image1)
label1.image = image1
label1.pack(expand=True)


def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1



if __name__=="__main__":
    root.mainloop()

