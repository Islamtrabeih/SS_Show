from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.filedialog import asksaveasfile
import functions, sys, os


def result():
    try:
        txt.delete('0.0', END)
        yy = int(year1.get())
        #print(yy)
        mm = int(month1.get())
        if mm > 12 :
            txt.insert(END, f' \nPlease insert valid month number \n')
        #print(mm)
        dd = int(day1.get())
        if dd > 31 :
            txt.insert(END, f' \nPlease insert valid day number \n')
        #print(dd)
        else:
            x = functions.search(yy, mm, dd)
            #print(x)
            txt.insert(END, f'Number of SSN at {dd}.{mm}.{yy} = {x[1]} SSN \nThe data per day from 01.01.1910 is {x[0][1]}')
    except ValueError:
        txt.insert(END, 'Insert valid numbers')


def show_plot():
    global dd
    yy = int(year1.get())
    #print(yy)
    mm = int(month1.get())
    if mm > 12 :
        txt.insert(END, f'\nPlease insert valid month number \n')
    #print(mm)
    dd = int(day1.get())
    if dd > 31 :
        txt.insert(END, f'\nPlease insert valid day number \n')
    txt.delete('0.0', END)
    d = functions.plot('out', yy, mm, dd)
    dirname = os.path.dirname(__file__)
    dd = PhotoImage(file=f"{dirname}/images/fig1.png")
    #txt.window_create("current", window = Label(txt, image = dd))
    txt.image_create("current", image = dd)


def cycle_view():
    global dd
    i = var_t.get()
    txt2_0.delete('0.0', END)
    txt2_1.delete('0.0', END)
    txt2_2.delete('0.0', END)
    d = functions.cycle_info(i)
    dirname = os.path.dirname(__file__)
    dd = PhotoImage(file=f"{dirname}/images/fig1.png")
    dt = d[1]
    mx = d[2]
    sl = d[3]
    txt2_1.image_create("current", image = dd)
    txt2_2.insert(END, f'The cycle data from {d[4]} to {d[5]} per day is {dt} \n')
    txt2_0.insert(END,
                  f'Start = {d[4]}\nEnd = {d[5]}\n')
    if var_0.get()==True:
        txt2_0.insert(END, f'The maximum SSN = {mx} sunspot\n')
    if var_1.get()==True:
        txt2_0.insert(END, f'The spotless days = {sl} days\n')
    if var_2.get()==True:
        txt2_0.insert(END, f'The cycle duration = {d[6]} years\n')


def pro_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt'),
                                        ('Excel File', '*.xls'),
                                        ('CSV File', '*.csv')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(f'{txt.get(0.0, END)}')
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


# main window
q=ThemedTk(theme = "arc")
q.title('Solar Cycle Prediction')
q.geometry('700x600')

# position
positionRight = int(q.winfo_screenwidth()/4)
positionDown = int(q.winfo_screenheight()/10)
q.geometry("+{}+{}".format(positionRight, positionDown))

q.tk.call("source", "sun-valley/sv.tcl")
#ttk.Style().theme_use('forest-light')
q.tk.call("set_theme", "dark")

# menubar
menu_bar = Menu(q, background='black', foreground='white', activebackground='orange',
                activeforeground='black', relief='flat')
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Restart",  compound='left', command=functions.new, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.add_command(label="Close", compound='left', command=sys.exit, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.bind("<Control-Q>", sys.exit)
menu_bar.add_cascade(label="File", menu=file_menu)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", compound='left', command=functions.help_index, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
help_menu.add_command(label="About...", compound='left', command=functions.about, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
menu_bar.add_cascade(label="Help", menu=help_menu)
q.config(menu=menu_bar)

# tabs
my_notebook=ttk.Notebook(q)
tab1=ttk.Frame(my_notebook)
tab2=ttk.Frame(my_notebook)
my_notebook.add(tab1, text="Data_show")
my_notebook.add(tab2, text="Chart_View")
tab1.grid_columnconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)
tab1.rowconfigure(0, weight=1)
tab2.rowconfigure(0, weight=1)

#----------------tab1-------------------
# frames
my_Frame1 = ttk.LabelFrame(tab1, text="inputs")
my_Frame1.grid(column=0, row=0, columnspan=2, sticky="WE", \
             padx=5, pady=0, ipadx=0, ipady=0)
my_Frame1_1 = ttk.LabelFrame(tab1, text="result")
my_Frame1_1.grid(column=0, row=1, columnspan=2, sticky="WE", \
             padx=5, pady=0, ipadx=0, ipady=0)

# tab1 labels
frame1_day = ttk.Label(my_Frame1,text="Day:",font=(10)).grid(column=0, row=1, padx=20, pady=20)
frame1_month = ttk.Label(my_Frame1,text="Month:",font=(10)).grid(column=2, row=1, padx=20, pady=20)
frame1_year = ttk.Label(my_Frame1,text="Year:",font=(10)).grid(column=4, row=1, padx=20, pady=20)

# tab1 spinbox
day1 = ttk.Spinbox(my_Frame1, from_= 1,to_= 31, width=5)
day1.grid(column=1, row=1, padx=20, pady=20)
year1 =ttk.Spinbox(my_Frame1, from_= 1910,to_= 2030,width=5)
year1.grid(column=5, row=1, padx=20, pady=20)
month1 = ttk.Spinbox(my_Frame1,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=5)
month1.grid(column=3, row=1, padx=20, pady=20)

# tab1 buttons
BTN_frame1 = ttk.Button(my_Frame1,text="Get Data",command=result,width=15).grid(column=0, row=2, columnspan=2, pady=10)
save_frame1 = ttk.Button(my_Frame1,text="Plot",command=show_plot,width=15).grid(column=2, columnspan=2, row=2, pady=10)
plot_frame1 = ttk.Button(my_Frame1,text="Save",command=pro_save,width=15).grid(column=4, row=2, columnspan=2, pady=10)
#frame1_2 = ttk.Label(my_Frame1,text="",font=("arial",30,"bold")).grid(column=0, row=4)
txt = Text(my_Frame1_1, height=18, relief=FLAT)
txt.grid(column=0, columnspan=6, row=0, sticky="WE", padx=15, pady=15)

# weight
for col in range(6):
    my_Frame1.columnconfigure(col, weight=1)
my_Frame1.rowconfigure(5, weight=1)
for col in range(6):
    my_Frame1_1.columnconfigure(col, weight=1)
my_Frame1_1.rowconfigure(3, weight=1)

#----------------tab2-------------------
# frames
my_Frame2 = ttk.LabelFrame(tab2, text="inputs")
my_Frame2.grid(column=0, row=0, columnspan=2, sticky="WE", \
             padx=5, pady=0, ipadx=0, ipady=0)
my_Frame2_1 = ttk.LabelFrame(tab2, text="result")
my_Frame2_1.grid(column=0, row=1, columnspan=2, sticky="WE", \
             padx=5, pady=0, ipadx=0, ipady=0)

# tab1 labels
frame2_l = ttk.Label(my_Frame2,text="Cycle:",font=(10)).grid(column=0, row=0, padx=0, pady=20, ipadx=0, ipady=0)

# tab2 button
var_t = StringVar()
BTN_combox = ttk.Combobox(my_Frame2, textvariable=var_t)
BTN_combox['values'] = [f"cycle{m}" for m in range(15, 26, 1)]
BTN_combox.grid(column=1, row=0, padx=0, pady=20, ipadx=0, ipady=0)
BTN_frame2 = ttk.Button(my_Frame2,text="Get Data",command=cycle_view,width=15).grid(column=2, columnspan=2, row=0, padx=0, pady=20, ipadx=0, ipady=0)
var_0 = BooleanVar()
togglebutton_0 = ttk.Checkbutton(my_Frame2, text='Maximum', variable=var_0, onvalue=1, style="Switch.TCheckbutton")
togglebutton_0.grid(column=0, row=1, padx=0, pady=20, ipadx=0, ipady=0)
var_1 = BooleanVar()
togglebutton_1 = ttk.Checkbutton(my_Frame2, text='Spotless', variable=var_1, onvalue=1, style="Switch.TCheckbutton")
togglebutton_1.grid(column=1, row=1, padx=0, pady=20, ipadx=0, ipady=0)
var_2 = BooleanVar()
togglebutton_2 = ttk.Checkbutton(my_Frame2, text='Duration', variable=var_2, onvalue=1, style="Switch.TCheckbutton")
togglebutton_2.grid(column=2, row=1, padx=0, pady=20, ipadx=0, ipady=0)

# text
txt2_0 = Text(my_Frame2_1, height=10, relief=FLAT)
txt2_0.grid(column=0, row=0, columnspan=4, padx=15, pady=0, ipadx=0, ipady=0, sticky="WE")
txt2_1 = Text(my_Frame2_1, height=10, relief=FLAT)
txt2_1.grid(column=4, row=0, columnspan=2, padx=15, pady=0, ipadx=0, ipady=0, sticky="WE")
txt2_2 = Text(my_Frame2_1, height=6,relief=FLAT)
txt2_2.grid(column=0, columnspan=6, row=1, padx=15, pady=15, ipadx=0, ipady=0, sticky="WE")

# weight
for col in range(3):
    my_Frame2.columnconfigure(col, weight=1)
my_Frame2.rowconfigure(1, weight=1)
for col in range(6):
    my_Frame2_1.columnconfigure(col, weight=1)
my_Frame2_1.rowconfigure(6, weight=1)

# main loop
q.wm_minsize(620, 560)
q.resizable(False, False)
my_notebook.pack(expand=True, fill='both')
#q.state('iconic')
#q.wm_attributes("-transparentcolor", 'white')
q.mainloop()
