try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from datetime import date
from tkcalendar import Calendar

current_date= date.today()
string= "Amount date of birth will upcoming : "
def amount_dateOfBirth():
    global string
    if(calendar.selection_get()<=current_date):
        _date = date(current_date.year, calendar.selection_get().month,calendar.selection_get().day)
        _final_date_ = _date-current_date
        print(_final_date_.days)
        if _final_date_.days==0 :
            _final_date_="your birth day is today."
            text.insert(tk.END, string+ ": "+ str(_final_date_)+"\n")
        elif _final_date_.days<30:
            text.insert(tk.END, string + ": " + str(_final_date_)+ "\n")
        else:
            month=_final_date_.days/30
            day=_final_date_.days%30
            text.insert(tk.END, string + ": " + str(int(month)) + " month "+ str(day) +" day"+ "\n")
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
