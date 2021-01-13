try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from datetime import date
from tkcalendar import Calendar

current_date= date.today()
string= "Remain life : "
def amount_dateOfBirth():
    global string
    if(calendar.selection_get()<=current_date):
        _date = date(calendar.selection_get().year, calendar.selection_get().month,calendar.selection_get().day)

        _days_ = current_date-_date
        # suppose each person cal live 100 year  = 100*365days
        _aliveDays= 100*365

        print("current Date : ", current_date)
        print("DoB: ",calendar.selection_get())
        print(_days_.days)
        __remainlife__ =_aliveDays -  _days_.days;
        print("Amount Days in 100years: ", _aliveDays)
        print("Remain Life : ",__remainlife__)
        year = int(__remainlife__/365)
        month = int(__remainlife__%365/30.25)
        day = __remainlife__%365%30
        print (year, month, day)
        text.insert(tk.END, string + ": "+str(int(year))+ " year " + str(int(month)) + " month " + str(day) + " day" + "\n")

    else:
        str1="Invalid date, wrong input date!"
        text.insert(tk.END, str1+ "\n")

root= tk.Tk()
# top= tk.Toplevel(root)
calendar = Calendar(root, font="Arial 12", selectmode='day',
                   cursor="hand1")
calendar.pack(fill="both",expand=True)
ttk.Button(root, text="ok", command=amount_dateOfBirth).pack()
text = tk.Text(root, heigh=10, width=70)
text.pack()

root.mainloop()
