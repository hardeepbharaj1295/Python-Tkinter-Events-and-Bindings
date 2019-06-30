from tkinter import *
from tkcalendar import DateEntry


class EventsWindow:

    def __init__(self):
        self.win  = Tk()

        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()

        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)

        str1 = "600x500+"+str(x)+ "+" + str(y)

        self.win.geometry(str1)
        self.win.resizable(width=False, height=False)
        self.win.title("Events and Bindings")

    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        self.label = Label(self.frame, text="Events and Bindings")
        self.label.config(font=('Courier', 20, 'bold'))
        self.label.place(x= x +10, y=y+50)

        self.label = Label(self.frame, text='Enter name')
        self.label.config(font=('Courier', 12, 'bold'))
        self.label.place(x = 50, y = y + 130)

        self.name = Entry(self.frame, font='Courier 12')
        self.name.place(x=200, y = y + 130)

        self.name.bind('<KeyRelease>',self.keyup)

        # calendar in tkinter
        self.label = Label(self.frame, text='Select DOB')
        self.label.config(font=('Courier', 12, 'bold'))
        self.label.place(x=50, y=y + 160)

        self.dob = DateEntry(self.frame, font=('Courier', 12, 'bold'), bg='darkblue',
                             fg='white', borderwidth=2, command=self.dates)
        self.dob.place(x=200, y = y + 160)

        #on date change listener
        self.dob.bind('<<DateEntrySelected>>',self.dates)

        # radio buttons
        self.var = StringVar()
        self.label = Label(self.frame, text='Select Gender')
        self.label.config(font=('Courier', 12, 'bold'))
        self.label.place(x=50, y=y + 190)

        self.male = Radiobutton(self.frame, variable=self.var, font='Courier 12',
                                text='Male', value= 'Male', command=self.sel)
        self.male.place(x=200, y = y + 190)

        self.female = Radiobutton(self.frame, variable=self.var, font='Courier 12',
                                text='FeMale', value='FeMale', command=self.sel)
        self.female.place(x=280, y=y + 190)

        # Drop down menu
        OPTIONS = [
            'Jalandhar',
            'Amritsar',
            'Phagwara'
        ]

        self.variable = StringVar(self.win)
        self.variable.set(OPTIONS[0])

        self.label = Label(self.frame, text='Select City')
        self.label.config(font=('Courier', 12, 'bold'))
        self.label.place(x=50, y=y + 220)

        self.city = OptionMenu(self.frame, self.variable, *OPTIONS, command=self.dropdown)
        self.city.place(x = 200, y = y + 220)

        self.win.mainloop()

    def keyup(self, value, *args):
        print(self.name.get())

    def dates(self, value, *args):
        print(self.dob.get_date())

    def sel(self):
        print(self.var.get())

    def dropdown(self, value, *args):
        print(self.variable.get())


if __name__ == "__main__":
    x = EventsWindow()
    x.add_frame()