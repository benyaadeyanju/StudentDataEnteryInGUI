from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import mysql.connector
import time
#import datetime

class DataEntryForm:
    def __init__(self,root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')


        MainFrame = Frame(self.root,bd=10, width=1350, height=700, relief=RIDGE)
        MainFrame.grid()

        #=================================variables==========================================
        RefNo= StringVar()
        Firstname= StringVar()
        Surname = StringVar()
        Address = StringVar()
        Telephone = StringVar()
        RegDate = StringVar()
        Prove = StringVar()
        CurrentDate = StringVar()
        MemberType = StringVar()
        MemberFee = StringVar()
        Search = StringVar()
        DateDay = StringVar()
        DateToDay = StringVar()



        RegDate.set(time.strftime("%d/%m/%Y"))
        DateToDay.set(time.strftime("%d/%m/%Y"))

        ###################################Functions===================================
        def Reset():
            RefNo.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Telephone.set("")
            RegDate.set("")
            Prove.set("")
            CurrentDate.set("")
            MemberType.set("")
            MemberFee.set("")
            Search.set("")
            DateDay.set("")
            DateToDay.set("")


            RegDate.set(time.strftime("%d/%m/%Y"))
            DateToDay.set(time.strftime("%d/%m/%Y"))


        def iExit():
            iExit = tkinter.messagebox.askyesno("Data Entry Form","Cofirm if you want to exit or not")
            if iExit > 0:
                root.destroy()
                return



        def addData():
            if RefNo.get() == "" or Firstname.get()=="" or Surname.get() =="":
                tkinter.messagebox.showerror("Data Entry Form","Enter Correctly")
            else:
                sqlCon =mysql.connector.connect(host="localhost",user="root",password="",database="dataentry")
                cur = sqlCon.cursor()
                cur.execute("insert into dataentry values(%s,%s,%s,%s, %s, %s, %s,%s, %s, %s)",(RefNo.get(),
                                                                                             Firstname.get(),
                                                                                             Surname.get(),
                                                                                          
                                                                                             Address.get(),
                                                                                             Telephone.get(),
                                                                                             RegDate.get(),
                                                                                             Prove.get(),
                                                                                             CurrentDate.get(),
                                                                                             MemberType.get(),
                                                                                             MemberFee.get()))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
           
            tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successively")


        def DisplayData():
            sqlCon =mysql.connector.connect(host="localhost",user="root",password="",database="dataentry")
            cur = sqlCon.cursor()
            cur.execute("select * from dataentry")
            rows = cur.fetchall()
            if len(rows) != 0:
                tree_records.delete(*tree_records.get_children())
                for row in rows:
                    tree_records.insert('', END,values = row)
                    sqlCon.commit()
                sqlCon.close()



        def LearnersInfo(self,ev=""):
            viewInfo = tree_records.focus()
            LearnerData = tree_records.item(viewInfo)
            row = LearnerData['values']
            RefNo.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Telephone.set(row[4])
            RegDate.set(row[5])
            Prove.set(row[6])
            DateDay.set(row[7])
            MemberType.set(row[8])
            MemberFee.set(row[9])


        def update():
             sqlCon =mysql.connector.connect(host="localhost",user="root",password="",database="dataentry")
             cur = sqlCon.cursor()
             cur.execute("update dataentry set Firstname=%s, Surname=%s,Address=%s, Telephone=%s, RegDate=%s, ProveID=%s, CurrentDate=%s, MemberType=%s,MemberFee=%s where  RefNo=%s",(
                 
             Firstname.get(),
             Surname.get(),
             Address.get(),
             Telephone.get(),
             RegDate.get(),
             Prove.get(),
             DateDay.get(),
             MemberType.get(),
             MemberFee.get(),
             RefNo.get()))

             
             sqlCon.commit()
             DisplayData()
             sqlCon.close()
           
             tkinter.messagebox.showinfo("Data Entry Form","Record Updated Successively")


        def deleteDB():
            sqlCon =mysql.connector.connect(host="localhost",user="root",password="",database="dataentry")
            cur = sqlCon.cursor()
            query= "delete from dataentry where RefNo=%s"
            value=(RefNo.get(),)
            cur.execute(query,value)

            sqlCon.commit()
            sqlCon.close()
            DisplayData()
            tkinter.messagebox.showinfo("Delete","Record Deleted Successfully")


        def SearchDB():

            try:
                sqlCon =mysql.connector.connect(host="localhost",user="root",password="",database="dataentry")
                cur = sqlCon.cursor()
                cur.execute("select * from dataentry where RefNo='%s'"%Search.get())

                row = cur.fetchone()

                RefNo.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Telephone.set(row[4])
                RegDate.set(row[5])
                Prove.set(row[6])
                DateDay.set(row[7])
                MemberType.set(row[8])
                MemberFee.set(row[9])

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form","No such Record Found")
                Reset()
            sqlCon.close()
            Search.set("")

        

        
         #========================Widgets==========================================================
        TopFrame1 = Frame(MainFrame,bd=5, width=1340, height=200, relief=RIDGE, bg="cadet blue")
        TopFrame1.grid(row=0, column=0)
        TopFrame2 = Frame(MainFrame,bd=5, width=1340, height=50, relief=RIDGE, bg="cadet blue")
        TopFrame2.grid(row=1, column=0)
        TopFrame3 = Frame(MainFrame,bd=5, width=1340, height=300, relief=RIDGE, bg="cadet blue")
        TopFrame3.grid(row=2, column=0)


        InnerTopFrame1 = Frame(TopFrame1,bd=5, width=1330, height=190, relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2 = Frame(TopFrame2,bd=5, width=1330, height=48, relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3 = Frame(TopFrame3,bd=5, width=1330, height=280, relief=RIDGE)
        InnerTopFrame3.grid()



        #==========================================Labels==============================
        lblReference = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Reference No",bd=10)
        lblReference.grid(row=0, column=0, sticky=W)
        txtReference = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left',textvariable= RefNo)
        txtReference.grid(row=0, column=1)

        

        self.lblFirstname = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Firstname",bd=10)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left',textvariable= Firstname)
        self.txtFirstname.grid(row=1, column=1)


        self.lblSurname = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Surname",bd=10)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left',textvariable= Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Address",bd=10)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width= 83,justify='left',textvariable= Address)
        self.txtAddress.grid(row=3, column=1,columnspan=3)

        self.lblTelephone = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Telephone",bd=10)
        self.lblTelephone.grid(row=0, column=2, sticky=W)
        self.txtTelephone = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left',textvariable= Telephone)
        self.txtTelephone.grid(row=0, column=3)

        self.lblRegistrationDate = Label(InnerTopFrame1,font=('arial',12,'bold'), text="RegistrationDate",bd=10)
        self.lblRegistrationDate.grid(row=1, column=2, sticky=W)
        self.txtRegistrationDate = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left', textvariable= RegDate)
        self.txtRegistrationDate.grid(row=1, column=3)

        self.lblSearch = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Search",bd=10)
        self.lblSearch.grid(row=0, column=4, sticky=W)
        self.txtSearch = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=33,justify='left', textvariable= Search)
        self.txtSearch.grid(row=0, column=5)

        self.lblDate = Label(InnerTopFrame1,font=('arial',12,'bold'), text="Date",bd=10)
        self.lblDate.grid(row=1, column=4, sticky=W)
        self.txtDate = Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=32,justify='left', textvariable=DateToDay)
        self.txtDate.grid(row=1, column=5)
        

        self.lblProveofID= Label(InnerTopFrame1, font=('arial',12,'bold'),text="Prove ID", bd=10)
        self.lblProveofID.grid(row=2, column=2,sticky=W)
        self.cboProveofID=ttk.Combobox(InnerTopFrame1,font=('arial',12,'bold'),state='readonly', width=31,textvariable= Prove)
        self.cboProveofID['values'] =('','Pilot Licence','Driving Licence','Student ID','Passport')
        self.cboProveofID.current(0)
        self.cboProveofID.grid(row=2, column=3)

        self.lblMemberFee= Label(InnerTopFrame1, font=('arial',12,'bold'),text="Member Fee", bd=10)
        self.lblMemberFee.grid(row=3, column=4,sticky=W)
        self.cboMemberFee=ttk.Combobox(InnerTopFrame1,font=('arial',12,'bold'),state='readonly', width=31,textvariable= MemberFee)
        self.cboMemberFee['values'] =('','₦1000:00','₦500:00','₦250:00','₦150:00')
        self.cboMemberFee.current(0)
        self.cboMemberFee.grid(row=3, column=5)

        self.lblMemberType= Label(InnerTopFrame1, font=('arial',12,'bold'),text="Member Type", bd=10)
        self.lblMemberType.grid(row=2, column=4,sticky=W)
        self.cboMemberType=ttk.Combobox(InnerTopFrame1,font=('arial',12,'bold'),state='readonly', width=31,textvariable= MemberType)
        self.cboMemberType['values'] =('','Annual','Quartely','Monthly','Weekly')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=2, column=5)
        #============================================Scrool Bar=======================================================
        scroll_x = Scrollbar(InnerTopFrame3, orient=HORIZONTAL)
        scroll_y = Scrollbar(InnerTopFrame3, orient= VERTICAL)

        tree_records=ttk.Treeview(InnerTopFrame3,height=13,columns=("RefNo","Firstname","Surname","Address",
         "Telephone","RegDate","ProveID","CurrentDate","MemberType","MemberFee"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        tree_records.heading("RefNo", text="Reference")
        tree_records.heading("Firstname", text="Firstname")
        tree_records.heading("Surname", text="Suranme")      
        tree_records.heading("Address", text="Address")
        tree_records.heading("Telephone", text="Telephone")
        tree_records.heading("RegDate", text="Reg. date")
        tree_records.heading("ProveID", text="Prove of ID")
        tree_records.heading("CurrentDate", text="Current Date")
        tree_records.heading("MemberType", text="Member Tpye")
        tree_records.heading("MemberFee", text="Member Fee")

        tree_records['show']='headings'

        tree_records.column("RefNo", width=100)
        tree_records.column("Firstname", width=150)
        tree_records.column("Surname", width=150)
        tree_records.column("Address", width=252)
        tree_records.column("Telephone", width=100)
        tree_records.column("RegDate", width=100)
        tree_records.column("ProveID", width=100)
        tree_records.column("CurrentDate", width=100)
        tree_records.column("MemberType", width=150)
        tree_records.column("MemberFee", width=100)

        tree_records.pack(fill = BOTH, expand =1)


        tree_records.bind("<ButtonRelease-1>",LearnersInfo)

        DisplayData()




        

        #============================================Button=======================================================
        self.btnAddNew = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=14,text="Add New", command = addData)
        self.btnAddNew.grid(row=0, column=0)
        
        self.btnDisplay = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=13,text="Display", command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)
        
        self.btnUpdate = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=13,text="Update", command=update)
        self.btnUpdate.grid(row=0, column=2)
        
        self.btnDelete = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=13,text="Delete", command=deleteDB)
        self.btnDelete.grid(row=0, column=3)
        
        self.btnReset = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=13,text="Reset", command = Reset)
        self.btnReset.grid(row=0, column=4)
        
        self.btnExit = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=13,text="Exit", command=iExit)
        self.btnExit.grid(row=0, column=5)
        
        self.btnSearch = Button(InnerTopFrame2, pady=1,bd=4,font=('arial',16,'bold'), width=14,text="Search", command= SearchDB)
        self.btnSearch.grid(row=0, column=6)






if __name__=='__main__':
    root = Tk()
    application =DataEntryForm(root)
    root.mainloop()
