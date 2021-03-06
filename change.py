gh = open('D:\\3\\linux_python\\dist\\cmd\\pass.txt')
ghr = gh.read()
gh.close()
j = input('password>')
if ghr in j:
    import webbrowser

    webbrowser.open('D:\\3\\linux_python\\cccc.jar')
    i = input('change name to ?>')
    i1 = input('change fullname to ?>')
    i2 = input('change password to ?>')

    f = open('D:\\3\\linux_python\\dist\\cmd\\name.txt', 'w')
    f1 = open('D:\\3\\linux_python\\dist\\cmd\\fullname.txt', 'w')
    f2 = open('D:\\3\\linux_python\\dist\\cmd\\pass.txt', 'w')
    f.write(i)
    f1.write(i1)
    f2.write(i2)
    # fr = f.read()
    # fr1 = f1.read()
    # fr2 = f2.read()
    f.close()
    f1.close()
    f2.close()
