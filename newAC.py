import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
from customtkinter import*
import mysql.connector

class NewAC:
    def __init__(self,root3,main_root):
        self.root3=root3
        self.main_root = main_root
        self.root3.geometry("760x500+380+100")
        self.root3.title('login window')
        
        #background image
        bg_img=CTkImage(light_image=Image.open(r"Used Pictures\peak.jpg"),size=(760,500))
                    
        bg_label=CTkLabel(master=self.root3,image=bg_img,text=None)
        bg_label.place(x=0,y=0)

        login_frame=CTkFrame(master=self.root3,width=410,height=500,corner_radius=0,fg_color='black')
        login_frame.place(x=350,y=0)

        logo_img=CTkImage(light_image=Image.open(r'Used Pictures\iitlogo.png'),size=(50,50))

        logo_label=CTkLabel(master=login_frame,image=logo_img,text=None,bg_color='black')
        logo_label.place(x=180,y=40)

        text1=CTkLabel(master=login_frame,text='Create New Account',font=('Arial',15,'bold'),text_color='white',fg_color='black')
        text1.place(x=135,y=105)

        self.user_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Username',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        self.user_entry.place(x=100,y=150)

        self.pswd_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        self.pswd_entry.place(x=100,y=195)

        self.cnfrm_pswd_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Conform Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        self.cnfrm_pswd_entry.place(x=100,y=240)

        #SECUIRITY QUESTION
        self.S_ques_combo=CTkComboBox(master=login_frame,font=('Arial',10),dropdown_font=('Arial',10),text_color='white',dropdown_fg_color='white',dropdown_text_color='black',dropdown_hover_color='#595959',button_hover_color='black',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,state='readonly')
        self.S_ques_combo.configure(values=['Select Security Question','Your favorite color','Your favorite teacher','Your favorite book','Your favorite hobby'])
        self.S_ques_combo.set('Select Security Question')
        self.S_ques_combo.place(x=100,y=290)

        #SECUIRITY ANSWER
        self.S_ans_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Security Answer',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        self.S_ans_entry.place(x=100,y=340)

        #SIGN UP BUTTON
        signIN1_button=CTkButton(master=login_frame,text='Sign Up',command=self.SIGNUP,font=('Arial',10),text_color='black',width=200,corner_radius=8,fg_color='white',hover_color='#595959')
        signIN1_button.place(x=100,y=400)

        text2=CTkLabel(master=login_frame,text='Already have an account ?',compound='left',font=('Arial',9,'bold'),text_color='white',fg_color='black')
        text2.place(x=100,y=440)

        signIN_button=CTkButton(master=login_frame,text='Sign In',command=self.SIGNIN,width=80,corner_radius=8,font=('Arial',9,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#595959')
        signIN_button.place(x=225,y=440)
    def SIGNUP(self):
        try:
            connection=mysql.connector.connect(host="localhost", username="root",password="khanskmk",database="face_recognition_sys")
            cursor_my=connection.cursor()
            query=("select * from student_password where User_name=%s")
            value=(self.user_entry.get(),)
            cursor_my.execute(query,value)
            row=cursor_my.fetchone()
            if row!=None:
                messagebox.showerror("Error!","This username already exitst",parent=self.root3)
            else:
                if self.pswd_entry.get()!=self.cnfrm_pswd_entry.get():
                    messagebox.showerror("Error!","Password and Conform Password are not same",parent=self.root3)
                elif self.S_ques_combo.get()=='Select Security Question' or self.S_ans_entry.get()=='':
                    messagebox.showerror("Error!","Please select security question and answer",parent=self.root3)
                else:
                    query=("insert into student_password values(%s,%s,%s,%s,%s)")
                    S_lower=self.S_ans_entry.get().lower()
                    value=(self.user_entry.get(),self.pswd_entry.get(),self.cnfrm_pswd_entry.get(),self.S_ques_combo.get(),S_lower)
                    cursor_my.execute(query,value)
                    connection.commit()
                    messagebox.showinfo("Success!","Your account has been created successfully",parent=self.root3)
                    # self.root3.destroy()
                    # self.main_root.deiconify()
                    self.SIGNIN()#after creating the account, it will redirect to singin window
            
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root3)
        finally:
            connection.close()

    def SIGNIN(self):
        self.root3.destroy()
        self.main_root.deiconify()




if __name__ == "__main__":
    root3 = CTk()
    obj2 = NewAC(root3,root3)# i have added one extra 'root' here for back button
    root3.mainloop()