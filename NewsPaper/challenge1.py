# making a newspaper
from datetime import datetime
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("guglani's newspaper")
root.geometry("3840x2160")
#root.maxsize(3840,2160)
#root.minsize(3840,2160)
labe1=Label(text="GUGLANI'S NEWSPAPER",font="comicsansms 22 bold")
labe1.pack()
label2=Label(text=f"Date {datetime.now().date()}",font="comicsansns 19 bold")

label2.pack()
sam1=Label(text="KNOWLEDGE ABOUT FRUITS",bg="red",fg="white",font="comicsansms 25 bold",pady=7,padx=3840)
sam1.pack(side=TOP,pady=15)

scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)

image=Image.open("pngs/fruit.jpg")
photo=ImageTk.PhotoImage(image)
sam_label=Label(image=photo)
sam_label.pack(side=TOP,pady=22)
# photo1=PhotoImage(file="pngs/water-drop.png")
# sam_label=Label(image=photo1,bg="pink",fg="blue",font=1)
# sam_label.pack(side=TOP,anchor="n",pady=1190)
#
# image1=Image.open("pngs/fruits1(1).jpg")
# photo1=ImageTk.PhotoImage(image1)
# sam_label=Label(image=photo1)
# sam_label.pack(side=LEFT,anchor="e",pady=280,padx=24)


gugu1=Label(root,text="In botany, a fruit is the seed-bearing structure in flowering plants (also known as angiosperms) formed from the ovary after flowering"
" \n            Fruits are the means by which angiosperms disseminate seeds. "
"\n             In particular, have propagated with the movements of humans and animals in a symbiotic relationship as a means for seed dispersal;"
"\n             in fact, humans and many animals have become dependent on fruits as a source of food.[1] Accordingly, "
"\n             fruits account for a substantial fraction of the world's agricultural output,' "
        " \n    and some (such as the apple and the pomegranate) have acquired extensive cultural and symbolic meanings.",font="comicsansms 17 bold",bg="black",fg="white",
           )
gugu1.pack(fill=BOTH)






root.mainloop()
