from tkinter import *

ches_game = Tk()

ches_game.title('ches')
ches_game.resizable(0, 0)
ches_game.wm_attributes('-transparentcolor', 'white')
ches_game.geometry('300x600+900+300')
ches_game.attributes('-alpha', 0.70)
ches_game.overrideredirect(1)

t = ''


def wates_p(e=''):
    global t
    if t == '':
        html = open('title.txt')
        firk = html.read()
        html.close()
        c78['text'] = firk
        for x__y in range(0, 700):
            html = open('title.txt')
            firk = html.read()
            html.close()
            c78['text'] = firk
            print(x__y)
            import time
            # time.sleep(0.01)

            # l2.place(x = 20, y = x__y)
            # l3.place(x = 20, y = x__y)
            # l4.place(x = 20, y = x__y)
            # l.place(x = 20, y = x__y)
            t = 't'
            ches_game.bind('<Enter>', None)


def d8(e=''):
    c1.place(x=900, y=9800)
    c2.place(x=900, y=9800)
    d.place(x=900, y=9800)
    d1.place(x=900, y=9800)
    # .place(x = 900, y = 9800)
    # c2['text'] = ''
    # d['text'] = ''
    # d1['text'] = ''
    user_name.place(x=30, y=330)
    user_name_ch.place(x=60, y=380)
    gui_s = user_name.get()
    import webbrowser
    webbrowser.open('file_s.jar')
    you = open('title.txt', 'w')
    you.write(gui_s)
    you.close()
    ft = open('title.txt')
    ftr = ft.read()
    ft.close()
    c78['text'] = ftr


def d4(e=''):
    import webbrowser as os
    os.open('pccc.bat')
    exit()


o = ''


def re(e=''):
    global o
    if o == '':
        o = 'p'
        user_name.delete(0, END)


def change(r=''):
    gui_s = user_name.get()
    import webbrowser
    webbrowser.open('file_s.jar')
    ft = open('title.txt', 'a')
    ft.write(gui_s)
    ft.close()
    c78['text'] = gui_s
    l1.place(x=0, y=0)
    l2.place(x=20, y=10)
    l3.place(x=20, y=270)
    l4.place(x=0, y=0)
    l5.place(x=220, y=240)
    l6.place(x=0, y=530)
    user_name.place(x=900000, y=9000)
    user_name_ch.place(x=900000, y=9000)
    c.place(x=60, y=130)
    c1.place(x=110, y=330)
    c2.place(x=20, y=380)
    d.place(x=80, y=460)
    d1.place(x=80 + 80, y=460)


l = Label(bg='#756666', width=500, pady=500).place(x=0, y=0)
l1 = Label(bg='#F4F4F4', width=1, pady=500)
l1.place(x=0, y=0)
l2 = Label(bg='#7A7A7A', border=5, width=37, pady=5550)
l2.place(x=20, y=10)
# l4 = Label(bg='#7A7A7A', border = 5, width = 37, pady = 150).place(x=380, y=10)
l3 = Label(bg='#C1C5C5', width=37, pady=150, border=5)
l4 = Label(bg='#756666', width=10, pady=25)
l5 = Label(bg='#756666', width=10, pady=25)
l6 = Label(bg='#756666', width=10, pady=25)
l3.place(x=20, y=270)
l4.place(x=0, y=0)
l5.place(x=220, y=240)
l6.place(x=0, y=530)

fi = open('title.txt')
fir = fi.read()
fi.close()
c = Label(fg='#C1C5C5', bg='#7A7A7A', text='CHES_PRO78', font=('Chiller', 30))
c78 = Label(fg='#C1C5C5', bg='#7A7A7A', text=fir, font=('Chiller', 30))
c1 = Label(fg='#7A7A7A', bg='#C1C5C5', text='INFO', font=('Chiller', 30))
d = Label(fg='#7A7A7A', bg='#C1C5C5', text='NO', font=('Chiller', 30))
d1 = Label(fg='#7A7A7A', bg='#C1C5C5', text='YES', font=('Chiller', 30))
c78['text'] = fir
c2 = Label(fg='#7A7A7A', bg='#C1C5C5',
           text='do you want to change your username\n ? you can change by click yes\n ok enjoy ches game \nwell come to app',
           font=(3))

user_name = Entry(bg='#C1C5C5', fg='#7A7A7A', width=40)
user_name_ch = Label(bg='#C1C5C5', fg='#7A7A7A', text='CHANGE', font=(25))
user_name.place(x=900000, y=9000)
user_name_ch.place(x=900000, y=9000)

user_name.insert(0, 'username')

c.place(x=60, y=130)
c78.place(x=100, y=20)
c1.place(x=110, y=330)
c2.place(x=20, y=380)
d.place(x=80, y=460)
d1.place(x=80 + 80, y=460)

ches_game.bind('<Enter>', wates_p)
user_name.bind('<Button-1>', re)
d.bind('<Button-1>', d4)
d1.bind('<Button-1>', d8)
user_name_ch.bind('<Button-1>', change)

ches_game.mainloop()
