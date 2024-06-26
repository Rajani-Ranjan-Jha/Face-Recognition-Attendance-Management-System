
from tkinter import*
from customtkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student_STUDENT import Student1 #for student window of a student
import os
from tkinter import messagebox
import numpy as np
import cv2


from time import strftime
from datetime import datetime


import mysql.connector



class FaceRecognitionSystem1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("15000x900+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')
    
        #1st image
        img1=Image.open(r"Used Pictures\firstImg.png")
        img1=img1.resize((1550,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        label1=Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=1550,height=130)

        #2nd image
        #img2=Image.open(r"Used Pictures\top2.jpg")
        #img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        #self.photoimg2=ImageTk.PhotoImage(img2)
        
        #label2=Label(self.root,image=self.photoimg2)
        #label2.place(x=500,y=0,width=500,height=130)

        #3rd image
        #img3=Image.open(r"Used Pictures\top3.jpg")
        #img3=img3.resize((530,130),Image.Resampling.LANCZOS)
        #self.photoimg3=ImageTk.PhotoImage(img3)
        
        #label3=Label(self.root,image=self.photoimg3)
        #label3.place(x=1000,y=0,width=530,height=130)

        #background image
        img4=Image.open(r"Used Pictures\MainWindowBG.png")
        img4=img4.resize((1530,750),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        label4=Label(self.root,image=self.photoimg4)
        label4.place(x=0,y=130,width=1530,height=750)

        #creating title for the bg image
        title=Label(label4,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=('times new roman',25,'bold'),fg='black',bg='white')
        title.place(x=-5,y=-5,width=1550,height=40)

        #CREATING BUTTONS
        #student button
        img5=Image.open(r"Used Pictures\studentDetailButton.png")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        button1=Button(label4,command=self.student_details,image=self.photoimg5,cursor='hand2',bd=2)
        button1.place(x=320,y=100,width=200,height=200)

        buttonlbl1=CTkButton(label4,command=self.student_details,width=200,height=40,text='Student Details',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl1.place(x=320,y=300)

        #_______________FACE DETECTOR BUTTON___________
        img6=Image.open(r"Used Pictures\faceDetector.png")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        button2=Button(label4,image=self.photoimg6,cursor='hand2',command=self.face_recogG,bd=0)
        button2.place(x=700,y=100,width=200,height=200)

        buttonlbl2=CTkButton(label4,command=self.face_recogG,width=200,height=40,text='Face Recognition',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl2.place(x=700,y=300)

        #help desk button
        img8=Image.open(r"Used Pictures\helpButton.png")
        img8=img8.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        button4=Button(label4,image=self.photoimg8,cursor='hand2',bd=0)
        button4.place(x=1050,y=100,width=200,height=200)

        buttonlbl4=CTkButton(label4,width=200,height=40,text='Help',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl4.place(x=1050,y=300)

        #Train Data button
        img10=Image.open(r"Used Pictures\trainButton.png")
        self.photoimg10=ImageTk.PhotoImage(img10)

        button6=Button(label4,image=self.photoimg10,cursor='hand2',command=self.train_data,bd=0)
        button6.place(x=320,y=400,width=200,height=200)

        buttonlbl6=CTkButton(label4,command=self.train_data,width=200,height=40,text='Train Data',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl6.place(x=320,y=600)

        #Developer button
        img11=Image.open(r"Used Pictures\devloperButton.png")
        img11=img11.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        button7=Button(label4,image=self.photoimg11,cursor='hand2',bd=0)
        button7.place(x=700,y=400,width=200,height=200)

        buttonlbl7=CTkButton(label4,width=200,height=40,text='Developers',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl7.place(x=700,y=600)

        #Exit button
        img12=Image.open(r"Used Pictures\exitButton.png")
        img12=img12.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        button8=Button(label4,image=self.photoimg12,cursor='hand2',command=self.exit_button,bd=0)
        button8.place(x=1050,y=400,width=200,height=200)

        buttonlbl8=CTkButton(label4,command=self.exit_button,width=200,height=40,text='Exit',font=('times new roman',15,'bold'),fg_color='grey',corner_radius=0,text_color='white',hover_color='#595959')
        buttonlbl8.place(x=1050,y=600)

    #______FUNCTION BUTTONS______
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student1(self.new_window, self.root)

    #train data
    def train_data(self):
        try:
            ask_train = messagebox.askyesno("Train data!", "Do you really want to train this data?", parent=self.root)
            if ask_train > 0:
                data_dir = "stored_pictures"
                path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

                faces = []
                ids = []
                for image in path:
                    img = Image.open(image).convert('L')  # Gray scale image
                    imageNp = np.array(img, 'uint8')
                    id = int(os.path.split(image)[-1].split('_')[1])
                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1) == 13
                ids = np.array(ids)

                # Train the classifier and save
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces, ids)
                clf.write("classifier.xml")
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Training datasets completed!", parent=self.root)
            else:
                if not ask_train:
                    return
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    #to add data in CSV file
    def mark_attendanceG(self,n,i,d):#currenly i have removed 'i' from arguments. when add it, add inside all part of this fun.
        with open("Attendances.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((n not in name_list) and (i not in name_list) and (d not in name_list)):
                now=datetime.now()
                Date=now.strftime("%d/%m/%Y")
                Time=now.strftime("%H:%M:%S")
                f.writelines(f"{n},{i},Present,{d},{Date},{Time}\n")
                
    #face recognition 
    def face_recogG(self):
        try:
            def draw_rect(img, classifier, scaleF, minN, color, text, clf):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray, scaleF, minN)
                coord = []
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    id, pred = clf.predict(gray[y:y + h, x:x + w])
                    confidence = int(100 * (1 - pred / 300))

                    if confidence > 77:
                        connection = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="khanskmk",
                            database="face_recognition_sys"
                        )
                        cursor_my = connection.cursor()
                        cursor_my.execute("SELECT Name FROM student WHERE Student_Id=%s", (str(id),))
                        n = cursor_my.fetchone()
                        if n:
                            n = n[0]
                        else:
                            n = "Error(Unknown)"


                        cursor_my.execute("SELECT Department FROM student WHERE Student_Id=%s", (str(id),))
                        d = cursor_my.fetchone()
                        if d:
                            d = d[0]
                        else:
                            d = "Error(Unknown)"

                        cursor_my.execute("SELECT Student_Id FROM student WHERE Student_Id=%s", (str(id),))
                        i = cursor_my.fetchone()
                        if i:
                            i = i[0]
                        else:
                            i = "Error(Unknown)"

                        cv2.putText(img, f'Name: {n}', (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f'Student ID:  {i}', (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f'Department: {d}', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendanceG(n,i,d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        cv2.putText(img, "Unknown User", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)

                    coord = [x, y, w, h]
                return coord

            def recognize(img, clf, faceCascade):
                draw_rect(img, faceCascade, 1.1, 10, (0, 225, 0), 'Face', clf)
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_capture = cv2.VideoCapture(0)

            while True:
                ret, img = video_capture.read()
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Face Recognizer", img)
                if cv2.waitKey(1) == 13:
                    break

            video_capture.release()
            cv2.destroyAllWindows()

        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    #exit
    def exit_button(self):
        ask_exit=messagebox.askyesno("Exit!","Do you want to exit?",parent=self.root)
        if ask_exit:
            os._exit(0)#to close all running proggrams immediately

            
if __name__ == "__main__":
    root = Tk()
    obj1 = FaceRecognitionSystem1(root)
    root.mainloop()






