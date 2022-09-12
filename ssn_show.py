from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import pandas as pd
import plotly.express as px
from datetime import datetime


def julian(year, month, day):
    ''' julian date function '''
    if month < 2 :
        year = year - 1
        month = month + 12
    if year > 1582 :
        a = int(year/100)
        b = 2 - a + int(a/4)
    elif month <= 10:
        if day <= 15:
            b = 0
        else:
            a = int(year/100)
            b = 2 - a + int(a/4)
    if year < 0 :
        c = int((365.25 * year) - 0.75)
    else : c = int(365.25 * year)
    d = int(30.6001 * (month + 1))
    j_date =  b + c + d + day + 1720994.5
    return j_date


def search(yy, mm, dd):
    at = pd.read_csv('sheet.csv', header = None)
    # x = [[], []]
    yy, mm, dd = int(yy), int(mm), int(dd)
    rr = int(julian(yy, mm, dd) - julian(1910, 1, 1) + 2)
    if rr < at.index[-1]:
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, 1]))
    elif rr > at.index[-1]:
        print("please input correct date ")
    return x, at.loc[rr,1]


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
            x = search(yy, mm, dd)
            #print(x)
            txt.insert(END, f' \nvariation of a = {x[1]} SSN \n')
    except ValueError:
        txt.insert(END, 'Insert valid numbers')


def plot(out, x):
    title = "SSN Plot"
    # x = [[], []]              # date / data
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': 'SSN number', 'x': 'Date'})
    fig.update_layout(title={'text': title, 'y': 0.06, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    #if out == 'html':
        #newfig = fig.to_html(include_plotlyjs='cdn', config=config)
        #return newfig
    #elif out == 'instant':
        #fig.show(config=config)
    #elif out == 'png':
        #if not os.path.exists("images"):
            #os.mkdir("images")
    return fig.write_image("images/fig1.png")


def show_plot():
    txt.delete('0.0', END)
    dd = plot('out', x)
    txt.image_create("current", image = dd)


lst = [ "Solar Flare","SSN","All"]
x = [[], []]
q=ThemedTk(theme = "arc")
q.title('Solar Cycle Prediction')
q.geometry('700x600')

positionRight = int(q.winfo_screenwidth()/4)
positionDown = int(q.winfo_screenheight()/10)
q.geometry("+{}+{}".format(positionRight, positionDown))

my_notebook=ttk.Notebook(q)
my_Frame1=ttk.Frame(my_notebook, relief="solid")
my_Frame2=ttk.Frame(my_notebook, relief="solid")
my_notebook.add(my_Frame1,text="Data_show")
my_notebook.add(my_Frame2,text="Chart_View")
my_Frame1.grid_columnconfigure(0, weight=1)
my_Frame2.grid_rowconfigure(0, weight=1)

#photo4 = PhotoImage(file="/home/islam/Downloads/0.png")
#photo1 = PhotoImage(file="/home/islam/Downloads/0.png")
#panel4= Label(my_Frame1, image= photo4)
#panel4.place(x=0,y=0)

frame1_0 = ttk.Label(my_Frame1,text="",font=("arial",30,"bold")).grid(column=0, row=0)
frame1_day = ttk.Label(my_Frame1,text="Day",font=(15)).grid(column=0, row=1)
frame1_month = ttk.Label(my_Frame1,text="Month",font=(15)).grid(column=2, row=1)
frame1_year = ttk.Label(my_Frame1,text="Year",font=(15)).grid(column=4, row=1)
frame1_1 = ttk.Label(my_Frame1,text="",font=("arial",30,"bold")).grid(column=0, row=2)

day1 = ttk.Spinbox(my_Frame1, from_= 1,to_= 31, width=8)
day1.grid(column=1, row=1)
year1 =ttk.Spinbox(my_Frame1, from_= 1910,to_= 2030,width=8)
year1.grid(column=5, row=1)
month1 = ttk.Spinbox(my_Frame1,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=8)
month1.grid(column=3, row=1)

BTN_frame1 = ttk.Button(my_Frame1,text="Get Data",command=result,width=8).grid(column=1, row=3)
save_frame1 = ttk.Button(my_Frame1,text="Plot",command=show_plot,width=16).grid(column=2, columnspan=2, row=3)
plot_frame1 = ttk.Button(my_Frame1,text="Save",command=result,width=8).grid(column=4, row=3)
frame1_2 = ttk.Label(my_Frame1,text="",font=("arial",30,"bold")).grid(column=0, row=4)
txt = Text(my_Frame1, height=18)
txt.grid(column=0, columnspan=6, row=5)

for col in range(6):
    my_Frame1.columnconfigure(col, weight=1)
my_Frame1.rowconfigure(15, weight=1)
q.wm_minsize(625, 567)
q.resizable(True, True)
my_notebook.pack(expand=True, fill='both')
#q.state('iconic')
#q.wm_attributes("-transparentcolor", 'white')
q.mainloop()
