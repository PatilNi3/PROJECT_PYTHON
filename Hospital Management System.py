'''
- In this project we will create Pharmacy Management System and we will also include if we need to book doctor's appointment.
- Password will seen as ***
- Created button for Login, Reset, Exit
- when the user has not attempted true user name or password we will keep all 4 button as disabled, as soon as user gives
  correct credentials buttons will be normal state.
-
'''

import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()

class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")            # X-AXIS, Y-AXIS and 0,0 ARE LOCATION FROM LEFT TOPMOST
        self.frame = Frame(self.master)
        self.frame.pack()
        # ----------- #
        self.Username = StringVar()
        self.Password = StringVar()
        # ----------- #
        self.LabelTitle = Label(self.frame, text= "•○    PHARMACY MANAGEMENT SYSTEM    ○•",
                                font= ("Copperplate Gothic Light",30,"bold"), bd = 10, relief= "sunken")
        self.LabelTitle.grid(row= 0, column= 0, columnspan= 2, pady= 20)
        # ----------- #
        self.Loginframe1 = Frame(self.frame, width= 1000, height= 300, bd= 10, relief= "groove")
        self.Loginframe1.grid(row= 1, column= 0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady= 15)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=6, column=0, pady= 5)
        # ----------- #
        self.button_registration = Button(self.Loginframe3, text= "Patient Registration Window", state= DISABLED,
                                 font= ("arial", 15, "bold"), command= self.Registration_Window)
        self.button_registration.grid(row= 0, column= 0, padx= 10, pady= 10)

        self.button_hospital = Button(self.Loginframe3, text="Hospital Management Window", state= DISABLED,
                                 font=("arial", 15, "bold"), command=self.Hospital_Window)
        self.button_hospital.grid(row=0, column=1, padx=10, pady=10)

        self.button_dr_appointment = Button(self.Loginframe3, text="Doctor Management Window", state= DISABLED,
                                 font=("arial", 15, "bold"), command=self.Dr_Appointment_Window)
        self.button_dr_appointment.grid(row=1, column=0, padx=10, pady=10)

        self.button_medicine_store = Button(self.Loginframe3, text="Medicine Stock Window", state= DISABLED,
                                 font=("arial", 15, "bold"), command=self.Medicine_Store)
        self.button_medicine_store.grid(row=1, column=1, padx=10, pady=10)
        # ----------- #

    # Now we will make username and password frame

        self.LabelUsername = Label(self.Loginframe1, text= "User Name", font= ("arial", 20, "bold"), bd= 3)
        self.LabelUsername.grid(row= 0, column= 0)

        self.textUsername = Entry(self.Loginframe1, font= ("arial", 20, "bold"), bd = 3, textvariable= self.Username)
        self.textUsername.grid(row= 0, column= 1, padx= 40, pady= 15)

        self.LabelPassword = Label(self.Loginframe1, text= "Password", font= ("arial", 20, "bold"), bd= 3)
        self.LabelPassword.grid(row= 1, column= 0)

        self.textPassword = Entry(self.Loginframe1, font=("arial", 20, "bold"), show= "*", bd=3, textvariable=self.Password)
        self.textPassword.grid(row= 1, column= 1, padx=40, pady=15)
        # ----------- #
        self.button_Login = Button(self.Loginframe2, text= "Login", width= 20, font= ("arial", 18, "bold"),
                                   command= self.login_system)
        self.button_Login.grid(row= 0, column= 0, padx=10, pady=10)

        self.button_Reset = Button(self.Loginframe2, text="Reset", width=20, font=("arial", 18, "bold"),
                                   command= self.reset_button)
        self.button_Reset.grid(row=0, column=3, padx=10, pady=10)

        self.button_Exit = Button(self.Loginframe2, text="Exit", width=20, font=("arial", 18, "bold"),
                                  command= self.exit_button)
        self.button_Exit.grid(row=0, column=6, padx=10, pady=10)

    def login_system(self):
        user = self.Username.get()
        password = self.Password.get()

        if(user == str("admin") and (password == str("admin"))):
            self.button_registration.config(state= NORMAL)
            self.button_hospital.config(state= NORMAL)
            self.button_dr_appointment.config(state= NORMAL)
            self.button_medicine_store.config(state= NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", 'You have entered an invalid username or password')
            self.button_registration.config(state= DISABLED)
            self.button_hospital.config(state= DISABLED)
            self.button_dr_appointment.config(state= DISABLED)
            self.button_medicine_store.config(state= DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_button(self):
        self.button_registration.config(state=DISABLED)
        self.button_hospital.config(state=DISABLED)
        self.button_dr_appointment.config(state=DISABLED)
        self.button_medicine_store.config(state=DISABLED)
        # because when we will reset still we haven't given correct username and password
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def exit_button(self):
        self.exit_button = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure want to exit?")
        if self.exit_button > 0:
            # we will close that master screen
            self.master.destroy()
            return

    # First of all we will define our window
    def Registration_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def Dr_Appointment_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)

    def Medicine_Store(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background= "black")

        # I'm taking live time and date by using time module
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()

        ### this var1,2,3,5 are for combo_box ###
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()     # I'll keep as int because we I've keep here nemerical values

        Membership = StringVar()
        Membership.set("0") # when membership checkbox is unchecked or reset has been done it will automatically set as 0

        ##### functions #####
        def exitbtn():
            exitbtt = tkinter.messagebox.askyesno("Member Registration Form", "are you sure want to exit ?")
            if exitbtt > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return

        def resetbtt():
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Firstname.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state=DISABLED)

        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askyesno("Member Registration Form", "You want to add as new record")
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)
                return

        def Reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def membership_fees():
            if (var5.get() == 1):   # when checkbox is checked
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000) # it is random price for membership plan, i can change it as I want
                Membership.set(str(item)+ "Rs")
            elif (var5.get() == 0):
                # when checkbox is unchecked
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")

        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t" + Date_of_Registration.get() + "\t" + Ref.get() + "\t\t" + Firstname.get() +
                                   "\t\t" + Lastname.get() + "\t" + Mobile_no.get() + "\t" + Address.get() + "\t\t" +
                                    Pincode.get() + "\t" + member_gendercmb.get() + "\t\t" + Membership.get() + "\n")

        ##### TITLE #####
        title = Label(self.root, text="Member Registration Form", font=("monotype corsiva",30,"bold"), bd=5,
                      relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)

        ##### Member Frame #####
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        Manage_Frame.place(x=20, y=100, width=450, height=630)

        ##### text, label, combo_boxes in Manage Frame #####
        Cus_title = Label(Manage_Frame, text="Customer Detail", font=("arail",20,"bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        member_datelbl = Label(Manage_Frame, text="Date", font=("arial",15,"bold"), bg="#001a66", fg="white")
        member_datelbl.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        member_datetxt = Entry(Manage_Frame, font=("arial",15,"bold"), textvariable=Date_of_Registration)
        member_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("arial",15,"bold"), state=DISABLED, text= Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnamelbl = Label(Manage_Frame, text="First Name", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_fnamelbl.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnamelbl = Label(Manage_Frame, text="Last Name", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_lnamelbl.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobilelbl = Label(Manage_Frame, text="Mobile No.", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_mobilelbl.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobiletxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addresslbl = Label(Manage_Frame, text="Address", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_addresslbl.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addresstxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodelbl = Label(Manage_Frame, text="Pin Code", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_pincodelbl.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderlbl = Label(Manage_Frame, text="Gender", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_genderlbl.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gendercmb = ttk.Combobox(Manage_Frame, text= var4, state="readonly", font=("arial",15,"bold"), width=18)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0) # when nothing will be given it will set as empty which I given at index 0
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_prooflbl = Label(Manage_Frame, text="ID Proof", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_id_prooflbl.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proofcmb = ttk.Combobox(Manage_Frame, text=var3, state="readonly", font=("arial", 15, "bold"), width=18)
        member_id_proofcmb['values'] = ("", "Aadhar Card", "Pan Card", "Passport", "Driving Licence")
        member_id_proofcmb.current(0)  # when nothing will be given it will set as empty which I given at index 0
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelbl = Label(Manage_Frame, text="Member Type", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_memtypelbl.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_memtypecmb = ttk.Combobox(Manage_Frame, text=var2, state="readonly", font=("arial", 15, "bold"), width=18)
        member_memtypecmb['values'] = ("", "Ayushman Card", "Insurance", "Pay Immediately", "Pay when leaving")
        member_memtypecmb.current(0)  # when nothing will be given it will set as empty which I given at index 0
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentwithlbl = Label(Manage_Frame, text="Payment with", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_paymentwithlbl.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text=var1, state="readonly", font=("arial", 15, "bold"), width=18)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card - Rupay", "Debit Card - Visa", "Debit Card - Mastercard",
                                           "Credit Card", "PhonePay", "GooglePay", "PayTM")
        member_paymentwithcmb.current(0)  # when nothing will be given it will set as empty which I given at index 0
        member_paymentwithcmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Membership Fees", variable=var5, onvalue=1, offvalue=0,
                                        font= ("arial",15,"bold"), bg="#001a66", fg="white", command=membership_fees)
        member_membership.grid(row=12, column=0, sticky="w")
        member_membershiptxt = Entry(Manage_Frame, font=("arial", 15, "bold"), state=DISABLED, justify=RIGHT,
                                     textvariable=Membership)
        member_membershiptxt.grid(row=12, column=1, pady=5, padx=10, sticky="w")

        ##### Detail Frame #####
        detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        detail_frame.place(x=500, y=100, width=820, height=630)

        detail_label = Label(detail_frame, font=("arial", 11, "bold"), pady=10, padx=2, width=95, text="Date\t Ref ID    Firstname    Lastname    Mobile No    Address    Pincode    Gender    Membership")
        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")
        detail_labeltxt = Text(detail_frame, width=123, height=34, font=("arial",10))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)

        ##### I have added button in detail frame #####
        receiptbtn = Button(detail_frame, padx=15, bd=5, font=("arail",12,"bold"), bg="#ff9966", width=20, text="Receipt",
                            command=Receipt)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(detail_frame, padx=15, bd=5, font=("arail", 12, "bold"), bg="#ff9966", width=20, text="Reset",
                          command=reeesetbtt)
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_frame, padx=15, bd=5, font=("arail", 12, "bold"), bg="#ff9966", width=20, text="Exit",
                         command=exitbtn)
        exitbtn.grid(row=2, column=2)

class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")  # I will consider full screen (max window)
        self.root.configure(background="black")

#### VARIABLE DECLARATION #####
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTableNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientID = StringVar()
        PatientNHnumber = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        def Reference_numfunc():    #to generate random number automatically
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptionfunc():
            Reference_numfunc()
            TextPrescription.insert(END, "Patient ID: "+PatientID.get()+"\n")
            TextPrescription.insert(END, "Patient Name: "+Patientname.get()+"\n")
            TextPrescription.insert(END, "Tablet: "+cmbTableNames.get()+"\n")
            TextPrescription.insert(END, "Number of Tablets: "+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END, "Daily Dose: "+DailyDose.get()+"\n")
            TextPrescription.insert(END, "Issued Date: "+IssuedDate.get()+"\n")
            TextPrescription.insert(END, "Expiry Date: "+ExpiryDate.get()+"\n")
            TextPrescription.insert(END, "Storage: "+StorageAdvice.get()+"\n")
            TextPrescription.insert(END, "More Information: "+MoreInformation.get()+"\n")
            return

        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+
                                        Patientname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTableNames.get()
                                        +"\t"+Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+
                                        "\t\t"+DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t"+PatientID.get()+"\n")
            return

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital management Sysytem", "are you sure want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return

        def deletefunc():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return

        def resetfunc():
            Ref.set("")
            cmbTableNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientID.set("")
            PatientNHnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0", END)
            return

##### TITLE #####
        title = Label(self.root, text="Hospital Management System", font=("monotype corsiva",42,"bold"), bd=5,
                      relief=GROOVE, bg="#2eb8b8", fg="black")
        title.pack(side=TOP, fill=X)

##### FRAMES #####
        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Data_Frame.place(x=10, y=510)

##### INNER FRAMES #####
        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information", font=("arial",20,"italic bold"),
                                    height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription", font=("arial", 20, "italic bold"),
                                    height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data", font=("arial",12,"italic bold"),
                                    height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)

##### LABELS #####
        Datelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Data", padx=2, bg="#0099cc")
        Datelbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        ##### REF #####
        Reflbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Reference Number", padx=2, bg="#0099cc")
        Reflbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, state=DISABLED, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        ##### PATIENT ID #####
        PatientIDlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient ID", padx=2, bg="#0099cc")
        PatientIDlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        PatientIDtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientID)
        PatientIDtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        ##### PATIENT NAME #####
        PatientNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2,
                             bg="#0099cc")
        PatientNamelbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Patientname)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        ##### DATE OF BIRTH #####
        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Birth", padx=2,
                               bg="#0099cc")
        Dateofbirthlbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        ##### ADDRESS #####
        Addresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Address", padx=2, bg="#0099cc")
        Addresslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        ##### NHS NUMBER #####
        NHSnumberlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="NHS Unique Number", padx=2,
                             bg="#0099cc")
        NHSnumberlbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        ##### TABLET NAME #####
        Tabletlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Tablet", padx=2, bg="#0099cc")
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=cmbTableNames, width=25, state="readonly",
                                 font=("arial",12,"bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dolo", "Vicks Action 500", "Crocin", "Azithromycin", "Ketofresh Active",
                               "Terbinadoc", "Himalaya Telekt", "Himalaya Purim")
        Tabletcmb.current(0)    # I will keep index 0 when nothing is selected
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)

        ##### NO. OF TABLETS #####
        No_of_tabletslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="No. of Tablets", padx=2,
                                 bg="#0099cc")
        No_of_tabletslbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        No_of_tabletstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Number_of_Tablets)
        No_of_tabletstxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

##### NOW I WILL MAKE THE SECOND COLUMN OF OTHER DETAILS IN SAME FRAME #####

        ##### HOSPITAL CODE #####
        HospitalCodelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Hospital Code", padx=2, bg="#0099cc")
        HospitalCodelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        ##### HOSPITAL CODE #####
        StorageAdvicelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Storage Advice", padx=2,
                                bg="#0099cc")
        StorageAdvicelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvice, width=23, state="readonly",
                                 font=("arial", 12, "bold"))
        StorageAdvicecmb['values'] = ("", "Under room temp", "below 5*C", "Regrigeration", )
        StorageAdvicecmb.current(0)  # I will keep index 0 when nothing is selected
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        ##### LOT NO. OF MEDICINE #####
        Lot_nolbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Lot No", padx=2,
                                bg="#0099cc")
        Lot_nolbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        ##### ISSUED DATE #####
        IssuedDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Issued Date", padx=2,
                          bg="#0099cc")
        IssuedDatelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=IssuedDate)
        IssuedDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        ##### EXPIRY DATE #####
        ExpiryDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Expiry Date", padx=2,
                              bg="#0099cc")
        ExpiryDatelbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        ##### DAILY DOSE #####
        DailyDoselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Daily Dose", padx=2,
                              bg="#0099cc")
        DailyDoselbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        DailyDosetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=DailyDose)
        DailyDosetxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        ##### SIDE EFFECTS #####
        SideEffectslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Side Effects", padx=2,
                             bg="#0099cc")
        SideEffectslbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        ##### MORE INFORMATION #####
        MoreInformationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="More Information", padx=2,
                               bg="#0099cc")
        MoreInformationlbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        ##### MEDICATION [YES/NO] #####
        Medicationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Medication",padx=2, bg="#0099cc")
        Medicationlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)

        ##### Text Field for Prescription #####
        TextPrescription = Text(Data_FrameRight, font=("arial",12,"bold"), width=55, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0, column=0)

        ##### Text for Prescription Data #####
        TextPrescriptionData = Text(Data_Framedata, font=("arial", 12, "bold"), width=203, height=12)
        TextPrescriptionData.grid(row=1, column=0)

        ##### I am going to add button to the middle frame #####
        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial",15,"bold"), width=22, command=prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Button_Frame, text="Prescription Data", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial", 15, "bold"), width=22, command=prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial", 15, "bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial", 15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        prescriptiondatarow = Label(Data_Framedata, bg="white", font=("arial",12,"bold"),
                                    text="Data\tReference ID\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo. of Tablets\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatient ID")
        prescriptiondatarow.grid(row=0, column=0, sticky=W)

class Doctor():
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

##### all function declared here #####
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId = StringVar()
        Drname = StringVar()
        DateofBirth = StringVar()
        Spec = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experience = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Diease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Management System", "are you sure want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return

        def resetfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spec.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Diease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return

        def deletefunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spec.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Diease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return
        def Patient_idFunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            DrId.set(randomnumber)

        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+DrId.get()+"\t"+Drname.get()+"\t\t"+
                                        DateofBirth.get()+"\t\t"+Spec.get()+"\t\t"+GovtPri.get()+"\t\t"+Surgeries.get()+
                                        "\t\t"+Experience.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+PtName.get()
                                        +"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")
            return

        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END, "Date: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END, "Patient Name: \t\t"+PtName.get()+"\n")
            TextPrescription.insert(END, "Appointment Time: \t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END, "Age: \t\t"+PtAge.get()+"\n")
            TextPrescription.insert(END, "Address: \t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END, "Disease: \t\t"+Diease.get()+"\n")
            TextPrescription.insert(END, "Case: \t\t"+Case.get()+"\n")
            TextPrescription.insert(END, "Benefit Card: \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END, "To meet Dr: \t\t"+Drname.get()+"\n")
            TextPrescription.insert(END, "Dr. Mobile No.: \t\t"+DrMobile.get()+"\n")
            return

        ##### TITLE LABEL #####
        title = Label(self.root, text="Doctor Management system", font=("monotype corsiva",42,"bold"), bd=5,
                      relief=GROOVE, bg="#b7d8d6", fg="black")
        title.pack(side=TOP, fill=X)

        ##### FRAME #####
        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10, y=80)

        Buttons_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10, y=460)

        Data_Frame = Frame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#eef3db")
        Data_Frame.place(x=10, y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",font=("arial",20,"italic bold"),
                                    height=390, bd=7, pady=1, relief=RIDGE, bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Doctor & Details", font=("arial",12,"italic bold"),
                                    height=390, bd=7, relief=RIDGE, bg="#b7d8d6")
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Patient & Information", font=("arial",15,"italic bold"),
                                    height=390, bd=7, relief=RIDGE, bg="#789e9e")
        Data_FrameRight.pack(side=RIGHT)

        ##### DOCTOR'S ID #####
        DrIdlbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Doctor ID", bg="#789e9e")
        DrIdlbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        DrIdtxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, state=DISABLED, textvariable=DrId)
        DrIdtxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        DrNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Doctor Name", bg="#789e9e")
        DrNamelbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        DrNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Drname)
        DrNametxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        DateofBirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Birth", bg="#789e9e")
        DateofBirthlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        DateofBirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=DateofBirth)
        DateofBirthtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        Speclbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Specialisation", bg="#789e9e")
        Speclbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Spectxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Spec)
        Spectxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        GovtPrilbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Govt/Private", bg="#789e9e")
        GovtPrilbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable=GovtPri, width=25, state="readonly", font=("arial",12,"bold"))
        GovtPricmb['values'] = ("","Goverment","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        Surgerieslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Surgeries", bg="#789e9e")
        Surgerieslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Surgeries)
        Surgeriestxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        Experiencelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Experience", bg="#789e9e")
        Experiencelbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        Experiencetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Experience)
        Experiencetxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Nurseslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Nurses under Dr", bg="#789e9e")
        Nurseslbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        Nursestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Nurses)
        Nursestxt.grid(row=7, column=1, padx=10, pady=5, sticky=E)

        DrMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Doctor Mobile No.", bg="#789e9e")
        DrMobilelbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=DrMobile)
        DrMobiletxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        Datelbl = Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Date", padx=2, bg="#789e9e")
        Datelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        PtNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2, bg="#789e9e")
        PtNamelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        PtNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtName)
        PtNametxt.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        Apptimelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Appointment Time", padx=2,
                          bg="#789e9e")
        Apptimelbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Apptimetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Apptime)
        Apptimetxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        PtAgelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Age", padx=2,
                           bg="#789e9e")
        PtAgelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        PtAgetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtAge)
        PtAgetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        PatientAddresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Address", padx=2,
                         bg="#789e9e")
        PatientAddresslbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        PatientAddresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientAddress)
        PatientAddresstxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        PtMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Mobile", padx=2,
                                  bg="#789e9e")
        PtMobilelbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtMobile)
        PtMobiletxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        Dieaselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Disease", padx=2,
                            bg="#789e9e")
        Dieaselbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        Dieasetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Diease)
        Dieasetxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        Caselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Case", padx=2,
                          bg="#789e9e")
        Caselbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable=Case, width=25, state="readonly", font=("arial",12,"bold"))
        Casecmb['values'] = ("","New Case", "Old Case")
        Casecmb.current(0)
        Casecmb.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        BenefitCardlbl = Label(Data_FrameLeft, font=("arial",12,"bold"), text="Benefit Card", width=20, padx=10,
                               bg="#789e9e")
        BenefitCardlbl.grid(row=8, column=2, sticky=W)

        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable=BenefitCard, width=25, state="readonly",
                                      font=("arial",12,"bold"))
        BenefitCardcmb['values'] = ("","Ayushman Card","Health Insurance","Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8, column=3, padx=10, sticky=E)

        ##### TEXT PRESCRIPTION #####
        TextPrescription = Text(Data_FrameRight, font=("arial",12,"bold"), width=55, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0, column=0)

        TextPrescriptionData = Text(Data_Framedata, font=("arial",12,"bold"), width=203, height=12)
        TextPrescriptionData.grid(row=1, column=0)

        ##### TEXT PRESCRIPTION #####
        Prescriptionbtn = Button(Buttons_Frame, text="Patient Information", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial",15,"bold"), width=22, command=prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        DoctorDetailbtn = Button(Buttons_Frame, text="Doctor's Details", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=prescriptiondatafunc)
        DoctorDetailbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Buttons_Frame, text="Reset", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Buttons_Frame, text="Delete", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Buttons_Frame, text="Exit", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Prescriptiondatarow = Label(Data_Framedata, bg="white", font=("arial",12,"bold"),
                                    text="Date\tDoctorId\tDoctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\tPatient Age")
        Prescriptiondatarow.grid(row=0, column=0, sticky=W)

class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine Management System")
        self.master.geometry("1350x750+0+0")            # X-AXIS, Y-AXIS and 0,0 ARE LOCATION FROM LEFT TOPMOST
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()
















