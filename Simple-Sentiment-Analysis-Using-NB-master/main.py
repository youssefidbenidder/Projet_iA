from tkinter import *

from classifier import get_classifier
from preprocess import creation_list_mots
from preprocess import process

root = Tk()
root.wm_title("Application d'analyse de sentiments")

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

l1 = Label(top_frame, text='entrer votre texte')
l1.pack(side=LEFT)

w = Text(top_frame, height=3)
w.pack(side=LEFT)

clf = get_classifier()


def main_op():
    review_spirit = w.get('1.0', END)
    demo = process(review_spirit)

    demo1 = creation_list_mots(demo)
    demo2 = ('sentiment est ' + clf.classify(demo1))
    l2 = Label(bottom_frame, text=demo2)
    l2.pack()


button = Button(bottom_frame, text='Analyse', command=main_op)
button.pack(side=BOTTOM)

root.mainloop()
