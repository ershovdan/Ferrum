import requests
import json
import calendar
from datetime import datetime


# =======================================================================================================================
AllMoneyPerMonth_EUR = 0.00
AllMoneyPerMonth = 0.00
AllMoneyPerDay_EUR = 0.00
AllMoneyPerDay = 0.00

def JsonSumClear(AllMoneyType):
    MoneyFile = open('data.json', 'r', encoding='utf-8')
    MoneyFileRead2 = MoneyFile.read()
    MoneyFileRead = json.loads(MoneyFileRead2)
    MoneyFile.close()

    MoneyFileRead['AllMoney'][AllMoneyType] = 0

    g = json.dumps(MoneyFileRead)
    MainFile2 = open('data.json', 'w', encoding='utf-8')
    MainFile2.write(g)
    MainFile2.close()

#=======================================================================================================================
def MainOperation():
    def CreditMounthClear():
        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead2 = MoneyFile.read()
        MoneyFileRead = json.loads(MoneyFileRead2)
        MoneyFile.close()
        j = 0
        for i in MoneyFileRead['CreditMounth']:
            MoneyFileRead['CreditMounth'] = []
            j+=1

        g = json.dumps(MoneyFileRead)

        MainFile2 = open('data.json', 'w', encoding='utf-8')
        MainFile2.write(g)
        MainFile2.close()
    # -----------------------------------------------------------------------------------------------------------------------
    def JsonOperation(Sum):
        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead2 = MoneyFile.read()
        MoneyFileRead = json.loads(MoneyFileRead2)
        MoneyFile.close()
        sum2 = MoneyFileRead['AllMoney']['Sum']
        sum2 += float(Sum)
        MoneyFileRead['AllMoney']['Sum'] = sum2

        g = json.dumps(MoneyFileRead)

        MainFile2 = open('data.json', 'w', encoding='utf-8')
        MainFile2.write(g)
        MainFile2.close()
    # -----------------------------------------------------------------------------------------------------------------------
    def Income():
        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead = MoneyFile.read()
        MoneyFileRead2 = json.loads(MoneyFileRead)
        MoneyFile.close()
        data = MoneyFileRead2['Income']

        for i in data:
            a = i['Sum']
            if i["Periodicity"] == 'day':
                a = 2 * calendar._monthlen(datetime.now().year,datetime.now().month)
            if i["Periodicity"] == 'year':
                a = a / 12
            if i["TaxWith"] == 'without':
                a = int(a) - int(i["Tax"]) * 0.01 * int(a)
            JsonOperation(int(a))

    #----------------------------------------------------------------------------------------------------------------------
    def SimpleExpense():
        MoneyFile = open('data.json', 'r', encoding='utf-8')
        MoneyFileRead = MoneyFile.read()
        MoneyFileRead2 = json.loads(MoneyFileRead)
        MoneyFile.close()
        data = MoneyFileRead2['SimpleExpense']

        for i in data:
            a = int(i['Sum'])
            if i["TaxWith"] == 'without':
                a = a + int(i["Tax"]) * 0.01 * a
            JsonOperation(-a)

    # ----------------------------------------------------------------------------------------------------------------------
    def GetEX():
        response = requests.get('https://api.exchangeratesapi.io/latest')
        data = response.json()
        File = open('s_currency.txt', 'r', encoding='utf-8')
        MainCurrent = File.read()
        File.close()
        ER_MainRead = data['rates'][MainCurrent]
        MainER = ER_MainRead

    # -----------------------------------------------------------------------------------------------------------------------
    def Credit():
        MainFile = open('data.json', 'r', encoding='utf-8')
        MainData = json.load(MainFile)


        def differentiatedCredit(Sum, I_R, Time, AddTime, StartPay, Day):
            dt = datetime.date(datetime.strptime(AddTime, "%Y/%m/%d"))
            dt2 = datetime.date(datetime.now())
            MonthNow2 = dt2.year - dt.year
            MonthNow2 = MonthNow2*12
            MonthNow = dt2.month - dt.month + MonthNow2
            if MonthNow < int(Time) + int(StartPay):
                MonthNow = MonthNow - int(StartPay)
                MonthsLeft = int(Time) - MonthNow
                PerMonthPr = float(I_R) / 12
                PerMonth = int(Sum) / (int(Time))
                a = PerMonth + PerMonthPr * (PerMonth * MonthsLeft) / 100
                a = round(a, 2)
                JsonOperation(-a)
                MainData['CreditMounth'].append({"Day": int(Day), "Sum": int(a)})



        def annuityCredit(Sum, I_R, Time, AddTime, StartPay, Day):
            dt = datetime.date(datetime.strptime(AddTime, "%Y/%m/%d"))
            dt2 = datetime.date(datetime.now())
            MonthNow = dt2.month - dt.month
            if MonthNow < int(Time) + int(StartPay) and MonthNow > int(StartPay):
                PerMonthPr = float(I_R) / 12 / 100
                b = PerMonthPr * ((1 + PerMonthPr) ** int(Time))
                c = ((1 + PerMonthPr) ** int(Time)) - 1
                d = b / c
                a = int(Sum) * d
                JsonOperation(-a)
                MainData['CreditMounth'].append({"Day": int(Day), "Sum": int(a)})


        for i in MainData['Credit']:
            if i['Type'] == 'annuity':
                annuityCredit(i['Sum'], i['I_R'], i['Time'], i['AddTime'], i['StartPay'], i['Day'])
            if i['Type'] == 'differentiated':
                differentiatedCredit(i['Sum'], i['I_R'], i['Time'], i['AddTime'], i['StartPay'], i['Day'])

        MainFile.close()

        MainFile = open('data.json', 'w', encoding='utf-8')
        g = json.dumps(MainData)
        MainFile.write(g)
        MainFile.close()

    JsonSumClear('Sum')
    CreditMounthClear()
    Income()
    GetEX()
    Credit()
    SimpleExpense()


MainOperation()
