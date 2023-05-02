from   tkinter import *
from   tkinter import ttk
import  pymysql
class  Student :
   #--------------------------------------------إنشاء نافدة -----------------------------------------------
   def __init__(self,root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('برنامج إدارة كلية العلوم و الادآب بدر')
        self.root.configure(background="silver")
        self.root.resizable(False, False)
        title = Label(self.root, text='نظام تسجيل الطلاب ',
        bg='#1AAEFA',
        font=('monospace', 14),
        fg='black'
        )
        title.pack(fill= X )
   #------------------------------variables----------------------------------------------
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()
        self.moahal_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.dell_var=StringVar()
        self.se_var=StringVar()
   #-------------------------------أدوات التحكم--------------------------
        Manage_Frame = Frame(self.root , bg='white')
        Manage_Frame.place (x= 1137, y=30,width=210,height=400)
        lbl_ID = Label(Manage_Frame, text='رقم الاستاذ', bg='white')
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame,textvariable=self.id_var, bd='2', justify='center')
        ID_Entry.pack()
        lbl_name = Label(Manage_Frame, bg='white', text='اسم الاستاذ ')
        lbl_name.pack()
        Name_Entry = Entry(Manage_Frame,textvariable=self.name_var, bd='2', justify='center')
        Name_Entry.pack()
        lbl_email = Label(Manage_Frame, bg='white', text='إيميل  الاستاد')
        lbl_email.pack()
        email_Entry = Entry(Manage_Frame,textvariable=self.email_var, bd='2', justify='center')
        email_Entry.pack()
        lbl_phone = Label(Manage_Frame, bg='white', text='هاتف الاستاد ')
        lbl_phone.pack()
        phone_Entry = Entry(Manage_Frame, textvariable=self.phone_var,bd='2', justify='center')
        phone_Entry.pack()
        lbl_Certi = Label( Manage_Frame, bg='white', text='مؤهل الاستاد')
        lbl_Certi.pack()
        Certi_Entry = Entry(Manage_Frame,textvariable=self.moahal_var, bd='2', justify='center')
        Certi_Entry.pack()
        lbl_gender= Label(Manage_Frame, bg='white', text='إختر جنس الاستاد ')
        lbl_gender.pack()
        Combo_gender= ttk.Combobox(Manage_Frame,textvariable=self.gender_var,)
        Combo_gender['value']=('ذكر','أنثى')
        Combo_gender.pack()
        lbl_address= Label(Manage_Frame,text='عنوان الطالب',bg='white')
        lbl_address.pack()
        address_Entry = Entry(Manage_Frame,textvariable=self.address_var, bd='2', justify='center')
        address_Entry.pack()
        lbl_delete = Label(Manage_Frame, fg='red',bg='white',text='حذف اسم الاستاد')
        lbl_delete.pack()
        delete_Entry= Entry(Manage_Frame,textvariable=self.dell_var,bd='2', justify='center')
        delete_Entry.pack()
   #-------------------------------------------------الازرار---------------------------
        btn_Frame = Frame(self.root,bg='white')
        btn_Frame.place(x=1137,y=435,width=210,height=253)
        title1= Label(btn_Frame, text='لوحة التحكم',font=('Deco',14) , fg='white' , bg='#2980B9')
        title1.pack(fill=X)
        add_btn=Button(btn_Frame, text='إضافة الاستاذ',bg='#58D68D',command=self.add_student)
        add_btn.place(x=33,y=39,width=150,height=30)
        del_btn=Button(btn_Frame, text='حذف الاستاذ',bg='#CB4335')
        del_btn.place(x=33,y=80,width=150,height=30)
        update_btn=Button(btn_Frame, text='تعديل بيانات الاستاد',bg='#5DADE2')
        update_btn.place(x=33,y= 115,width=150,height=30)
        clear_btn=Button(btn_Frame, text='إفراغ الحقول',bg='#283747')
        clear_btn.place(x=33,y=150,width=150,height=30)
        about_btn=Button(btn_Frame, text='من نحن',bg='#5B2C6B')
        about_btn.place(x=33,y=185,width=150,height=30)
        exit_btn=Button(btn_Frame, text='إغلاق البرنامج',bg='blue')
        exit_btn.place(x=33,y=183,width=150,height=30)
   #---------------------------------Search Manage--------------------------
        search_Frame= Frame(self.root, bg='white')
        search_Frame.place(x=1,y=30,width=1134,height=50)
        lbl_search=Label(search_Frame,text= 'البحث عن  استاذ ',bg='white')
        lbl_search.place(x=1034,y=12)
        Combo_search = ttk.Combobox(search_Frame, justify='right')
        Combo_search['value']=('id','name','email','phone' )
        Combo_search.place(x=880,y=12)
        Search_Entry =Entry (search_Frame,textvariable=self.se_var, justify='right', bd='2')
        Search_Entry.place( x=470, y=12)
        Se_btn = Button(search_Frame ,text='بحث', bg='#3498DB', fg='white')
        Se_btn.place(x=360, y=12,width= 100, height=25 )

   #--------------------------------عرض النتائج و البيانات---------------------------
        Dietals_Frame = Frame(self.root, bg='#F2F4F4')
        Dietals_Frame.place(x=1 ,y=82 , width=1134 , height=605 )
              #-------------Scroll---------------------------------------------------------
        Scroll_X= Scrollbar(Dietals_Frame,  orient= HORIZONTAL)
        Scroll_Y= Scrollbar(Dietals_Frame, orient= VERTICAL)
         #------------------------------treeveiw-------------------------------------------
        self.student_table= ttk.Treeview(Dietals_Frame,
        columns=('address','gender','certi','phone','email','name','id'),
        xscrollcommand= Scroll_X.set,
        yscrollcommand= Scroll_Y.set )
        self.student_table.place(x=1,y=18,width=1130,height=587)
        Scroll_X.pack(side=BOTTOM,fill=X)
        Scroll_Y.pack(side=LEFT,fill=Y)
        Scroll_X.config(command=self.student_table.xview)
        Scroll_Y.config(command=self.student_table.yview)
        self.student_table['show']='headings'
        self.student_table.heading('address',text='عنوان الاستاذ')
        self.student_table.heading('gender', text= 'جنس الاستاد ')
        self.student_table.heading('certi', text= 'مؤهلات الاستاذ')
        self.student_table.heading('phone', text= 'رقم الاستاذ')
        self.student_table.heading('email', text= 'البريد الاكتروني')
        self.student_table.heading('name', text='اسم الاستاذ')
        self.student_table.heading('id', text='رقم الاستاد ')
        self.student_table.column( 'address' , width =125 )
        self.student_table.column( 'gender' ,  width =30 )
        self.student_table.column( 'certi' , width =65 )
        self.student_table.column( 'phone' , width =65 )
        self.student_table.column( 'email' , width =70 )
        self.student_table.column( 'name' , width =100 )
        self.student_table.column( 'id' , width =17 )
   #--------------------------------------------con+add------------------------------
   def add_student(self):
         con = pymysql.connect(host = 'localhost', user = 'root', password='',databese ='rakoto')
         cur = con.cursor()
         cur.execute("insert into teacher values(%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.id_var.get(),
                                                            self.name_var.get(),
                                                            self.email_var.get(),
                                                            self.phone_var.get(),
                                                            self.moahal_var.get(),
                                                            self.gender_var.get(),
                                                            self.address_var.get()
                                                             ))
         con.commit()
         self.fetch_all()
         con.close() 
   def fetch_all(self):
             con = pymysql.connect(host = 'localhost', user = 'root', password='',database ='rakoto')
             cur = con.cursor()
             cur.execute('select * from teacher')
             rows = cur.fetchall()
             if len (rows)!=0:
               self.student_table.delete(*self.teacher_table.get_children())
               for row in rows:
                   self.student_table.insert("",END,value=row)
               con.commit()
             con.close()
              
             con.commit()
             con.close()

   def fetch_all (self):
              con.cursor()

root = Tk()
ob=Student(root)
root.mainloop()
