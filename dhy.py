from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
root=Tk()
root.geometry('800x800')
root.title('BILLING SYSTEM')
mycon=mysql.connector.connect(host='localhost',user='root',password='3113',database='billing',charset='utf8')
mycur=mycon.cursor()
mycur.execute('create database if not exists billing')
mycur.execute('use billing')
f1=Frame(root,height=100,width=800,bg='black')
f1.pack(side='top')
f2=Frame(root,height=100,width=800,bg='gray40')
f2.pack()
f3=Frame(root,height=50,width=800,bg='gray24')
f3.pack()
f4=Frame(root,height=300,width=800,bg='gray79')
f4.pack()
f5=Frame(root,height=300,width=500,bg='gray24')
f5.pack(side='left')
f6=Frame(root,height=155,width=400,bg='black')
f6.pack(side='left')
Label(f4,text='''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=50,y=0)
Label(f3,text='''|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray24').place(x=50,y=0)
Label(f4,text='''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=130,y=0)
Label(f3,text='''|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray24').place(x=130,y=0)
Label(f4,text='''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=400,y=0)
Label(f3,text='''|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray24').place(x=400,y=0)
Label(f4,text='''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=550,y=0)
Label(f3,text='''|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray24').place(x=550,y=0)
Label(f4,text='''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=650,y=0)
Label(f3,text='''|
|
|
''',font=('comic sana ms',13,'bold'),fg='black',bg='gray24').place(x=650,y=0)
Label(f3,text='S.no',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=0,y=5)
Label(f3,text='''Item
Code''',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=68,y=0)
Label(f3,text='Item Name',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=210,y=10)
Label(f3,text='Rate',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=450,y=5)
Label(f3,text='(per item/kg)',font=('comic sana ms',10,'bold'),fg='white',bg='gray24').place(x=440,y=30)
Label(f3,text='Qty',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=580,y=5)
Label(f3,text='''Total
Amount''',font=('comic sana ms',15,'bold'),fg='white',bg='gray24').place(x=680,y=0)
Label(f1,text='  SUPER MART',font=('comic sana ms',40,'bold'),fg='white',bg='black').place(x=0,y=15)
Label(f1,text='''
email: admin@supermart.ac.in
phone: 0441 9341 0025
Branch: Coimbatore''',font=('comic sana ms',13,'bold'),fg='white',bg='black').place(x=500,y=0)
Label(f2,text='Customer Name :',font=('comic sana ms',15,'bold'),fg='white',bg='gray40').place(x=10,y=5)
Label(f2,text='Customer Phone:',font=('comic sana ms',15,'bold'),fg='white',bg='gray40').place(x=10,y=30)
Label(f2,text='Bill No.               :',font=('comic sana ms',15,'bold'),fg='white',bg='gray40').place(x=10,y=56)
Label(f2,text='Date:',font=('comic sana ms',15,'bold'),fg='white',bg='gray40').place(x=630,y=20)

Label(f5,text='THANK YOU! VISIT AGAIN',font=('comic sana ms',18,'bold'),fg='white',bg='gray24').place(x=100,y=55)
def clickb1():
    print('saved')
    messagebox.showinfo('information', 'Data has been saved!')
def clickb111():
    a31=q31.get()
    a32=q32.get()
    a33='Bill'+q33.get()
    a34=q34.get()
    print('Customer Name:',a31)
    print('Customer Phone Number:',a32)
    print('Bill number:',a33)
    print('date:',a34)
    #table name is bill number
    c1='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10))'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c1)
    print(c1) 


def clickb2():
    a11=q11.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a11)
    a111=int(a11)
    print(items[a111])
    Label(f4,text=items[a111][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=0)
    Label(f4,text=items[a111][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=0)
    a21=q21.get()
    a211=int(a21)
    Label(f4,text=a211*items[a111][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=0)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a111,items[a111][0],items[a111][1],a211,a211*items[a111][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

    

def clickb3():
    a12=q12.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a12)
    a121=int(a12)
    print(items[a121])
    Label(f4,text=items[a121][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=30)
    Label(f4,text=items[a121][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=30)
    a22=q22.get()
    a221=int(a22)
    Label(f4,text=a221*items[a121][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=30)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a121,items[a121][0],items[a121][1],a221,a221*items[a121][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()
    
def clickb4():
    a13=q13.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a13)
    a131=int(a13)
    print(items[a131])
    Label(f4,text=items[a131][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=60)
    Label(f4,text=items[a131][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=60)
    a23=q23.get()
    a231=int(a23)
    Label(f4,text=a231*items[a131][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=60)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a131,items[a131][0],items[a131][1],a231,a231*items[a131][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

def clickb5():
    a14=q14.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a14)
    a141=int(a14)
    print(items[a141])
    Label(f4,text=items[a141][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=90)
    Label(f4,text=items[a141][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=90)
    a24=q24.get()
    a241=int(a24)
    Label(f4,text=a241*items[a141][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=90)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a141,items[a141][0],items[a141][1],a241,a241*items[a141][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()
    
def clickb6():
    a15=q15.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a15)
    a151=int(a15)
    print(items[a151])
    Label(f4,text=items[a151][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=120)
    Label(f4,text=items[a151][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=120)
    a25=q25.get()
    a251=int(a25)
    Label(f4,text=a251*items[a151][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=120)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a151,items[a151][0],items[a151][1],a251,a251*items[a151][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

def clickb7():
    a16=q16.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a16)
    a161=int(a16)
    print(items[a161])
    Label(f4,text=items[a161][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=150)
    Label(f4,text=items[a161][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=150)
    a26=q26.get()
    a261=int(a26)
    Label(f4,text=a261*items[a161][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=150)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a161,items[a161][0],items[a161][1],a261,a261*items[a161][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

def clickb8():
    a17=q17.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a17)
    a171=int(a17)
    print(items[a171])
    Label(f4,text=items[a171][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=180)
    Label(f4,text=items[a171][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=180)
    a27=q27.get()
    a271=int(a27)
    Label(f4,text=a271*items[a171][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=180)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a171,items[a171][0],items[a171][1],a271,a271*items[a171][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

def clickb9():
    a18=q18.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a18)
    a181=int(a18)
    print(items[a181])
    Label(f4,text=items[a181][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=210)
    Label(f4,text=items[a181][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=210)
    a28=q28.get()
    a281=int(a28)
    Label(f4,text=a281*items[a181][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=210)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a181,items[a181][0],items[a181][1],a281,a281*items[a181][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()



def clickb10():
    a19=q19.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a19)
    a191=int(a19)
    print(items[a191])
    Label(f4,text=items[a191][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=240)
    Label(f4,text=items[a191][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=240)
    a29=q29.get()
    a291=int(a29)
    Label(f4,text=a291*items[a191][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=240)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a191,items[a191][0],items[a191][1],a291,a291*items[a191][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()

def clickb11():
    a10=q20.get()
    items={101:['Apple       ',100],
       102:['Green grapes',60],
       103:['black grapes',65],
       104:['orange      ',100],
       105:['guava       ',55],
       106:['pomegranate ',124],
       107:['banana      ',62],
       108:['onion       ',48],
       109:['potato      ',64],
       110:['tomato      ',49],
       111:['carrot      ',106],
       112:['capsicum    ',120],
       113:['cabbage     ',57],
       114:['beans       ',58],
       115:['beetroot    ',89],
       116:['egg         ',7],
       117:['corriander  ',10],
       118:['lemon       ',5],
       119:['garlic      ',240],
       120:['sugar       ',38],
       121:['coke-300ml  ',40],
       122:['min.water-5L',70],
       123:['maaza 150ml ',10],
       124:['pepsi 250ml ',27],
       125:['lays-chips-s',10],
       126:['lays-chips-m',18],
       127:['oreo-biscuit',12],
       128:['moong dal   ',25],
       129:['milk bikies ',10],
       130:['maggi-small ',12]}
    print(a10)
    a101=int(a10)
    print(items[a101])
    Label(f4,text=items[a101][0],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=210,y=270)
    Label(f4,text=items[a101][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=450,y=270)
    a20=q30.get()
    print(a20)
    a201=int(a20)
    Label(f4,text=a201*items[a101][1],font=('comic sana ms',13,'bold'),fg='black',bg='gray79').place(x=730,y=270)
    a33='Bill'+q33.get()
    c2='create table if not exists {} (ITEM_NUM int(5),ITEM_NAME varchar(50),RATE_PER_ITEM int(5),QUANTITY  int(10),TOTAL_AMOUNT int(10));'.format(a33,)    #"CUSTOMER TABLE"
    mycur.execute(c2)
    print(c2)
    st1=('insert into {} values ("{}","{}","{}","{}","{}")').format(a33,a101,items[a101][0],items[a101][1],a201,a201*items[a101][1])
    print(st1)
    mycur.execute(st1)
    mycon.commit()



#=================================================================================================
b11=Button(f2,text='submit',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb111).place(x=450,y=58)
b1=Button(f5,text='Save',font=('comic sana ms',18,'bold'),bg='White',fg='black',command=clickb1).place(x=200,y=6)
e1=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e1.place(x=0,y=0)
q1=e1.get()

e2=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e2.place(x=0,y=30)
q2=e2.get()
e3=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e3.place(x=0,y=60)
q3=e3.get()
e4=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e4.place(x=0,y=90)
q4=e4.get()
e5=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e5.place(x=0,y=120)
q5=e5.get()
e6=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e6.place(x=0,y=150)
q6=e6.get()
e7=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e7.place(x=0,y=180)
q7=e7.get()
e8=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e8.place(x=0,y=210)
q8=e8.get()
e9=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e9.place(x=0,y=240)
q9=e9.get()
e10=Entry(f4,width=4,font=('comic sans ms',15),bd=1,bg='gray79')
e10.place(x=0,y=0)
q10=e10.get()
#===================================================================
#item number
q11=StringVar()
e11=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q11)
e11.place(x=57,y=0)
q12=StringVar()
e12=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q12)
e12.place(x=57,y=30)
q13=StringVar()
e13=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q13)
e13.place(x=57,y=60)
q14=StringVar()
e14=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q14)
e14.place(x=57,y=90)
q15=StringVar()
e15=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q15)
e15.place(x=57,y=120)
q16=StringVar()
e16=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q16)
e16.place(x=57,y=150)
q17=StringVar()
e17=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q17)
e17.place(x=57,y=180)
q18=StringVar()
e18=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q18)
e18.place(x=57,y=210)
q19=StringVar()
e19=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q19)
e19.place(x=57,y=240)
q20=StringVar()
e20=Entry(f4,width=6,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q20)
e20.place(x=57,y=270)

#==================================================================
q21=StringVar()
e21=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q21)
e21.place(x=560,y=0)
q22=StringVar()
e22=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q22)
e22.place(x=560,y=30)
q23=StringVar()
e23=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q23)
e23.place(x=560,y=60)
q24=StringVar()
e24=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q24)
e24.place(x=560,y=90)
q25=StringVar()
e25=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q25)
e25.place(x=560,y=120)
q26=StringVar()
e26=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q26)
e26.place(x=560,y=150)
q27=StringVar()
e27=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q27)
e27.place(x=560,y=180)
q28=StringVar()
e28=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q28)
e28.place(x=560,y=210)
q29=StringVar()
e29=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q29)
e29.place(x=560,y=240)
q30=StringVar()
e30=Entry(f4,width=7,font=('comic sans ms',15),bd=1,bg='gray79',textvariable=q30)
e30.place(x=560,y=270)

#=====================================================
q31=StringVar()
e31=Entry(f2,width=30,font=('comic sans ms',10),bd=1,bg='white',textvariable=q31)
e31.place(x=190,y=7)
q32=StringVar()
e32=Entry(f2,width=30,font=('comic sans ms',10),bd=1,bg='white',textvariable=q32)
e32.place(x=190,y=35)
q33=StringVar()
e33=Entry(f2,width=30,font=('comic sans ms',10),bd=1,bg='white',textvariable=q33)
e33.place(x=190,y=63)

#======================================================
q34=StringVar()
e34=Entry(f2,width=10,font=('comic sans ms',10),bd=1,bg='white',textvariable=q34)
e34.place(x=690,y=25)
#=======================================================

b2=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb2).place(x=779,y=0)
b3=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb3).place(x=779,y=30)
b4=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb4).place(x=779,y=60)
b5=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb5).place(x=779,y=90)
b6=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb6).place(x=779,y=120)
b7=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb7).place(x=779,y=150)
b8=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb8).place(x=779,y=180)
b9=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb9).place(x=779,y=210)
b10=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb10).place(x=779,y=240)
b11=Button(f4,text='✔',font=('comic sana ms',8,'bold'),bg='White',fg='black',command=clickb11).place(x=779,y=270)
#=========================================================================


def clickbtot():
    a1000='Bill'+q33.get()
    mycur.execute(" select SUM(TOTAL_AMOUNT) from {}".format(a1000,))
    tot=0
    r1=mycur.fetchone()
    print(r1)

    Label(f6,text=r1,font=('comic sana ms',20,'bold'),fg='white',bg='black').place(x=180,y=30)
btot=Button(f6,text='TOTAL',font=('comic sana ms',20,'bold'),fg='White',bg='black',command=clickbtot).place(x=20,y=20)
root.mainloop()
    
