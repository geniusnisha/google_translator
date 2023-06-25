from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
     s=comb_sor.get()
     d=comb_dest.get()
     masg=sor_txt.get(1.0,END)
     textget=change(text=masg,src=s,dest=d)
     dest_txt.delete(1.0,END)
     dest_txt.insert(END,textget)
     
root = Tk()
root.title("Google Translator")
root.geometry("500x500")
root.config(bg="pink")
# heading translator
lab_txt=Label(root,text="Translator",font=("Time New Roman",20,"bold"),bg="red")
lab_txt.place(x= 100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)
# heading source
lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),bg="pink")
lab_txt.place(x=100,y=85,height=50,width=300)
# source text box
sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=140,height=80,width=480)
# list
list_text=list(LANGUAGES.values())

# source combobox
comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=230,height=30,width=75)
comb_sor.set("english")
# translator change button
button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=120,y=230,height=30,width=75)
# destination combobox
comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=230,y=230,height=30,width=75)
comb_dest.set("english")
# destination heading
lab_txt=Label(root,text="dest Text",font=("Time New Roman",20,"bold"),bg="pink")
lab_txt.place(x="40",y="280",height="50",width="450")
# destination text box
dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x="10",y="330",height="90",width="480")


root.mainloop()  