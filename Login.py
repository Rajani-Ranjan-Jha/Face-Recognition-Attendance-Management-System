from PIL import Image
from tkinter import messagebox
from customtkinter import*#"pip install customtkinter"
from main_STUDENT import FaceRecognitionSystem1 #for login as student
from main_ADMIN import FaceRecognitionSystem2 #for login as admin
from newAC import NewAC #importing class NewAC from file newAC
import mysql.connector #connecting to the database


root1=CTk()
root1.title('login window')
root1.geometry("760x500+380+100")
root1.resizable(FALSE,FALSE)



def create_AC():
    create_window=CTkToplevel(root1)
    app=NewAC(create_window,root1)
    root1.withdraw()
    

def main_window1():
    new_window=CTkToplevel(root1)
    app=FaceRecognitionSystem1(new_window)
    root1.withdraw()

def forget_password_student():
    root4=CTkToplevel(root1)
    root4.geometry("760x500+380+100")
    root4.title('Forgot Passowrd')


    def BACK():
        root4.destroy()
        root1.deiconify()
    def RESET():
        try:
            connection=mysql.connector.connect(host="localhost", username="root",password="khanskmk",database="face_recognition_sys")
            cursor_my=connection.cursor()
            query = ("select * from student_password where User_name=%s and S_Question=%s")
            value = (forgot_password_entry.get(), S_ques_combo.get())
            cursor_my.execute(query, value)
            row = cursor_my.fetchone()
            
            if forgot_password_entry.get()=='' or S_ques_combo.get() == "Select Security Question" or S_ans_entry.get() == "" or new_entry.get()=='' or cnfrm_entry.get()=='':
                messagebox.showerror("Error!", "All fields are required!", parent=root4)
            else:
                if row is None:
                    messagebox.showerror("Error!", "The username or sequrity question doesn't exist", parent=root4)
                else:
                    if row[4] != S_ans_entry.get().lower():
                        messagebox.showerror("Invalid Security Answer !", "You have entered wrong security answer", parent=root4)
                    elif new_entry.get()!=cnfrm_entry.get():
                        messagebox.showerror("Error!", "New Passwords must be same", parent=root4)
                    else:
                        queryF = ("update student_password set Password=%s, C_Password=%s where User_name=%s and S_Question=%s and S_Answer=%s")
                        valueF = (new_entry.get(), cnfrm_entry.get(), forgot_password_entry.get(), S_ques_combo.get(), S_ans_entry.get().lower())
                        cursor_my.execute(queryF, valueF)
                        connection.commit()
                        messagebox.showinfo("Success!", "Your password has been reset successfully", parent=root4)
                        #after forgetting password it will destroy forgot password window and deiconify the login window
                        # root4.destroy()
                        # root1.deiconify()
                        BACK()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=root4)
        finally:
            connection.close()

    #background image
    bg_img=CTkImage(light_image=Image.open(r"Used Pictures\peak.jpg"),size=(760,500))
                    
    bg_label=CTkLabel(master=root4,image=bg_img,text=None)
    bg_label.place(x=0,y=0)

    login_frame=CTkFrame(master=root4,width=410,height=500,corner_radius=0,fg_color='black')
    login_frame.place(x=350,y=0)

    logo_img=CTkImage(light_image=Image.open(r'Used Pictures\iitlogo.png'),size=(50,50))

    logo_label=CTkLabel(master=login_frame,image=logo_img,text=None,bg_color='black')
    logo_label.place(x=180,y=40)

    #GO BACK
    back_img=CTkImage(light_image=Image.open(r'Used Pictures\left.png'),size=(30,30))
    back_button=CTkButton(master=login_frame,command=BACK,width=0,height=0,border_width=0,corner_radius=0,border_spacing=0,image=back_img,text=None,bg_color='black',fg_color='black',hover_color='white')
    back_button.place(x=0,y=0)

    text1=CTkLabel(master=login_frame,text='Reset Password',font=('Arial',15,'bold'),text_color='white',fg_color='black')
    text1.place(x=140,y=100)

    #USERNAME
    forgot_password_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Username',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
    forgot_password_entry.place(x=100,y=150)

    #SECUIRITY QUESTION
    S_ques_combo=CTkComboBox(master=login_frame,font=('Arial',10),dropdown_font=('Arial',10),text_color='white',dropdown_fg_color='white',dropdown_text_color='black',dropdown_hover_color='#595959',button_hover_color='black',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,state='readonly')
    S_ques_combo.configure(values=['Select Security Question','Your favorite color','Your favorite teacher','Your favorite book','Your favorite hobby'])
    S_ques_combo.set('Select Security Question')
    S_ques_combo.place(x=100,y=200)

    #SECUIRITY ANSWER
    S_ans_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Security Answer',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
    S_ans_entry.place(x=100,y=240)

    #NEW PASSWORD AND CONFORM NEW PASSWORD
    new_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Enter New Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
    new_entry.place(x=100,y=290)

    cnfrm_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Conform New Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
    cnfrm_entry.place(x=100,y=330)

    signIN1_button=CTkButton(master=login_frame,text='Reset Password',command=RESET,font=('times new romal',10),text_color='black',width=200,corner_radius=8,fg_color='white',hover_color='#595959')
    signIN1_button.place(x=100,y=400)


    root1.withdraw()
    root4.mainloop()

# TO OPEN A NEW WINDOW IF THE USER IS AN ADMINISTRATOR
def the_administrator():
    root2=CTkToplevel(root1)
    root2.geometry("760x500+380+100")
    root2.title('login window')

    def main_window2():
        new_window2=CTkToplevel(root2)
        app=FaceRecognitionSystem2(new_window2)
        root2.withdraw()

    def forget_password_admin():
        root4=CTkToplevel(root2)
        root4.geometry("760x500+380+100")
        root4.title('Forgot Passowrd')

        def BACK():
            root4.destroy()
            root2.deiconify()

        def RESET():
            try:
                connection=mysql.connector.connect(host="localhost", username="root",password="khanskmk",database="face_recognition_sys")
                cursor_my=connection.cursor()
                query = ("select * from admin_password where User_name=%s and S_Question=%s")
                value = (forgot_password_entry.get(), S_ques_combo.get())
                cursor_my.execute(query, value)
                row = cursor_my.fetchone()
                
                if forgot_password_entry.get()=='' or S_ques_combo.get() == "Select Security Question" or S_ans_entry.get() == "" or new_entry.get()=='' or cnfrm_entry.get()=='':
                    messagebox.showerror("Error!", "All fields are required!", parent=root4)
                else:
                    if row is None:
                        messagebox.showerror("Error!", "The username or sequrity question doesn't exist", parent=root4)
                    else:
                        if row[4] != S_ans_entry.get().lower():
                            messagebox.showerror("Invalid Security Answer !", "You have entered wrong security answer", parent=root4)
                        elif new_entry.get()!=cnfrm_entry.get():
                            messagebox.showerror("Error!", "New Passwords must be same", parent=root4)
                        else:
                            queryF = ("update admin_password set Password=%s, C_Password=%s where User_name=%s and S_Question=%s and S_Answer=%s")
                            valueF = (new_entry.get(), cnfrm_entry.get(), forgot_password_entry.get(), S_ques_combo.get(), S_ans_entry.get().lower())
                            cursor_my.execute(queryF, valueF)
                            connection.commit()
                            messagebox.showinfo("Success!", "Your password has been reset successfully", parent=root4)
                            #after forgetting password it will destroy forgot password window and deiconify the login window
                            # root4.destroy()
                            # root1.deiconify()
                            BACK()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=root4)
            finally:
                connection.close()

        #background image
        bg_img=CTkImage(light_image=Image.open(r"Used Pictures\peak.jpg"),size=(760,500))
                        
        bg_label=CTkLabel(master=root4,image=bg_img,text=None)
        bg_label.place(x=0,y=0)

        login_frame=CTkFrame(master=root4,width=410,height=500,corner_radius=0,fg_color='black')
        login_frame.place(x=350,y=0)

        logo_img=CTkImage(light_image=Image.open(r'Used Pictures\iitlogo.png'),size=(50,50))

        logo_label=CTkLabel(master=login_frame,image=logo_img,text=None,bg_color='black')
        logo_label.place(x=180,y=40)

        #GO BACK
        back_img=CTkImage(light_image=Image.open(r'Used Pictures\left.png'),size=(30,30))
        back_button=CTkButton(master=login_frame,command=BACK,width=0,height=0,border_width=0,corner_radius=0,border_spacing=0,image=back_img,text=None,bg_color='black',fg_color='black',hover_color='white')
        back_button.place(x=0,y=0)

        text1=CTkLabel(master=login_frame,text='Reset Password',font=('Arial',15,'bold'),text_color='white',fg_color='black')
        text1.place(x=140,y=100)

        #USERNAME
        forgot_password_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Username',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        forgot_password_entry.place(x=100,y=150)

        #SECUIRITY QUESTION
        S_ques_combo=CTkComboBox(master=login_frame,font=('Arial',10),dropdown_font=('Arial',10),text_color='white',dropdown_fg_color='white',dropdown_text_color='black',dropdown_hover_color='#595959',button_hover_color='black',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,state='readonly')
        S_ques_combo.configure(values=['Select Security Question','Your favorite color','Your favorite teacher','Your favorite book','Your favorite hobby'])
        S_ques_combo.set('Select Security Question')
        S_ques_combo.place(x=100,y=200)

        #SECUIRITY ANSWER
        S_ans_entry=CTkEntry(master=login_frame,font=('Arial',10),placeholder_text='Security Answer',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        S_ans_entry.place(x=100,y=240)

        new_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Enter New Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        new_entry.place(x=100,y=290)

        cnfrm_entry=CTkEntry(master=login_frame,font=('times new romal',10),placeholder_text='Conform New Password',placeholder_text_color='gray',text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8)
        cnfrm_entry.place(x=100,y=330)

        signIN1_button=CTkButton(master=login_frame,text='Reset Password',command=RESET,font=('times new romal',10),text_color='black',width=200,corner_radius=8,fg_color='white',hover_color='#595959')
        signIN1_button.place(x=100,y=400)


        root2.withdraw()
        root4.mainloop()

    def login_admin():
        try:
            connection = mysql.connector.connect(host="localhost", username="root", password="khanskmk", database="face_recognition_sys")
            cursor_my = connection.cursor()
            
            if '@iitp.ac.in' not in admin_login_entry.get():
                query = ("select * from admin_password where `User_name`=%s")
                value = (admin_login_entry.get()+'@iitp.ac.in',)
                cursor_my.execute(query, value)
                row = cursor_my.fetchone()
                # Check if username and password fields are empty
                if admin_login_entry.get() == "" or password_entry.get() == "":
                    messagebox.showerror("Error!", "All fields are required!", parent=root1)
                
                else:
                    if row is None:
                        messagebox.showerror("Error!", "This username doesn't exist", parent=root1)
                    else:
                        # Check if password is correct
                        if row[1] != password_entry.get():
                            messagebox.showerror("Invalid Password !", "You have entered wrong password", parent=root1)
                        else:
                            # If username and password are correct, open main_window2
                            main_window2()

            else:
                query = ("select * from admin_password where `User_name`=%s")
                value = (admin_login_entry.get(),)
                cursor_my.execute(query, value)
                row = cursor_my.fetchone()
                # Check if username and password fields are empty
                if admin_login_entry.get() == "" or password_entry.get() == "":
                    messagebox.showerror("Error!", "All fields are required!", parent=root1)
                
                else:
                    if row is None:
                        messagebox.showerror("Error!", "This username doesn't exist", parent=root1)
                    else:
                        # Check if password is correct
                        if row[1] != password_entry.get():
                            messagebox.showerror("Invalid Password !", "You have entered wrong password", parent=root1)
                        else:
                            # If username and password are correct, open main_window2
                            main_window2()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=root1)
        finally:
            connection.close()
    
    def sing_in():
         root2.destroy()
         root1.deiconify()

    #background image
    bg_img=CTkImage(light_image=Image.open(r"Used Pictures\peak.jpg"),size=(760,500))
                
    bg_label=CTkLabel(master=root2,image=bg_img,text=None)
    bg_label.place(x=0,y=0)

    login_frame=CTkFrame(master=root2,width=410,height=500,corner_radius=0,fg_color='black')
    login_frame.place(x=350,y=0)

    logo_img=CTkImage(light_image=Image.open(r'Used Pictures\iitlogo.png'),size=(50,50))

    logo_label=CTkLabel(master=login_frame,image=logo_img,text=None,bg_color='black')
    logo_label.place(x=180,y=40)

    text1=CTkLabel(master=login_frame,text='Login as Administrator',font=('Arial',15,'bold'),text_color='white',fg_color='black')
    text1.place(x=125,y=110)

    admin_login_entry=CTkEntry(master=login_frame,font=('Arial',11),text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,placeholder_text='Username',placeholder_text_color='gray')
    admin_login_entry.place(x=100,y=160)

    password_entry=CTkEntry(master=login_frame,font=('Arial',11),text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,placeholder_text='Password',placeholder_text_color='gray')
    password_entry.place(x=100,y=210)

    forgot_button=CTkButton(master=login_frame,text='Forgot Password?',command=forget_password_admin,font=('Arial',10,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#595959')
    forgot_button.place(x=190,y=240)

    #___SIGN IN BUTTON
    signIN1_button=CTkButton(master=login_frame,text='Sign In',command=login_admin,font=('Arial',11),text_color='black',width=200,corner_radius=8,fg_color='white',hover_color='#595959')
    signIN1_button.place(x=100,y=300)

    text2=CTkLabel(master=login_frame,text='Are you a Student ?',compound='left',font=('Arial',10,'bold'),text_color='white',fg_color='black')
    text2.place(x=80,y=350)

    signIN_button=CTkButton(master=login_frame,text='Sign In as Student',command=sing_in,font=('Arial',10,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#595959')
    signIN_button.place(x=205,y=350)

    root1.withdraw()
    root2.mainloop()


def login_student():
    try:
        connection = mysql.connector.connect(host="localhost", username="root", password="khanskmk", database="face_recognition_sys")
        cursor_my = connection.cursor()

        if '@iitp.ac.in' not in student_login_entry.get():
            query = ("select * from student_password where `User_name`=%s")
            value = (student_login_entry.get()+'@iitp.ac.in',)
            cursor_my.execute(query, value)
            row = cursor_my.fetchone()
            # Check if username and password fields are empty
            if student_login_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror("Error!", "All fields are required!", parent=root1)
            
            else:
                if row is None:
                    messagebox.showerror("Error!", "This username doesn't exist", parent=root1)
                else:
                    # Check if password is correct
                    if row[1] != password_entry.get():
                        messagebox.showerror("Invalid Password !", "You have entered wrong password", parent=root1)
                    else:
                        # If username and password are correct, open main_window1
                        main_window1()

        else:
            query = ("select * from student_password where `User_name`=%s")
            value = (student_login_entry.get(),)
            cursor_my.execute(query, value)
            row = cursor_my.fetchone()
            # Check if username and password fields are empty
            if student_login_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror("Error!", "All fields are required!", parent=root1)

            else:
                if row is None:
                    messagebox.showerror("Error!", "This username doesn't exist", parent=root1)
                else:
                    # Check if password is correct
                    if row[1] != password_entry.get():
                        messagebox.showerror("Invalid Password !", "You have entered wrong password", parent=root1)
                    else:
                        # If username and password are correct, open main_window1
                        main_window1()
    except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=root1)
    finally:
        connection.close()

#background image
bg_img=CTkImage(light_image=Image.open(r"Used Pictures\peak.jpg"),size=(760,500))
        
bg_label=CTkLabel(master=root1,image=bg_img,text=None)
bg_label.place(x=0,y=0)

login_frame=CTkFrame(master=root1,width=410,height=500,corner_radius=0,fg_color='black')
login_frame.place(x=350,y=0)

logo_img=CTkImage(light_image=Image.open(r'Used Pictures\iitlogo.png'),size=(50,50))

logo_label=CTkLabel(master=login_frame,image=logo_img,text=None,bg_color='black')
logo_label.place(x=180,y=40)

text1=CTkLabel(master=login_frame,text='Login as Student',font=('Arial',15,'bold'),text_color='white',fg_color='black')
text1.place(x=145,y=110)

student_login_entry=CTkEntry(master=login_frame,font=('Arial',11),text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,placeholder_text='Username',placeholder_text_color='gray')
student_login_entry.place(x=100,y=160)

password_entry=CTkEntry(master=login_frame,font=('Arial',11),text_color='white',fg_color='black',border_width=1,border_color='white',width=200,corner_radius=8,placeholder_text='Password',placeholder_text_color='gray')
password_entry.place(x=100,y=210)

forgot_button=CTkButton(master=login_frame,text='Forgot Password?',command=forget_password_student,font=('Arial',10,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#595959')
forgot_button.place(x=190,y=240)

#___SIGN IN BUTTON
signIN1_button=CTkButton(master=login_frame,text='Sign In',command=login_student,font=('Arial',11),text_color='black',width=200,corner_radius=8,fg_color='white',hover_color='#595959')
signIN1_button.place(x=100,y=300)

text2=CTkLabel(master=login_frame,text='Are You a Administrator?',compound='left',font=('Arial',10,'bold'),text_color='white',fg_color='black')
text2.place(x=80,y=350)

signIN_button=CTkButton(master=login_frame,text='Sing In as Administrator',command=the_administrator,font=('Arial',9,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#595959')
signIN_button.place(x=205,y=350)

#TO CREATE A NEW AC
text3=CTkLabel(master=login_frame,text="Don't have an account ?",compound='left',font=('Arial',10,'bold'),text_color='white',fg_color='black')
text3.place(x=80,y=380)

newAC_button=CTkButton(master=login_frame,text='Create new account',command=create_AC,font=('Arial',10,'bold'),text_color='#0080FF',fg_color='transparent',hover_color='#9A9498')
newAC_button.place(x=208,y=380)

root1.mainloop()