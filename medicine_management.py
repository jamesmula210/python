from tkinter import *
import random
import time
import datetime
import tkinter.messagebox
from tkinter import ttk


def main():
    root = Tk()
    project = Project1(root)


class Project1:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine management system")
        self.frame = Frame(self.master)
        self.master.geometry('1350x750+0+0')
        self.frame.pack()

        self.Password = StringVar()
        self.Username = StringVar()

        self.LabelTitle = Label(self.frame, text='Medicine management system', font=('arial', 50, 'bold'), bd=20, )
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame = LabelFrame(self.frame, width=1010, height=600, bd=20, font=('arial', 20, 'bold'),
                                     relief='ridge')
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=90, bd=20, font=('arial', 20, 'bold'),
                                      relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        self.LoginFrame3 = LabelFrame(self.frame, width=1000, height=100, bd=20, font=('arial', 20, 'bold'),
                                      relief='ridge')
        self.LoginFrame3.grid(row=3, column=0, pady=40)

        self.Username_label = Label(self.LoginFrame, text='Username', font=('arial', 20, 'bold'), bd=20, )
        self.Username_label.grid(row=0, column=0, columnspan=2, pady=40)

        self.Username_text = Entry(self.LoginFrame, text='Username', font=('arial', 20, 'bold'), bd=20,
                                   txtvar=self.Username)
        self.Username_text.grid(row=0, column=1, columnspan=2, pady=40)

        self.Password_label = Label(self.LoginFrame, text='Password', font=('arial', 20, 'bold'), bd=20, )
        self.Password_label.grid(row=1, column=0, columnspan=2, pady=40)

        self.Password_text = Entry(self.LoginFrame, text='Password', font=('arial', 20, 'bold'), bd=20,
                                   txtvar=self.Username)
        self.Password_text.grid(row=1, column=0, columnspan=2, pady=40)

        self.btnLogin = Button(self.LoginFrame2, text="Login", width=30, font=('ariel', 30),
                               command=self.system_access)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.LoginFrame2, text="Reset", width=30, font=('ariel', 30),
                               command=self.reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.LoginFrame2, text="Exit", width=30, font=('ariel', 30),
                              command=self.exit)
        self.btnExit.grid(row=0, column=2)

        self.btnRegister = Button(self.LoginFrame3, text="Registration system window", state=DISABLED,
                                  command=self.project_register)

        self.btnRegister.grid(row=0, column=0)

        self.btnAdminister = Button(self.LoginFrame3, text="Administration management system",
                                    state=DISABLED, command=self.project_administer)
        self.btnAdminister.grid(row=0, column=1)

    def system_access(self):
        user = (self.Username.get())
        passwd = (self.Password.get())

        if(user == str("james")) and (passwd == str(123)):
            self.btnRegister.config(state=NORMAL)
            self.btnAdminister.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Medicine system", "invalid details")
            self.btnRegister.config(state=DISABLED)
            self.btnAdminister.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.Username_text.focus()

    def reset(self):
        self.btnRegister.config(state=DISABLED)
        self.btnAdminister.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.Username_text.focus()

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Medicine system", "Do you want to exit?")

        if self.exit > 0:
            self.master.destroy()
            return


    def project_register(self):
        self.project_window = Toplevel(self.master)
        self.project = Project2(self.project_window)

    def project_administer(self):
        self.project_window = Toplevel(self.master)
        self.project = Project3(self.project_window)


class Project2:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration system window")
        self.frame = Frame(self.master)
        self.master.geometry('1350x750+0+0')
        self.frame.pack()

        DateOfOrder=StringVar()
        DateOfOrder.set(time.strftime("%d/%m/%y"))

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()

        firstname = StringVar()
        surname = StringVar()
        postcode = StringVar()
        telephone = StringVar()
        address = StringVar()
        ref = StringVar()

        Membership = StringVar()
        Membership.set("0")

        def exit():
            exit = tkinter.messagebox.askyesno("registration system window","do you want to exit?")
            if exit>0:
                master.destroy()
                return

        def reset():
            firstname.set("")
            surname.set("")
            postcode.set("")
            telephone.set("")
            address.set("")
            ref.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_id.current(0)
            self.cboType_of_member.current(0)
            self.cboMethod_of_payment.current(0)

        def add_new_record():
            add_new_record = tkinter.messagebox.askokcancel("registration system window",
                                                            "do you want to add new record?")
            if add_new_record > 0:
                reset()
            elif add_new_record <= 0:
                reset()
                self.txtReceipt.delete("1.0", END)
                return

        def reference_no():
            ref_mem = StringVar()
            y = random.randint(10000, 700000)
            random_ref = str(y)
            ref_mem.set(random_ref)
            ref.set(random_ref)

        def receipt():
            reference_no()
            self.txtReceipt.insert(END, "\t" + ref.get()+"\t"+firstname.get()+"\t"+surname.get()+"\t"+address.get()+
                                   "\t"+DateOfOrder.get()+"\t"+telephone.get()+"\t"+Membership.get()+"\n")

        def period_fees():
            global fee1
            if var4.get() == 1:
                self.txtMembership.configure(state=NORMAL)
                object1 = float(40)
                Membership.set("$" + str(object1))
                fee1 = Membership.get()
            elif var4.get() == 0:
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")


        Mainframe = Frame(self.master)
        Mainframe.grid()

        Titleframe = Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        Titleframe.pack(side=TOP)
        self.lblTitle = Label(Titleframe, font=('ariel', 59, 'bold'), text="Registration system window", padx=2)
        self.lblTitle.grid()

        MemberDetailsFrame = LabelFrame(Mainframe, width=1350, height=800, bd=20, relief=RIDGE, pady=5)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=880, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, width=350, height=400, bd=20, relief=RIDGE, text="Customername")
        MembersName_F.grid(row=0, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, width=1000, height=400, bd=20, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        self.lblReferenceNo = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Reference number", bd=7)
        self.lblReferenceNo.grid(row=0, column=0)
        self.txtReferenceNo = Entry(MembersName_F, font=('ariel', 20, 'bold'), textvariable=ref, state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstname = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(MembersName_F, font=('ariel', 20, 'bold'), textvariable=firstname, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(MembersName_F, font=('ariel', 20, 'bold'), text="surname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(MembersName_F, font=('ariel', 20, 'bold'), textvariable=surname, insertwidth=2)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Address", bd=7)
        self.lblAddress .grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(MembersName_F, font=('ariel', 20, 'bold'),textvariable=address, insertwidth=2)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostcode = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Postcode", bd=7)
        self.lblPostcode.grid(row=4, column=0, sticky=W)
        self.txtPostcode = Entry(MembersName_F, font=('ariel', 20, 'bold'),textvariable=postcode, insertwidth=2)
        self.txtPostcode.grid(row=4, column=1)

        self.lblTelephone = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(MembersName_F, font=('ariel', 20, 'bold'),textvariable=telephone, insertwidth=2)
        self.txtTelephone.grid(row=5, column=1)

        self.lblDate = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(MembersName_F, font=('ariel', 20, 'bold'), textvariable=DateOfOrder, insertwidth=2)
        self.txtDate.grid(row=6, column=1)

        self.lblProve_id = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Prove id", bd=7)
        self.lblProve_id.grid(row=7, column=0, sticky=W)

        self.cboProve_id = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly',
                                        font=('ariel', 14, 'bold'), width=19)
        self.cboProve_id['value'] = ('', 'visa', 'national id', 'drivers license', 'master card')
        self.cboProve_id.current(0)
        self.cboProve_id.grid(row=7, column=1)

        self.lblType_of_member = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Type of member", bd=7)
        self.lblType_of_member .grid(row=8, column=0, sticky=W)

        self.cboType_of_member = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly',
                                              font=('ariel', 14, 'bold'), width=19)

        self.cboType_of_member['value'] = ('', 'perennial', 'full', 'annual', 'temporary')
        self.cboType_of_member.current(0)
        self.cboType_of_member.grid(row=8, column=1)

        self.lblMethod_of_payment = Label(MembersName_F, font=('ariel', 20, 'bold'), text="Method of payment", bd=7)
        self.lblMethod_of_payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_payment = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly',
                                                 font=('ariel', 14, 'bold'), width=19)

        self.cboMethod_of_payment['value'] = ('', 'cash', 'mpesa', 'western union', 'paypal')
        self.cboMethod_of_payment.current(0)
        self.cboMethod_of_payment.grid(row=9, column=1)

        self.chkMembership = Checkbutton(MembersName_F, text="Fees", variable=var4, onvalue=1, offvalue=0,
                                         font=('ariel', 16, 'bold')).grid(row=10, column=0, sticky=W)
        self.txtMembership = Entry(MembersName_F, font=('ariel', 16, 'bold'), textvariable=Membership, bd=7,insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10, column=1)

        self.lblLabel = Label(Receipt_ButtonFrame, font=('ariel', 16, 'bold'), pady=10,
                              text="Reference\tFirstname\tSurname\tAddress\t reg_date\ttelephone\tmember_paid", bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame, font=('ariel', 16, 'bold'), width=112, height=22, pady=14, bd=7)
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        self.btnReceipt = Button(Receipt_ButtonFrame, font=('ariel', 20, 'bold'), command=receipt, text="receipt", padx=20,
                                 bd=8, width=16).grid(row=2, column=0)
        self.btnReset = Button(Receipt_ButtonFrame, font=('ariel', 20, 'bold'), text="reset", command=add_new_record, padx=20,
                               bd=8, width=16).grid(row=2, column=1)
        self.btnExit = Button(Receipt_ButtonFrame, font=('ariel', 20, 'bold'), text="exit", command=exit, padx=20,
                              bd=8, width=16).grid(row=2, column=2)
class Project3:
    def __init__(self, master):
        self.master = master
        self.master.title("Administration management system")
        self.frame = Frame(self.master)
        self.master.geometry('1350x750+0+0')
        self.frame.pack()


if __name__ == '__main__':
    main()