from tkinter import *
 
root=Tk()
root.title("Messages")
root.configure(bg='peach puff')

root.geometry("600x400")

name_var=StringVar()
passw_var=StringVar()
msg_var=StringVar()
to_var=StringVar()
message = msg_var.get()


def encrypt_button():
    newWindow2 = Toplevel(root)
    newWindow2.title("Encryption")
    newWindow2.geometry("600x400")
    newWindow2.configure(bg='peach puff')
    s=3
    newmsg=msg_var.get()
    ciper=encrypted(newmsg,s)
    decryptedmsg=decrypted(ciper,s)
    encry = Label(newWindow2, text = "The encrypted text is: ",font=('calibre',12),bg='peach puff')
    encryptedtext = Label(newWindow2, text = ciper, font=('calibre',12,'bold'),bg="peach puff")
    decry = Label(newWindow2, text = "The decrypted text is: ",font=('calibre',12),bg="peach puff")
    decryptedtext = Label(newWindow2, text = decryptedmsg, font=('calibre',12,'bold'),bg="peach puff")
    encry.grid(row=0,column=0)
    encryptedtext.grid(row=1,column=0)
    decry.grid(row=2,column=0)
    decryptedtext.grid(row=3,column=0)
    
def send():
    newWindow=Toplevel(root)
    newWindow.title("Sent Status")
    newWindow.geometry("200x200")
    newWindow.configure(bg='peach puff')
    msg=Label(newWindow,text="Message sent",font=('bold'),bg="peach puff")
    ok=Button(newWindow,text = 'OK',command=newWindow.destroy)
    ok.grid(row=1,column=2)    
    msg.grid(row=0,column=1)

   
 

def submit():
    name=name_var.get()
    password=passw_var.get()
    message = msg_var.get()
    toadd=to_var.get()
    s=3
 
   
    if name == 'abcde123@school.com' and password == '123456':
        newWindow = Toplevel(root)
        newWindow.title("Message")
        newWindow.configure(bg='peach puff')
        newWindow.geometry("600x400")
        w=Label(newWindow,
              text ="Access Granted",font=('calibre',12, 'bold'),bg="peach puff")
        msg = Label(newWindow, text = 'Message', font=('calibre',12, 'bold'),bg="peach puff")

        msg_entry = Entry(newWindow,text = msg_var,  font=('calibre',12,'normal'))

        to = Label(newWindow, text = 'To', font=('calibre',12, 'bold'),bg="peach puff")

        to_entry = Entry(newWindow,textvariable =to_var , font=('calibre',12,'normal'))
        send_btn=Button(newWindow,text = 'Send',command=send)
        
        encry_btn=Button(newWindow,text = 'Encrypt',command = encrypt_button)
        
        

        w.grid(row=0,column=1)
        to.grid(row=1,column=0)
        to_entry.grid(row=1,column=1)
        msg.grid(row=2,column=0)
        msg_entry.grid(row=2,column=1)
        send_btn.grid(row=3,column=1)
        encry_btn.grid(row=4,column=1) 
       
             
       
    elif name == 'alphabets@number.com' and password == '98765':
       newWindow = Toplevel(root)
       newWindow.title("Message")
       newWindow.geometry("600x400")
       newWindow.configure(bg='peach puff')
       w=Label(newWindow,
               text ="Access Granted",font=('calibre',12, 'bold'),bg="peach puff")
       msg = Label(newWindow, text = 'Message', font=('calibre',12, 'bold'),bg="peach puff")
       msg_entry = Entry(newWindow,textvariable = msg_var,  font=('calibre',12,'normal'))
       to = Label(newWindow, text = 'To', font=('calibre',12, 'bold'),bg="peach puff")
       encry_btn=Button(newWindow,text = 'Encrypt',command = encrypt_button)
       to_entry = Entry(newWindow,textvariable =to_var , font=('calibre',12,'normal'))
       send_btn=Button(newWindow,text = 'Send',command=send)
       w.grid(row=0,column=1)
       to.grid(row=1,column=0)
       to_entry.grid(row=1,column=1)
       msg.grid(row=2,column=0)
       msg_entry.grid(row=2,column=1)
       encry_btn.grid(row=4,column=1)
       send_btn.grid(row=3,column=1)

       
       
    else:
        newWindow = Toplevel(root)
        newWindow.title("Message")
        newWindow.geometry("600x400")
        newWindow.configure(bg='peach puff')
        w=Label(newWindow,
              text ="Access Denied",font=('calibre',12, 'bold'),bg="peach puff").pack()
        w.pack(pady = 10)
     
    name_var.set("")
    passw_var.set("")

   
   
def encrypted(string,shift):
    ciper=''
    for char in string:
        if char==' ':
            ciper=ciper+char
        elif char.isupper():
            ciper=ciper+chr((ord(char)+shift-65)%26+65)
        else:
            ciper=ciper+chr((ord(char)+shift-97)%26+97)
    return ciper
def decrypted(string,shift):
    code=''
    for char in string:
        if char==' ':
            code=code+char
        elif char.isupper():
            code=code+chr((ord(char)-shift-65)%26+65)
        else:
            code=code+chr((ord(char)-shift-97)%26+97)
    return code

name_label = Label(root, text = 'Username', font=('calibre',12, 'bold'),bg="peach puff")
 
name_entry = Entry(root,textvariable = name_var, font=('calibre',12,'normal'))
 
passw_label = Label(root, text = 'Password', font = ('calibre',12,'bold'),bg="peach puff")

passw_entry=Entry(root, textvariable = passw_var, font = ('calibre',12,'normal'), show = '*')

sub_btn=Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)


root.mainloop()
