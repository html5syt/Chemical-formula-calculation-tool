'''
开源软件，使用GPLv3协议
请遵守开源规则！！！
主函数文件
'''

import tkinter as tk
import window as wd
import function as func
import tkinter.ttk


class main():
    hxs=tk.Tk()
    wd.window.mainwdmake(hxs)
    wd.window.maincompmake(hxs)
    wd.window.showmainWindow(hxs)

main()