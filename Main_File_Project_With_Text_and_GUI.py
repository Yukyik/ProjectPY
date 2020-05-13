#Pangko and Nonny student score adder and delete project
#Com-ED15 
from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox
from pathlib import Path
#สัพเพเหระ
def checker(tab_in):
    global emtryornot,jumnum
    while True:
        try:
            file=open("d:\\UserData\\STD_DATA.txt", "r")
            Check = file.read()
            Check = Check.split(":")
            jumnum = len(Check) #เช็คว่ามีข้อมูลนักเรียนอยู่ในไฟล์หรือไม่
            if jumnum <= 3: #ต้องมีข้อมูลมากกว่า 3 ช่องเพราะว่านักเรียน 1 คนมีข้อมูล 4 ช่อง ห้อง,รหัสนักเรียน,ชื่อ,คะแนน
                emtryornot = 0
                break
            else: 
                emtryornot = 1
                break
        except FileNotFoundError: #ถ้าไม่พบไฟล์ข้อมูล
            messagebox.showinfo(title="Tab",message="No Student Data yet") 
            do_quit(tab_in) #เรียกใช้ do_quit() เพื่อปิดหน้าที่รับเข้ามาไว้ในตัวแปร tab_in
            break
#ทำลายหน้าต่าง
def do_quit(self):
    self.destroy()
    self.update()
#ทำลายหน้าต่างเหมือนกัน แต่สร้างมาเพื่อใช้ในหน้า main เพราะเรียกใช้ do_quit ในปุ่มไม่ได้
def Logout():
    login_first.destroy()
    login_first.update()
#แก้ไขข้อมูลนักเรียน
def edit_tab():
    global edit_show,root
    global Line,new_room,new_id,new_name,new_score
    edit_show = Toplevel(root) #หน้าชื่อว่า edit_show
    edit_show.title("Program")
    edit_show.geometry("625x350+800+350")
    edit_show.configure(background = '#FDF5E6')
    Line = IntVar()         #ตัวแปรบรรทัด
    new_room = StringVar()  #ตัวแปรห้องที่จะแก้ไข
    new_id = StringVar()    #ตัวรหัสนักเรียนที่จะแก้ไข
    new_name = StringVar()  #ตัวชื่อนักเรียนที่จะแก้ไข
    new_score = IntVar()    #ตัวคะแนนนักเรียนที่จะแก้ไข
    Label(edit_show,text="แถวในตาราง:",font=('supermarket',16),bg='#FDF5E6').grid(row=0,column=0)
    Label(edit_show,text="ห้องของนักเรียน :",font=('supermarket',16),bg='#FDF5E6').grid(row=1,column=0)
    Label(edit_show,text="รหัสนักเรียน :",font=('supermarket',16),bg='#FDF5E6').grid(row=2,column=0)
    Label(edit_show,text="ชื่อนักเรียน :",font=('supermarket',16),bg='#FDF5E6').grid(row=3,column=0)
    Label(edit_show,text="คะแนนนักเรียนแก้ :",font=('supermarket',16),bg='#FDF5E6').grid(row=4,column=0)
    Line = Entry(edit_show,textvariable=Line,width=40,font=('supermarket',16))
    Line.grid(row=0,column=2,padx=10)
    new_room = Entry(edit_show,textvariable=new_room,width=40,font=('supermarket',16))
    new_room.grid(row=1,column=2,padx=10)
    new_id = Entry(edit_show,textvariable=new_id,width=40,font=('supermarket',16))
    new_id.grid(row=2,column=2,padx=10)
    new_name = Entry(edit_show,textvariable=new_name,width=40,font=('supermarket',16))
    new_name.grid(row=3,column=2,padx=10)
    new_score = Entry(edit_show,textvariable=new_score,width=40,font=('supermarket',16))
    new_score.grid(row=4,column=2,padx=10)
    edit = Button(edit_show,text="Edit",height=1,width=10,command=edit_run,font=('supermarket'),bg='#FF6347')
    edit.grid(row=5,column=2,sticky="nsew")
def edit_run():
    Line_1 = Line.get()  
    new_room_1 = new_room.get() 
    new_id_1 = new_id.get() 
    new_name_1 = new_name.get() 
    new_score_1 = new_score.get() #รับค่า แถว,ห้อง,รหัส,ชื่อ,คะแนน
    file=open("d:\\UserData\\STD_DATA.txt", "r") 
    Check = file.read() 
    Check = Check.split(":") 
    del Check[-1] 
    j = len(Check) 
    Line_1 = int(Line_1) 
    if Line_1 > (j//4): #นักเรียน 1 คนมีข้อมูล 4 ช่อง ห้อง,รหัสนักเรียน,ชื่อ,คะแนน ดังนั้นนำจำนวนข้อมูลมาหารด้วย 4 จะได้จำนวนแถวทั้งหมด
        messagebox.showinfo(title="Process",message="Error")
    else:
        Line_1 = Line_1*4 #กำหนัดให้ Line_1 คูณด้วย 4
        new_room_1 = str(new_room_1)
        new_id_1 = str(new_id_1)
        new_name_1 = str(new_name_1)
        new_score_1 = str(new_score_1)
        Check[Line_1-4] = new_room_1 #แก้ค่าช่องที่ 0 ถ้า line เป็น 1
        Check[Line_1-3] = new_id_1 #แก้ค่าช่องที่ 1 ถ้า line เป็น 1
        Check[Line_1-2] = new_name_1 #แก้ค่าช่องที่ 2 ถ้า line เป็น 1
        Check[Line_1-1] = new_score_1 #แก้ค่าช่องที่ 3 ถ้า line เป็น 1
        file=open("d:\\UserData\\STD_DATA.txt", "w")
        for i in range(0,j): #เขียนข้อมูลลงในไฟล์ทีละ 1 ตัว ค่อยๆวนตามช่องโดยใช้ i เป็นตัววน
            file.write(Check[i])
            file.write(":")
        file.close()
        messagebox.showinfo(title="Success",message="Success")
        do_quit(edit_show) #เรียกใช้ do_quit() เพื่อปิดหน้า edit_show
        do_quit(show) #เรียกใช้ do_quit() เพื่อปิดหน้า show
#หักคะแนนนักเรียน
def Deducepoints_Tab():
    global Deducepoints_tab,root,input_do
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20
    Deducepoints_tab = Toplevel(root)
    Deducepoints_tab.title("Deducepoints")
    Deducepoints_tab.geometry("925x650+400+50")
    Deducepoints_tab.configure(background = '#FDF5E6')
    input_do = StringVar()  #กำหนดค่าขึ้นมาค่ารหัสนักเรียน
    c1 = IntVar() #กำหนดค่าขึ้นมาเพื่อรับค่าการติ๊กช่องต่างๆ
    c2 = IntVar()
    c3 = IntVar()
    c4 = IntVar()
    c5 = IntVar()
    c6 = IntVar()
    c7 = IntVar()
    c8 = IntVar()
    c9 = IntVar()
    c10 = IntVar()
    c11 = IntVar()
    c12 = IntVar()
    c13 = IntVar()
    c14 = IntVar()
    c15 = IntVar()
    c16 = IntVar()
    c17 = IntVar()
    c18 = IntVar()
    c19 = IntVar()
    c20 = IntVar()
    Header =  Label(Deducepoints_tab,text="กรุณากรอกข้อมูลนักเรียนที่ต้องการหักคะแนน",font=('supermarket',22),bg='#FFB6C1')
    Header.grid(row=0,column=1,padx=10)
    H1 =  Label(Deducepoints_tab,text="รหัสนักเรียน : ",font=('supermarket',14),bg='#FDF5E6')
    H1.grid(row=1,column=0,padx=10)
    input_do = Entry(Deducepoints_tab,textvariable=input_do,width=40,font=('supermarket',14))
    input_do.grid(row=1,column=1,padx=10)
    H2 =  Label(Deducepoints_tab,text="ความประพฤติที่ไม่ดีในโรงเรียน",font=('supermarket',12),bg='#40E0D0')
    H2.grid(row=2,column=1,padx=10,sticky='w')
    H3 =  Label(Deducepoints_tab,text="ความประพฤติที่ไม่ดีในห้องเรียน",font=('supermarket',12),bg='#40E0D0')
    H3.grid(row=2,column=2,padx=10,sticky='w')
    Checkbutton(Deducepoints_tab,text="(1) มาเรียนสาย",variable=c1,font=('supermarket',12),bg='#FDF5E6').grid(row=3,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(2) ปีนรั้วเข้าหรือออกโรงเรียน",variable=c2,font=('supermarket',12),bg='#FDF5E6').grid(row=4,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(3) ไม่เข้าแถวเคารพธงชาติ",variable=c3,font=('supermarket',12),bg='#FDF5E6').grid(row=5,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(4) แอบอ้างบุคคลอื่นเป็นผู้ปกครอง",variable=c4,font=('supermarket',12),bg='#FDF5E6').grid(row=6,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(5) แต่งกายผิดระเบียบโดยเจตนา",variable=c5,font=('supermarket',12),bg='#FDF5E6').grid(row=7,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(6) รับฝาก และฝากสแกนบัตรแทนกัน",variable=c6,font=('supermarket',12),bg='#FDF5E6').grid(row=8,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(7) ไม่สแกนบัตรลงเวลาเรียน",variable=c7,font=('supermarket',12),bg='#FDF5E6').grid(row=9,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(8) ขับขี่รถจักรยานยนต์และรถบนต์ภายในโรงเรียน",variable=c8,font=('supermarket',12),bg='#FDF5E6').grid(row=10,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(9) พกบุหรี่หรือที่จุดบุหรี่",variable=c9,font=('supermarket',12),bg='#FDF5E6').grid(row=11,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(10) ปลอมลายมือ",variable=c10,font=('supermarket',12),bg='#FDF5E6').grid(row=12,column=1, sticky="w")
    Checkbutton(Deducepoints_tab,text="(1) ขาดเรียนโดยไม่ทราบสาเหตุ",variable=c11,font=('supermarket',12),bg='#FDF5E6').grid(row=3,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(2) ไม่ทำเวร",variable=c12,font=('supermarket',12),bg='#FDF5E6').grid(row=4,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(3) ใช้วาจาไม่สุภาพ",variable=c13,font=('supermarket',12),bg='#FDF5E6').grid(row=5,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(4) โดดเรียนหรือกิจกรรม",variable=c14,font=('supermarket',12),bg='#FDF5E6').grid(row=6,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(5) เข้าห้องเรียนสาย",variable=c15,font=('supermarket',12),bg='#FDF5E6').grid(row=7,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(6) ไม่เข้าโฮมรูม",variable=c16,font=('supermarket',12),bg='#FDF5E6').grid(row=8,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(7) ไม่ตั้งใจเรียน",variable=c17,font=('supermarket',12),bg='#FDF5E6').grid(row=9,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(8) ทิ้งขยะไม่เป็นที่",variable=c18,font=('supermarket',12),bg='#FDF5E6').grid(row=10,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(9) กระเป๋านักเรียนผิดระเบียบ",variable=c19,font=('supermarket',12),bg='#FDF5E6').grid(row=11,column=2, sticky="w")
    Checkbutton(Deducepoints_tab,text="(10) นำอาหารและเครื่องดื่มขึ้นไปรับประทานบนห้องเรียน",variable=c20,font=('supermarket',12),bg='#FDF5E6').grid(row=12,column=2, sticky="w")
    Button(Deducepoints_tab,text = "หักคะแนน",font=('supermarket'), height = "1", width = "20", command = Deducepoints,bg="#990033",fg="#FFFFFF").grid(row=13,column=1,pady=10,padx=10,sticky=E)
    checker(Deducepoints_tab) #เรียกใช้ฟังค์ชั่น checker() เพื่อตรวจว่าฐานข้อมูลว่างหรือไม่
    if emtryornot == 0: #ส่งให้เรียกใช้ฟังค์ชั่น do_quit() เมื่อฐานข้อมูลเป็นค่าว่าง
        do_quit(Deducepoints_tab)
        messagebox.showinfo(title="Tab",message="No Student Data yet")
def Deducepoints():
    Buffer,s = 0,0
    Check1 = c1.get() #รับค่าจากช่อง c1 มาเก็บใน Check1
    Check2 = c2.get() #ค่าที่ส่งมาจะมีค่าเป็น 0 กับ 1 
    Check3 = c3.get() #เนื่องจากช่องเหล่านี้เป็น checkbutton มีการติ๊กกับไม่ติ๊กเท่านั้น
    Check4 = c4.get()
    Check5 = c5.get()
    Check6 = c6.get()
    Check7 = c7.get()
    Check8 = c8.get()
    Check9 = c9.get()
    Check10 = c10.get()
    Check11 = c11.get()
    Check12 = c12.get()
    Check13 = c13.get()
    Check14 = c14.get()
    Check15 = c15.get()
    Check16 = c16.get()
    Check17 = c17.get()  # |
    Check18 = c18.get()  # |
    Check19 = c19.get()  # |
    Check20 = c20.get() #  V รวมช่องที่โดนติ๊กว่ามีกี่ช่อง
    SumCheck = Check1+Check2+Check3+Check4+Check5+Check6+Check7+Check8+Check9+Check10+Check11+Check12+Check13+Check14+Check15+Check16+Check17+Check18+Check19+Check20
    STD_id_to_do = input_do.get() #รับค่ารหัสนักเรียนจากช่อง input_do
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    STD_id_find = file.read()
    STD_id_find = STD_id_find.split(":")
    j = len(STD_id_find)
    for i in range(0,j):
        if STD_id_to_do == STD_id_find[i]:
            if j-i == 2: break #ช่องรหัสนักเรียนจะห่างจากช่องคะแนน 2 ช่องดังนั้นส่งให้ break ก่อนที่จะเหลือ 2 ตัวสุดท้าย
            Buffer = STD_id_find[i+2] #กำหนดให้ Buffer เท่ากับคะแนนของนักเรียน
            Buffer = int(Buffer) #กำหนดให้ Buffer เป็นตัวแปร int
            Buffer -= SumCheck*5 #ลบค่าออกโดยใช้ค่า SumCheck มาคูณด้วย 5 คะแนน
            STD_id_find[i+2] = Buffer #นำค่าคะแนนที่คำนวนมากลับมาใส่ในตำแหน่งเดิม
            s+=1 #เอาไว้ตรวจว่าทำงานไปกี่รอบ
            do_quit(Deducepoints_tab)
            messagebox.showinfo(title="Process",message="Success")
            if STD_id_find[i+2] < 0:
                STD_id_find[i+2] = 0
    if s == 0: #ถ้าทำงาน 0 รอบแสดงว่าหาไม่เจอ
        messagebox.showinfo(title="Process",message="Can't find student with this ID")
    elif s == 1: #ถ้าทำงาน 1 รอบแสดงว่าหาเจอตำแหน่งเดียวและถูกต้องให้ทำงานต่อ
        file=open("d:\\UserData\\STD_DATA.txt", "w")
        for a in range(0,j):
            write = STD_id_find[a]
            write = str(write)
            if 1 == j-a:break
            else:file.write(write+":")       
        file.close()
    else: messagebox.showinfo(title="Process",message="Find more than one pointer pls edit data-file") #นอกนั้นแสดงว่าข้อมูลผิดพลาดต้องแก้ไข
#เพิ่มคะแนนนักเรียน
def Addpoints_Tab():
    global Addpoints_Tab,root,input_do
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20
    Addpoints_Tab = Toplevel(root)
    Addpoints_Tab.title("Addpoints")
    Addpoints_Tab.geometry("925x650+400+50")
    Addpoints_Tab.configure(background = '#FDF5E6')
    input_do = StringVar()
    c1 = IntVar()
    c2 = IntVar()
    c3 = IntVar()
    c4 = IntVar()
    c5 = IntVar()
    c6 = IntVar()
    c7 = IntVar()
    c8 = IntVar()
    c9 = IntVar()
    c10 = IntVar()
    c11 = IntVar()
    c12 = IntVar()
    c13 = IntVar()
    c14 = IntVar()
    c15 = IntVar()
    c16 = IntVar()
    c17 = IntVar()
    c18 = IntVar()
    c19 = IntVar()
    c20 = IntVar()
    Header =  Label(Addpoints_Tab,text="กรุณากรอกข้อมูลนักเรียนที่ต้องการเพิ่มคะแนน",font=('supermarket',22),bg='#FFB6C1')
    Header.grid(row=0,column=1,padx=10)
    H1 =  Label(Addpoints_Tab,text="รหัสนักเรียน : ",font=('supermarket',14),bg='#FDF5E6')
    H1.grid(row=1,column=0,padx=10)
    input_do = Entry(Addpoints_Tab,textvariable=input_do,width=40,font=('supermarket',14))
    input_do.grid(row=1,column=1,padx=10)
    H2 =  Label(Addpoints_Tab,text="ความประพฤติที่ดีในโรงเรียน",font=('supermarket',12),bg='#40E0D0')
    H2.grid(row=2,column=1,padx=10,sticky='w')
    H3 =  Label(Addpoints_Tab,text="ความประพฤติที่ดีในห้องเรียน",font=('supermarket',12),bg='#40E0D0')
    H3.grid(row=2,column=2,padx=10,sticky='w')
    Checkbutton(Addpoints_Tab,text="(1) มีความเสียสระช่วยเหลือครู",variable=c1,font=('supermarket',12),bg='#FDF5E6').grid(row=3,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(2) บำเพ็ญประโยชน์ต่อโรงเรียน",variable=c2,font=('supermarket',12),bg='#FDF5E6').grid(row=4,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(3) ช่วยเหลืองานโรงเรียน",variable=c3,font=('supermarket',12),bg='#FDF5E6').grid(row=5,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(4) ร่วมประกวด/แข่งขัน ในและนอกโรงเรียน",variable=c4,font=('supermarket',12),bg='#FDF5E6').grid(row=6,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(5) ไม่พกบุหรี่หรือที่จุดบุหรี่",variable=c5,font=('supermarket',12),bg='#FDF5E6').grid(row=7,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(6) ไม่ปีนรั้วเข้าหรือออกโรงเรียน",variable=c6,font=('supermarket',12),bg='#FDF5E6').grid(row=8,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(7) ไม่แอบอ้างบุคคลอื่นเป็นผู้ปกครอง",variable=c7,font=('supermarket',12),bg='#FDF5E6').grid(row=9,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(8) ไม่รับฝาก และฝากสแกนบัตรแทนกัน",variable=c8,font=('supermarket',12),bg='#FDF5E6').grid(row=10,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(9) ไม่ขับขี่รถจักรยานยนต์และรถยนต์ภายในโรงเรียน",variable=c9,font=('supermarket',12),bg='#FDF5E6').grid(row=11,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(10) ไม่ปลอมลายมือ",variable=c10,font=('supermarket',12),bg='#FDF5E6').grid(row=12,column=1, sticky="w")
    Checkbutton(Addpoints_Tab,text="(1) มาเรียนเป็นประจำ",variable=c11,font=('supermarket',12),bg='#FDF5E6').grid(row=3,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(2) ใช้วาจาสุภาพ",variable=c12,font=('supermarket',12),bg='#FDF5E6').grid(row=4,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(3) ส่งการบ้านตรงเวลา",variable=c13,font=('supermarket',12),bg='#FDF5E6').grid(row=5,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(4) สนใจเรียน",variable=c14,font=('supermarket',12),bg='#FDF5E6').grid(row=6,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(5) ทำเวรประจำวัน",variable=c15,font=('supermarket',12),bg='#FDF5E6').grid(row=7,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(6) ไม่แกล้งเพื่อน",variable=c16,font=('supermarket',12),bg='#FDF5E6').grid(row=8,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(7) เข้าโฮมรูมตอนเช้า",variable=c17,font=('supermarket',12),bg='#FDF5E6').grid(row=9,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(8) ทิ้งขยะเป็นที่",variable=c18,font=('supermarket',12),bg='#FDF5E6').grid(row=10,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(9) ไม่นำอาหารและเครื่องดื่มขึ้นไปรับประทานในห้องเรียน",variable=c19,font=('supermarket',12),bg='#FDF5E6').grid(row=11,column=2, sticky="w")
    Checkbutton(Addpoints_Tab,text="(10) แต่งตัวถูกระเบียบ",variable=c20,font=('supermarket',12),bg='#FDF5E6').grid(row=12,column=2, sticky="w")
    Button(Addpoints_Tab,text = "เพิ่มคะแนน",font=('supermarket'), height = "1", width = "20", command = Addpoints,bg="#990033",fg="#FFFFFF").grid(row=13,column=1,pady=10,padx=10,sticky=E)
    checker(Addpoints_Tab)
    if emtryornot == 0:
        do_quit(Addpoints_Tab)
        messagebox.showinfo(title="Tab",message="No Student Data yet")
def Addpoints():
    Buffer,s = 0,0
    Check1 = c1.get()
    Check2 = c2.get()
    Check3 = c3.get()
    Check4 = c4.get()
    Check5 = c5.get()
    Check6 = c6.get()
    Check7 = c7.get()
    Check8 = c8.get()
    Check9 = c9.get()
    Check10 = c10.get()
    Check11 = c11.get()
    Check12 = c12.get()
    Check13 = c13.get()
    Check14 = c14.get()
    Check15 = c15.get()
    Check16 = c16.get()
    Check17 = c17.get()
    Check18 = c18.get()
    Check19 = c19.get()
    Check20 = c20.get()
    SumCheck = Check1+Check2+Check3+Check4+Check5+Check6+Check7+Check8+Check9+Check10+Check11+Check12+Check13+Check14+Check15+Check16+Check17+Check18+Check19+Check20
    STD_id_to_do = input_do.get()
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    STD_id_find = file.read()
    STD_id_find = STD_id_find.split(":")
    file.close()
    j = len(STD_id_find)
    for i in range(0,j):
        if STD_id_to_do == STD_id_find[i]:
            if j-i == 2: break
            Buffer = STD_id_find[i+2]
            Buffer = int(Buffer)
            Buffer += SumCheck*5
            STD_id_find[i+2] = Buffer
            s+=1 #เอาไว้ตรวจว่าทำงานไปกี่รอบ
            do_quit(Addpoints_Tab)
            messagebox.showinfo(title="Process",message="Success")
            if STD_id_find[i+2] > 100:
                STD_id_find[i+2] = 100
    if s == 0:
        messagebox.showinfo(title="Process",message="Can't find student with this ID")
    elif s == 1:
        file=open("d:\\UserData\\STD_DATA.txt", "w")
        for a in range(0,j):
            write = STD_id_find[a]
            write = str(write)
            if 1 == j-a:break
            else:file.write(write+":")       
        file.close()
    else: messagebox.showinfo(title="Process",message="Find more than one pointer pls edit data-file")
#เพิ่มนักเรียนเข้าระบบ
def Addstudent_Tab():
    global Addstudent_first,root
    Addstudent_first = Toplevel(root)
    Addstudent_first.title("Addstudent")
    Addstudent_first.geometry("625x250+800+50")
    Addstudent_first.configure(background = '#FDF5E6')
    Addstudent_first.grid_columnconfigure(0, minsize=75)
    global std_room,std_id,std_name
    std_room = StringVar()
    std_id = StringVar()
    std_name = StringVar()
    Header =  Label(Addstudent_first,text="เพิ่มข้อมูลนักเรียน",font=('supermarket',16),bg='#FDF5E6')
    Header.grid(row=0,column=2)
    H1 = Label(Addstudent_first,text="ห้องของนักเรียน : ",font=('supermarket',16),bg='#FDF5E6')
    H1.grid(row=1,column=0, sticky=E)
    std_room = Entry(Addstudent_first,textvariable=std_room,width=40,font=('supermarket',16))
    std_room.grid(row=1,column=2,padx=10)
    H2 = Label(Addstudent_first,text="รหัสนักเรียน : ",font=('supermarket',16),bg='#FDF5E6')
    H2.grid(row=2,column=0, sticky=E)
    std_id = Entry(Addstudent_first,textvariable=std_id,width=40,font=('supermarket',16))
    std_id.grid(row=2,column=2,padx=10)
    H3 = Label(Addstudent_first,text="ชื่อนักเรียน : ",font=('supermarket',16),bg='#FDF5E6')
    H3.grid(row=3,column=0, sticky=E)
    std_name = Entry(Addstudent_first,textvariable=std_name,width=40,font=('supermarket',16))
    std_name.grid(row=3,column=2,padx=10)
    register = Button(Addstudent_first,text="ADD",height=2,width=30,command=Addstudent_Add,bg='#B22222',activebackground='#CD853F')
    register.grid(row=4,column=2,padx=10, pady=10)
def Addstudent_Add():
    std_room_1 = std_room.get()
    std_id_1 = std_id.get()
    std_name_1 = std_name.get()
    if std_room_1 == "" or std_id_1 == "" or std_name_1 == "" :
        messagebox.showinfo(title="Error",message="กรุณากรอกข้อมูลให้ครบถ้วน")
    else:
        file=open("d:\\UserData\\STD_DATA.txt", "a")
        file.write(std_room_1)
        file.write(":")
        file.write(std_id_1)
        file.write(":")
        file.write(std_name_1)
        file.write(":100:")
        file.close()
        messagebox.showinfo(title="Success",message="Success")
        do_quit(Addstudent_first)
#แสดงข้อมูลนักเรียน
def Checkpoints_STD():
    topic = ["Room","Student Id","Name","Score"]
    ptr = 0
    show = Toplevel(root)
    show.geometry("625x250+800+50")
    show.title("Show Student list and score")
    frame1 = Frame(show,bg='#FDF5E6')
    frame1.pack(fill="both")
    tablelayout = Notebook(frame1)
    tab1 = Frame(tablelayout,bg='#FDF5E6')
    tab1.pack(fill="both")
    checker(show)
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    many = file.read()
    many = many.split(":")
    j = len(many)
    j = j//4
    for row in range(0,j+1):
        for column in range(0,4):
            if row == 0:
                label = Label(tab1,text=topic[column],bg="#FDF5E6",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
            else:
                label = Label(tab1,text=str(many[ptr]),bg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
                ptr += 1
    tablelayout.add(tab1,text="Student Data")
    tablelayout.pack(fill="both")
def Checkpoints():
    global show
    topic = ["No.","Room","Student Id","Name","Score"] #หัวตาราง
    ptr = 0
    show = Toplevel(root) 
    show.geometry("625x250+800+50")
    show.title("Show Student list and score")
    frame1 = Frame(show,bg='#FDF5E6')
    frame1.pack(fill="both")
    tablelayout = Notebook(frame1)
    tab1 = Frame(tablelayout,bg='#FDF5E6')
    tab1.pack(fill="both")
    checker(show)
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    many = file.read()
    many = many.split(":")
    j = len(many)
    j = j//4
    for row in range(0,j+1):
        for column in range(0,5):
            if row == 0:
                label = Label(tab1,text=topic[column],bg="#FDF5E6",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
            elif column == 0:
                label = Label(tab1,text=row,bg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
            else:
                label = Label(tab1,text=str(many[ptr]),bg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                tab1.grid_columnconfigure(column,weight=1)
                ptr += 1
    edit = Button(tab1,text="Edit",height=1,width=10,command=edit_tab,font=('supermarket'),bg='#FA8072')
    edit.grid(row=j+1,column=4,sticky="E")
    tablelayout.add(tab1,text="Student Data")
    tablelayout.pack(fill="both")
#ตรวจการเข้าสู่ระบบ
def login_check():
        i,s = 0,0
        in1_1 = inbox1.get()
        in2_2 = inbox2.get()
        file=open("d:\\UserData\\Source.txt", "r")
        Check = file.read() # Check = ["aaa:111:bbb:222:ccc:333:] มี 1 จำนวน
        Check = Check.split(":") # Check = ["aaa":"111":"bbb":"222":"ccc":"333",""] มี 6 จำนวน
        del Check[-1] #ลบช่องท้ายสุดของ list Check = ["aaa":"111":"bbb":"222":"ccc":"333"] มี 5 จำนวน
        in2.delete(0, END) #ลบข้อความออกจากช่อง in2
        file.close()
        if in1_1 not in Check or in1_1 == "": #ถ้า username ไม่อยู่ใน Check หรือ username เป็นช่องว่าง
            messagebox.showinfo(title="Error",message="Error Invaid Username or Password")
        if in1_1 in Check and in2_2 == "": #ถ้า username อยู่ใน check และค่า password เป็นช่องว่าง
            messagebox.showinfo(title="Error",message="Error Invaid Username or Password")
        j = len(Check)
        for i in range(0,j):
            if s != 1:
                if in1_1 == Check[i] and in2_2 == Check[i+1] and Check[i+2] == "teacher": #ตรวจหา key สำหรับ user ของอาจารย์
                    in1.delete(0, END) #ลบข้อความออกจากช่อง in1
                    login_run() #เรียกใช้หน้าเมนเมนูสำหรับอาจารย์
                    s +=1
                elif in1_1 == Check[i] and in2_2 == Check[i+1]:
                    in1.delete(0, END) #ลบข้อความออกจากช่อง in1
                    login_run_STD() #เรียกใช้หน้าเมนเมนูสำหรับนักเรียน
                    s +=1
            else : break 
#หน้าหลักของโปรแกรม
def login_run_STD():
    global login_first,root
    login_first = Toplevel(root)
    login_first.title("Login")
    login_first.geometry("525x300+150+50")
    login_first.grid_columnconfigure(0, minsize=75)
    Label(login_first,text="โปรแกรมบันทึกคะแนนความประพฤตินักเรียน",font=('supermarket',20),bg="#000080",fg="#FFFFFF").grid(row=0,column=1)
    Label(login_first,text = "").grid(row=1,column=0)
    Button(login_first,text = "ตรวจสอบคะแนนความประพฤติ",font=('supermarket',16), height = "2", width = "30", command = Checkpoints_STD,bg="#2E8B57",fg="#FFFFFF").grid(row=8,column=1)
    Label(login_first,text = "").grid(row=9,column=0)
    Button(login_first,text = "ออกจากระบบ",font=('supermarket'), height = "1", width = "10", command = Logout,bg="#990033",fg="#FFFFFF").grid(row=10,column=1,sticky=W)
    Button(login_first,text = "ออกจากโปรแกรม",font=('supermarket'), height = "1", width = "20", command = quit,bg="#B22222",fg="#FFFFFF").grid(row=10,column=1,sticky=E)
def login_run():
    global login_first,root
    login_first = Toplevel(root)
    login_first.title("Main menu")
    login_first.geometry("525x700+800+50")
    login_first.configure(background = '#FDF5E6')
    login_first.grid_columnconfigure(0, minsize=75)
    Label(login_first,text="โปรแกรมบันทึกคะแนนความประพฤตินักเรียน",font=('supermarket',20),bg="#000080",fg="#FFFFFF").grid(row=0,column=1)
    Label(login_first,text = "").grid(row=1,column=0)
    Button(login_first,text = "หักคะแนนความประพฤติ",font=('supermarket',16), height = "2", width = "30", command = Deducepoints_Tab,bg="#FF8C00",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=2,column=1)
    Label(login_first,text = "").grid(row=3,column=0)
    Button(login_first,text = "เพิ่มคะแนนความประพฤติ",font=('supermarket',16), height = "2", width = "30", command = Addpoints_Tab,bg="#FF6347",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=4,column=1)
    Label(login_first,text = "").grid(row=5,column=0)
    Button(login_first,text = "เพิ่มรายชื่อนักเรียน",font=('supermarket',16), height = "2", width = "30", command = Addstudent_Tab,bg="#6A5ACD",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=6,column=1)
    Label(login_first,text = "").grid(row=7,column=0)
    Button(login_first,text = "ตรวจสอบคะแนนความประพฤติ",font=('supermarket',16), height = "2", width = "30", command = Checkpoints,bg="#2E8B57",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=8,column=1)
    Label(login_first,text = "").grid(row=9,column=0)
    Button(login_first,text = "ออกจากระบบ",font=('supermarket'), height = "1", width = "10", command = Logout,bg="#990033",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=10,column=1,sticky=W)
    Button(login_first,text = "ออกจากโปรแกรม",font=('supermarket'), height = "1", width = "20", command = quit,bg="#B22222",fg="#FFFFFF",activebackground='#FFFFCC').grid(row=10,column=1,sticky=E)
#สมัครเข้าสู่ระบบ
def register_write():
    username = username_in.get() #รับค่าจากช่อง username_in มาไว้ในตัวแปร username
    password = password_in.get() #รับค่าจากช่อง password_in มาไว้ในตัวแปร password
    key = key_in.get() #รับค่าจากช่อง key_in มาไว้ในตัวแปร key
    if username == "" or password == "" or key == "": #เช็คไม่ให้ตัวแปร username password key เป็นค่าว่าง
        messagebox.showinfo(title="Register",message="Error invaid input") #เปิดหน้าต่างเพื่อบอกว่าค่า error
    else:
        Path("d:\\UserData").mkdir(parents=True, exist_ok=True) #ถ้าไม่มีโฟล์เดอร์ UserData ที่ไดฟ์ d ให้สร้างโฟล์เดอร์ขึ้นมา
        file=open("d:\\UserData\\Source.txt", "a") #เปิดไฟล์ที่ d:\\UserData\\Source.txt แบบเพิ่มเติมได้
        file.write(username+":") #เขียน username ตามด้วย :
        file.write(password+":") #เขียน password ตามด้วย :
        file.write(key+":") #เขียน key ตามด้วย :
        file.close() #ปิดไฟล์
        messagebox.showinfo(title="Register",message="Success") #เปิดหน้าต่างเพื่อบอกว่าบันทึกสำเร็จ
        do_quit(root_register) #เรียกใช้ฟังค์ชั่น do_quit() ส่งค่า root_register ไปที่ฟังค์ชั่น
def register_run():
    global root_register
    root_register = Toplevel(root) #กำหนดหน้า root_register เป็นหน้ารอง โดยเปิดขึ้นมาจากหน้า root
    root_register.title("Register") #แถบด้านบนของโปรแกรม
    root_register.geometry("575x300+800+150") #กำหนดค่าขนาดของหน้าต่าง กว้าง x ยาว + เปิดจอห่างจากจอด้านซ้าย + เปิดจอห่างจากจอด้านบน
    root_register.configure(background = 'moccasin') #กำหนดพื้นหลังของหน้าต่าง root_register
    global username_in,password_in,key_in
    global username_entry,password_entry,key_entry
    username_in = StringVar() #username_in รับค่า str
    password_in = StringVar() #password_in รับค่า str
    key_in = StringVar() #key_in รับค่า str
    Label (root_register, text = "Please enter details below",bg='moccasin',font=('supermarket',22)).grid(row=0,column=2, sticky=NSEW)
    Label (root_register, text = "Username :",bg='moccasin',font=('supermarket',16)).grid(row=1, sticky=E)
    Label (root_register, text = "Password :",bg='moccasin',font=('supermarket',16)).grid(row=2, sticky=E)
    Label (root_register, text = "User-Key :",bg='moccasin',font=('supermarket',16)).grid(row=3, sticky=E)
    username_entry = Entry(root_register,textvariable=username_in,width=40,font=('supermarket',16))
    username_entry.grid(row=1,column=2,padx=10)
    password_entry = Entry(root_register,textvariable=password_in,width=40,font=('supermarket',16))
    password_entry.grid(row=2,column=2,padx=10)
    key_entry = Entry(root_register,textvariable=key_in,width=40,font=('supermarket',16))
    key_entry.grid(row=3,column=2,padx=10)
    register = Button(root_register,text="Register",bg='orange',activebackground='gold',height=1,width=30,command=register_write,font=('supermarket',16))
    register.grid(row=4,column=2,padx=10, pady=10)
def main():
    global inbox1,inbox2,username_in,password_in,in1,in2
    global root
    root = Tk() #กำหนด root ให้เป็นหน้าหลักของการแสดง gui
    inbox1 = StringVar() #inbox1 รับค่า str
    inbox2 = StringVar() #inbox2 รับค่า str
    root.geometry("600x250+150+150") #กำหนดค่าขนาดของหน้าต่าง กว้าง x ยาว + เปิดจอห่างจากจอด้านซ้าย + เปิดจอห่างจากจอด้านบน
    root.title("Student total score and behaviour score") #แถบด้านบนของโปรแกรม
    root.configure(background = 'AntiqueWhite1') #กำหนดพื้นหลังของหน้าต่าง root
    Header = Label(text="โปรแกรมบันทึกคะแนนนักเรียน",bg= 'AntiqueWhite1',font=('supermarket',18))
    Header.grid(row=0,column=1)
    H1 = Label(text="Username :",bg= 'AntiqueWhite1',font=('supermarket',16))
    H1.grid(row=1,column=0, sticky="nsew")
    in1 = Entry(root,textvariable=inbox1,width=40,font=('supermarket',16))
    in1.grid(row=1,column=1,pady=5, sticky="nsew")
    H2 = Label(text="Password :",bg= 'AntiqueWhite1',font=('supermarket',16)) 
    H2.grid(row=2,column=0, sticky="nsew")
    in2 = Entry(root,textvariable=inbox2,width=40,show="*",font=('supermarket',16))
    in2.grid(row=2,column=1,pady=5, sticky="nsew")
    login = Button(root, text="Log-in", height=1,width=15,command=login_check,font=('supermarket',16),bg='#FF9900')
    login.grid(row=4,column=1,padx=10, sticky="e")
    register_in = Button(text="Register",height=1,width=15,command=register_run,font=('supermarket',16),bg='#FA8072')
    register_in.grid(row=4,column=1,sticky="w")
    root.mainloop() #กำหนดให้หน้า root เป็นลูปหลักเพื่อการแสดงค่า
main()