from tkinter import *


def calculate():  # 执行计算并显示结果
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))


def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)


def backspace():  # 删除前一个字符
    equ.set(str(equ.get()[:-1]))


def clear():  # 清除显示区，放置00
    equ.set("0")


root = Tk()
root.title("计算器")

equ = StringVar()
equ.set("0")  # 默认显示 0

# 设计显示区
label = Label(root, width=25, height=2, relief="raised", anchor=SE,
              textvariable=equ)
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# 清除显示区按钮
clearButton = Button(root, text="C", fg="blue", width=5, command=clear)
clearButton.grid(row=1, column=0)
# 以下是 row1 的其他按钮
clearButton = Button(root, text="DEL", width=5, command=backspace).grid(row=1, column=1)
clearButton = Button(root, text="%", width=5, command=lambda: show("%")).grid(row=1, column=2)
clearButton = Button(root, text="%", width=5, command=lambda: show("/")).grid(row=1, column=3)
# 以下是 row2 的其他按钮
clearButton = Button(root, text="7", width=5, command=lambda: show("7")).grid(row=2, column=0)
clearButton = Button(root, text="8", width=5, command=lambda: show("8")).grid(row=2, column=1)
clearButton = Button(root, text="9", width=5, command=lambda: show("9")).grid(row=2, column=2)
clearButton = Button(root, text="*", width=5, command=lambda: show("*")).grid(row=2, column=3)
# 以下是 row3 的其他按钮
clearButton = Button(root, text="4", width=5, command=lambda: show("4")).grid(row=3, column=0)
clearButton = Button(root, text="5", width=5, command=lambda: show("5")).grid(row=3, column=1)
clearButton = Button(root, text="6", width=5, command=lambda: show("6")).grid(row=3, column=2)
clearButton = Button(root, text="-", width=5, command=lambda: show("-")).grid(row=3, column=3)
# 以下是 row4 的其他按钮
clearButton = Button(root, text="1", width=5, command=lambda: show("1")).grid(row=4, column=0)
clearButton = Button(root, text="2", width=5, command=lambda: show("2")).grid(row=4, column=1)
clearButton = Button(root, text="3", width=5, command=lambda: show("3")).grid(row=4, column=2)
clearButton = Button(root, text="+", width=5, command=lambda: show("+")).grid(row=4, column=3)
# 以下是 row5 的其他按钮
clearButton = Button(root, text="0", width=12, command=lambda: show("0")).grid(row=5, column=0, columnspan=2)
clearButton = Button(root, text=".", width=5, command=lambda: show(".")).grid(row=5, column=2)
clearButton = Button(root, text="=", width=5, bg="yellow", command=lambda: calculate()).grid(row=5, column=3)

root.mainloop()
