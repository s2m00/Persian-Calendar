## This is a Persian calendar for Jalali date.
## این یک تقویم فارسی برای تاریخ جلالی میباشد.
#coding=UTF-*

import DConvert
import datetime

from bidi.algorithm import get_display
import arabic_reshaper

def cPT(txt):   # Convet Persian text
    reshaped_text = arabic_reshaper.reshape(txt)
    return get_display(reshaped_text)

gDate = datetime.datetime.today()
# gDate = datetime.date(1988, 5, 22)
# gDate = datetime.date(2017, 2, 4)

jDate = DConvert.gregorian_to_jalali(gDate.year, gDate.month, gDate.day)

def getDayNumber(n):
    return n == jDate[2]

def DateFormat(f):
    if f=='1': return str(jDate[0]) + "/" + str(jDate[1])  + "/" + str(jDate[2])
    elif f=='2': return str(jDate[0]) + "  " + lstMonthName[jDate[1] - 1] + "  " + str(jDate[2])
    elif f=='3': return str(jDate[0]);
    elif f=='4': return str(jDate[1]);
    else:  return 'error in input!';
        

# Return name of the first day of the month.
def getFirstDayMonthWeekDayName():
    wd = jDate[2] % 7
    wd = wd - (gDate.isoweekday() + 2)

    if wd < 0:
        wd = -wd

    else:
        wd = 7 - wd

    return wd

#Number of days of the month.
def getMonthDays():
    if jDate[1] < 7:
        return 32
    elif jDate[1] < 12:
        return 31
    else:
        if jDate[0] % 4 == 3:
            return 31
        else:
            return 30


from tkinter import *

w = Tk()
strT = "تقویم فارسی"
w.title(strT)
w.minsize(450, 350)
w.maxsize(450, 350)


def about():
    a = Tk()
    a.title("درباره")
    a.minsize(500, 250)
    a.maxsize(500, 250)
    aboutText = cPT(u"""Hello.
    This is a Jalali Calendr fo persian user.
    Thanks for use, and please help me for make better at
     s2m00@yahoo.com

     سلام
     این یک تقویم جلالی(هجری شمسی) برای کاربران فارسی زبان است.
     از اینکه از این برنامه استفاده کردید سپاسگذارم.
     لطفا برای بهبودی برنامه به من کمک کنید.
     s2m00@yahoo.com""")
    Label(a, text=aboutText, padx=20, pady=40).pack()


menu = Menu(w)
w.config(menu=menu)
aboutMenu = Menu(menu)
menu.add_command(label=cPT(u"درباره..."), command=about)


lstMonthName = [cPT(u"فروردین"), cPT(u"اردیبهشت"), cPT(u"خرداد"), cPT(u"تیر"), cPT(u"مرداد"), cPT(u"شهریور"), cPT(u"مهر"), \
               cPT(u"آبان"), cPT(u"آذر"), cPT(u"دی"), cPT(u"بهمن"), cPT(u"اسفند")]
lblFullJDate = Label(w, text=DateFormat('2'), bg="light green", padx=130, pady=20, bd=5, font="Arabic", justify=RIGHT).grid(row=0, column=1, columnspan=5)

lstWeekDaysName = [cPT(u"شنبه"), cPT(u"یکشنبه"), cPT(u"دوشنبه"), cPT(u"سه شنبه"), cPT(u"چارشنبه"), cPT(u"پنجشنبه"), cPT(u"جمعه")]
def printCalendar():
    c = 0
    l=0
    for l in lstWeekDaysName:
        Label(text=l.title(), fg="white", bg="blue", font="arial", padx=20, pady=20, bd=10).grid(row=1, column=c, ipadx=2,
                                                                                                  ipady=2)
        c += 1

    n = 1
    weekName = getFirstDayMonthWeekDayName()
    ft = True
    for n1 in range(2, 8):
        for n2 in range(weekName, 7):
            if getDayNumber(n):
                if n < getMonthDays():
                    Label(w, text=n, bg="dark grey", bd=20, padx=20, pady=20).grid(row=n1, column=n2)
            else:
                if n < getMonthDays():
                    Label(w, text=n, bg="light grey", bd=20, padx=20, pady=20).grid(row=n1, column=n2)
            n += 1
        if ft == True:
            ft = False
            weekName = 0

    for lw in range(0, n):
        w.grid_rowconfigure(lw, weight=1)
        w.grid_columnconfigure(lw, weight=1)

printCalendar()
w.mainloop()
