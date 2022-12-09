import tkinter
#import command
import subprocess

#p = subprocess.run("cp", "dirA/file", "dirB")
count = 0
window_main = tkinter.Tk()
window_main.geometry("550x250")
 
check_1 = tkinter.IntVar()
check_2 = tkinter.IntVar()
check_3 = tkinter.IntVar()
 
def check1Clicked():
    global count
    if check_1.get():
        print('Unit 1 selected')
        count = count +1
       # res = subprocess.run("python3","demo_2.py")
       # print(res.output)
       # print(res.exit)
    else :
        print('Unit 1 unselected')
 
def check2Clicked():
    global count
    if check_2.get() :
        print('Unit 2 selected')
         
        count = count +1
    else :
        print('Unit 2 unselected')
 
def check3Clicked():
    global count
    if check_3.get() :
        count = count +1
        print('Unit 3 selected')
    else :
        print('Unit 3 unselected')
 
check_but_1 = tkinter.Checkbutton(window_main, text = 'UINT 1', variable = check_1,
                onvalue = 1, offvalue = 0, command=check1Clicked)
check_but_1.pack()
 
check_but_2 = tkinter.Checkbutton(window_main, text = 'UINT 2', variable = check_2,
                onvalue = 1, offvalue = 0, command=check2Clicked)
check_but_2.pack()
 
check_but_3 = tkinter.Checkbutton(window_main, text = 'UNIT 3', variable = check_3,
                onvalue = 1, offvalue = 0, command=check3Clicked)
check_but_3.pack()



window_main.mainloop()

print("Total no. of unit selected for automation is ",count)

