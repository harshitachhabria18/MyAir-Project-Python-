import mysql.connector as con
mydb=con.connect(host="localhost",user="root",password="Sep@2006",database="project")
cur=mydb.cursor()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def screen21():
    import webbrowser
    top21=Toplevel()
    def open_web():
        url="https://www.airportschoolahm.in/"
        webbrowser.open(url)
    top21.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top21,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="For more information about the school click below",font=("Courier 28 bold"),bg="cadetblue2",width=50)
    choose.place(anchor="center",relx=0.5,rely=0.27)
    button=Button(canvas,text="GO TO WEBSITE",height=4,width=18,font=("Coppergothicbold 16 bold"),fg="blue",bg="light green",command=open_web)
    button.pack()
    button.place(x=550,y=340)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top21.destroy)
    button1.pack()
    button1.place(x=170,y=650)

    top21.mainloop()


def screen20():
    top20=Toplevel()
    def atten():
        gr_no = gr_type.get()
        get1 = cur.execute("select attendance from attendance")
        data = cur.fetchall()
        total_count=0
        for i in data:
            for j in i:
                if(j=="Present" or j=="Absent"):
                    total_count=total_count+1           
        total=total_count

        present_count=0
        for i in data:
            for j in i:
                if(j=="Present"):
                    present_count=present_count+1
        present=present_count

        absent_count=0
        for i in data:
            for j in i:
                if(j=="Absent"):
                    absent_count=absent_count+1
        absent=absent_count

        attendance_present=(present_count*100)/total_count
        attendance_absent=(absent_count*100)/total_count

        labels = ['Present', 'Absent']
        sizes = [attendance_present,attendance_absent]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        canvas1= FigureCanvasTkAgg(fig, master=canvas)
        canvas1_widget = canvas1.get_tk_widget()
        canvas1_widget.place(x=660,y=240)

    
    top20.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top20,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
    grno.place(x=230, y=100)
    gr_type=IntVar()
    grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
    grentry.pack()
    grentry.place(x=430, y=103)
    gr_label = Label(canvas, text="Click here to view your attendance",font=("Courier 22 bold"), bg="cadetblue2", width=40)
    gr_label.place(x=70, y=170)
    button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=atten)
    button.pack()
    button.place(x=340,y=240)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top20.destroy)
    button1.pack()
    button1.place(x=170,y=650)
    
    top20.mainloop()

def screen19():
    top19=Toplevel()
    def pt1():
        def submit1():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, eco, acc, comp, bs, eng FROM pt1_4")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Economics', 'Accounts', 'Computer', 'BS','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT1 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit1)
        button.pack()
        button.place(x=620,y=400)
    def pt2():
        def submit2():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, eco, acc, comp, bs, eng FROM pt2_4")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Economics', 'Accounts', 'Computer', 'BS','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT2 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit2)
        button.pack()
        button.place(x=620,y=400)

    def halfy():
        def submit3():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, eco, acc, comp, bs, eng FROM halfy_4")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Economics', 'Accounts', 'Computer', 'BS','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("HALF YEARLY MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit3)
        button.pack()
        button.place(x=620,y=400)

    def final():
        def submit4():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, eco, acc, comp, bs, eng FROM final_4")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Economics', 'Accounts', 'Computer', 'BS','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("FINAL MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit4)
        button.pack()
        button.place(x=620,y=400)


        
    top19.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top19,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)
    
    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfy)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top19.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
    
    top19.mainloop()

def screen18():
    top18=Toplevel()
    def pt1():
        def submit1():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, maths, phy, comp, chem, eng FROM pt1_3")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Maths', 'Physics', 'Comoputer', 'Chemistry','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT1 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit1)
        button.pack()
        button.place(x=620,y=400)
    def pt2():
        def submit2():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, maths, phy, comp, chem, eng FROM pt2_3")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Maths', 'Physics', 'Comoputer', 'Chemistry','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT2 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit2)
        button.pack()
        button.place(x=620,y=400)

    def halfy():
        def submit3():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, maths, phy, comp, chem, eng FROM halfy_3")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Maths', 'Physics', 'Comoputer', 'Chemistry','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("HALF YEARLY MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit3)
        button.pack()
        button.place(x=620,y=400)

    def final():
        def submit4():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, maths, phy, comp, chem, eng FROM final_3")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Maths', 'Physics', 'Comoputer', 'Chemistry','English']
                    values=[i[1],i[2],i[3],i[4],i[5]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("FINAL MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit4)
        button.pack()
        button.place(x=620,y=400)


        
    top18.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top18,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)
    
    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfy)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top18.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
    top18.mainloop()

def screen17():
    top17=Toplevel()
    def sci_window():
        screen18()
    def comm_window():
        screen19()
    top17.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top17,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="Select any option",font=("Courier 28 bold"),bg="cadetblue2",width=25)
    choose.place(anchor="center",relx=0.5,rely=0.27)

    sci=Button(canvas,text="SCIENCE",height=5,width=23,font=("Courier 14 bold"),fg="black",bg="light green",command=sci_window)
    sci.place(x=550,y=300)

    comm=Button(canvas,text="COMMERCE",height=5,width=23,font=("Courier 14 bold"),fg="black",bg="light green",command=comm_window)
    comm.place(x=550,y=450)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top17.destroy)
    button1.pack()
    button1.place(x=170,y=650)

    top17.mainloop()

def screen16():
    top16=Toplevel()
    def pt1():
        def submit1():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, sans, eng, sst, comp FROM pt1_2")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Sanskrit','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT1 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit1)
        button.pack()
        button.place(x=620,y=400)
    def pt2():
        def submit2():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, sans, eng, sst, comp FROM pt2_2")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Sanskrit','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT2 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit2)
        button.pack()
        button.place(x=620,y=400)

    def halfy():
        def submit3():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, sans, eng, sst, comp FROM halfy_2")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Sanskrit','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("HALF YEARLY MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit3)
        button.pack()
        button.place(x=620,y=400)

    def final():
        def submit4():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, sans, eng, sst, comp FROM final_2")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Sanskrit','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("FINAL MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=250)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit4)
        button.pack()
        button.place(x=620,y=400)


        
    top16.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top16,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)
    
    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfy)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top16.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
    
    top16.mainloop()

def screen15():
    top15=Toplevel()
    def pt1():
        def submit1():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, guj, eng, sst, comp FROM pt1")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Gujarati','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT1 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720, y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445, y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit1)
        button.pack()
        button.place(x=620,y=400)
    def pt2():
        def submit2():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, guj, eng, sst, comp FROM pt2")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Gujarati','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("PT2 MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit2)
        button.pack()
        button.place(x=620,y=400)

    def halfy():
        def submit3():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, guj, eng, sst, comp FROM halfy")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Gujarati','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("HALF YEARLY MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit3)
        button.pack()
        button.place(x=620,y=400)

    def final():
        def submit4():
            gr_no = gr_type.get()
            get1 = cur.execute("SELECT grno, sci, maths, hindi, guj, eng, sst, comp FROM final")
            data = cur.fetchall()
            for i in data:
                if(i[0]==gr_no):
                    categories=['Science', 'Maths', 'Hindi', 'Gujarati','Eng','SST','Computer']
                    values=[i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                    plt.bar(categories, values, color='orange')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.title("FINAL MARKS")
                    plt.show()
        grno = Label(canvas, text="GRNO",font=("Courier 22 bold"), bg="cadetblue2", width=10)
        grno.place(x=520,y=250)
        gr_type=IntVar()
        grentry = Entry(canvas,textvariable=gr_type,width=12, font=("Courier 18 bold"))
        grentry.pack()
        grentry.place(x=720,y=252.5)
        gr_label = Label(canvas, text="Click here to view your marks",font=("Courier 22 bold"), bg="cadetblue2", width=30)
        gr_label.place(x=445,y=325)
        button = Button(canvas, text="SHOW", height=3, width=15, font=("Coppergothicbold 12 bold"), fg="blue", bg="light green", command=submit4)
        button.pack()
        button.place(x=620,y=400)
        
    top15.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top15,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)
    
    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfy)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top15.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
    
    top15.mainloop()

def screen14():
    def change():
        var1=var.get()
        if(var1<=5):
            screen15()
        elif(var1>=6 and var1<=10):
            screen16()
        else:
            screen17()
    def get():
        label1.config(text=var.get())
    top14=Toplevel()
    top14.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top14,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    var=IntVar()
    var.set("Select Your Class")
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    option_menu=OptionMenu(canvas,var,*options)
    option_menu.config(height=3,width=40,bg="light green",font=("Coppergothicbold 25 bold"))
    option_menu.pack()
    option_menu.place(anchor="center",relx=0.5,rely=0.32)

    button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get)
    button.place(x=500,y=420)
    label1 = Label( canvas , text = " ",font=("Coppergothicbold 12 bold"),width=15,height=3) 
    label1.place(x=700,y=415)

    b1=Button(canvas,text="NEXT",command=change,
                       bg="blue",
                       fg="white",
                       font=('Coppergothicbold 12 bold'),height=2,width=15,)
    b1.place(x=1050,y=650)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top14.destroy)
    button1.pack()
    button1.place(x=170,y=650)
    top14.mainloop()


def screen13():
    import webbrowser
    top13=Toplevel()
    def open_web():
        url="https://www.airportschoolahm.in/"
        webbrowser.open(url)
    top13.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top13,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="For more information about the school click below",font=("Courier 28 bold"),bg="cadetblue2",width=50)
    choose.place(anchor="center",relx=0.5,rely=0.27)
    button=Button(canvas,text="GO TO WEBSITE",height=4,width=18,font=("Coppergothicbold 16 bold"),fg="blue",bg="light green",command=open_web)
    button.pack()
    button.place(x=550,y=340)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top13.destroy)
    button1.pack()
    button1.place(x=170,y=650)

    top13.mainloop()

def screen12():
    def on_date_change():
        gr_no=grentry.get()
        selected_date = cal.get_date()
        atten_1=var.get()
        if(atten_1=="Present"):
            cur.execute("insert into attendance values({},'{}','{}')".format(gr_no,selected_date,atten_1))         
            mydb.commit()
            messagebox.showinfo("Information", "Your attendance has been recorded!", parent=top12)
            
        elif(atten_1=="Absent"):
            cur.execute("insert into attendance values({},'{}','{}')".format(gr_no,selected_date,atten_1))          
            mydb.commit()
            messagebox.showinfo("Information", "Your attendance has been recorded!", parent=top12)

        else:
            cur.execute("insert into attendance values({},'{}','{}')".format(gr_no,selected_date,atten_1))         
            mydb.commit()
            messagebox.showinfo("Information", "Your attendance has been recorded!", parent=top12)

    top12=Toplevel()
    top12.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top12,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    grno.place(x=500,y=97)

    grentry=Entry(canvas,width=12,font=("Courier 18 bold"))
    grentry.pack()
    grentry.place(x=700,y=100)

    l_date=Label(canvas,text="SELECT DATE",font=("Courier 30 bold"),fg="blue")
    l_date.place(x=550,y=170)
    cal = DateEntry(canvas, width=20,background='darkblue', foreground='white', borderwidth=2)
    cal.place(x=610,y=250)

    cal.bind("<<DateEntrySelected>>", on_date_change)

    var = StringVar()
    present = Radiobutton(canvas, text="PRESENT", variable=var, value="Present")
    present.config(font=("Calibri 20 bold"),width=10)
    present.place(x=595,y=320)
    
    absent = Radiobutton(canvas, text="ABSENT", variable=var, value="Absent")
    absent.config(font=("Calibri 20 bold"),width=10)
    absent.place(x=595,y=400)
    
    holiday = Radiobutton(canvas, text="HOLIDAY", variable=var, value="Holiday")
    holiday.config(font=("Calibri 20 bold"),width=10)
    holiday.place(x=595,y=480)

    button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=on_date_change)
    button.pack()
    button.place(x=602,y=580)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top12.destroy)
    button1.pack()
    button1.place(x=170,y=650)

    
    top12.mainloop()


def screen11():
    top11=Toplevel()
    def pt1():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get1():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top11)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get1)
        button1.place(x=600,y=15)
        def marks1():
            gr_no=grentry.get()
            eco=slider1.get()
            acc=slider2.get()
            comp=slider3.get()
            bs=slider4.get()
            eng=slider5.get()
            cur.execute("insert into pt1_4 values({},{},{},{},{},{})".format(gr_no,eco,acc,comp,bs,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top11)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_eco=Label(canvas,text="ECONOMICS",font=("Courier 27 bold"),fg="blue")
        l_eco.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_acc=Label(canvas,text="ACCOUNTS",font=("Courier 27 bold"),fg="blue")
        l_acc.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_bs=Label(canvas,text="BUSINESS STUDIES",font=("Courier 27 bold"),fg="blue")
        l_bs.place(x=750,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks1)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def pt2():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get2():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top11)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get2)
        button1.place(x=600,y=15)
        def marks2():
            gr_no=grentry.get()
            eco=slider1.get()
            acc=slider2.get()
            comp=slider3.get()
            bs=slider4.get()
            eng=slider5.get()
            cur.execute("insert into pt2_4 values({},{},{},{},{},{})".format(gr_no,eco,acc,comp,bs,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top11)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)

        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_eco=Label(canvas,text="ECONOMICS",font=("Courier 27 bold"),fg="blue")
        l_eco.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_acc=Label(canvas,text="ACCOUNTS",font=("Courier 27 bold"),fg="blue")
        l_acc.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_bs=Label(canvas,text="BUSINESS STUDIES",font=("Courier 27 bold"),fg="blue")
        l_bs.place(x=750,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks2)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def halfyearly():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get3():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top11)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get3)
        button1.place(x=600,y=15)
        def marks3():
            gr_no=grentry.get()
            eco=slider1.get()
            acc=slider2.get()
            comp=slider3.get()
            bs=slider4.get()
            eng=slider5.get()
            cur.execute("insert into halfy_4 values({},{},{},{},{},{})".format(gr_no,eco,acc,comp,bs,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top11)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_eco=Label(canvas,text="ECONOMICS",font=("Courier 27 bold"),fg="blue")
        l_eco.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_acc=Label(canvas,text="ACCOUNTS",font=("Courier 27 bold"),fg="blue")
        l_acc.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_bs=Label(canvas,text="BUSINESS STUDIES",font=("Courier 27 bold"),fg="blue")
        l_bs.place(x=750,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider15var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks3)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def final():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get4():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top11)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get4)
        button1.place(x=600,y=15)
        def marks4():
            gr_no=grentry.get()
            eco=slider1.get()
            acc=slider2.get()
            comp=slider3.get()
            bs=slider4.get()
            eng=slider5.get()
            cur.execute("insert into final_4 values({},{},{},{},{},{})".format(gr_no,eco,acc,comp,bs,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top11)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_eco=Label(canvas,text="ECONOMICS",font=("Courier 27 bold"),fg="blue")
        l_eco.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_acc=Label(canvas,text="ACCOUNTS",font=("Courier 27 bold"),fg="blue")
        l_acc.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_bs=Label(canvas,text="BUSINESS STUDIES",font=("Courier 27 bold"),fg="blue")
        l_bs.place(x=750,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)
        
        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks4)
        button.pack()
        button.place(relx=0.762,rely=0.9)

          
    top11.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top11,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)

    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfyearly)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top11.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
            
    top11.mainloop()
    


def screen10():
    top10=Toplevel()
    def pt1():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get1():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top10)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get1)
        button1.place(x=600,y=15)
        def marks1():
            gr_no=grentry.get()
            maths=slider1.get()
            phy=slider2.get()
            comp=slider3.get()
            chem=slider4.get()
            eng=slider5.get()
            cur.execute("insert into pt1_3 values({},{},{},{},{},{})".format(gr_no,maths,phy,comp,chem,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top10)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_phy=Label(canvas,text="PHYSICS",font=("Courier 27 bold"),fg="blue")
        l_phy.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_chem=Label(canvas,text="CHEMISTRY",font=("Courier 27 bold"),fg="blue")
        l_chem.place(x=830,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks1)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def pt2():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get2():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top10)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get2)
        button1.place(x=600,y=15)
        def marks2():
            gr_no=grentry.get()
            maths=slider1.get()
            phy=slider2.get()
            comp=slider3.get()
            chem=slider4.get()
            eng=slider5.get()
            cur.execute("insert into pt2_3 values({},{},{},{},{},{})".format(gr_no,maths,phy,comp,chem,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top10)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            

        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_phy=Label(canvas,text="PHYSICS",font=("Courier 27 bold"),fg="blue")
        l_phy.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_chem=Label(canvas,text="CHEMISTRY",font=("Courier 27 bold"),fg="blue")
        l_chem.place(x=830,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks2)
        button.pack()
        button.place(relx=0.762,rely=0.9)

        

    def halfyearly():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get3():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top10)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get3)
        button1.place(x=600,y=15)
        def marks3():
            gr_no=grentry.get()
            maths=slider1.get()
            phy=slider2.get()
            comp=slider3.get()
            chem=slider4.get()
            eng=slider5.get()
            cur.execute("insert into halfy_3 values({},{},{},{},{},{})".format(gr_no,maths,phy,comp,chem,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top10)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_phy=Label(canvas,text="PHYSICS",font=("Courier 27 bold"),fg="blue")
        l_phy.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_chem=Label(canvas,text="CHEMISTRY",font=("Courier 27 bold"),fg="blue")
        l_chem.place(x=830,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks3)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def final():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get4():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top10)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get4)
        button1.place(x=600,y=15)
        def marks4():
            gr_no=grentry.get()
            maths=slider1.get()
            phy=slider2.get()
            comp=slider3.get()
            chem=slider4.get()
            eng=slider5.get()
            cur.execute("insert into final_3 values({},{},{},{},{},{})".format(gr_no,maths,phy,comp,chem,eng))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top10)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            

        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=430,y=120)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=160)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=200)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_phy=Label(canvas,text="PHYSICS",font=("Courier 27 bold"),fg="blue")
        l_phy.place(x=835,y=120)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=160)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=200)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=300)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=340)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=380)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_chem=Label(canvas,text="CHEMISTRY",font=("Courier 27 bold"),fg="blue")
        l_chem.place(x=830,y=300)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=340)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=380)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=630,y=480)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=600,y=520)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=630,y=560)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks4)
        button.pack()
        button.place(relx=0.762,rely=0.9)

          
    top10.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top10,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)

    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfyearly)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top10.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
            
    top10.mainloop()

def screen9():
    top9=Toplevel()
    def back8():
        screen6()
    def sci_window():
        screen10()
    def comm_window():
        screen11()
    top9.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top9,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="Select any option",font=("Courier 28 bold"),bg="cadetblue2",width=25)
    choose.place(anchor="center",relx=0.5,rely=0.27)

    sci=Button(canvas,text="SCIENCE",height=5,width=23,font=("Courier 14 bold"),fg="black",bg="light green",command=sci_window)
    sci.place(x=550,y=300)

    comm=Button(canvas,text="COMMERCE",height=5,width=23,font=("Courier 14 bold"),fg="black",bg="light green",command=comm_window)
    comm.place(x=550,y=450)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top9.destroy)
    button1.pack()
    button1.place(x=170,y=650)
            

    top9.mainloop()

def screen8():
    top8=Toplevel()
    def pt1():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get1():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top8)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get1)
        button1.place(x=600,y=15)
        def marks1():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            sans=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into pt1_2 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,sans,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!",parent=top8)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_sans=Label(canvas,text="SANSKRIT",font=("Courier 27 bold"),fg="blue")
        l_sans.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks1)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def pt2():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get2():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top8)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get2)
        button1.place(x=600,y=15)
        def marks2():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            sans=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into pt2_2 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,sans,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!",parent=top8)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_sans=Label(canvas,text="SANSKRIT",font=("Courier 27 bold"),fg="blue")
        l_sans.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks2)
        button.pack()
        button.place(relx=0.762,rely=0.9)

        

    def halfyearly():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get3():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top8)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get3)
        button1.place(x=600,y=15)
        def marks3():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            sans=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into halfy_2 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,sans,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!",parent=top8)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_sans=Label(canvas,text="SANSKRIT",font=("Courier 27 bold"),fg="blue")
        l_sans.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider6_var,length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)
        
        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks3)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def final():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get4():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top8)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get4)
        button1.place(x=600,y=15)
        def marks4():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            sans=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into final_2 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,sans,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!",parent=top8)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        
        def on_slider_change1(value):
           l1.config(text=f'Marks:{slider1.get()}')
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_sans=Label(canvas,text="SANSKRIT",font=("Courier 27 bold"),fg="blue")
        l_sans.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks4)
        button.pack()
        button.place(relx=0.762,rely=0.9)

             
    top8.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top8,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)

    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfyearly)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top8.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
            
    top8.mainloop()

def screen7():
    top7=Toplevel()
    def pt1():    
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get1():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top7)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get1)
        button1.place(x=600,y=15)
        def marks1():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            guj=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into pt1 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,guj,eng,sst,comp))        
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!",parent=top7)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
            
        def on_slider_change1(value):
           l1.config(text=f'Marks:{slider1.get()}')
        
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_guj=Label(canvas,text="GUJARATI",font=("Courier 27 bold"),fg="blue")
        l_guj.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks1)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def pt2():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get2():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top7)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get2)
        button1.place(x=600,y=15)

        def marks2():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            guj=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into pt2 values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,guj,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top7)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
 
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
            
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_guj=Label(canvas,text="GUJARATI",font=("Courier 27 bold"),fg="blue")
        l_guj.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=20, orient=HORIZONTAL, variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=20, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks2)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def halfyearly():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.pack()
        grentry.place(x=400,y=25)
        def get3():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top7)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get3)
        button1.place(x=600,y=15)

        def marks3():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            guj=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into halfy values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,guj,eng,sst,comp))
            mydb.commit()
            
            messagebox.showinfo("Message","Your record has been submitted!", parent=top7)
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
            
        def on_slider_change1(value):
            l1.config(text=f'Marks:{slider1.get()}')
            
        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)
        
        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider1_var, length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)

        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_guj=Label(canvas,text="GUJARATI",font=("Courier 27 bold"),fg="blue")
        l_guj.place(x=830,y=280)

        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)

        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks3)
        button.pack()
        button.place(relx=0.762,rely=0.9)

    def final():
        grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
        grno.place(x=200,y=20)
        var1=IntVar()
        grentry=Entry(canvas,width=12,font=("Courier 18 bold"), textvariable=var1)
        grentry.place(x=400,y=25)
        def get4():
            gr_no=var1.get()
            query=cur.execute("select * from sdetails")
            data=cur.fetchall()
            for i in data:
                if (gr_no==i[1]):
                    label1 = Label(canvas ,text=f"Name:{i[0]}",font=("Courier 18 bold"), bg="cadetblue2", width=30, height=1) 
                    label1.place(x=774,y=25)
                    break
            else:
                messagebox.showerror("Error","Enter correct GRNO!",parent=top7)

        button1=Button(canvas,text="OK",height=2,width=10,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get4)
        button1.place(x=600,y=15)
        def marks4():
            gr_no=grentry.get()
            sci=slider1.get()
            maths=slider2.get()
            hindi=slider3.get()
            guj=slider4.get()
            eng=slider5.get()
            sst=slider6.get()
            comp=slider7.get()
            cur.execute("insert into final values({},{},{},{},{},{},{},{})".format(gr_no,sci,maths,hindi,guj,eng,sst,comp))
            mydb.commit()
            messagebox.showinfo("Message","Your record has been submitted!", parent=top7)
            
            slider1_var.set(0)
            slider2_var.set(0)
            slider3_var.set(0)
            slider4_var.set(0)
            slider5_var.set(0)
            slider6_var.set(0)
            slider7_var.set(0)
                        
        def on_slider_change1(value):
           l1.config(text=f'Marks:{slider1.get()}')

        l_sci=Label(canvas,text="SCIENCE",font=("Courier 27 bold"),fg="blue")
        l_sci.place(x=430,y=100)

        slider1_var=DoubleVar()
        slider1=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider1_var,length=200, command=on_slider_change1)
        slider1.place(x=400,y=140)

        l1=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l1.place(x=430,y=180)

        def on_slider_change2(value):
            l2.config(text=f'Marks:{slider2.get()}')

        l_maths=Label(canvas,text="MATHS",font=("Courier 27 bold"),fg="blue")
        l_maths.place(x=835,y=100)
        
        slider2_var=DoubleVar()
        slider2=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider2_var, length=200, command=on_slider_change2)
        slider2.place(x=800,y=140)

        l2=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l2.place(x=830,y=180)

        def on_slider_change3(value):
            l3.config(text=f'Marks:{slider3.get()}')
                    
        l_comp=Label(canvas,text="HINDI",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=430,y=280)

        slider3_var=DoubleVar()
        slider3=Scale(canvas, from_=0, to=80, orient=HORIZONTAL, variable=slider3_var, length=200, command=on_slider_change3)
        slider3.place(x=400,y=320)

        l3=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l3.place(x=430,y=360)

        def on_slider_change4(value):
            l4.config(text=f'Marks:{slider4.get()}')

        l_guj=Label(canvas,text="GUJARATI",font=("Courier 27 bold"),fg="blue")
        l_guj.place(x=830,y=280)
        
        slider4_var=DoubleVar()
        slider4=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider4_var, length=200, command=on_slider_change4)
        slider4.place(x=800,y=320)

        l4=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l4.place(x=830,y=360)

        def on_slider_change5(value):
            l5.config(text=f'Marks:{slider5.get()}')

        l_eng=Label(canvas,text="ENGLISH",font=("Courier 27 bold"),fg="blue")
        l_eng.place(x=830,y=460)

        slider5_var=DoubleVar()
        slider5=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider5_var, length=200, command=on_slider_change5)
        slider5.place(x=800,y=500)

        l5=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l5.place(x=830,y=540)


        def on_slider_change6(value):
            l6.config(text=f'Marks:{slider6.get()}')
            
        l_sst=Label(canvas,text="SST",font=("Courier 27 bold"),fg="blue")
        l_sst.place(x=430,y=460)

        slider6_var=DoubleVar()
        slider6=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider6_var, length=200, command=on_slider_change6)
        slider6.place(x=400,y=500)

        l6=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l6.place(x=430,y=540)

        def on_slider_change7(value):
            l7.config(text=f'Marks:{slider7.get()}')

        l_comp=Label(canvas,text="COMPUTER",font=("Courier 27 bold"),fg="blue")
        l_comp.place(x=630,y=630)

        slider7_var=DoubleVar()
        slider7=Scale(canvas, from_=0, to=80, orient=HORIZONTAL,variable=slider7_var, length=200, command=on_slider_change7)
        slider7.place(x=600,y=670)

        l7=Label(canvas,text="Marks: 0",font=("Calibri 15 bold"))
        l7.place(x=630,y=710)

        button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="blue",bg="light green",command=marks4)
        button.pack()
        button.place(relx=0.762,rely=0.9)
             
    top7.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top7,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    main_frame=Frame(canvas,width=1200,height=950)
    main_frame.place(x=0,y=0)

    side_menu=Frame(canvas,width=200,height=950,bg="pink")
    side_menu.place(x=0,y=0.5)

    pt1_button=Button(canvas,text="PT1",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt1)
    pt1_button.place(x=0,rely=0.28)

    pt2_button=Button(canvas,text="PT2",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=pt2)
    pt2_button.place(x=0,rely=0.36)

    halfy_button=Button(canvas,text="HALF YEARLY",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=halfyearly)
    halfy_button.place(x=0,rely=0.44)

    final_button=Button(canvas,text="FINAL",width=16,fg="red",bg="light green",font=("Courier 15 bold"),command=final)
    final_button.place(x=0,rely=0.52)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top7.destroy)
    button1.pack()
    button1.place(relx=0.146,rely=0.9)
            
    top7.mainloop()

def screen6():
    def change():
        var1=var.get()
        if(var1<=5):
            screen7()
        elif(var1>=6 and var1<=10):
            screen8()
        else:
            screen9()
    def get():
        label1.config(text=var.get())
    top6=Toplevel()
    top6.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top6,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    var=IntVar()
    var.set("Select Your Class")
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    option_menu=OptionMenu(canvas,var,*options)
    option_menu.config(height=3,width=40,bg="light green",font=("Coppergothicbold 25 bold"))
    option_menu.pack()
    option_menu.place(anchor="center",relx=0.5,rely=0.37)

    button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=get)
    button.place(x=500,y=440)
    label1 = Label( canvas , text = " ",font=("Coppergothicbold 12 bold"),width=15,height=3) 
    label1.place(x=700,y=435)

    b1=Button(canvas,text="NEXT",command=change,
                       bg="blue",
                       fg="white",
                       font=('Coppergothicbold 12 bold'),height=2,width=15,)
    b1.place(x=1050,y=650)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top6.destroy)
    button1.pack()
    button1.place(x=170,y=650)
    top6.mainloop()

def screen5():
    top5=Toplevel()
    def marks_window():
        screen6()
    def attendance_window():
        screen12()
    def info_window():
        screen13()
    top5.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top5,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="Select any option",font=("Courier 28 bold"),bg="cadetblue2",width=25)
    choose.place(anchor="center",relx=0.5,rely=0.22)

    info=Button(canvas,text="INFORMATION",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=info_window)
    info.place(x=550,y=260)

    marks=Button(canvas,text="MARKS",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=marks_window)
    marks.place(x=550,y=410)

    attendance=Button(canvas,text="ATTENDANCE",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=attendance_window)
    attendance.place(x=550,y=560)
    
    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top5.destroy)
    button1.pack()
    button1.place(x=170,y=650)
            
    top5.mainloop()

def screen4():
    top4=Toplevel()
    def marks_window():
        screen14()
    def attendance_window():
        screen20()
    def info_window():
        screen21()
    top4.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top4,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    choose=Label(canvas,text="Select any option",font=("Courier 28 bold"),bg="cadetblue2",width=25)
    choose.place(anchor="center",relx=0.5,rely=0.22)

    info=Button(canvas,text="INFORMATION",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=info_window)
    info.place(x=550,y=260)

    marks=Button(canvas,text="MARKS",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=marks_window)
    marks.place(x=550,y=410)

    attendance=Button(canvas,text="ATTENDANCE",height=5,width=23,font=("Courier 12 bold"),fg="black",bg="light green",command=attendance_window)
    attendance.place(x=550,y=560)


    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top4.destroy)
    button1.pack()
    button1.place(x=170,y=650)
    
    top4.mainloop()

def screen3():
    top3=Toplevel()
    def next():
        screen5()  
    def submit():
        name_get=entry1.get()
        gr_get=entry2.get()
        class_get=entry3.get()
        section_get=entry4.get()
        cur.execute("insert into sdetails values('{}',{},{},'{}')".format(name_get,gr_get,class_get,section_get))
        mydb.commit()
    top3.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top3,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)

    details=Label(canvas,text="ENTER STUDENT DETAILS:",font=("Calibri 30 underline"),bg="white",width=25)
    details.place(anchor="center",relx=0.5,rely=0.25)

    Name=Label(canvas,text="NAME",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    Name.place(anchor="center",relx=0.43,rely=0.35)
    entry1=Entry(canvas,width=12,font=("Courier 18 bold"))
    entry1.pack()
    entry1.place(anchor="center",relx=0.57,rely=0.35)

    grno=Label(canvas,text="GRNO",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    grno.place(anchor="center",relx=0.43,rely=0.42)
    entry2=Entry(canvas,width=12,font=("Courier 18 bold"))
    entry2.pack()
    entry2.place(anchor="center",relx=0.57,rely=0.42)
    
    class1=Label(canvas,text="CLASS",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    class1.place(anchor="center",relx=0.43,rely=0.49)
    entry3=Entry(canvas,width=12,font=("Courier 18 bold"))
    entry3.pack()
    entry3.place(anchor="center",relx=0.57,rely=0.49)

    section=Label(canvas,text="SECTION",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    section.place(anchor="center",relx=0.43,rely=0.56)
    entry4=Entry(canvas,width=12,font=("Courier 18 bold"))
    entry4.pack()
    entry4.place(anchor="center",relx=0.57,rely=0.56)

    button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=submit)
    button.pack()
    button.place(anchor="center",relx=0.5,rely=0.68)

    

    b1=Button(canvas,text="SKIP",command=next,
                       bg="blue",
                       fg="white",
                       font=('Coppergothicbold 12 bold'),height=2,width=15,
                       highlightcolor="purple")
    b1.place(x=1050,y=650)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top3.destroy)
    button1.pack()
    button1.place(x=170,y=650)
    top3.mainloop()


def screen2():
    top2=Toplevel()
    def show():
          teacher=clicked.get()
          if(teacher=="STUDENT/PARENT"):
            cur.execute("Select * from student")
            data=cur.fetchall()                              
            userlst=[]
            passlst=[]
            for i in data:
                userlst.append(i[0])        
                passlst.append(i[1])        
            user_name=username.get()
            pass_word=passwrd.get()
            for i in range(0,len(userlst)):
                if(user_name==userlst[i] and pass_word==passlst[i]):
                    screen4()
            else:
                messagebox.showerror("Error","Please enter correct username or password!",parent=top2)
          elif(teacher=="TEACHER"):
                cur.execute("Select * from teacher")
                data=cur.fetchall()
                userlst=[]
                passlst=[]
                for i in data:
                    userlst.append(i[0])
                    passlst.append(i[1])    
                user_name=username.get()
                pass_word=passwrd.get()
                for i in range(0,len(userlst)):
                    if(user_name==userlst[i] and pass_word==passlst[i]):
                        screen3()
                else:
                    messagebox.showerror("Error","Please enter correct username or password!",parent=top2)

    def passwrd1():
            if(entry2.cget('show') == ''):
                entry2.config(show='*')
                toggle_btn.config(text='Show Password')
            else:
                entry2.config(show='')
                toggle_btn.config(text='Hide Password')           
        
        
    top2.attributes('-fullscreen',True)
    logo=Image.open("airportschoollogo.png")
    resize_logo=logo.resize((200,200))
    new_logo=ImageTk.PhotoImage(resize_logo)
    canvas=Canvas(top2,width=700,height=3700,bg="royal blue")
    canvas.pack(fill=BOTH,expand=True)
    canvas.create_image(1585,18,anchor='ne',image=new_logo)
        
    clicked = StringVar()
    present = Radiobutton(canvas, text="TEACHER", variable=clicked, value="TEACHER")
    present.config(font=("Calibri 20 bold"),width=18)
    present.place(x=390,y=240)
    
    absent = Radiobutton(canvas, text="STUDENT/PARENT", variable=clicked, value="STUDENT/PARENT")
    absent.config(font=("Calibri 20 bold"),width=18)
    absent.place(x=710,y=240)
    
    label=Label(top2,text='')
    label.pack()

    user=Label(canvas,text="USERNAME",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    user.place(anchor="center",relx=0.435,rely=0.47)
    username=StringVar()
    entry1=Entry(canvas,textvariable=username,width=12,font=("Courier 18 bold"))
    entry1.pack()
    entry1.place(anchor="center",relx=0.575,rely=0.47)

    password=Label(canvas,text="PASSWORD",font=("Courier 22 bold"),bg="cadetblue2",width=10)
    password.pack()
    password.place(anchor="center",relx=0.435,rely=0.55)
    passwrd=IntVar()
    entry2=Entry(canvas,textvariable=passwrd,show="*",width=12,font=("Courier 18 bold"))
    entry2.pack()
    entry2.place(anchor="center",relx=0.575,rely=0.55)

    button=Button(canvas,text="SUBMIT",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=show)
    button.pack()
    button.place(anchor="center",relx=0.505,rely=0.7)

    button1=Button(canvas,text="BACK",height=2,width=15,font=("Coppergothicbold 12 bold"),fg="white",bg="blue",command=top2.destroy)
    button1.pack()
    button1.place(x=170,y=650)
   
    toggle_btn = Button(canvas, text='Show Password', width=13,font=("Coppergothicbold 12 bold"),command=passwrd1)
    toggle_btn.pack()
    toggle_btn.place(anchor="center",relx=0.70,rely=0.55)
    top2.mainloop()
    
def screen1():
    root=Tk()
    def click():
        screen2()
    canvas=Canvas(root,width=700,height=3500)
    canvas.pack(fill=BOTH,expand=True)
    image=Image.open("airportschoolimage.jpg")
    root.title('MyAir')
    root.iconbitmap('airportschoollogo.ico')
    resize_img=image.resize((1400,720))
    new_img=ImageTk.PhotoImage(resize_img)
    canvas.create_image(0,0,anchor='nw',image=new_img)

   
    txt = Label(canvas, text="WELCOME TO MyAIR:",font=("Courier 28 bold"))
    txt.place(x=115, y=22)

    txt = Label(canvas, text="SCHOOL MANAGEMENT APP",font=("Courier 28 bold"))
    txt.place(x=70, y=70)

    
    b1=Button(canvas,text="Next",command=click,bg="royal blue", fg="white",font=('Helvetica 24 bold'),height=1,width=8)
    b1.place(x=1130,y=620)                                   
    root.mainloop()
screen1()
