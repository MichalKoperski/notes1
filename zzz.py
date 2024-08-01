from rich.console import Console
from rich.table import Table
from rich import print as rprint
import calendar
from datetime import date
from datetime import timedelta
import tkinter

window = tkinter.Tk()

# to rename the title of the window window.title("GUI")
l1 = Label(window, text="edureka!“ font=("Arial Bold", 50))

l1.grid(column=0, row=0)
# pack is used to show the object in the window

label = tkinter.Label(window, text="Hello World!").pack()

window.mainloop()


czynsz = 1264.89
D13 = 91.74
D14 = 91.74
piwnica = 13.97
prąd = 342.47
gaz = 0
upc = 65.96
orange = 83
netflix = 60
wwe = 60
hbo = 20
spotify = 25
youtube = 24
onedrive = 30
amazon = 49
iCloud = 40
polsat = 30
player = 159
tvp = 45
canal = 198
disney = 290
tvn24 = 100

pensja = 7762.45

moneyStart = input("How much cash: ")
if len(moneyStart) == 0:
    moneyStart = -43000
moneyStart = int(moneyStart)
howManyColumns = input("How many columns: ")
if len(howManyColumns) == 0:
    howManyColumns = 6
howManyColumns = int(howManyColumns)

monthNow = date.today().month
yearNow = date.today().year
restMonths = []
columns = []

for month in range(13):
    if month >= monthNow:
        if restMonths.__len__() < howManyColumns:
            restMonths.append(month)

vacations = 42
calList = []
restVacations = []
i = 0
for cal in restMonths:
    calList.append(calendar.TextCalendar(calendar.MONDAY).formatmonth(yearNow, restMonths[i]))
    restVacations.append("       " + str(int(vacations + cal * 26/12)) + " days")
    i += 1

i = 0
while calList.__len__() < howManyColumns:
    calList.append(calendar.TextCalendar(calendar.MONDAY).formatmonth(yearNow + 1, i + 1))
    i += 1

i = 0
if restMonths.__len__() == howManyColumns:
    restMonths.pop(0)
columns.append("       " + str("{:,}".format(moneyStart)))
for money in restMonths:
    if restMonths[i] == 4 or restMonths[i] == 9:
        moneyStart = int(moneyStart + int(1.8*pensja) - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1
    elif restMonths[i] % 2 != 0:
        moneyStart = int(moneyStart + pensja - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat - prąd)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1
    else:
        moneyStart = int(moneyStart + pensja - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat - gaz)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1

while columns.__len__() < howManyColumns:
    i = 1
    if i == 4:
        moneyStart = int(moneyStart + int(
            1.8 * pensja) - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1
    elif i % 2 != 0:
        moneyStart = int(
            moneyStart + pensja - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat - prąd)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1
    else:
        moneyStart = int(
            moneyStart + pensja - czynsz - D13 - D14 - piwnica - upc - orange - netflix - wwe - hbo - spotify - youtube - onedrive - iCloud - polsat - gaz)
        convMoney = "       " + str("{:,}".format(moneyStart))
        columns.append(convMoney)
        i += 1

table = Table(title='--- SAVE MONEY ---', style='yellow', title_style='bold red')

rows = [
    calList,
    restVacations,
]

for column in columns:
    table.add_column(column, style='green')

for row in rows:
    table.add_row(*row, style='green')

Console().print(table)

fertility1 = date.fromisoformat("2021-12-27") + timedelta(days=14)
while fertility1 < date.today():
    fertility1 += timedelta(days=28)
fertility2 = fertility1 + timedelta(days=28)
rprint("Fertility:", fertility1, "", fertility2)



