import tkinter  # imports
import calendar
from tkinter import *
import json
from tkinter import ttk
import tkcalendar
from tkcalendar import *
from datetime import datetime, date, time
from operation import MainOperation as MainOperation

# ===========================================================================================================================
def MainWindow():
    CreditNames = []

    root = Tk()
    canv = Canvas(root, width=800, height=600)
    canv.pack()

    # -------------------------------------------------
    def ViewDataUpdate():
        MainOperation()

        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead2 = MoneyFile.read()
        MoneyFileRead = json.loads(MoneyFileRead2)
        MoneyFile.close()

        a = tkinter.StringVar()
        a.set(round(MoneyFileRead['AllMoney']['Sum'], 2))
        l2 = Label(root, text="This mounth:                                      ", font=30)
        l2.place(x=10, y=10)
        l1 = Label(root, textvariable=a, font=30)
        l1.place(x=100, y=10)

    # -----------------------------------------------------------------------------------------------------------------------
    def MainW():
        root.title("Ferrum")

        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead2 = MoneyFile.read()
        MoneyFileRead = json.loads(MoneyFileRead2)
        MoneyFile.close()

        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        creatmenu = Menu(mainmenu, tearoff=0)
        delmenu = Menu(mainmenu, tearoff=0)
        settingmenu = Menu(mainmenu, tearoff=0)
        gridmenu = Menu(mainmenu, tearoff=0)

        mainmenu.add_cascade(label='Create', menu=creatmenu)
        mainmenu.add_cascade(label='Delete', menu=delmenu)
        mainmenu.add_cascade(label='Settings', menu=settingmenu)
        mainmenu.add_cascade(label='Grids', menu=gridmenu)
        creatmenu.add_command(label='Loan', command=Credit)
        creatmenu.add_command(label='Simple expense', command=SimpleExpense)
        creatmenu.add_command(label='Income', command=Income)
        settingmenu.add_command(label='Currency', command=CurrencySettings)
        delmenu.add_command(label='Loan', command=DelCredit)
        delmenu.add_command(label='Income', command=DelIncome)
        delmenu.add_command(label='Simple expense', command=DelSimpleExpense)
        gridmenu.add_command(label='Main Grid', command=MainGrid)

        ViewDataUpdate()

    # ------------------------------------------------------------------------------------------------------------------------

    def SimpleExpense():
        rootExpense = Tk()
        canvExpense = Canvas(rootExpense, width=600, height=360)
        canvExpense.pack()

        def assignment():
            flag = True
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                temp = data2["SimpleExpense"]
                if temp != []:
                    for i in temp:
                        try:
                            if str(NameEntry.get()) == i['Name']:
                                flag = False
                        except KeyError:
                            temp = data2["SimpleExpense"]
            try:
                b = float(SumEntry.get())
            except ValueError:
                flag = False

            for k in CreditNames:
                if NameEntry.get() == k:
                    flag = False
            if flag != False:
                with open('data.json', 'r', encoding='utf-8') as file:
                    data2 = json.load(file)
                    temp = data2["SimpleExpense"]
                    y = {"Name": NameEntry.get(),
                         "Sum": SumEntry.get(),
                         "AddTime": cal1.get_date(),
                         "TaxWith": TaxEntry.get(),
                         "Day": DayEntry.get()}
                    temp.append(y)
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data2, f, indent=4)
                rootExpense.destroy()
                MainOperation()
                ViewDataUpdate()
            else:
                b1.destroy()
                MainOperation()
                l6 = Label(rootExpense, text='ERROR!')
                l6.place(x=80, y=320)
                b2 = Button(rootExpense, text='OK', command=rootExpense.destroy)
                b2.place(x=250, y=320)
                b2.pack()


        NameEntry = Entry(rootExpense)
        NameEntry.place(x=150, y=20)
        SumEntry = Entry(rootExpense)
        SumEntry.place(x=150, y=70)
        DayEntry = Entry(rootExpense)
        DayEntry.place(x=150, y=170)
        TaxEntry = Entry(rootExpense)
        TaxEntry.place(x=150, y=270)

        cal1 = Calendar(rootExpense, selectmode='day', date_pattern='Y/mm/dd')
        cal1.place(x=300, y=120)

        var = tkinter.StringVar(rootExpense)
        r1 = Radiobutton(rootExpense, text="With", variable=var, value='with')
        r1.place(x=150, y=220)
        r2 = Radiobutton(rootExpense, text="Without", variable=var, value='without')
        r2.place(x=220, y=220)

        l1 = Label(rootExpense, text='Name')
        l1.place(x=10, y=20)
        l3 = Label(rootExpense, text='Sum')
        l3.place(x=10, y=70)
        l7 = Label(rootExpense, text='Date of create -------------------------------->')
        l7.place(x=10, y=120)
        l9 = Label(rootExpense, text='Date of pay(DD)')
        l9.place(x=10, y=170)
        l9 = Label(rootExpense, text='With or without tax')
        l9.place(x=10, y=220)
        l10 = Label(rootExpense, text='Tax')
        l10.place(x=10, y=270)

        b1 = Button(rootExpense, text='OK', command=assignment)
        b1.place(x=250, y=320)

        MainOperation()

        rootExpense.mainloop()

    # ------------------------------------------------------------------------------------------------------------------------
    def DelSimpleExpense():
        rootDel = Tk()
        canvDel = Canvas(rootDel, width=500, height=150)
        canvDel.pack()

        DelEntry = Entry(rootDel, width=50)
        DelEntry.place(x=150, y=60)

        def destroy():
            rootDel.destroy()

        def assignment():
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                MainCounter = 0
                MainCounter2 = 0
                for i in data2['SimpleExpense']:
                    MainCounter2 += 1
                    if i['Name'] == DelEntry.get():
                        data2['SimpleExpense'].remove(i)
                    else:
                        MainCounter += 1
                if MainCounter == MainCounter2:
                    l2 = Label(rootDel, text='ERROR')
                    l2.place(x=30, y=100)
                    b1.destroy()
                    b2 = Button(rootDel, text='OK', command=destroy)
                    b2.place(x=200, y=100)
                    MainOperation()
                else:
                    rootDel.destroy()
                    MainOperation()
                    ViewDataUpdate()

                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data2, f)

        l1 = Label(rootDel, text='Name')
        l1.place(x=30, y=57)

        b1 = Button(rootDel, text='OK', command=assignment)
        b1.place(x=200, y=100)

        MainOperation()

    # -------------------------------------------------------------------------------------------------------------------
    def Credit():
        rootCredit = Tk()
        canvCredit = Canvas(rootCredit, width=600, height=600)
        canvCredit.pack()

        def assignment():
            flag = True
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                temp = data2["Credit"]
                if temp != []:
                    for i in temp:
                        if str(NameEntry.get()) == i['Name']:
                            flag = False
            try:
                a = float(TimeEntry.get())
                b = float(SumEntry.get())
                c = float(I_REntry.get())
            except ValueError:
                flag = False

            for k in CreditNames:
                if NameEntry.get() == k:
                    flag = False
            if flag != False:
                with open('data.json', 'r', encoding='utf-8') as file:
                    data2 = json.load(file)
                    temp = data2["Credit"]
                    y = {"Name": NameEntry.get(),
                         "Time": TimeEntry.get(),
                         "Sum": SumEntry.get(),
                         "I_R": I_REntry.get(),
                         "AddTime": cal1.get_date(),
                         "Day": DayEntry.get(),
                         "Type": var.get(),
                         "StartPay": StartEntry.get()}
                    temp.append(y)
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data2, f, indent=4)
                ViewDataUpdate()
                rootCredit.destroy()

            else:
                b1.destroy()
                MainOperation()
                l6 = Label(rootCredit, text='ERROR!')
                l6.place(x=80, y=420)
                b2 = Button(rootCredit, text='OK', command=rootCredit.destroy)
                b2.place(x=250, y=420)
                b2.pack()

        NameEntry = Entry(rootCredit)
        NameEntry.place(x=150, y=20)
        TimeEntry = Entry(rootCredit)
        TimeEntry.place(x=150, y=70)
        SumEntry = Entry(rootCredit)
        SumEntry.place(x=150, y=120)
        I_REntry = Entry(rootCredit)
        I_REntry.place(x=150, y=170)
        DayEntry = Entry(rootCredit)
        DayEntry.place(x=150, y=270)
        StartEntry = Entry(rootCredit)
        StartEntry.place(x=150, y=370)

        cal1 = Calendar(rootCredit, selectmode='day', date_pattern='Y/mm/dd')
        cal1.place(x=300, y=220)

        var = tkinter.StringVar(rootCredit)
        r1 = Radiobutton(rootCredit, text="Differentiated", variable=var, value='differentiated')
        r1.place(x=150, y=320)
        r2 = Radiobutton(rootCredit, text="Annuity", variable=var, value='annuity')
        r2.place(x=220, y=320)

        l1 = Label(rootCredit, text='Name')
        l1.place(x=10, y=20)
        l2 = Label(rootCredit, text='Time')
        l2.place(x=10, y=70)
        l3 = Label(rootCredit, text='Sum')
        l3.place(x=10, y=120)
        l4 = Label(rootCredit, text='Interest rate')
        l4.place(x=10, y=170)
        l5 = Label(rootCredit, text='%')
        l5.place(x=300, y=170)
        l6 = Label(rootCredit, text='Month')
        l6.place(x=285, y=70)
        l7 = Label(rootCredit, text='Date of create -------------------------------->')
        l7.place(x=10, y=220)
        l9 = Label(rootCredit, text='Date of pay(DD)')
        l9.place(x=10, y=270)
        l9 = Label(rootCredit, text='Type')
        l9.place(x=10, y=320)
        l10 = Label(rootCredit, text='Start pay after x month')
        l10.place(x=10, y=370)

        b1 = Button(rootCredit, text='OK', command=assignment)
        b1.place(x=250, y=420)

        rootCredit.mainloop()
        MainOperation()

    # -------------------------------------------------------------------------------------------------------------------
    def DelCredit():
        rootDel = Tk()
        canvDel = Canvas(rootDel, width=500, height=150)
        canvDel.pack()

        DelEntry = Entry(rootDel, width=50)
        DelEntry.place(x=150, y=60)

        def destroy():
            rootDel.destroy()

        def assignment():
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                MainCounter = 0
                MainCounter2 = 0
                for i in data2['Credit']:
                    MainCounter2 += 1
                    if i['Name'] == DelEntry.get():
                        data2['Credit'].remove(i)
                    else:
                        MainCounter += 1
                if MainCounter == MainCounter2:
                    l2 = Label(rootDel, text='ERROR')
                    l2.place(x=30, y=100)
                    b1.destroy()
                    b2 = Button(rootDel, text='OK', command=destroy)
                    b2.place(x=200, y=100)
                else:
                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data2, f)
                    ViewDataUpdate()
                    rootDel.destroy()

        l1 = Label(rootDel, text='Name')
        l1.place(x=30, y=57)

        b1 = Button(rootDel, text='OK', command=assignment)
        b1.place(x=200, y=100)

        MainOperation()

    # ------------------------------------------------------------------------------------------------------------------
    def DelIncome():
        rootDel = Tk()
        canvDel = Canvas(rootDel, width=500, height=150)
        canvDel.pack()

        DelEntry = Entry(rootDel, width=50)
        DelEntry.place(x=150, y=60)

        def destroy():
            rootDel.destroy()

        def assignment():
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                MainCounter = 0
                MainCounter2 = 0
                for i in data2['Income']:
                    MainCounter2 += 1
                    if i['Name'] == DelEntry.get():
                        data2['Income'].remove(i)
                    else:
                        MainCounter += 1
                if MainCounter == MainCounter2:
                    l2 = Label(rootDel, text='ERROR')
                    l2.place(x=30, y=100)
                    b1.destroy()
                    b2 = Button(rootDel, text='OK', command=destroy)
                    b2.place(x=200, y=100)
                    MainOperation()
                else:
                    rootDel.destroy()
                    MainOperation()
                    ViewDataUpdate()

                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data2, f)

        l1 = Label(rootDel, text='Name')
        l1.place(x=30, y=57)

        b1 = Button(rootDel, text='OK', command=assignment)
        b1.place(x=200, y=100)

        MainOperation()

    # ------------------------------------------------------------------------------------------------------------------
    def Income():
        rootIncome = Tk()
        canvIncome = Canvas(rootIncome, width=600, height=420)
        canvIncome.pack()

        var = tkinter.StringVar(rootIncome)
        r1 = Radiobutton(rootIncome, text="With", variable=var, value='with')
        r1.place(x=150, y=220)
        r2 = Radiobutton(rootIncome, text="Without", variable=var, value='without')
        r2.place(x=200, y=220)

        var2 = tkinter.StringVar(rootIncome)
        r3 = Radiobutton(rootIncome, text="Day", variable=var2, value='day')
        r3.place(x=150, y=270)
        r3 = Radiobutton(rootIncome, text="Mounth", variable=var2, value='mounth')
        r3.place(x=230, y=270)
        # r4 = Radiobutton(rootIncome, text="Year", variable=var2, value='year')
        # r4.place(x=310, y=270)

        def assignment():
            flag = True
            with open('data.json', 'r', encoding='utf-8') as file:
                data2 = json.load(file)
                temp = data2["Income"]
                if temp != []:
                    for i in temp:
                        if str(NameEntry.get()) == i['Name']:
                            flag = False
            try:
                a = float(TimeEntry.get())
                b = float(SumEntry.get())
                c = float(TaxEntry.get())
            except ValueError:
                flag = False

            if flag != False:
                with open('data.json', 'r', encoding='utf-8') as file:
                    data2 = json.load(file)
                    temp = data2["Income"]
                    y = {"Name": NameEntry.get(),
                         "Time": TimeEntry.get(),
                         "Sum": SumEntry.get(),
                         "AddTime": TimeEntry.get(),
                         "Tax": TaxEntry.get(),
                         "TaxWith": var.get(),
                         "Periodicity": var2.get(),
                         "Day": DatePayEntry.get()}
                    temp.append(y)
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data2, f, indent=4)
                rootIncome.destroy()
                MainOperation()
                ViewDataUpdate()
            else:
                b1.destroy()
                l6 = Label(rootIncome, text='ERROR!')
                l6.place(x=80, y=370)
                b2 = Button(rootIncome, text='OK', command=rootIncome.destroy)
                b2.place(x=250, y=370)
                b2.pack()

        NameEntry = Entry(rootIncome)
        NameEntry.place(x=150, y=20)
        TimeEntry = Entry(rootIncome)
        TimeEntry.place(x=150, y=70)
        SumEntry = Entry(rootIncome)
        SumEntry.place(x=150, y=120)
        TaxEntry = Entry(rootIncome)
        TaxEntry.place(x=150, y=170)
        DatePayEntry = Entry(rootIncome)
        DatePayEntry.place(x=150, y=320)

        l1 = Label(rootIncome, text='Name')
        l1.place(x=10, y=20)
        l2 = Label(rootIncome, text='Add time')
        l2.place(x=10, y=70)
        l3 = Label(rootIncome, text='Sum')
        l3.place(x=10, y=120)
        l4 = Label(rootIncome, text='Tax')
        l4.place(x=10, y=170)
        l4 = Label(rootIncome, text='%')
        l4.place(x=290, y=170)
        l5 = Label(rootIncome, text='With or without tax')
        l5.place(x=10, y=220)
        l5 = Label(rootIncome, text='Periodicity')
        l5.place(x=10, y=270)
        l5 = Label(rootIncome, text='Day of pay')
        l5.place(x=10, y=320)

        b1 = Button(rootIncome, text='OK', command=assignment)
        b1.place(x=250, y=370)

        rootIncome.mainloop()

        MainOperation()

    # -------------------------------------------------------------------------------------------------------------------
    def CurrencySettings():
        MainFile = open('exchange_rates.txt', 'r', encoding='utf-8')
        MainData = MainFile.read()
        MainFile.close()

        names = ['RUB', 'USD', 'EUR']

        def assignment():
            MainName = ''
            MainFile = open('s_currency.txt', 'w', encoding='utf-8')
            MainName = NameEntry.get()
            MainName2 = MainName.upper()
            k = 0
            for i in names:
                if MainName2 != i:
                    k += 1
                else:
                    MainFile.write(MainName2)
                    rootCS.destroy()
            MainFile.close()
            if k == 3:
                b1.destroy()
                b2 = Button(rootCS, text='OK', command=rootCS.destroy)
                b2.place(x=200, y=120)
                l1 = Label(rootCS, text='ERROR!')
                l1.place(x=120, y=120)

        rootCS = Tk()
        canvCS = Canvas(rootCS, width=500, height=150)
        canvCS.pack()

        l2 = Label(rootCS, text='Name(RUB, USD or EUR)')
        l2.place(x=10, y=60)

        NameEntry = Entry(rootCS, width=15)
        NameEntry.place(x=190, y=60)

        b1 = Button(rootCS, text='OK', command=assignment)
        b1.place(x=200, y=120)

        MainOperation()

    # -------------------------------------------------------------------------------------------------------------------
    def MainGrid():
        MounthDays = calendar._monthlen(datetime.now().year, datetime.now().month)
        MaxDay = 0

        rootGrid = Tk()
        canvGrid = Canvas(rootGrid, width=MounthDays * 50, height=360)
        canvGrid.place(x=0, y=0)

        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead = json.loads(MoneyFile.read())
        MoneyFile.close()

        DaysDict = {}
        DaysDict2 = {}
        for i in range(MounthDays + 1):
            DaysDict.update({str(i): 0})
            DaysDict2.update({str(i): []})

        trash = 0

        for i in MoneyFileRead:
            for j in MoneyFileRead[i]:
                try:
                    DaysDict[str(j['Day'])] += 1
                    if i == 'Credit':
                        for k in MoneyFileRead['CreditMounth']:
                            DaysDict2[str(k['Day'])].append(str('-' + str(k['Sum'])))

                    elif i == 'SimpleExpense':
                        DaysDict2[j['Day']].append(str('-' + j['Sum']))
                    elif i == 'Income' and j['Periodicity'] == 'day':
                        if j['Periodicity'] == 'day':
                            for k in DaysDict2:
                                DaysDict2[k].append(j['Sum'])
                    elif i == 'Income':
                        if j['TaxWith'] == 'without':
                            DaysDict2[j['Day']].append(int(int(j['Sum']) - int(j['Tax']) * 0.01 * int(j['Sum'])))
                    # else:
                    #     DaysDict2[j['Day']].append(str(j['Sum']))
                except TypeError:
                    trash += 1

        for i in DaysDict:
            if DaysDict[i] > MaxDay:
                MaxDay = DaysDict[i]
        # print(DaysDict2)

        NumberOfItems = 0

        def GridItem(Color, Width, Height, NumberX, NumberY, Text):
            Name = str(NumberOfItems) + 'item'
            Name = Label(rootGrid, height=Height, width=Width, bg=Color, text=Text)
            Name.grid(row=NumberY, column=NumberX)

        for i in range(2 * MounthDays - 1):
            if i % 2 == 0:
                GridItem('Grey', 6, 2, i, 0, str(int((i + 1) / 2 + 0.5)))
            if i % 2 != 0:
                GridItem('Black', 1, 2, i, 0, '')

        MaxLine = 0

        for i in range(MaxDay * 2):
            MaxLine += 1
            for j in range(2 * MounthDays - 1):
                if (i + 1) % 2 == 0:
                    if (j % 2) == 0:
                        a = ''
                        b = ''
                        trueJ = int((j + 1) / 2 + 0.5)
                        trueI = int((i + 1) / 2 + 0.5)
                        if trueJ <= MounthDays:
                            l = 0
                            for k in DaysDict2[str(trueJ)]:
                                l += 1
                            if trueI <= l:
                                a = DaysDict2[str(trueJ)]
                                b = a[trueI - 1]
                        GridItem('White', 6, 2, j, i + 1, b)
                    else:
                        GridItem('Black', 1, 2, j, i + 1, '')
                if (i + 1) % 2 != 0:
                    if (j % 2) == 0:
                        GridItem('Black', 6, 1, j, i + 1, '')
                    else:
                        GridItem('Black', 1, 1, j, i + 1, '')

        for i in range(2 * MounthDays - 1):
            if i % 2 == 0:
                GridItem('Black', 6, 2, i, MaxLine + 1, '')
            if i % 2 != 0:
                GridItem('Black', 1, 2, i, MaxLine + 1, '')

        DaysDict3 = DaysDict2

        for i in DaysDict2:
            a = 0
            for j in DaysDict2[i]:
                a += int(j)
            DaysDict3[i] = a

        for i in range(2 * MounthDays - 1):
            if i % 2 == 0:
                TrueI = int(i / 2 + 0.5 + 1)
                # print(DaysDict3[str(TrueI)])
                GridItem('White', 6, 2, i, MaxLine + 2, DaysDict3[str(TrueI)])
            if i % 2 != 0:
                GridItem('Black', 1, 2, i, MaxLine + 2, '')

        rootGrid.mainloop()

    # ===================================================================================================================
    MainW()

    root.mainloop()
