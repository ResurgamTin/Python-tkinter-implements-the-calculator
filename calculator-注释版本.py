from tkinter import *

root = Tk()  # Create a window创建主窗口
root.title("千阳学习计算器")  # 设置标题
root.geometry("800x400+500+200")  # 设置窗口大小同时窗口距离左边屏幕的距离为 500（以像素为单位），距离屏幕顶部的距离为 200，这里我们将带“+”的参数值称为“位置参数”
# StringVar,调用 get() 方法可以读取这些变量的当前值；调用 set() 方法则可改变变量值。
equ = StringVar()
equ.set("0")  # 默认显示 0


def calculate():  # 执行计算并显示结果
    result = eval(equ.get())  # 把显示区的内容计算出来
    equ.set(equ.get() + "=\n" + str(result))  # 既显示之前显示区的内容又显示计算结果


# 获取按钮上的值并且要追加到显示区上，因为如果不追加到显示区，那么之后的eval函数无法进行计算
def show(buttonString):
    content = equ.get()
    if content == "0":
        content = ""
    # 上面三行语句是为了让显示区之前显示的0变成空字符串，然后显示新的点击的数字
    equ.set(content + buttonString)


def backspace():  # 删除前一个字符
    equ.set(str(equ.get()[:-1]))


def clear():  # 清除显示区，放置0
    equ.set("0")


# 所有的label和按钮都要基于主窗口创建
# 设计显示label和计算器按钮
# 创建一个label，并设置宽度100和高度10，并设置为边框风格raised，anchor是文本显示方位， SE表示0显示在东南（右下角），必须使用大写字母如NW表示0显示在西北（左上角）
# textvariable	输入框内值，也称动态字符串，使用 StringVar() 对象来设置，而 text 为静态字符串对象，只有这里使用了 textvariable 属性，才能使用 textvariable 对象的 get() 方法来获取值，其他地方是不会变的，因为没有引用这个属性
# 这里可以直接用Label控件因为最上面的导入语局是from tkinter import *，所以可以直接使用Label控件不需要前面加上tk.
label = Label(root, width=100, height=10, relief="raised", anchor=SE, textvariable=equ)
# grid方法排列按钮布局，row是行，column是列，columnsapn	控件实例所跨的列数，默认为 1 列，通过该参数可以合并一行中多个领近单元格，padx,pady用于控制外边距，在单元格外部，左右、上下方向上填充指定大小的空间
label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# 清除显示区按钮
# 同样Button也就可以直接使用，不需要前面加上tk.
# fg前景色，bg背景色，font字体，command命令，text文本，width宽度，height高度，relief边框风格，anchor文本显示方位
# command	用来执行按钮关联的回调函数。当按钮被点击时，执行该函数
Button(root, text="Clean", fg="red", width=10, command=clear).grid(row=1, column=0)
# 以下是 row1 的其他按钮
Button(root, text="DEL", width=10, command=backspace).grid(row=1, column=1)
Button(root, text="%", width=10, command=lambda: show("%")).grid(row=1, column=2)
Button(root, text="/", width=10, command=lambda: show("/")).grid(row=1, column=3)
# 以下是 row2 的其他按钮
Button(root, text="7", width=10, command=lambda: show("7")).grid(row=2, column=0)
Button(root, text="8", width=10, command=lambda: show("8")).grid(row=2, column=1)
Button(root, text="9", width=10, command=lambda: show("9")).grid(row=2, column=2)
Button(root, text="*", width=10, command=lambda: show("*")).grid(row=2, column=3)
# 以下是 row3 的其他按钮
Button(root, text="4", width=10, command=lambda: show("4")).grid(row=3, column=0)
Button(root, text="5", width=10, command=lambda: show("5")).grid(row=3, column=1)
Button(root, text="6", width=10, command=lambda: show("6")).grid(row=3, column=2)
Button(root, text="-", width=10, command=lambda: show("-")).grid(row=3, column=3)
# 以下是 row4 的其他按钮
Button(root, text="1", width=10, command=lambda: show("1")).grid(row=4, column=0)
Button(root, text="2", width=10, command=lambda: show("2")).grid(row=4, column=1)
Button(root, text="3", width=10, command=lambda: show("3")).grid(row=4, column=2)
Button(root, text="+", width=10, command=lambda: show("+")).grid(row=4, column=3)
# 以下是 row5 的其他按钮
Button(root, text="0", width=20, command=lambda: show("0")).grid(row=5, column=0, columnspan=2)
Button(root, text=".", width=10, command=lambda: show(".")).grid(row=5, column=2)
Button(root, text="=", width=10, bg="yellow", command=lambda: calculate()).grid(row=5, column=3)

root.mainloop()  # 和Tk()一起显示窗口循环
