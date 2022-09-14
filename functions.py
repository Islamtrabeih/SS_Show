from tkinter import *
from tkinter import ttk
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys, os


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
    x = [[], []]
    yy, mm, dd = int(yy), int(mm), int(dd)
    rr = int(julian(yy, mm, dd) - julian(1910, 1, 1) + 2)
    if rr < at.index[-1]:
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, 1]))
    elif rr > at.index[-1]:
        print("please input correct date ")
    return x, at.loc[rr,1]


def plot(out, yy, mm, dd):
    at = pd.read_csv('sheet.csv', header = None)
    x = [[], []]
    yy, mm, dd = int(yy), int(mm), int(dd)
    rr = int(julian(yy, mm, dd) - julian(1910, 1, 1) + 2)
    if rr < at.index[-1]:
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, 1]))
    elif rr > at.index[-1]:
        print("please input correct date ")

    title = "SSN Plot"
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': 'SSN number', 'x': 'Date'})
    fig.update_layout(title={'text': title, 'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    # fig.show()
    if not os.path.exists("images"):
        os.mkdir("images")
    return fig.write_image("images/fig1.png", width=600, height=300)


def new():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def help_index():
    os.system('information.pdf')            # هيتغير لأسم ملف الشرح


def about():
    about_win = Toplevel(height=550, width=900)
    about_win.minsize(height=550, width=900)
    about_win.resizable(False, False)

    columns1 = ('#1', '#2', '#3')
    tree1 = ttk.Treeview(about_win, columns=columns1, show='headings')
    tree1.heading('#1', text='Students')
    tree1.heading('#2', text='Sections')
    tree1.heading('#3', text='Email')
    contacts1 = [('------------name', 'Tab[Theoretical(1,2,3,6), Pro(1,2,3,4,5,6)]',
                 '-------------email')]
    for contact in contacts1:
        tree1.insert('', END, values=contact)
    tree1.pack(side=BOTTOM, fill='x')

    columns = ('#1', '#2', '#3')
    tree = ttk.Treeview(about_win, columns=columns, show='headings')
    tree.heading('#1', text='Supervisor')
    tree.heading('#2', text='Orgnization')
    tree.heading('#3', text='Email')
    contacts = [('Kamel Abdelatif Khalil Gadallah', 'Al-Azhar, Faculity of science', 'k.gadallah@azhar.edu.eg'),
                ('Wael Mohamed Mahmoud', 'EgSA', 'wael.mohamed@egsa.gov.eg'),]
    for contact in contacts:
        tree.insert('', END, values=contact)
    tree.pack(side=BOTTOM, fill='both')

    data1 = StringVar()
    data1.set("solar activity \nBy: Al_Azhar University students 2022")
    label_Dir = Message(about_win, textvariable=data1, width=1000)
    lst2 = ('Times New Roman', 13)
    label_Dir.config(font=lst2)
    label_Dir.pack(side=BOTTOM, fill='both')


def cycle_info(cycle):
    c = {"cycle15_start":"1/7/1913","cycle15_end":"1/8/1923","cycle15_duration":11.3,"cycle16_start":"1/8/1923",
         "cycle16_end":"1/9/1933","cycle16_duration":10.1,"cycle17_start":"1/9/1933","cycle17_end":"1/2/1944",
         "cycle17_duration":10.4,"cycle18_start":"1/2/1944","cycle18_end":"1/4/1954","cycle18_duration":10.2,"cycle19_start":"1/4/1954",
         "cycle19_end":"1/10/1964","cycle19_duration":10.5,"cycle20_start":"1/10/1964","cycle20_end":"1/3/1976",
         "cycle20_duration":11.4,"cycle21_start":"1/3/1976","cycle21_end":"1/9/1986","cycle21_duration":10.5,"cycle22_start":"1/9/1986",
         "cycle22_end":"1/8/1996","cycle22_duration":9.9,"cycle23_start":"1/8/1996","cycle23_end":"1/12/2008","cycle23_duration":12.3,
         "cycle24_start":"1/12/2008","cycle24_end":"1/12/2019","cycle24_duration":11.1, "cycle25_start":"1/12/2019",
         "cycle25_end":"1/12/2029","cycle25_duration":11}
    at = pd.read_csv('sheet.csv', header = None)
    x = [[],[]]
    start = datetime.strptime(c[f"{cycle}_start"], "%d/%m/%Y")
    end = datetime.strptime(c[f"{cycle}_end"], "%d/%m/%Y")
    duration = c[f"{cycle}_start"]
    rr0 = int(julian(end.year, end.month, end.day) - julian(1910, 1, 1) + 2)
    rr1 = int(julian(start.year, start.month, start.day) - julian(1910, 1, 1) + 2)
    for i in range(rr1, rr0, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, 1]))
    title = f"{cycle}"
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': 'SSN number', 'x': 'Date'})
    fig.update_layout(title={'text': title, 'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    # fig.show()
    if not os.path.exists("images"):
        os.mkdir("images")
    z = x[1].count(0)
    for i in x[1]:
        if i <= 0 : z += 1
    return fig.write_image("images/fig1.png", width=600, height=300), x[1], max(x[1]), z, start, end, c[f"{cycle}_duration"]
