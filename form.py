from tkinter import *
def save_info():
    first_name_info=firstname.get()
    Email_info=Email.get()
    contact_info=contact.get()
    Address_info=Address.get()
    print(first_name_info,Email_info,contact_info,Address_info)

    file=open("user.txt","w")
    file.write("Frist name: "+first_name_info)
    file.write("\n")
    file.write("Email: "+Email_info)
    file.write("\n")
    file.write("Contact: "+ str(contact_info))
    file.write("\n")
    file.write("Address: "+Address_info)
    file.close()

form=Tk()
form.geometry("500x500")
form.title("python form")
label_0 = Label(form, text="Registration form",width=20,font=("bold", 20),bg="yellow")
label_0.place(x=60,y=30)

name=Label(text="Name : ")
Email=Label(text="Email : ")
contact=Label(text="Contact : ")
Address=Label(text="Address: ")


name.place(x=100,y=80)
Email.place(x=100,y=130)
contact.place(x=100, y=180)
Address.place(x=100, y=230)

firstname=StringVar()
Email=StringVar()
contact=IntVar()
Address=StringVar()

name_entry=Entry(textvariable= firstname,width="30")
Email_entry=Entry(textvariable= Email,width="30")
contact_entry=Entry(textvariable=contact,width="30")
Address_entry=Entry(textvariable=Address,width="30")

name_entry.place(x=100, y=100)
Email_entry.place(x=100,y=150)
contact_entry.place(x=100,y=200)
Address_entry.place(x=100, y=250)

button=Button(form,text="Submit",command=save_info,width="15", height="1", bg="brown")
button.place(x=100, y=300)


mainloop()