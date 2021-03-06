from tkinter import *


app = Tk()
# app.configure(background = 'white')
# app.wm_attributes('-transparentcolor', 'white')
# app.attributes('-alpha', 1)

#root.configure(background = 'black')
#root.wm_attributes('-transparentcolor', 'black')
#root.attributes('-alpha', 1)
app.title('linux 78.9')
app.geometry('8000x1300')
app.overrideredirect(1)
# app.attributes('-fullscreen', TRUE)


# for background in range(0, 100):
#     import time
#     app.configure(bg = 'black')
#     time.sleep(0.1)

ipbg = PhotoImage('5085-planets-and-moons-in-universe-hq-image-free-wallpaper.png')

lbgs = Label(image=ipbg)
lbgs.place(x=0, y=0)

g = 'a'


def win(e=''):
    global g
    if g == 'a':
        p.place(x=0, y=0)
        bs.place(x=0, y=930 - 100)
        bs1.place(x=300, y=930 - 100)
        bs100.place(x=0, y=930 - 750)
        bs2.place(x=0, y=0)
        # bs1999555.place(x = 900000, y = 9000)
        g = 'p'
    else:
        p.place(x=9000000, y=900)
        bs.place(x=9000000, y=900)
        bs1.place(x=9000000, y=900)
        bs2.place(x=9000000, y=900)
        bs100.place(x=9000000, y=900)
        bs5.place(x=9000000, y=9000000)
        bs54.place(x=9000000, y=9000000)
        # bs1999555.place(x = 10, y = 10)
        g = 'a'


def func(e):
    global g
    p.place(x=9000000, y=900)
    bs.place(x=9000000, y=900)
    bs1.place(x=9000000, y=900)
    bs2.place(x=9000000, y=900)
    bs100.place(x=9000000, y=900)
    bs5.place(x=9000000, y=9000000)
    bs54.place(x=9000000, y=9000000)
    # bs1999555.place(x = 10, y = 10)
    g = 'a'


def ex(e=''):
    import webbrowser
    webbrowser.open('e.bat')
    exit()


def cm():
    import webbrowser as os
    os.open('cmd.lnk')


# def ch(e):
#     yui = open('dist/cmd/pass.txt')
#     yuir = yui.read()
#     yui.close()
#     ehr = eh.get()
#     if ehr in yuir:
# eh.place(x = 90000000000000000000000, y = 9000000000000000000000000000000000000)
# lpass.place(x = 90000000000000000000000, y = 9000000000000000000000000000000000000)
# else:
#     app.destroy()

kp = open('dist/cmd/im1.txt')
kpr = kp.read()
kp.close()
kp1 = open('dist/cmd/im2.txt')
kpr1 = kp1.read()
kp1.close()

i = PhotoImage(file=kpr)
i2 = PhotoImage(file=kpr1)

cms = PhotoImage(file='sh.png')

u = 'a'


def wallp(e=''):
    global u
    if 'a' in u:
        bs5.place(x=494, y=0)
        bs54.place(x=494, y=50)
        # bs1999555.place(x = 90000000, y = 90900)
        u = 'p'
    else:
        bs5.place(x=9000000, y=9000000)
        bs54.place(x=9000000, y=9000000)
        # bs1999555.place(x = 10, y = 10)
        u = 'a'


def wallp1():
    import webbrowser
    webbrowser.open('%windir%\\System32\\Control.exe')


def restart():
    import webbrowser
    webbrowser.open('lanch.bat')
    exit()


def img2(e=''):
    import webbrowser
    webbrowser.open('im2.jar')
    from tkinter import filedialog
    app.fn1 = filedialog.askopenfilename(filetypes=(('png', '*.png'), ('png', '*.png')))
    yyyyyy = open('im2.txt', 'a')
    yyyyyy.write(app.fn1)
    yyyyyy.close()
    import webbrowser
    webbrowser.open('p.bat')
    exit()
    atp = PhotoImage(file=app.fn1)
    l45['image'] = atp


def img1():
    import webbrowser
    webbrowser.open('im1.jar')
    from tkinter import filedialog
    app.fn = filedialog.askopenfilename(filetypes=(('png', '*.png'), ('png', '*.png')))
    yyyyyy = open('im1.txt', 'a')
    yyyyyy.write(app.fn)
    yyyyyy.close()
    import webbrowser
    webbrowser.open('p.bat')
    exit()
    jk = PhotoImage(file=app.fn)
    l['image'] = jk


l = Label(image=i)
l.place(x=0, y=0)
l5555 = Label(image=i)
l5555.place(x=9000000, y=9000000)
l45 = Label(image=i2)
l45.place(x=1920, y=0)
l1 = Label(bg='black', width=200, pady=50, borderwidth=5).place(x=350, y=950)

p = Label(width=100, pady=494 - 20, border=0, bg='black')
p.place(x=9000000, y=9000)
sh = PhotoImage(file='shu.png')
bs = Button(pady=12, font=('chiller', 50), border=0, bg='black', fg='red', command=ex, text='shutdown')
bs5 = Button(pady=12, border=0, bg='black', fg='red', text='screen 1 image', command=img1)
bs54 = Button(pady=12, border=0, bg='black', fg='red', text='screen 2 image', command=img2)
bs5.place(x=900000, y=900000)
bs54.place(x=900000, y=900000)
bs2 = Button(pady=30, border=0, bg='black', fg='white', command=wallp, padx=30, text='WALLPAPER', font=('Chiller', 50))
bs100 = Button(pady=30, border=0, bg='black', fg='white', command=wallp1, padx=30, text='PC', font=('Chiller', 50))
bs1 = Button(font=('chiller', 50), pady=12, border=0, bg='black', fg='red', text='restart', command=restart)
cms1 = PhotoImage(file='cmd.png')
cms2 = PhotoImage(file='notepad.png')
cms3 = PhotoImage(file='google.png')
cf = PhotoImage(file='pc.png')
cfff = PhotoImage(file='pycharm.png')


def no():
    import webbrowser
    webbrowser.open('notepad.exe')


def nog():
    import webbrowser
    webbrowser.open('google.exe')


def nogg():
    import webbrowser
    webbrowser.open('D:\\3\\linux_python')


def py():
    import webbrowser
    webbrowser.open('"D:\\softwares\\vsc\\Microsoft VS Code\\Code.exe"')


int_puush_1 = 0
int_puush_2 = 0
npo = PhotoImage(file='pycharm.png')


def int_plush_1_2(e=''):
    global int_puush_1, int_puush_2
    int_puush_2 = int_puush_2 + 1

    def op1():
        from tkinter import filedialog
        app.lo = filedialog.askopenfilename(title='open')

    sj = 'a'

    def op():
        import webbrowser
        webbrowser.open(app.lo)

    def op5(e):
       try:
        from pynput.mouse import Controller
        import time
        global sj
        mouse = Controller()
        print('cliked')

        if 'a' in sj:
            # time.sleep(0.3)
            sj = 'b'

        if 'b' in sj:
            sj = 'a'
       except:
           print('err')

    op1()
    pop = Button(image=npo, border=0, width=150, pady=20, command=op)
    pop.grid(row=int_puush_1, column=int_puush_2)
    peo = Label(text=app.lo, width=20)
    peo.grid(row=2, column=int_puush_2)
    pop.bind('<Button-3>', op5)
    peo.bind('<Button-3>', op5)


def cm90():
    import webbrowser
    webbrowser.open('hy.lnk')


def n():
    import webbrowser
    webbrowser.open('"D:\\softwares\\intelle ide\\IntelliJ IDEA Community Edition 2020.1.1\\bin\\idea64.exe"')


inteljid = PhotoImage(file='idea.png')
bs1999 = Button(pady=12, border=0, bg='gray', fg='red', image=cms1, command=cm)
bs1999s = Button(pady=12, border=0, bg='gray', fg='red', image=cms1, command=cm90)
bs19995 = Button(pady=12, border=0, bg='gray', fg='red', image=cms2, command=no)
bs199955 = Button(pady=12, border=0, bg='gray', fg='red', image=cms3, command=nog)
bs1999555 = Button(pady=12, border=0, bg='gray', fg='red', image=cf, command=nogg)
bs19995556 = Button(pady=12, border=0, bg='gray', fg='red', image=inteljid, command=n)
bs199955567 = Button(pady=12, border=0, bg='gray', fg='red', image=cfff, command=py)
bs1999.place(x=400, y=970)
bs19995.place(x=650, y=960)
bs199955.place(x=800, y=960)
bs1999555.place(x=930, y=960)
bs19995556.place(x=1070, y=960)
bs199955567.place(x=1200, y=960)
bs1999s.place(x=1200 + 180, y=960)
# lpass = Label(text = 'ENTER LINUX PASSWORD', bg = 'black', fg = 'blue')
# lpass.place(x = 700, y = 380)
# eh = Entry(width = 100, border = 5, bg = 'white', fg = 'blue')
# eh.place(x = 700, y = 400)

ip = PhotoImage(file='win.png')

b = Button(image=ip, command=win)
b.place(x=0, y=980)

# eh.bind('<Return>', ch)
# p.bind('<Leave>', win)
l.bind('<Button-3>', int_plush_1_2)
l45.bind('<Button-3>', int_plush_1_2)

l.bind('<Button-1>', func)
l45.bind('<Button-1>', func)

app.mainloop()
