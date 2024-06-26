from tkinter import*
from customtkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root,main_root):
        self.root = root
        self.main_root = main_root
        self.root.geometry("1360x688+0+0")
        self.root.title("Face Recoginiton System")
        self.root.state('zoomed')


        #___VARIABLES____
        self.name_var=StringVar()
        self.dep_var=StringVar()
        self.A_status_var=StringVar()
        self.date_var=StringVar()
        self.time_var=StringVar()
        self.std_id_var=StringVar()

        self.search_by_var=StringVar()
        self.search_value_var=StringVar()

        #1st image
        img13=Image.open(r"Used Pictures\studenttop1.webp")
        img13=img13.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        label13=Label(self.root,image=self.photoimg13)
        label13.place(x=0,y=0,width=500,height=130)

        #2nd image
        img14=Image.open(r"Used Pictures\studenttop2.jpg")
        img14=img14.resize((400,130),Image.Resampling.LANCZOS)
        self.photoimg14=ImageTk.PhotoImage(img14)
        
        label14=Label(self.root,image=self.photoimg14)
        label14.place(x=500,y=0,width=400,height=130)

        #3rd image
        img15=Image.open(r"Used Pictures\student2.jpg")
        img15=img15.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg15=ImageTk.PhotoImage(img15)
        
        label15=Label(self.root,image=self.photoimg15)
        label15.place(x=900,y=0,width=500,height=130)

        #background image
        img16=Image.open(r"Used Pictures\faceR.webp")
        img16=img16.resize((1500,600),Image.Resampling.LANCZOS)
        self.photoimg16=ImageTk.PhotoImage(img16)
        
        label16=Label(self.root,image=self.photoimg16)
        label16.place(x=0,y=130,width=1500,height=600)

        #creating title for the bg image
        title=Label(label16,text="ATTENDANCE MANAGEMENT SYSTEM",font=('times new roman',25,'bold'),fg='white',bg='black')
        title.place(x=-2,y=-2,width=1500,height=42)

        back_button=CTkButton(title,command=self.back_button,width=83,height=42,text='Back',font=('times new roman',15,'bold'),fg_color='white',corner_radius=8,bg_color='black',text_color='black',hover_color='gray')
        back_button.place(x=-2,y=-2)

        # main frame
        std_frame=Frame(label16,bd=2,bg='white')
        std_frame.place(x=80,y=40,width=1200,height=450)

        # left frame(inside main frame)
        left_frame1=LabelFrame(std_frame,bd=2,relief=RIDGE,text='Student Details',font=('times new roman',10),bg='white')
        left_frame1.place(x=10,y=5,width=580,height=395)

        # providing image for the left frame(line 58-63)
        img_left=Image.open(r"Used Pictures\top3.jpg")
        img_left=img_left.resize((580,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        label_left=Label(left_frame1,image=self.photoimg_left)
        label_left.place(x=0,y=0,width=580,height=100)

        #creating a frame for course details
        current_frame=LabelFrame(left_frame1,bd=2,relief=RIDGE,text=None,font=('times new roman',10),bg='white')
        current_frame.place(x=0,y=105,width=575,height=270)

         #Student Name
        studentname_label=Label(current_frame,text='Student Name',font=('times new roman',10,'bold'),bg='white')
        studentname_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentname_entry=ttk.Entry(current_frame,textvariable=self.name_var,width=25,font=('times new roman',10))
        studentname_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # studentID
        studentID_label=Label(current_frame,text='StudentID/ID No.',font=('times new roman',10,'bold'),bg='white')
        studentID_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(current_frame,textvariable=self.std_id_var,width=25,font=('times new roman',10))
        studentID_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Attendance status
        A_status_label=Label(current_frame,text='Attendance status',font=('times new roman',10,'bold'),bg='white')
        A_status_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        A_status_combo=ttk.Combobox(current_frame,textvariable=self.A_status_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        A_status_combo['values']=('Select','Present','Absent')
        A_status_combo.current(0)
        A_status_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #department
        dep_label=Label(current_frame,text='Department',font=('times new roman',10,'bold'),bg='white')
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.dep_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        dep_combo['values']=('Select Department','BSc. CSDA','BBA')
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # date
        date_label=Label(current_frame,text='Date',font=('times new roman',10,'bold'),bg='white')
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        
        date_entry=ttk.Entry(current_frame,textvariable=self.date_var,width=25,font=('times new roman',10))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # time
        time_label=Label(current_frame,text='Time',font=('times new roman',10,'bold'),bg='white')
        time_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        
        time_entry=ttk.Entry(current_frame,textvariable=self.time_var,width=25,font=('times new roman',10))
        time_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Creating frame1 for 2 buttons
        button_frame1=Frame(left_frame1,relief=RIDGE,bg='white')
        button_frame1.place(x=2,y=300,width=570,height=35)

        #import button
        ImportCSV_button=CTkButton(button_frame1,command=self.importCSV,text='Import CSV',width=283,height=31,font=('times new roman',12),fg_color='blue',corner_radius=8,bg_color='white',text_color='white',hover_color='#0D52BD')
        ImportCSV_button.grid(row=0,column=0,padx=0,pady=0)

        #export button
        ExportCSV_button=CTkButton(button_frame1,command=self.exportCSV,text='Export CSV',width=284,height=31,font=('times new roman',12),fg_color='blue',corner_radius=8,bg_color='white',text_color='white',hover_color='#0D52BD')
        ExportCSV_button.grid(row=0,column=1,padx=0,pady=0)

        #Creating frame2 for another 2 buttons
        button_frame2=Frame(left_frame1,relief=RIDGE,bg='white')
        button_frame2.place(x=2,y=335,width=570,height=35)

        #reset button
        Reset_button=CTkButton(button_frame2,command=self.reset_fun,text='Reset',width=283,height=31,font=('times new roman',12),fg_color='green',corner_radius=8,bg_color='white',text_color='white',hover_color='#5bb450')
        Reset_button.grid(row=0,column=1,padx=0,pady=0)

        #update button
        update_button=CTkButton(button_frame2,command=self.update_fun,text='Update',width=284,height=31,font=('times new roman',12),fg_color='green',corner_radius=8,bg_color='white',text_color='white',hover_color='#5bb450')
        update_button.grid(row=0,column=2,padx=0,pady=0)

        # right frame(inside main frame)
        right_frame1=LabelFrame(std_frame,bd=2,relief=RIDGE,text='Attendance Details',font=('times new roman',10),bg='white')
        right_frame1.place(x=600,y=5,width=580,height=395)

        #providing image for the right frame
        img_right=Image.open(r"Used Pictures\studenttop3.png")
        img_right=img_right.resize((580,100),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        label_right=Label(right_frame1,image=self.photoimg_right)
        label_right.place(x=0,y=0,width=580,height=100)

        #creating a frame for search system
        search_frame=LabelFrame(right_frame1,bd=2,relief=RIDGE,text=None,font=('times new roman',10),bg='white')
        search_frame.place(x=0,y=105,width=575,height=50)

        search_label=Label(search_frame,text='Search by:',font=('times new roman',11,'bold'),bg='white')
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=('times new roman',10,'bold'),textvariable=self.search_by_var,width=13,state='readonly')
        search_combo['values']=('Select','Status',"Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=18,textvariable=self.search_value_var,font=('times new roman',10))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_button=CTkButton(search_frame,text='Search',command=self.search_data,width=110,font=('times new roman',12,'bold'),text_color='white',fg_color='blue',hover_color='#0D52BD')
        search_button.grid(row=0,column=3,padx=5,pady=5)
        
        
        showall_button=CTkButton(search_frame,text='Show All',width=110,font=('times new roman',12,'bold'),text_color='white',fg_color='blue',hover_color='#0D52BD')
        showall_button.grid(row=0,column=4,padx=5,pady=5)

        table_frame=Frame(right_frame1,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=0,y=170,width=575,height=200)


        #creating scrollbars for the table frame
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.attendance_table=ttk.Treeview(table_frame,columns=('name','id','A_status','dep','date','time'),
                                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        #here orders doesn't matter.
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("id", text="Student ID")
        self.attendance_table.heading("A_status", text="Attendance status")
        self.attendance_table.heading("dep", text="Department")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text="Time")

        #here orders doesn't matter.
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("id", width=100)
        self.attendance_table.column("A_status", width=120)
        self.attendance_table.column("dep", width=100)
        self.attendance_table.column("date", width=80)
        self.attendance_table.column("time", width=80)

        self.attendance_table['show']='headings'
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

        #_____________back button_________
    def back_button(self):
        self.root.destroy()
        self.main_root.deiconify()

    #___________ger cursor(to load the data to entryfills, comboboxes when cursor is click on any data)____________
    def get_cursor(self, event=""):
        cursor_focus = self.attendance_table.focus()
        take_content = self.attendance_table.item(cursor_focus)
        rows = take_content["values"]
        if rows:  # Ensure rows is not empty
            self.name_var.set(rows[0])
            self.std_id_var.set(rows[1])
            self.A_status_var.set(rows[2])
            self.dep_var.set(rows[3])
            self.date_var.set(rows[4])
            self.time_var.set(rows[5])
            
    #______to reload the data_____
    def fetchData(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    #importing the data from CSV file
    def importCSV(self):
        try:
            global mydata
            mydata.clear()
            file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.csv'),('All Files','*.*')),parent=self.root)
            if file_name:
                with open(file_name) as myfile:
                    csv_read=csv.reader(myfile,delimiter=',')
                    for r in csv_read:
                        mydata.append(r)
                    self.fetchData(mydata)
            else:
                pass
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    #exporting the data in a  CSV file
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data available to export",parent=self.root)
            else:
                file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), initialfile="new attendance.csv", defaultextension='.csv', title='Save as CSV', filetypes=(('CSV File','*.csv'),('All Files','*.*')), parent=self.root)
                if file_name:
                    with open(file_name,mode='w',newline='') as myfile:
                        exp_write=csv.writer(myfile,delimiter=',')
                        for i in mydata:
                            exp_write.writerow(i)
                        messagebox.showinfo("Done!",f"Your data has been exported to {os.path.basename(file_name)} successfully",parent=self.root)
                else:
                    pass
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def update_fun(self):
        if (self.dep_var.get() == '' or self.name_var.get() == '' or 
            self.std_id_var.get() == '' or self.date_var.get() == '' or 
            self.time_var.get() == '' or self.A_status_var.get() == 'Select'):
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                ask_update = messagebox.askyesno("Update!", "Do you really want to update this data?", parent=self.root)
                if ask_update:
                    updated = False
                    data_list = []

                    with open('Attendances.csv', mode='r', newline='') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row['id'] == self.std_id_var.get():
                                row['name'] = self.name_var.get()
                                row['dep'] = self.dep_var.get()
                                row['date'] = self.date_var.get()
                                row['time'] = self.time_var.get()
                                row['A_status'] = self.A_status_var.get()
                                updated = True
                            data_list.append(row)

                    if updated:
                        with open('Attendances.csv', mode='w', newline='') as file:
                            fieldnames = ['id', 'name', 'dep', 'date', 'time', 'A_status']
                            writer = csv.DictWriter(file, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(data_list)
                        messagebox.showinfo("Success", "The data has been updated successfully", parent=self.root)
                        self.fetchData(mydata)
                    else:
                        messagebox.showerror('Error', 'No matching record found to update', parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_fun(self):
        if(self.dep_var.get()=='' and self.name_var.get()=='' and self.std_id_var.get()=='' and self.date_var=='' and self.time_var=='' and self.A_status_var=='Select'):
            messagebox.showerror('Error!','Your data is already empty!',parent=self.root)

        else:
            self.dep_var.set('')
            self.name_var.set('')
            self.std_id_var.set('')
            self.date_var.set('')
            self.time_var.set('')
            self.A_status_var.set('Select')

    def search_data(self):
        search_by = self.search_by_var.get()
        search_value = self.search_value_var.get()

        if search_by == 'Select' or search_value == '':
            messagebox.showerror('Error', 'Please provide either Student ID or Attendance Status to search', parent=self.root)
            return

        try:
            data_list = []

            with open('Attendances.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if (search_by == 'Student ID' and row['id'] == search_value) or (search_by == 'Status' and row['A_status'] == search_value):
                        data_list.append(row)

            # Clear the existing data in the attendance_table
            for item in self.attendance_table.get_children():
                self.attendance_table.delete(item)

            # Insert the filtered data into the attendance_table
            for row in data_list:
                self.attendance_table.insert('', 'end', values=(
                    row['name'],
                    row['std_id'],
                    row['A_status'],
                    row['dep'],
                    row['date'],
                    row['time']
                ))

            if not data_list:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj2 = Attendance(root,root)
    root.mainloop()