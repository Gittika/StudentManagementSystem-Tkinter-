from ast import Delete, excepthandler
from importlib.resources import contents
from msilib import add_data
from tkinter import messagebox
import mysql
import mysql.connector
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk







class Student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        
        
        
        # valriables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_admission_type=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        

        img=Image.open("campus.jfif")
        img=img.resize((1510,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.image_1=Label(self.root,image=self.photoimg,cursor="hand2")
        self.image_1.place(x=0,y=4,width=1540,height=160)   



        # img2=Image.open("girlreading.jfif")
        # img2=img2.resize((510,160),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # self.image_2=Label(self.root,image=self.photoimg2,cursor="hand2")
        # self.image_2.place(x=480,y=4,width=520,height=160)    


        # img3=Image.open("last.jfif")
        # img3=img3.resize((510,160),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # self.image_3=Label(self.root,image=self.photoimg3,cursor="hand2")
        # self.image_3.place(x=1000,y=4,width=510,height=160)  



        img4=Image.open("backgroundimage.jpg")
        img4=img4.resize((1530,600),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_lbl=Label(self.root,image=self.photoimg4,cursor="hand2")
        bg_lbl.place(x=15,y=170,width=1495,height=600)  


        lbl_title = Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("arial",37,"bold"),fg="black",bg="#B0E0E6")
        lbl_title.place(x=0,y=0,width=1530,height=55)

        Manage_frame=Frame(bg_lbl ,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=7,y=60,width=1475,height=510)

        # left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,text="Student Information",font=("times new roman",20,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=480)
        
        # image
        img5=Image.open("sm2.jfif")
        img5=img5.resize((650,120),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        my_img=Label(DataLeftFrame,image=self.photoimg5,cursor="hand2")
        my_img.place(x=0,y=0,width=650,height=120)  
 
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("arial",10,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=90)
        

        lbl_dept=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)
        dept_combo=ttk.Combobox(std_lbl_info_frame,font=("arial",12),width=17,textvariable=self.var_dept)
        dept_combo["value"]=("Select Department","CSE","ISE","EEE","ECE","MEC","ETE","CIVIL")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1)




        lbl_sem=Label(std_lbl_info_frame,text="Semester",font=("arial",12,"bold"),bg="white")
        lbl_sem.grid(row=1,column=0,padx=2,pady=5,sticky=W)
        sem_combo=ttk.Combobox(std_lbl_info_frame,font=("arial",12),width=17,textvariable=self.var_sem)
        sem_combo["value"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,pady=5)



        
        lbl_year=Label(std_lbl_info_frame,text="Batch",font=("arial",12,"bold"),bg="white")
        lbl_year.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        year_combo=ttk.Combobox(std_lbl_info_frame,font=("arial",12),width=17,textvariable=self.var_year)
        year_combo["value"]=("Select Year","2018-2022","2019-2023","2020-2024","2021-2025")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,pady=5)



        
        lbl_course=Label(std_lbl_info_frame,text="Course",font=("arial",12,"bold"),bg="white")
        lbl_course.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        course_combo=ttk.Combobox(std_lbl_info_frame,font=("arial",12),width=17,textvariable=self.var_course)
        course_combo["value"]=("Select Course","B.E","B.TECH","B.ARCH","M.TECH","MBA")
        course_combo.current(0)
        course_combo.grid(row=1,column=3,pady=5)
        
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("arial",12),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=210,width=650,height=175)
        # usn
        lbl_usn=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="USN",bg="white")
        lbl_usn.grid(row=0,column=0,sticky=W,padx=5,pady=5)
        txt_usn=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_usn)
        txt_usn.grid(row=0,column=1,padx=2,pady=5)
        # name
        lbl_name=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Name",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=5,pady=5)
        txt_name=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_name)
        txt_name.grid(row=0,column=3,padx=2,pady=5)
       
        # email
        lbl_email=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Email",bg="white")
        lbl_email.grid(row=1,column=0,sticky=W,padx=5,pady=5)
        txt_email=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_email)
        txt_email.grid(row=1,column=1,padx=2,pady=5)
        
        # phone no
        lbl_phone=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Phone No",bg="white")
        lbl_phone.grid(row=1,column=2,sticky=W,padx=5,pady=5)
        txt_phone=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_phone)
        txt_phone.grid(row=1,column=3,padx=2,pady=5)
        # address
        lbl_address=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Address",bg="white")
        lbl_address.grid(row=2,column=0,sticky=W,padx=5,pady=5)
        txt_address=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_address)
        txt_address.grid(row=2,column=1,padx=2,pady=5)
        # dob
        lbl_dob=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Dob",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=5,pady=5)
        txt_dob=ttk.Entry(std_lbl_class_frame,width=25,font=("arial",11,"bold"),textvariable=self.var_dob)
        txt_dob.grid(row=2,column=3,padx=2,pady=5)
         # gender
        lbl_gender=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Gender",bg="white")
        lbl_gender.grid(row=3,column=0,sticky=W,padx=5,pady=5)
        txt_gender=ttk.Combobox(std_lbl_class_frame,width=22,font=("arial",11),textvariable=self.var_gender) 
        txt_gender["value"]=("Select Gender" ,"Male","Female")
        txt_gender.current(0)
        txt_gender.grid(row=3,column=1,padx=2,pady=5)
        
        # addmission type
        lbl_addmission=Label(std_lbl_class_frame,font=("arial",11,"bold"),text="Admission Type",bg="white")
        lbl_addmission.grid(row=3,column=2,sticky=W,padx=5,pady=5)
        txt_addmission=ttk.Combobox(std_lbl_class_frame,width=22,font=("arial",11),textvariable=self.var_admission_type) 
       
        txt_addmission["value"]=("Select Type" ,"KCET","COMEDK","MANAGEMENT")
        txt_addmission.current(0)
        txt_addmission.grid(row=3,column=3,pady=5)
        
        
        # Button frame
        btn_frame=Frame(DataLeftFrame,bd=4,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=390,width=650,height=40)
        
        btn_Add=Button(btn_frame,text="Save",font=("arial",11,"bold"),width=16,bg="#1E90FF",fg="white",command=self.add_data)
        btn_Add.grid(row=0,column=0,padx=3)
        
        btn_Update=Button(btn_frame,text="Update",font=("arial",11,"bold"),width=16,bg="#00BFFF",fg="white",command=self.update_data)
        btn_Update.grid(row=0,column=1,padx=3)
        
        btn_Delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),width=16,bg="#87CEEB",fg="white",command=self.delete_data)
        btn_Delete.grid(row=0,column=2,padx=3)
        
        btn_Reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),width=16,bg="#4169E1",fg="white",command=self.reset_data)
        btn_Reset.grid(row=0,column=3,padx=3)
        
        
        
        

  # right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,text="Student Detail",font=("times new roman",20,"bold"),bg="white")
        DataRightFrame.place(x=690,y=10,width=770,height=480)
        
        
        
        # # image
        # img6=Image.open("sirmvit.jpg")
        # img6=img6.resize((760,120),Image.ANTIALIAS)
        # self.photoimg6=ImageTk.PhotoImage(img6)

        # my_img2=Label(DataRightFrame,image=self.photoimg6,cursor="hand2",bd=4)
        # my_img2.place(x=2,y=0,width=760,height=120)  
 
        std_lbl_search_frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",bg="white",font=("arial",10,"bold"),fg="red")
        std_lbl_search_frame.place(x=2,y=0,width=760,height=60)
        
        
        
        search_by_label =Label(std_lbl_search_frame,font=("arial",13,"bold"),text="Search By :",fg="black",bg="white")
        search_by_label.grid(row=0,column=0,padx=2)
        
        self.var_combo_search=StringVar()
        select_option=ttk.Combobox(std_lbl_search_frame,width=17,textvariable=self.var_combo_search,font=("arial",13,))
        select_option["value"]=("Search By" ,"USN","COURSE","DEPT")
        select_option.current(0)
        select_option.grid(row=0,column=1,padx=2)
        
        self.var_search=StringVar()
        entry =ttk.Entry(std_lbl_search_frame,font=("arial",13),textvariable=self.var_search)
        entry.grid(row=0,column=2,padx=2)
        
        btn_Search=Button(std_lbl_search_frame,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.search)
        btn_Search.grid(row=0,column=3,padx=2)
        
        btn_show=Button(std_lbl_search_frame,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white",command=self.fetch_data)
        btn_show.grid(row=0,column=4,padx=2)
        
        
        
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=65,width=760,height=370)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","usn","name","dob","address","admissiontype","phone","gender","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)             
                                        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        
        self.student_table.heading("year",text="Batch")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("usn",text="USN")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dob",text="Dob")
        
        self.student_table.heading("address",text="Address")
        self.student_table.heading("admissiontype",text="Admission Type")
        self.student_table.heading("phone",text="Phone No")
        
        self.student_table.heading("gender",text="Gender")
        
        self.student_table.heading("email",text="Email")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        
        self.student_table.column("usn",width=100)
        self.student_table.column("name",width=100)
        
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=100)
        
        
        self.student_table.column("admissiontype",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("gender",width=100)
        
        self.student_table.column("email",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    def add_data  (self):
         if(self.var_dept.get()=="" or self.var_usn.get()=="" or self.var_year.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
         else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="gittika",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                   
                 
                    self.var_usn.get(),
                    self.var_name.get(),
                    
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_admission_type.get(),
                    self.var_phone.get(),
                    self.var_gender.get(),
                    
                    self.var_email.get()
                    
                    
                )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="gittika",database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("select* from student")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
                
         # get cursor
    def get_cursor(self,event=""):
            cursor_row=self.student_table.focus()
            content=self.student_table.item(cursor_row)
            data=content["values"]
            
            self.var_dept.set(data[0])
            self.var_course.set(data[1])
            self.var_sem.set(data[3])
            self.var_year.set(data[2])
            self.var_usn.set(data[4])
            self.var_name.set(data[5])
            self.var_dob.set(data[6]),
            
            
            self.var_address.set(data[7]),
            self.var_admission_type.set(data[8]),
            self.var_phone.set(data[9]),       
            self.var_gender.set(data[10]),
           
            
            self.var_email.set(data[11])
           
                   
    
            # update
    def update_data(self):
        if(self.var_dept.get()=="" or self.var_email.get()=="" or self.var_usn.get()=="") :
                 messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                update =messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if(update>0):
                     conn=mysql.connector.connect(host="localhost",username="root",password="gittika",database="mydata")
                     my_cursur=conn.cursor()
                     my_cursur.execute('UPDATE student set dept=%s,course=%s,year=%s,sem=%s,name=%s,dob=%s,address=%s,admissiontype=%s,phone=%s,gender=%s,email=%s where usn=%s',(
                                                                                                                                                                                     self.var_dept.get(),
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_sem.get(),
                                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_admission_type.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_email.get() ,
                                                                                                                                                                                     self.var_usn.get()
                                                                                                                                                                                    ))
                                
                 
                else:
                    if not update:
                        return     
                conn.commit() 
                self.fetch_data()
                conn.close()   
                
                messagebox.showinfo("Success","Student successfully updated",parent=self.root)       
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def delete_data(self):
        if(self.var_usn.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                delete=messagebox.askyesno("delete","Are you sure delete this student")
                if(delete>0):
                    conn=mysql.connector.connect(host="localhost",username="root",password="gittika",database="mydata")
                    my_cursur=conn.cursor()
                    my_cursur.execute("delete from student where usn=%s",(self.var_usn.get(),))
                else:
                    if not delete :
                        return     
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)            
    def reset_data(self):
            self.var_dept.set("Select Department")
            self.var_course.set("Select Course")
            self.var_sem.set("Select Semester")
            self.var_year.set("Select Year")
            self.var_usn.set("")
            self.var_name.set("")
            self.var_dob.set(""),
            
            
            self.var_address.set(""),
            self.var_admission_type.set(""),
            self.var_phone.set(""),       
            self.var_gender.set(""),
           
            
            self.var_email.set("")
            # search data
    def search(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="gittika",database="mydata")
            my_cursur=conn.cursor() 
            my_cursur.execute("select* from student where "+str(self.var_combo_search.get())+" Like '%" +str(self.var_search.get())+"%'") 
            data=my_cursur.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()        
                 
                            
                
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()