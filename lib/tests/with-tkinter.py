# Copied from http://geometry.karazin.ua/resources/documents/20161225173818_3231ade03.pdf.
# (Конспект Доли П. Г., с. 39-45)
# (Was a little edited then.)


from tkinter import *


def fromCheckToLabel(): # реакция на выбор флажка
 if var1.get()==1:
  lblRez['text']='Флажок выбран'
 else:
  lblRez['text']='Флажок не выбран'

def fromRadioToLabel(): # реакция на выбор элемента из группы
 lblRez['text']='Выбрана кнопка '+str(vr.get())

def fromListToLabel(): # реакция на выбор из списка
 lblRez['text']=lstBox.get(lstBox.curselection())
# =====================================================
root=Tk()
root.title('Demo controls')
pw = PanedWindow(root, sashwidth=3,sashrelief=SUNKEN,
orient=VERTICAL, width = 316)
pw.pack(fill="both", expand="yes")

# ============ строка виджетов 1 (Флажок )==================
lf1=LabelFrame(pw,text=' Флажок ',borderwidth=2,
relief=SUNKEN, height=50)
pw.add(lf1)
var1=IntVar()
check1=Checkbutton(lf1,text='Проверка выбора',variable=var1,
onvalue=1,offvalue=0, command=fromCheckToLabel)
var1.set(1)
check1.place(x = 108, y = 4, width = 140, height=20)
btnCopyChk1=Button(lf1, command=fromCheckToLabel, bitmap="info")
btnCopyChk1.place(x = 268, y = 2, width = 28, height=28)

# ============ строка виджетов 2 (Радиокнопки) ================
lf2=LabelFrame(pw,text=' Кнопки выбора ',borderwidth=2,
relief=SUNKEN,height=54)
pw.add(lf2)
lblTxt2=Label(lf2,font='Arial 10',width=12,text='Выберите номер')
lblTxt2.place(x = 4, y = 4, width = 100, height=20)
frmRadio = Frame(lf2,bg = 'lightgray',relief=GROOVE,borderwidth=4)
frmRadio.place(x = 120, y = 0, width = 120, height=34)
vr=IntVar()
rb1=Radiobutton(frmRadio,text='1',variable=vr,value=1,
command=fromRadioToLabel)
rb2=Radiobutton(frmRadio,text='2',variable=vr,value=2,
command=fromRadioToLabel)
rb3=Radiobutton(frmRadio,text='3',variable=vr,value=3,
command=fromRadioToLabel)
rb1.pack(side = 'left')
rb2.pack(side = 'left')
rb3.pack(side = 'left')
vr.set(1)
btnCopyRadio=Button(lf2,bitmap="info",command=fromRadioToLabel,)
btnCopyRadio.place(x = 268, y = 4, width = 28, height=28)

# ============ строка виджетов 3 (Список) ================
lfList=LabelFrame(pw,text=' Список ',borderwidth=2,relief=SUNKEN, height=70)
pw.add(lfList)
lblTxtList=Label(lfList,font='Arial 10',width=12,text='Выберите фрукт')
lblTxtList.place(x = 4, y = 4, width = 100, height=20)
lstBox=Listbox(lfList,height=3,width=19,selectmode=SINGLE, borderwidth=3)
lst=["Яблоко","Груша","Слива"]
for elem in lst:
 lstBox.insert(END,elem)
lstBox.selection_set(first=0) # выделяем нулевой элемент списка
lstBox.place(x = 120, y = 1)
fromListToLabel2=lambda ev:\
lblRez.configure(text=lstBox.get(lstBox.curselection()))
lstBox.bind("<<ListboxSelect>>", fromListToLabel2)
btnCopyList=Button(lfList, bitmap="info",command=fromListToLabel)
btnCopyList.place(x = 268, y = 4, width = 28, height=28)

# ============ строка виджетов 4 (Шкала) =================
lfScale=LabelFrame(pw,text=' Ползунок ',borderwidth=2,
relief=SUNKEN, height=80)
pw.add(lfScale)
scl = Scale(lfScale,orient=HORIZONTAL,length=236,from_=0,to=100,
tickinterval=10,resolution=1, relief=SUNKEN)
scl.set(50)
scl.place(x = 4, y = 1)
getScaleMoveValue=lambda pos : lblRez.configure(text=pos)
scl['command']=getScaleMoveValue
getScaleValue=lambda : lblRez.configure(text=scl.get())
btnCopyScale=Button(lfScale, bitmap="info",command=getScaleValue)
btnCopyScale.place(x = 268, y = 4, width = 28, height=28)

# ================ полоса виджетов 5 (счетчик)===============
lfSpin=LabelFrame(pw,text=' Счетчик ',borderwidth=2,
relief=SUNKEN, height=54)
pw.add(lfSpin)
lblTxtSpin=Label(lfSpin,font='Arial 10',width=12,
text='Выберите число')
lblTxtSpin.place(x = 4, y = 4, width = 100, height=20)
spb = Spinbox(lfSpin, from_=0, to=10, width=16,
borderwidth=4, font='Arial 10')
spb.place(x = 180, y = 0, width = 60, height=30)
getSpbValue=lambda:lblRez.configure(text=spb.get())
spb['command']=getSpbValue
btnCopySpb=Button(lfSpin, bitmap="info",command=getSpbValue )
btnCopySpb.place(x = 268, y = 4, width = 28, height=28)

# ============ полоса результирующих виджетов ================
lfRez=LabelFrame(pw,text=' Проверка работы виджетов ',
borderwidth=2,relief=SUNKEN, height=54)
pw.add(lfRez)
lblTxtRez=Label(lfRez,text=' Выбор ',font='Arial 10')
lblTxtRez.place(x = 4, y = 4, width = 80, height=20)
lblRez=Label(lfRez,font='Arial 10',bg='white',relief=SUNKEN)
lblRez.place(x = 80, y = 4, width = 160, height=24)
btnQuit = Button(lfRez, text=" Конец ", command=root.destroy)
btnQuit.place(x = 250, y = 4, width = 46, height=28)

# Завершается код примера командами, подключающими процедуры
# тестирования виджетов к комбинациям клавиш клавиатуры. Последняя
# инструкция программы запускает цикл обработки сообщений
# ================= комбинации клавиш =======================
root.bind('<Control-c>', lambda ev: fromCheckToLabel())
root.bind('<Control-r>', lambda ev: fromRadioToLabel())
root.bind('<Control-l>', lambda ev: fromListToLabel())
root.bind('<Control-s>', lambda ev: getScaleValue())
root.bind('<Alt-c>', lambda ev: getSpbValue())
root.bind('<Control-z>', lambda ev: root.destroy())
root.mainloop()
