import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import datetime
def SequencePattern1():
    global labelqnoSequencePattern1,labelqSequencePattern1,labelmcqSequencePattern1,radiovarSequencePattern1,r1SequencePattern1,r2SequencePattern1,r3SequencePattern1,r4SequencePattern1,nextSequencePattern1,points,scoreq1
    labelqnoSequencePattern1=Label(root,text="Question 1",bg="#b3e7ff")
    labelqnoSequencePattern1.pack()
    scoreq1=0
    flag2=0
    qstr=""
    initial=random.randrange(0,201)
    num=random.randrange(2,20)
    sign=random.choice(["+","-"])
    pattern="initial"+sign+"num"
    l=[]
    count=1
    for i in range(0,6):
        g=eval(pattern)
        l.append(g)
        initial=g
    omitted=random.choice(l)
    index=l.index(omitted)
    l[index]="?"
    for i in l:
        if count<6:
            qstr=qstr+str(i)+","
        else:
            qstr=qstr+str(i)
        count=count+1
    labelqSequencePattern1=Label(root,text=qstr,font="ar 15 bold",bg="#b3e7ff")
    labelqSequencePattern1.pack(pady=20)
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted)+str(osign)+str(onum))
            ol.append(option)
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and omitted in ol:
            break
    random.shuffle(ol)
    labelmcqSequencePattern1=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqSequencePattern1.pack(pady=20)
    def selectedSequencePattern1():
        global labelqnoSequencePattern1,labelqSequencePattern1,labelmcqSequencePattern1,radiovarSequencePattern1,r1SequencePattern1,r2SequencePattern1,r3SequencePattern1,r4SequencePattern1,nextSequencePattern1,points,scoreq1
        flag2=0

        ans=int(radiovarSequencePattern1.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index(omitted)+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq1=5
        else:
            lans=[]
            l[index]=omitted
            for i in range(0,6):
                if i<5:
                    lans.append(str(l[i])+sign+str(num)+"="+str(l[i+1]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index(omitted)+1)+"\n"+"Pattern Explanation : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2]+"\n"+lans[3]+"\n"+lans[4])
        labelqnoSequencePattern1.destroy()
        labelqSequencePattern1.destroy()
        labelmcqSequencePattern1.destroy()
        r1SequencePattern1.destroy()
        r2SequencePattern1.destroy()
        r3SequencePattern1.destroy()
        r4SequencePattern1.destroy()
        nextSequencePattern1.destroy()
        root.quit()
    radiovarSequencePattern1=IntVar()
    radiovarSequencePattern1.set(-1)
    r1SequencePattern1=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarSequencePattern1,bg="#b3e7ff")
    r1SequencePattern1.pack(pady=20)
    r2SequencePattern1=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarSequencePattern1,bg="#b3e7ff")
    r2SequencePattern1.pack(pady=20)
    r3SequencePattern1=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarSequencePattern1,bg="#b3e7ff")
    r3SequencePattern1.pack(pady=20)
    r4SequencePattern1=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarSequencePattern1,bg="#b3e7ff")
    r4SequencePattern1.pack(pady=20)
    nextSequencePattern1=Button(root,text="Next Question",command=selectedSequencePattern1)
    nextSequencePattern1.pack(pady=10)
    root.mainloop()
def PiePattern():
    global labelqnoPiePattern,labelqPiePattern,labelmcqPiePattern,radiovarPiePattern,r1PiePattern,r2PiePattern,r3PiePattern,r4PiePattern,nextPiePattern,canvasPiePattern,points,scoreq4
    labelqnoPiePattern=Label(root,text="Question 4",bg="#b3e7ff")
    labelqnoPiePattern.pack()
    flag2=0
    scoreq4=0
    x1=random.randrange(1,6)
    x2=random.randrange(0,11)
    a=random.choice(["+","-"])
    n=random.randrange(1,50)
    n1=random.randrange(1,50)
    n2=random.randrange(1,50)
    pattern="x1*x"+a+str(x2)
    l=[n,n1,n2]
    l1=[1,1,1,1,1,1]
    l2=[n,n1,n2]
    for i in l2:
        x=i
        g=eval(pattern)
        l.append(g)
    omitted=random.choice(l)
    index=l.index(omitted)
    l[index]="?"
    figPiePattern=Figure(figsize=(2,2),dpi=100,facecolor="#b3e7ff")
    plotPiePattern=figPiePattern.add_subplot(111)
    plotPiePattern.pie(l1,labels=l,labeldistance=0.6,colors=["blue","red","green","blue","red","green"])
    canvasPiePattern=FigureCanvasTkAgg(figPiePattern,master=root)
    canvasPiePattern.draw()
    canvasPiePattern.get_tk_widget().pack()
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted)+str(osign)+str(onum))
            ol.append(option)
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and omitted in ol:
            break
    random.shuffle(ol)
    labelmcqPiePattern=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqPiePattern.pack(pady=20)
    def selectedPiePattern():
        global labelqnoPiePattern,labelqPiePattern,labelmcqPiePattern,radiovarPiePattern,r1PiePattern,r2PiePattern,r3PiePattern,r4PiePattern,nextPiePattern,canvasPiePattern,points,scoreq4
        flag2=0

        ans=int(radiovarPiePattern.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index(omitted)+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq4=5
        else:
            lans=[]
            l[index]=omitted
            for i in range(0,3):
                lans.append(str(l[i])+"*"+str(x1)+str(a)+str(x2)+"="+str(l[i+3]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index(omitted)+1)+"\n"+"Pattern Explanation : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2])
    
        labelqnoPiePattern.destroy()
        labelmcqPiePattern.destroy()
        r1PiePattern.destroy()
        r2PiePattern.destroy()
        r3PiePattern.destroy()
        r4PiePattern.destroy()
        nextPiePattern.destroy()
        canvasPiePattern._tkcanvas.destroy()
        root.quit()        
    radiovarPiePattern=IntVar()
    radiovarPiePattern.set(-1)
    r1PiePattern=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarPiePattern,bg="#b3e7ff")
    r1PiePattern.pack(pady=20)
    r2PiePattern=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarPiePattern,bg="#b3e7ff")
    r2PiePattern.pack(pady=20)
    r3PiePattern=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarPiePattern,bg="#b3e7ff")
    r3PiePattern.pack(pady=20)
    r4PiePattern=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarPiePattern,bg="#b3e7ff")
    r4PiePattern.pack(pady=20)
    nextPiePattern=Button(root,text="Next Question",command=selectedPiePattern)
    nextPiePattern.pack(pady=10)
    root.mainloop()
def SequencePattern2():
    global labelqnoSequencePattern2,labelqSequencePattern2,labelmcqSequencePattern2,radiovarSequencePattern2,r1SequencePattern2,r2SequencePattern2,r3SequencePattern2,r4SequencePattern2,nextSequencePattern2,points,scoreq1
    labelqnoSequencePattern2=Label(root,text="Question 1",bg="#b3e7ff")
    labelqnoSequencePattern2.pack()
    qstr=""
    flag2=0
    scoreq1=0
    initial=random.randrange(0,201)
    num=random.randrange(2,10)
    num2=random.randrange(1,4)
    sign=random.choice(["+","-"])
    sign2=random.choice(["+","-"])
    pattern="initial"+sign+"num"
    pattern2="num"+sign2+"num2"
    l=[]
    l2=[]
    count=1
    for i in range(0,6):
        g=eval(pattern)
        l.append(g)
        initial=g
        num=eval(pattern2)
        l2.append(num)
    omitted=random.choice(l)
    index=l.index(omitted)
    l[index]="?"
    for i in l:
        if count<6:
            qstr=qstr+str(i)+","
        else:
            qstr=qstr+str(i)
        count=count+1
    labelqSequencePattern2=Label(root,text=qstr,font="ar 15 bold",bg="#b3e7ff")
    labelqSequencePattern2.pack(pady=20)
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted)+str(osign)+str(onum))
            ol.append(option)
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and omitted in ol:
            break
    random.shuffle(ol)
    labelmcqSequencePattern2=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqSequencePattern2.pack(pady=20)
    def selectedSequencePattern2():
        global labelqnoSequencePattern2,labelqSequencePattern2,labelmcqSequencePattern2,radiovarSequencePattern2,r1SequencePattern2,r2SequencePattern2,r3SequencePattern2,r4SequencePattern2,nextSequencePattern2,points,scoreq1
        flag2=0
        ans=int(radiovarSequencePattern2.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index(omitted)+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq1=5
        else:
            lans=[]
            l[index]=omitted
            for i in range(0,6):
                if i<5:
                    lans.append(str(l[i])+sign+str(l2[i])+"="+str(l[i+1]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index(omitted)+1)+"\n"+"Pattern Explanation : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2]+"\n"+lans[3]+"\n"+lans[4])
        labelqnoSequencePattern2.destroy()
        labelqSequencePattern2.destroy()
        labelmcqSequencePattern2.destroy()
        r1SequencePattern2.destroy()
        r2SequencePattern2.destroy()
        r3SequencePattern2.destroy()
        r4SequencePattern2.destroy()
        nextSequencePattern2.destroy()
        root.quit()
    radiovarSequencePattern2=IntVar()
    radiovarSequencePattern2.set(-1)
    r1SequencePattern2=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarSequencePattern2,bg="#b3e7ff")
    r1SequencePattern2.pack(pady=20)
    r2SequencePattern2=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarSequencePattern2,bg="#b3e7ff")
    r2SequencePattern2.pack(pady=20)
    r3SequencePattern2=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarSequencePattern2,bg="#b3e7ff")
    r3SequencePattern2.pack(pady=20)
    r4SequencePattern2=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarSequencePattern2,bg="#b3e7ff")
    r4SequencePattern2.pack(pady=20)
    nextSequencePattern2=Button(root,text="Next Question",command=selectedSequencePattern2)
    nextSequencePattern2.pack(pady=20)
    root.mainloop()
def SquarePattern():
    global labelqnoSquarePattern,labelqSquarePattern,labelmcqSquarePattern,radiovarSquarePattern,r1SquarePattern,r2SquarePattern,r3SquarePattern,r4SquarePattern,nextSquarePattern,points,scoreq2
    labelqnoSquarePattern=Label(root,text="Question 2",bg="#b3e7ff")
    labelqnoSquarePattern.pack()
    flag2=0
    scoreq2=0
    qstr=""
    n1=random.randrange(1,4)
    n2=random.randrange(1,11)
    n3=random.randrange(1,4)
    n4=random.randrange(1,11)
    x=random.randrange(1,31)
    x2=random.randrange(1,31)
    x3=random.randrange(1,31)
    sign=random.choice(["+","-"])
    sign2=random.choice(["+","-"])
    pattern="n1*a"+sign+"n2"
    pattern2="n3*a"+sign2+"n4"
    q=random.randrange(0,3)
    w=random.randrange(0,3)
    while q==w or q>w:
        w=random.randrange(0,3)
        q=random.randrange(0,3)
    l=[x]
    l2=[x2]
    l3=[x3]
    count=1
    count2=1
    count3=1
    for i in range(0,2):
        a=l[i]
        if i==0:
            g=eval(pattern)
            l.append(g)
        else:
            g=eval(pattern2)
            l.append(g)
    for i in range(0,2):
        a=l2[i]
        if i==0:
            g=eval(pattern)
            l2.append(g)
        else:
            g=eval(pattern2)
            l2.append(g)
    for i in range(0,2):
        a=l3[i]
        if i==0:
            g=eval(pattern)
            l3.append(g)
        else:
            g=eval(pattern2)
            l3.append(g)
    List=random.choice([l,l2,l3])
    omitted=List[q]
    List[q]="?"
    omitted2=List[w]
    List[w]="?"
    for i in l:
        if count<3:
            qstr=qstr+str(i)+"\t"
        else:
            qstr=qstr+str(i)+"\n"
        count=count+1
    for i in l2:
        if count2<3:
            qstr=qstr+str(i)+"\t"
        else:
            qstr=qstr+str(i)+"\n"
        count2=count2+1
    for i in l3:
        if count3<3:
            qstr=qstr+str(i)+"\t"
        else:
            qstr=qstr+str(i)
        count3=count3+1
    labelqSquarePattern=Label(root,text=qstr,font="ar 15 bold",bg="#b3e7ff")
    labelqSquarePattern.pack(pady=20)
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted)+str(osign)+str(onum))
            osign2=random.choice(["+","-"])
            onum2=random.randrange(0,3)
            option2=eval(str(omitted2)+str(osign2)+str(onum2))
            ol.append([option,option2])
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and [omitted,omitted2] in ol:
            break
    random.shuffle(ol)
    labelmcqSquarePattern=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqSquarePattern.pack(pady=20)
    def selectedSquarePattern():
        global labelqnoSquarePattern,labelqSquarePattern,labelmcqSquarePattern,radiovarSquarePattern,r1SquarePattern,r2SquarePattern,r3SquarePattern,r4SquarePattern,nextSquarePattern,points,scoreq2
        flag2=0
        ans=int(radiovarSquarePattern.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index([omitted,omitted2])+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq2=5
        else:
            List[q]=omitted
            List[w]=omitted2
            lans=[]
            lans.append(str(n1)+"*"+str(l[0])+sign+str(n2)+"="+str(l[1])+"\t\t;\t\t"+str(n3)+"*"+str(l[1])+sign2+str(n4)+"="+str(l[2]))
            lans.append(str(n1)+"*"+str(l2[0])+sign+str(n2)+"="+str(l2[1])+"\t\t;\t\t"+str(n3)+"*"+str(l2[1])+sign2+str(n4)+"="+str(l2[2]))
            lans.append(str(n1)+"*"+str(l3[0])+sign+str(n2)+"="+str(l3[1])+"\t\t;\t\t"+str(n3)+"*"+str(l3[1])+sign2+str(n4)+"="+str(l3[2]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index([omitted,omitted2])+1)+"\n"+"Pattern Explanation : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2])
        labelqnoSquarePattern.destroy()
        labelqSquarePattern.destroy()
        labelmcqSquarePattern.destroy()
        r1SquarePattern.destroy()
        r2SquarePattern.destroy()
        r3SquarePattern.destroy()
        r4SquarePattern.destroy()
        nextSquarePattern.destroy()
        root.quit()
    radiovarSquarePattern=IntVar()
    radiovarSquarePattern.set(-1)
    r1SquarePattern=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarSquarePattern,bg="#b3e7ff")
    r1SquarePattern.pack(pady=20)
    r2SquarePattern=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarSquarePattern,bg="#b3e7ff")
    r2SquarePattern.pack(pady=20)
    r3SquarePattern=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarSquarePattern,bg="#b3e7ff")
    r3SquarePattern.pack(pady=20)
    r4SquarePattern=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarSquarePattern,bg="#b3e7ff")
    r4SquarePattern.pack(pady=20)
    nextSquarePattern=Button(root,text="Next Question",command=selectedSquarePattern)
    nextSquarePattern.pack(pady=20)
    root.mainloop()
def BoxPattern1():
    global labelqnoBoxPattern1,labelqBoxPattern1,labelmcqBoxPattern1,radiovarBoxPattern1,r1BoxPattern1,r2BoxPattern1,r3BoxPattern1,r4BoxPattern1,nextBoxPattern1,canvasBoxPattern1,points,scoreq5
    labelqnoBoxPattern1=Label(root,text="Question 5",bg="#b3e7ff")
    labelqnoBoxPattern1.pack()
    flag2=0
    scoreq5=0
    initial=random.randrange(0,201)
    num=random.randrange(2,20)
    sign=random.choice(["+","-"])
    pattern="initial"+sign+"num"
    l=[]
    for i in range(0,4):
        g=eval(pattern)
        l.append(g)
        initial=g
    omitted1=random.choice(l)
    index1=l.index(omitted1)
    l[index1]="?"
    initial2=random.randrange(0,201)
    num2=random.randrange(2,20)
    sign2=random.choice(["+","-"])
    pattern2="initial2"+sign2+"num2"
    l2=[]
    for i in range(0,4):
        g2=eval(pattern2)
        l2.append(g2)
        initial2=g2
    omitted2=l2[index1]
    l2[index1]="?"
    figBoxPattern1=Figure(figsize=(2,2),dpi=50)
    fig=figBoxPattern1.add_subplot(111)
    fig,ax=plt.subplots(facecolor="#b3e7ff")
    rectangles={str(l[0]):mpatch.Rectangle((1,3),2,2,color="blue"),str(l[1]):mpatch.Rectangle((4,3),2,2,color="blue"),str(l[2]):mpatch.Rectangle((7,3),2,2,color="blue"),str(l[3]):mpatch.Rectangle((10,3),2,2,color="blue")}
    rectangles2={str(l2[0]):mpatch.Rectangle((1,1),2,2,color="green"),str(l2[1]):mpatch.Rectangle((4,1),2,2,color="green"),str(l2[2]):mpatch.Rectangle((7,1),2,2,color="green"),str(l2[3]):mpatch.Rectangle((10,1),2,2,color="green")}
    for r in rectangles:
        ax.add_artist(rectangles[r])
        rx,ry=rectangles[r].get_xy()
        cx=rx+rectangles[r].get_width()/2
        cy=ry+rectangles[r].get_height()/2
        ax.annotate(r,(cx,cy),color="black",weight="bold",fontsize=12,ha="center",va="center")
    for r in rectangles2:
        ax.add_artist(rectangles2[r])
        rx,ry=rectangles2[r].get_xy()
        cx=rx+rectangles2[r].get_width()/2
        cy=ry+rectangles2[r].get_height()/2
        ax.annotate(r,(cx,cy),color="black",weight="bold",fontsize=12,ha="center",va="center")
    ax.set_xlim((0,13))
    ax.set_ylim((0,6))
    ax.set_aspect("equal")
    ax.set_facecolor("#b3e7ff")
    plt.axis("off")
    canvasBoxPattern1=FigureCanvasTkAgg(fig,master=root)
    canvasBoxPattern1.draw()
    canvasBoxPattern1.get_tk_widget().pack()
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted1)+str(osign)+str(onum))
            osign2=random.choice(["+","-"])
            onum2=random.randrange(0,3)
            option2=eval(str(omitted2)+str(osign2)+str(onum2))
            ol.append([option,option2])
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and [omitted1,omitted2] in ol:
            break
    random.shuffle(ol)
    labelmcqBoxPattern1=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqBoxPattern1.pack()
    def selectedBoxPattern1():
        global labelqnoBoxPattern1,labelqBoxPattern1,labelmcqBoxPattern1,radiovarBoxPattern1,r1BoxPattern1,r2BoxPattern1,r3BoxPattern1,r4BoxPattern1,nextBoxPattern1,canvasBoxPattern1,points,scoreq5,t6
        flag2=0
        ans=int(radiovarBoxPattern1.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index([omitted1,omitted2])+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq5=5
        else:
            lans=[]
            lans2=[]
            l[index1]=omitted1
            l2[index1]=omitted2
            for i in range(0,4):
                if i<3:
                    lans.append(str(l[i])+sign+str(num)+"="+str(l[i+1]))
            for i in range(0,4):
                if i<3:
                    lans2.append(str(l2[i])+sign2+str(num2)+"="+str(l2[i+1]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index([omitted1,omitted2])+1)+"\n"+"Pattern Explanation : \n"+"Pattern 1(blue) : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2]+"\n"+"Pattern 2(green) :\n"+lans2[0]+"\n"+lans2[1]+"\n"+lans2[2])
        labelqnoBoxPattern1.destroy()
        labelmcqBoxPattern1.destroy()
        r1BoxPattern1.destroy()
        r2BoxPattern1.destroy()
        r3BoxPattern1.destroy()
        r4BoxPattern1.destroy()
        nextBoxPattern1.destroy()
        canvasBoxPattern1._tkcanvas.destroy()
        t6=str(datetime.datetime.now())
        if t6[17:19]>t5[17:19]:
            if (int(t6[14:16])-int(t5[14:16]))*60+(int(t6[17:19])-int(t5[17:19]))>120:
                points=points-2
                scoreq5=scoreq5-2
        else:
            if (int(t6[14:16])-int(t5[14:16])-1)*60+(60-(int(t5[17:19])-int(t6[17:19])))>120:
                points=points-2
                scoreq5=scoreq5-2
        result()
    radiovarBoxPattern1=IntVar()
    radiovarBoxPattern1.set(-1)
    r1BoxPattern1=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarBoxPattern1,bg="#b3e7ff")
    r1BoxPattern1.pack()
    r2BoxPattern1=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarBoxPattern1,bg="#b3e7ff")
    r2BoxPattern1.pack()
    r3BoxPattern1=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarBoxPattern1,bg="#b3e7ff")
    r3BoxPattern1.pack()
    r4BoxPattern1=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarBoxPattern1,bg="#b3e7ff")
    r4BoxPattern1.pack()
    nextBoxPattern1=Button(root,text="Submit",command=selectedBoxPattern1)
    nextBoxPattern1.pack(pady=10)
    root.mainloop()
def BoxPattern2():
    global labelqnoBoxPattern2,labelqBoxPattern2,labelmcqBoxPattern2,radiovarBoxPattern2,r1BoxPattern2,r2BoxPattern2,r3BoxPattern2,r4BoxPattern2,nextBoxPattern2,canvasBoxPattern2,points,scoreq5
    labelqnoBoxPattern2=Label(root,text="Question 5",bg="#b3e7ff")
    labelqnoBoxPattern2.pack()
    flag2=0
    scoreq5=0
    initial=random.randrange(0,201)
    num=random.randrange(2,20)
    sign=random.choice(["+","-"])
    pattern="initial"+sign+"num"
    l=[]
    for i in range(0,4):
        g=eval(pattern)
        l.append(g)
        initial=g
    omitted1=random.choice(l)
    index1=l.index(omitted1)
    l[index1]="?"
    initial2=random.randrange(0,201)
    num2=random.randrange(2,20)
    sign2=random.choice(["+","-"])
    pattern2="initial2"+sign2+"num2"
    l2=[]
    for i in range(0,4):
        g2=eval(pattern2)
        l2.append(g2)
        initial2=g2
    omitted2=l2[index1]
    l2[index1]="?"
    figBoxPattern2=Figure(figsize=(2,2),dpi=50)
    fig=figBoxPattern2.add_subplot(111)
    fig,ax=plt.subplots(facecolor="#b3e7ff")
    rectangles={str(l[0]):mpatch.Rectangle((1,3),2,2,color="blue"),str(l2[1]):mpatch.Rectangle((4,3),2,2,color="green"),str(l[2]):mpatch.Rectangle((7,3),2,2,color="blue"),str(l2[3]):mpatch.Rectangle((10,3),2,2,color="green")}
    rectangles2={str(l2[0]):mpatch.Rectangle((1,1),2,2,color="green"),str(l[1]):mpatch.Rectangle((4,1),2,2,color="blue"),str(l2[2]):mpatch.Rectangle((7,1),2,2,color="green"),str(l[3]):mpatch.Rectangle((10,1),2,2,color="blue")}
    for r in rectangles:
        ax.add_artist(rectangles[r])
        rx,ry=rectangles[r].get_xy()
        cx=rx+rectangles[r].get_width()/2
        cy=ry+rectangles[r].get_height()/2
        ax.annotate(r,(cx,cy),color="black",weight="bold",fontsize=12,ha="center",va="center")
    for r in rectangles2:
        ax.add_artist(rectangles2[r])
        rx,ry=rectangles2[r].get_xy()
        cx=rx+rectangles2[r].get_width()/2
        cy=ry+rectangles2[r].get_height()/2
        ax.annotate(r,(cx,cy),color="black",weight="bold",fontsize=12,ha="center",va="center")
    ax.set_xlim((0,13))
    ax.set_ylim((0,6))
    ax.set_aspect("equal")
    ax.set_facecolor("#b3e7ff")
    plt.axis("off")
    canvasBoxPattern2=FigureCanvasTkAgg(fig,master=root)
    canvasBoxPattern2.draw()
    canvasBoxPattern2.get_tk_widget().pack()
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(omitted1)+str(osign)+str(onum))
            osign2=random.choice(["+","-"])
            onum2=random.randrange(0,3)
            option2=eval(str(omitted2)+str(osign2)+str(onum2))
            ol.append([option,option2])
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and [omitted1,omitted2] in ol:
            break
    random.shuffle(ol)
    labelmcqBoxPattern2=Label(root,text="The missing number is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqBoxPattern2.pack()
    def selectedBoxPattern2():
        global labelqnoBoxPattern2,labelqBoxPattern2,labelmcqBoxPattern2,radiovarBoxPattern2,r1BoxPattern2,r2BoxPattern2,r3BoxPattern2,r4BoxPattern2,nextBoxPattern2,canvasBoxPattern2,points,scoreq5,t6
        flag2=0
        ans=int(radiovarBoxPattern2.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index([omitted1,omitted2])+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq5=5
        else:
            lans=[]
            lans2=[]
            l[index1]=omitted1
            l2[index1]=omitted2
            for i in range(0,4):
                if i<3:
                    lans.append(str(l[i])+sign+str(num)+"="+str(l[i+1]))
            for i in range(0,4):
                if i<3:
                    lans2.append(str(l2[i])+sign2+str(num2)+"="+str(l2[i+1]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index([omitted1,omitted2])+1)+"\n"+"Pattern Explanation : \n"+"Pattern 1(blue) : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2]+"\n"+"Pattern 2(green) :\n"+lans2[0]+"\n"+lans2[1]+"\n"+lans2[2])
        labelqnoBoxPattern2.destroy()
        labelmcqBoxPattern2.destroy()
        r1BoxPattern2.destroy()
        r2BoxPattern2.destroy()
        r3BoxPattern2.destroy()
        r4BoxPattern2.destroy()
        nextBoxPattern2.destroy()
        canvasBoxPattern2._tkcanvas.destroy()
        t6=str(datetime.datetime.now())
        if t6[17:19]>t5[17:19]:
            if (int(t6[14:16])-int(t5[14:16]))*60+(int(t6[17:19])-int(t5[17:19]))>120:
                points=points-2
                scoreq5=scoreq5-2
        else:
            if (int(t6[14:16])-int(t5[14:16])-1)*60+(60-(int(t5[17:19])-int(t6[17:19])))>120:
                points=points-2
                scoreq5=scoreq5-2
        result()  
    radiovarBoxPattern2=IntVar()
    radiovarBoxPattern2.set(-1)
    r1BoxPattern2=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarBoxPattern2,bg="#b3e7ff")
    r1BoxPattern2.pack()
    r2BoxPattern2=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarBoxPattern2,bg="#b3e7ff")
    r2BoxPattern2.pack()
    r3BoxPattern2=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarBoxPattern2,bg="#b3e7ff")
    r3BoxPattern2.pack()
    r4BoxPattern2=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarBoxPattern2,bg="#b3e7ff")
    r4BoxPattern2.pack()
    nextBoxPattern2=Button(root,text="Submit",command=selectedBoxPattern2)
    nextBoxPattern2.pack(pady=10)
    root.mainloop()
def AlphabetPattern():
    global labelqnoAlphabetPattern,labelqAlphabetPattern,labelmcqAlphabetPattern,radiovarAlphabetPattern,r1AlphabetPattern,r2AlphabetPattern,r3AlphabetPattern,r4AlphabetPattern,nextAlphabetPattern,points,scoreq3
    labelqnoAlphabetPattern=Label(root,text="Question 3",bg="#b3e7ff")
    labelqnoAlphabetPattern.pack()
    flag2=0
    scoreq3=0
    qstr=""
    initial=random.randrange(76,79)
    num=random.randrange(2,4)
    sign=random.choice(["+","-"])
    pattern="initial"+sign+"num"
    l=[]
    count=1
    for i in range(0,4):
        g=eval(pattern)
        l.append(chr(g))
        initial=g
    omitted=random.choice(l)
    index=l.index(omitted)
    l[index]="?"
    for i in l:
        if count<4:
            qstr=qstr+str(i)+","
        else:
            qstr=qstr+str(i)
        count=count+1
    labelqAlphabetPattern=Label(root,text=qstr,font="ar 15 bold",bg="#b3e7ff")
    labelqAlphabetPattern.pack(pady=20)
    while True:
        ol=[]
        for i in range(0,4):
            osign=random.choice(["+","-"])
            onum=random.randrange(0,3)
            option=eval(str(ord(omitted))+str(osign)+str(onum))
            ol.append(chr(option))
        if ol.count(ol[0])==1 and ol.count(ol[1])==1 and ol.count(ol[2])==1 and omitted in ol:
            break
    random.shuffle(ol)
    labelmcqAlphabetPattern=Label(root,text="The missing alphabet is : ",font="ar 15 bold",bg="#b3e7ff")
    labelmcqAlphabetPattern.pack(pady=20)
    def selectedAlphabetPattern():
        global labelqnoAlphabetPattern,labelqAlphabetPattern,labelmcqAlphabetPattern,radiovarAlphabetPattern,r1AlphabetPattern,r2AlphabetPattern,r3AlphabetPattern,r4AlphabetPattern,nextAlphabetPattern,points,scoreq3
        flag2=0
        ans=int(radiovarAlphabetPattern.get())
        if ans==-1:
            messagebox.showerror(root,message="No answer selected.")
            return
        elif ans==ol.index(omitted)+1:
            messagebox.showinfo(root,message="Correct Answer !\n")
            flag2=1
            points=points+5
            scoreq3=5
        else:
            lans=[]
            l[index]=omitted
            for i in range(0,4):
                if i<3:
                    lans.append(str(l[i])+sign+str(num)+"="+str(l[i+1]))
            messagebox.showinfo(root,message="Incorrect Answer. Correct answer is option "+str(ol.index(omitted)+1)+"\n"+"Pattern Explanation : \n"+lans[0]+"\n"+lans[1]+"\n"+lans[2])
        labelqnoAlphabetPattern.destroy()
        labelqAlphabetPattern.destroy()
        labelmcqAlphabetPattern.destroy()
        r1AlphabetPattern.destroy()
        r2AlphabetPattern.destroy()
        r3AlphabetPattern.destroy()
        r4AlphabetPattern.destroy()
        nextAlphabetPattern.destroy()
        root.quit()
    radiovarAlphabetPattern=IntVar()
    radiovarAlphabetPattern.set(-1)
    r1AlphabetPattern=Radiobutton(root,text="1.\t"+str(ol[0]),value=1,variable=radiovarAlphabetPattern,bg="#b3e7ff")
    r1AlphabetPattern.pack(pady=20)
    r2AlphabetPattern=Radiobutton(root,text="2.\t"+str(ol[1]),value=2,variable=radiovarAlphabetPattern,bg="#b3e7ff")
    r2AlphabetPattern.pack(pady=20)
    r3AlphabetPattern=Radiobutton(root,text="3.\t"+str(ol[2]),value=3,variable=radiovarAlphabetPattern,bg="#b3e7ff")
    r3AlphabetPattern.pack(pady=20)
    r4AlphabetPattern=Radiobutton(root,text="4.\t"+str(ol[3]),value=4,variable=radiovarAlphabetPattern,bg="#b3e7ff")
    r4AlphabetPattern.pack(pady=20)
    nextAlphabetPattern=Button(root,text="Next Question",command=selectedAlphabetPattern)
    nextAlphabetPattern.pack(pady=10)
    root.mainloop()
################################################################################################################################################################################################
def Exit():
    root.destroy()
def mainscreen():
    global points,root,labelfrontbg,labelimage,conn,cursor,btn1,btn2,btn3,btn4
    points=0
    flag3=0
    root=tkinter.Tk()
    root.state("zoomed")
    root.title("PROJECT :  IQ TEST")
    root.geometry("700x600")
    root.config(background="#ffffff")
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    frontbg=Image.open("frontbg.png")
    frontbg=frontbg.resize((width,height),Image.LANCZOS)
    resize=ImageTk.PhotoImage(frontbg)
    labelfrontbg=Label(root,image=resize)
    labelfrontbg.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open("IQ-Test.jpg"))
    labelimage=Label(root,image=img,bg="#ffffff")
    labelimage.pack(pady=(30,0))
    try:
        conn=mysql.connector.connect(host="localhost",user="Parth",password="123456",database="parthproj")
        cursor=conn.cursor()
    except:
        conn=mysql.connector.connect(host="localhost",user="Parth",password="123456")
        cursor=conn.cursor()
        cursor.execute("create database parthproj;")
        cursor.execute("commit;")
        conn=mysql.connector.connect(host="localhost",user="Parth",password="123456",database="parthproj")
        cursor=conn.cursor()
    btn1=Button(root,text="About IQ Test",width=15,height=2,fg="white",bg="#01A9DB",command=abt)
    btn2=Button(root,text="Start Test",width=15,height=2,fg="white",bg="#01A9DB",command=start)
    btn3=Button(root,text="Check Scores",width=15,height=2,fg="white",bg="#01A9DB",command=checkscores)
    btn4=Button(root,text="Exit",width=15,height=2,fg="white",bg="#01A9DB",command=Exit) 
    btn1.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)
    btn4.pack(pady=10)
    root.mainloop()
def homepage():
    root.destroy()
    mainscreen()
def result():
    global labelAlphabetPattern1,labelAlphabetPattern2,homepagebtn
    try:
        query="insert into scores values ('{}',1,'Numerical','{}','{}',{}),('{}',2,'Numerical','{}','{}',{}),('{}',3,'Numerical','{}','{}',{}),('{}',4,'Visual','{}','{}',{}),('{}',5,'Visual','{}','{}',{});".format(usernameinfo,t1,t2,scoreq1,usernameinfo,t2,t3,scoreq2,usernameinfo,t3,t4,scoreq3,usernameinfo,t4,t5,scoreq4,usernameinfo,t5,t6,scoreq5)
        cursor.execute(query)
        cursor.execute("commit;")
    except:
        query="create table scores (Username varchar(16),QNo integer,Type varchar(10),Start_Time datetime,End_Time datetime,Score integer);"
        cursor.execute(query)
        cursor.execute("commit;")
        query="insert into scores values ('{}',1,'Numerical','{}','{}',{}),('{}',2,'Numerical','{}','{}',{}),('{}',3,'Numerical','{}','{}',{}),('{}',4,'Visual','{}','{}',{}),('{}',5,'Visual','{}','{}',{});".format(usernameinfo,t1,t2,scoreq1,usernameinfo,t2,t3,scoreq2,usernameinfo,t3,t4,scoreq3,usernameinfo,t4,t5,scoreq4,usernameinfo,t5,t6,scoreq5)
        cursor.execute(query)
        cursor.execute("commit;")
    labelAlphabetPattern1=Label(root,text="Results : ",font="ar 15 bold",bg="#b3e7ff")
    labelAlphabetPattern1.pack(pady=20)
    labelAlphabetPattern2=Label(root,text="You Scored "+str(points)+"/25",font="ar 15 bold",bg="#b3e7ff")
    labelAlphabetPattern2.pack(pady=20)
    if points<=0:
        Label(root,text="Your IQ is 99 or Below",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points>=1 and points<=5:
        Label(root,text="Your IQ is in the range 100-105",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points>=6 and points<=10:
        Label(root,text="Your IQ is in the range 106-111",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points>=11 and points<=15:
        Label(root,text="Your IQ is in the range 112-117",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points>=16 and points<=20:
        Label(root,text="Your IQ is in the range 118-123",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points>=21 and points<=24:
        Label(root,text="Your IQ is in the range 124-129",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    if points==25:
        Label(root,text="Your IQ is 130 or above",font="ar 15 bold",bg="#b3e7ff").pack(pady=20)
    homepagebtn=Button(root,text="Return",command=homepage)
    homepagebtn.pack()
    root.mainloop()
def questions():
    global points,scoreq1,scoreq2,scoreq3,scoreq4,scoreq5,t1,t2,t3,t4,t5
    regframe.destroy()
    labelregbg.destroy()
    reglabel1.destroy()
    reglabel2.destroy()
    reglabel3.destroy()
    entry1.destroy()
    entry2.destroy()
    regbtn.destroy()
    reghomepagebtn.destroy()
    root.config(background="#b3e7ff")
    for i in range(1,6):
        if i==1:
            t1=str(datetime.datetime.now())
            l=["SequencePattern1()","SequencePattern2()"]
            flag2=eval(random.choice(l))
        if i==4:
            t4=str(datetime.datetime.now())
            if t4[17:19]>t3[17:19]:
                if (int(t4[14:16])-int(t3[14:16]))*60+(int(t4[17:19])-int(t3[17:19]))>120:
                    points=points-2
                    scoreq3=scoreq3-2
            else:
                if (int(t4[14:16])-int(t3[14:16])-1)*60+(60-(int(t3[17:19])-int(t4[17:19])))>120:
                    points=points-2
                    scoreq3=scoreq3-2
            flag2=PiePattern()
        if i==2:
            t2=str(datetime.datetime.now())
            if t2[17:19]>t1[17:19]:
                if (int(t2[14:16])-int(t1[14:16]))*60+(int(t2[17:19])-int(t1[17:19]))>120:
                    points=points-2
                    scoreq1=scoreq1-2
            else:
                if (int(t2[14:16])-int(t1[14:16])-1)*60+(60-(int(t1[17:19])-int(t2[17:19])))>120:
                    points=points-2
                    scoreq1=scoreq1-2
            flag2=SquarePattern()
        if i==5:
            t5=str(datetime.datetime.now())
            if t5[17:19]>t4[17:19]:
                if (int(t5[14:16])-int(t4[14:16]))*60+(int(t5[17:19])-int(t4[17:19]))>120:
                    points=points-2
                    scoreq4=scoreq4-2
            else:
                if (int(t5[14:16])-int(t4[14:16])-1)*60+(60-(int(t4[17:19])-int(t5[17:19])))>120:
                    points=points-2
                    scoreq4=scoreq4-2
            l=["BoxPattern1()","BoxPattern2()"]
            flag2=eval(random.choice(l))
        if i==3:
            t3=str(datetime.datetime.now())
            if t3[17:19]>t2[17:19]:
                if (int(t3[14:16])-int(t2[14:16]))*60+(int(t3[17:19])-int(t2[17:19]))>120:
                    points=points-2
                    scoreq2=scoreq2-2
            else:
                if (int(t3[14:16])-int(t2[14:16])-1)*60+(60-(int(t2[17:19])-int(t3[17:19])))>120:
                    points=points-2
                    scoreq2=scoreq2-2
            flag2=AlphabetPattern()
def login():
    global username,password,labelregbg,regframe,reglabel1,reglabel2,reglabel3,entry1,entry2,regbtn,reghomepagebtn
    def loginuser():
        global usernameinfo,passwordinfo
        flag=0
        usernameinfo=username.get()
        passwordinfo=password.get()
        try:
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        except:
            query="create table users (Username varchar(16),Password varchar(16));"
            cursor.execute(query)
            cursor.execute("commit;")
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        for i in l:
            if i[0]==usernameinfo and i[1]==passwordinfo:
                flag=1
        if flag==1:
            messagebox.showinfo(title="Login Successful",message="Test begins now. All the best !")
            questions()
        else:
            messagebox.showerror(title="Login Failed",message="User not found.")
            return
    startframe.destroy()
    labelstartbg.destroy()
    labeltext.destroy()
    labelinstr.destroy()
    loginbtn.destroy()
    registerbtn.destroy()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    frontbg=Image.open("startbg.png")
    frontbg=frontbg.resize((width,height),Image.LANCZOS)
    resize=ImageTk.PhotoImage(frontbg)
    labelregbg=Label(root,image=resize)
    labelregbg.place(x=0,y=0)
    regframe=Frame(root,bg="#ffffff",width=1000,height=300)
    regframe.pack(pady=30)
    regframe.pack_propagate(0)
    username=StringVar()
    password=StringVar()
    reglabel1=Label(regframe,text="Enter your Details : ",font="ar 15 bold",bg="#ffffff")
    reglabel1.pack(pady=7)
    reglabel2=Label(regframe,text="Username : ",font="ar 15 bold",bg="#ffffff")
    reglabel2.pack(pady=7)
    entry1=Entry(regframe,textvariable=username,bd=5)
    entry1.pack(pady=7)
    reglabel3=Label(regframe,text="Password : ",font="ar 15 bold",bg="#ffffff")
    reglabel3.pack(pady=7)
    entry2=Entry(regframe,textvariable=password,bd=5)
    entry2.pack(pady=7)
    Label(regframe,text="")
    regbtn=Button(regframe,text="Login",command=loginuser)
    regbtn.pack(pady=7)
    reghomepagebtn=Button(regframe,text="Return",command=homepage)
    reghomepagebtn.pack()
    root.mainloop()
def register():
    global username,password,labelregbg,regframe,reglabel1,reglabel2,reglabel3,entry1,entry2,regbtn,reghomepagebtn
    def registeruser():
        global usernameinfo,passwordinfo
        flag=0
        flag2=0
        usernameinfo=username.get()
        passwordinfo=password.get()
        if usernameinfo=="" or passwordinfo=="":
            messagebox.showerror(title="Registration Failed",message="Username or Password cannot be left empty.")
            return
        if len(usernameinfo)>15:
            messagebox.showerror(title="Registration Failed",message="Username exceeds the character limit.")
            return 
        for i in usernameinfo:
            if i not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"]:
                flag2=1
        if flag2==1:
            messagebox.showerror(title="Registration Failed",message="Username can only contain Alphabets or Numbers (Ex. : A,a,1).")
            return
        try:
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        except:
            query="create table users (Username varchar(16),Password varchar(16));"
            cursor.execute(query)
            cursor.execute("commit;")
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        for i in l:
            if i[0]==usernameinfo:
                flag=1
        if flag==0:
            query="insert into users values ('{}','{}');".format(usernameinfo,passwordinfo)
            cursor.execute(query)
            query2="commit;"
            cursor.execute(query2)
            messagebox.showinfo(title="Registration Successful",message="Test begins now. All the best !")
            questions()
        else:
            messagebox.showerror(title="Registration Failed",message="Username already exists, try to input another Username.")
            return
    startframe.destroy()
    labelstartbg.destroy()
    labeltext.destroy()
    labelinstr.destroy()
    loginbtn.destroy()
    registerbtn.destroy()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    frontbg=Image.open("startbg.png")
    frontbg=frontbg.resize((width,height),Image.LANCZOS)
    resize=ImageTk.PhotoImage(frontbg)
    labelregbg=Label(root,image=resize)
    labelregbg.place(x=0,y=0)
    regframe=Frame(root,bg="#ffffff",width=1000,height=300)
    regframe.pack(pady=30)
    regframe.pack_propagate(0)
    username=StringVar()
    password=StringVar()
    reglabel1=Label(regframe,text="Enter your Details : ",font="ar 15 bold",bg="#ffffff")
    reglabel1.pack(pady=7)
    reglabel2=Label(regframe,text="Username : ",font="ar 15 bold",bg="#ffffff")
    reglabel2.pack(pady=7)
    entry1=Entry(regframe,textvariable=username,bd=5)
    entry1.pack(pady=7)
    reglabel3=Label(regframe,text="Password : ",font="ar 15 bold",bg="#ffffff")
    reglabel3.pack(pady=7)
    entry2=Entry(regframe,textvariable=password,bd=5)
    entry2.pack(pady=7)
    Label(regframe,text="")
    regbtn=Button(regframe,text="Register",command=registeruser)
    regbtn.pack(pady=7)
    reghomepagebtn=Button(regframe,text="Return",command=homepage)
    reghomepagebtn.pack()
    root.mainloop()
def checkscores():
    global checkusername,checkpassword,checkreglabel1,checkreglabel2,checkreglabel3,checkentry1,checkentry2,checkregbtn,checkhomepagebtn
    labelimage.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    def check():
        checkreglabel1.destroy()
        checkreglabel2.destroy()
        checkreglabel3.destroy()
        checkentry1.destroy()
        checkentry2.destroy()
        checkregbtn.destroy()
        checkhomepagebtn.destroy()
        query="select * from scores where Username='{}'".format(checkusernameinfo)
        cursor.execute(query)
        l=cursor.fetchall()
        frame=Frame(root)
        frame.pack(pady=20)
        tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6),show='headings',height=8)
        tv.pack(side=LEFT)
        tv.heading(1,text="Username")
        tv.heading(2,text="QNo")
        tv.heading(3,text="Type")
        tv.heading(4,text="Start Time")
        tv.heading(5,text="End Time")
        tv.heading(6,text="Score")
        sb=Scrollbar(frame,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        tv.config(yscrollcommand=sb.set)
        sb.config(command=tv.yview)
        indx=0
        Iid=0
        for i in l:
            tv.insert(parent='',index=indx,iid=Iid,values=i)
            indx=indx+1
            Iid=Iid+1
        homepagebtn=Button(root,text="Return",command=homepage)
        homepagebtn.pack()
    def checkloginuser():
        global checkusernameinfo,checkpasswordinfo
        flag=0
        checkusernameinfo=checkusername.get()
        checkpasswordinfo=checkpassword.get()
        try:
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        except:
            query="create table users (Username varchar(16),Password varchar(16));"
            cursor.execute(query)
            cursor.execute("commit;")
            query="select * from users;"
            cursor.execute(query)
            l=cursor.fetchall()
        for i in l:
            if i[0]==checkusernameinfo and i[1]==checkpasswordinfo:
                flag=1
        if flag==1:
            check()
        else:
            messagebox.showerror(title="Checking Failed",message="User not found.")
            return
    checkusername=StringVar()
    checkpassword=StringVar()
    checkreglabel1=Label(root,text="Enter your Details : ",font="ar 15 bold",bg="#ffffff")
    checkreglabel1.pack(pady=7)
    checkreglabel2=Label(root,text="Username : ",font="ar 15 bold",bg="#ffffff")
    checkreglabel2.pack(pady=7)
    checkentry1=Entry(root,textvariable=checkusername,bd=5)
    checkentry1.pack(pady=7)
    checkreglabel3=Label(root,text="Password : ",font="ar 15 bold",bg="#ffffff")
    checkreglabel3.pack(pady=7)
    checkentry2=Entry(root,textvariable=checkpassword,bd=5)
    checkentry2.pack(pady=7)
    Label(root,text="")
    checkregbtn=Button(root,text="Check Score",command=checkloginuser)
    checkregbtn.pack(pady=7)
    checkhomepagebtn=Button(root,text="Return",command=homepage)
    checkhomepagebtn.pack()
    root.mainloop()
def start():
    global labelstartbg,startframe,labeltext,labelinstr,loginbtn,registerbtn
    labelimage.destroy()
    labelfrontbg.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    frontbg=Image.open("startbg.png")
    frontbg=frontbg.resize((width,height),Image.LANCZOS)
    resize=ImageTk.PhotoImage(frontbg)
    labelstartbg=Label(root,image=resize)
    labelstartbg.place(x=0,y=0)
    startframe=Frame(root,bg="#ffffff",width=1000,height=300)
    startframe.pack(pady=30)
    startframe.pack_propagate(0)
    labeltext=Label(startframe,text=" Instructions : ",font="ar 15 bold",bg="#ffffff")
    labeltext.pack(pady=20)
    labelinstr=Label(startframe,text="There will be 5 questions including 3 questions testing numerical ability and 2 questions testing visual ability.\nOnce the answer is selected and the 'Next Question' button is pressed, the correct answer will be displayed immidiately and it will be impossible to navigate to that question again.\nKindly register/login to continue. ",bg="#ffffff")
    labelinstr.pack(pady=20)
    loginbtn=Button(startframe,text="Login",command=login)
    loginbtn.pack()
    registerbtn=Button(startframe,text="Register",command=register)
    registerbtn.pack(pady=20)
    root.mainloop()
def abt():
    messagebox.showinfo(title="About IQ Test",message="An intelligence quotient (IQ) is a total score derived from a set of standardized tests or subtests designed to assess human intelligence. The abbreviation IQ was coined by the psychologist William Stern for the German term Intelligenzquotient, his term for a scoring method for intelligence tests at University of Breslau he advocated in a 1912 book. Historically, IQ was a score obtained by dividing a person's mental age score, obtained by administering an intelligence test, by the person's chronological age, both expressed in terms of years and months. The resulting fraction (quotient) was multiplied by 100 to obtain the IQ score. For modern IQ tests, the raw score is transformed to a normal distribution with mean 100 and standard deviation 15. This results in approximately two-thirds of the population scoring between IQ 85 and IQ 115 and about 2.5 percent each above 130 and below 70. Scores from intelligence tests are estimates of intelligence. Unlike, for example, distance and mass, a concrete measure of intelligence cannot be achieved given the abstract nature of the concept of intelligence. IQ scores have been shown to be associated with such factors as morbidity and mortality, parental social status, and, to a substantial degree, biological parental IQ. While the heritability of IQ has been investigated for nearly a century, there is still debate about the significance of heritability estimates and the mechanisms of inheritance.")
mainscreen()
