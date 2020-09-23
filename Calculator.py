from tkinter import *
top = Tk()
top.geometry("400x500")
top.title('Calculator')
l=[]
def cal(l):
    s=0
    l1=list()
    l2=list()
    for i in range(len(l)):
        try:
            if type(int(l[i]))!=int:
                l2.append(i)
        except:
            if i==0:
                l1.append(0)
                l2.append(l[i])
            else:
                v=''
                if l1==[]:
                    for j in l[s:i]:
                        v=v+str(j)
                    l1.append(int(v))
                else:
                    for j in l[s+1:i]:
                        v=v+str(j)
                    l1.append(int(v))
                s=i
            if i!=0:
                l2.append(l[i])
    v=''
    for i in l[s+1:]:
        v=v+str(i)
    l1.append(int(v))
    print(l1,l2)
    while '*' in l2:
        for i in range(len(l2)):
            if l2[i]=='*':
                l1[i]=(l1[i]*l1[i+1])
                del l1[i+1]
                del l2[i]
                break
        print(l1,l2)
    while '/' in l2:
        for i in range(len(l2)):
            if l2[i]=='/':
                l1[i]=(l1[i]/l1[i+1])
                del l1[i+1]
                del l2[i]
                break
        print(l1,l2)
    while '+' in l2:
        for i in range(len(l2)):
            if l2[i]=='+':
                l1[i]=l1[i]+l1[i+1]
                del l1[i+1]
                del l2[i]
                break
        print(l1,l2)
    while '-' in l2:
        for i in range(len(l2)):
            if l2[i]=='-':
                l1[i]=l1[i]-l1[i+1]
                del l1[i+1]
                del l2[i]
                break
        print(l1,l2)
    return str(l1[0])
def fun(num):
    res=''
    if num!='Del':
        l.append(num)
    else:
        l.pop()
    str=''
    label =Label( top,text=l,height=2,fg='white',bg='black',width=40,font=('cambria bold',15))
    label.place(x=0,y=0)
    if '+' in l or '-' in l or '*' in l or '/' in l:
        res=True
    if res:
        try:
            label1 =Label(top,text=cal(l),height=2,fg='white',bg='black',width=40,font=('cambria bold',15))
            label1.place(x=0,y=50)
        except:
            mohan='try'
b1=Button(top,text='1',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('1'))
b2=Button(top,text='2',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('2'))
b3=Button(top,text='3',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('3'))
b1.place(x=0,y=100)
b2.place(x=90,y=100)
b3.place(x=190,y=100)
bp=Button(top,text='+',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('+'))
bp.place(x=280,y=100)
b4=Button(top,text='4',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('4'))
b4.place(x=0,y=200)
b5=Button(top,text='5',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('5'))
b5.place(x=90,y=200)
b6=Button(top,text='6',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('6'))
b6.place(x=190,y=200)
b7=Button(top,text='7',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('7'))
b7.place(x=0,y=300)
b8=Button(top,text='8',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('8'))
b8.place(x=90,y=300)
b9=Button(top,text='9',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('9'))
b9.place(x=190,y=300)
bdot=Button(top,text='.',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('.'))
bdot.place(x=0,y=400)
b0=Button(top,text='0',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('0'))
b0.place(x=90,y=400)
beq=Button(top,text='Del',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('Del'))
beq.place(x=190,y=400)
bmi=Button(top,text='-',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('-'))
bmi.place(x=280,y=200)
bmu=Button(top,text='*',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('*'))
bmu.place(x=280,y=300)
bd=Button(top,text='/',height=7,fg='white',bg='black',width=15,font=('cambria bold',10),command=lambda : fun('/'))
bd.place(x=280,y=400)
top.mainloop()
