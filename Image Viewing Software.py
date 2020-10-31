from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewing Software")

my_image0=ImageTk.PhotoImage(Image.open('icon.png'))
my_image1=ImageTk.PhotoImage(Image.open('house.png'))
my_image2=ImageTk.PhotoImage(Image.open('+.png'))
my_image3=ImageTk.PhotoImage(Image.open('arrow.png'))
my_image4=ImageTk.PhotoImage(Image.open('xs.png'))


image_list=[my_image0,my_image1,my_image2,my_image3,my_image4]

my_label=Label(image=image_list[0])
my_label.grid(row=0,column=0,columnspan=3)

def back(image_number):
    global my_label
    global btn_foward
    global btn_backwards

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    foward_btn = Button(root, text=">>", command=lambda: foward(image_number + 1))
    back_btn = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == 1:
        back_btn = Button(root, text="<<", state=DISABLED)

    back_btn.grid(row=1, column=0)
    foward_btn.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    label_bar = Label(root, text=f'Image {str(image_number)} of {str(len(image_list))}', bd=1, relief=SUNKEN, anchor=E)
    label_bar.grid(row=2, column=0, columnspan=3, pady=10)  # sticky,anchor is used to position within a cell


def foward(image_number):
    global my_label
    global btn_foward
    global btn_backwards

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    foward_btn = Button(root, text=">>", command=lambda: foward(image_number+1))
    back_btn = Button(root, text="<<", command=lambda:back(image_number-1))
    if image_number==5:
        foward_btn=Button(root, text=">>",state=DISABLED)

    label_bar = Label(root, text=f'Image {str(image_number)} of {str(len(image_list))}', bd=1, relief=SUNKEN, anchor=E)
    label_bar.grid(row=2, column=0, columnspan=3, pady=10)  # sticky,anchor is used to position within a cell

    back_btn.grid(row=1, column=0)

    foward_btn.grid(row=1, column=2)


    my_label.grid(row=0,column=0,columnspan=3)



back_btn=Button(root,text="<<",command=back,state=DISABLED)
exit_btn=Button(root,text="EXIT PROGRAM",command=root.quit)
foward_btn=Button(root,text=">>",command=lambda:foward(2))

#POSITIONING
back_btn.grid(row=1,column=0)
exit_btn.grid(row=1,column=1)
foward_btn.grid(row=1,column=2)



#ADDING STATUS BAR

label_bar=Label(root, text=f'Image 1 of {str(len(image_list))}',bd=1,relief=SUNKEN,anchor=E)
label_bar.grid(row=2,column=0,columnspan=3,pady=10)#sticky,anchor is used to position within a cell




root.mainloop()