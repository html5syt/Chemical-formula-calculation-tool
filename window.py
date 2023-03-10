import tkinter as tk
import function as func
import PTOElist as Plst
import tkinter.ttk
import tkinter.messagebox as tkmsg
from PIL import Image,ImageTk

#下标键盘是否存在
keyboardopen=None

#彩蛋
EasterEgg=0

#窗口文字部件变量

#tkinter窗口部分
class window():
    def __init__(self):
        pass

    
    def mainwdmake(win):#制作主窗口
        win.title("化学式计算工具")
        #win和Linux不同的全屏指令
        try:
            width=800
            height=650
            screenwidth = win.winfo_screenwidth()
            screenheight = win.winfo_screenheight()
            geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            win.geometry(geometry)
            win.state('zoomed')
        except:                                                                                                
            width = win.winfo_screenwidth()
            height = win.winfo_screenheight()                                                                                                                                                                              
            screenwidth = win.winfo_screenwidth()
            screenheight = win.winfo_screenheight()
            geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            win.geometry(geometry)
        win.minsize(530,650)
        try:
            win.iconbitmap(True,'./icon.ico')
        except:
            pass
    def showmainWindow(win):
        win.mainloop()
    
    def maincompmake(win):
        #制作主窗口
            #制作菜单栏
        mainmenu=tk.Menu(win)
                    #工具
        toolsmenu=tk.Menu(mainmenu, tearoff=False)
        toolsmenu.add_command(label="导入(I)",command=func.function.menuCmd,underline=3)
        toolsmenu.add_command(label="导出(O)",command=func.function.menuCmd,underline=3)
        toolsmenu.add_separator()
        toolsmenu.add_command(label="元素周期表查询(F)",command=lambda:window.qwertymake(win),underline=8)
        toolsmenu.add_separator()
        toolsmenu.add_command(label="退出(Q)",command=win.quit,underline=3)
                    #关于
        aboutmenu=tk.Menu(mainmenu, tearoff=False)
        aboutmenu.add_command(label="帮助(H)",command=lambda:window.HelpMake(win),underline=3)
        aboutmenu.add_separator()
        aboutmenu.add_command(label="关于(A)",command=lambda:window.aboutmake(win),underline=3)
                #显示菜单
        mainmenu.add_cascade(label="工具(T)",menu=toolsmenu,underline=3)
        mainmenu.add_cascade(label="关于(A)",menu=aboutmenu,underline=3)
        win.config(menu=mainmenu)
        
        #彩蛋
        win.bind('<Control-Alt-E>',func.function.funcAdaptor(window.EasterEggMake,win=win))
        win.bind('<Control-Alt-e>',func.function.funcAdaptor(window.EasterEggMake,win=win))
        win.bind('<Control-Alt-T>',window.EasterEggShow)
        win.bind('<Control-Alt-t>',window.EasterEggShow)
        win.bind('<Control-Alt-R>',window.EasterEggReset)
        win.bind('<Control-Alt-r>',window.EasterEggReset)
        
        
        #主窗口组件制作
            #缩放调整
                #行
        win.rowconfigure(1,weight=2)
        win.rowconfigure(2,weight=0)
        win.rowconfigure(3,weight=2)
        win.rowconfigure(4,weight=2)
        win.rowconfigure(5,weight=2)
        win.rowconfigure(6,weight=2)
        
                #列
        win.columnconfigure(1,weight=0)
        win.columnconfigure(2,weight=3)
        win.columnconfigure(3,weight=0)
        win.columnconfigure(4,weight=0)
        win.columnconfigure(5,weight=0)
        win.columnconfigure(6,weight=3)
        win.columnconfigure(7,weight=0)
        win.columnconfigure(8,weight=0)
        
            #制作输入区
        inputarea=tk.Label(win,text='输入区',font=('./font.ttf',22))
        inputarea.grid(row=1,column=1,padx=5,pady=5,sticky='NWSE')
        inputarea_input=tk.Text(win,font=('./font.ttf',45),height=2)
        inputarea_input.grid(row=1,column=2,columnspan=8,padx=5,pady=5,sticky='NWSE')
        inputarea_scr=tk.Scrollbar(win,command=inputarea_input.yview)
        inputarea_input.config(yscrollcommand=inputarea_scr.set)
        inputarea_scr.grid(row=1,column=8,padx=(0,5),pady=5,sticky='NWSE')
        
            #制作输出区
                #式量
        ShiLiang=tk.Label(win,text='式量',font=('./font.ttf',22))
        ShiLiang.grid(row=2,column=1,padx=5,pady=5,sticky='NWSE')
        ShiLiang_output=tk.Entry(win,font=('./font.ttf',15))
        ShiLiang_output.grid(row=2,column=2,columnspan=2,padx=5,pady=5,sticky='NWSE')
        ShiLiang_get=tk.Button(win,text='⇚',font=('./font.ttf',15),command=lambda:func.function.ShiLiangCalc(input=inputarea_input,output=ShiLiang_output))
        ShiLiang_get.grid(row=2,column=4,padx=5,pady=5,sticky='NWSE')
                #质量比
        ZhiLiangBi=tk.Label(win,text='质量比',font=('./font.ttf',22))
        ZhiLiangBi.grid(row=2,column=5,rowspan=2,padx=5,pady=5,sticky='NWSE')
        ZhiLiangBi_output=tk.Text(win,font=('./font.ttf',22),height=5)
        ZhiLiangBi_output.grid(row=2,column=6,rowspan=2,padx=5,pady=5,sticky='NWSE')
        ZhiLiangBi_scr=tk.Scrollbar(win,command=ZhiLiangBi_output.yview)
        ZhiLiangBi_output.config(yscrollcommand=ZhiLiangBi_scr.set)
        ZhiLiangBi_scr.grid(row=2,column=7,rowspan=2,padx=(0,5),pady=5,sticky='NWSE')
        ZhiLiangBi_get=tk.Button(win,text='⇚',font=('./font.ttf',15),command=func.function.menuCmd)
        ZhiLiangBi_get.grid(row=2,column=8,rowspan=2,padx=5,pady=5,sticky='NWSE')
                #各元素质量分数
        ZhiLiangFS=tk.Label(win,text='各元素\n质量分数',font=('./font.ttf',22))
        ZhiLiangFS.grid(row=3,column=1,rowspan=3,padx=5,pady=5,sticky='NWSE')
        ZhiLiangFS_output=tk.Text(win,font=('./font.ttf',22),height=5)
        ZhiLiangFS_output.grid(row=3,column=2,rowspan=3,padx=5,pady=5,sticky='NWSE')
        ZhiLiangFS_scr=tk.Scrollbar(win,command=ZhiLiangFS_output.yview)
        ZhiLiangFS_output.config(yscrollcommand=ZhiLiangFS_scr.set)
        ZhiLiangFS_scr.grid(row=3,column=3,rowspan=3,padx=(0,5),pady=5,sticky='NWSE')
        ZhiLiangFS_get=tk.Button(win,text='⇚',font=('./font.ttf',15),command=lambda:func.function.ZhiLiangFSCalc(input=inputarea_input,output=ZhiLiangFS_output))
        ZhiLiangFS_get.grid(row=3,column=4,rowspan=3,padx=5,pady=5,sticky='NWSE')
                #原子个数比
        YZGeShuBi=tk.Label(win,text='原子\n个数比',font=('./font.ttf',22))
        YZGeShuBi.grid(row=4,column=5,rowspan=2,padx=5,pady=5,sticky='NWSE')
        YZGeShuBi_output=tk.Text(win,font=('./font.ttf',22),height=5)
        YZGeShuBi_output.grid(row=4,column=6,rowspan=2,padx=5,pady=5,sticky='NWSE')
        YZGeShuBi_scr=tk.Scrollbar(win,command=YZGeShuBi_output.yview)
        YZGeShuBi_output.config(yscrollcommand=YZGeShuBi_scr.set)
        YZGeShuBi_scr.grid(row=4,column=7,rowspan=2,padx=(0,5),pady=5,sticky='NWSE')
        YZGeShuBi_get=tk.Button(win,text='⇚',font=('./font.ttf',15),command=func.function.menuCmd)
        YZGeShuBi_get.grid(row=4,column=8,rowspan=2,padx=5,pady=5,sticky='NWSE')
                #化合物质量
        HuaHeWuZL=tk.Label(win,text='化合物\n质量',font=('./font.ttf',22))
        HuaHeWuZL.grid(row=6,column=1,padx=5,pady=5,sticky='NWSE')
        HuaHeWuZL_output=tk.Text(win,font=('./font.ttf',22),height=5)
        HuaHeWuZL_output.grid(row=6,column=2,padx=5,pady=5,sticky='NWSE')
        HuaHeWuZL_scr=tk.Scrollbar(win,command=HuaHeWuZL_output.yview)
        HuaHeWuZL_output.config(yscrollcommand=HuaHeWuZL_scr.set)
        HuaHeWuZL_scr.grid(row=6,column=3,padx=(0,5),pady=5,sticky='NWSE')
        HuaHeWuZL_get=tk.Button(win,text='⇚',font=('./font.ttf',15),command=func.function.menuCmd)
        HuaHeWuZL_get.grid(row=6,column=4,padx=5,pady=5,sticky='NWSE')
                #四个功能按钮
        FuncBut=tk.Frame(win)
        FuncBut.grid(row=6,column=5,columnspan=4,sticky='NWSE')
                    #缩放设置（功能按钮）
                        #行
        FuncBut.rowconfigure(1,weight=1)
        FuncBut.rowconfigure(2,weight=1)
                        #列
        FuncBut.columnconfigure(1,weight=1)
        FuncBut.columnconfigure(2,weight=1)
              
                    #下标键盘
        FuncBut1=tk.Button(FuncBut,text='下标键盘',font=('./font.ttf',22),command=lambda:window.keyboardmake(win))
        FuncBut1.grid(row=1,column=1,padx=5,pady=5,sticky='NWSE')
                    #计算全部
        FuncBut2=tk.Button(FuncBut,text='计算全部',font=('./font.ttf',22),command=func.function.menuCmd)
        FuncBut2.grid(row=1,column=2,padx=5,pady=5,sticky='NWSE')
                    #检查输入
        FuncBut3=tk.Button(FuncBut,text='检查输入',font=('./font.ttf',22),command=func.function.menuCmd)
        FuncBut3.grid(row=2,column=1,padx=5,pady=5,sticky='NWSE')
                    #清空全部
        FuncBut4=tk.Button(FuncBut,text='清空全部',font=('./font.ttf',22),command=func.function.menuCmd)
        FuncBut4.grid(row=2,column=2,padx=5,pady=5,sticky='NWSE')
        
        #子窗口-下标键盘
    def keyboardmake(win):
        global keyboardopen
            #制作窗体
        if keyboardopen == None:            
            keyboard = tk.Toplevel(win)
            keyboard.title('下标键盘')
            keyboard.resizable(False,False)   
            try:
                keyboard.attributes('-toolwindow',True,
                                    '-topmost', True)  
            except:
                keyboard.attributes('-topmost', True)        
            keyboardopen = True            
            keyboard.protocol('WM_DELETE_WINDOW',lambda:window.keyboardclose(keyboard))
            #制作组件
            ButText1=['*','2','3']
            ButText2=['4','5','6']
            ButText3=['7','8','9']
            for row in range(1,4):
                for col in range(1,4):
                    if row==1:
                        window.keyboardinput(keyboard,row,col,ButText1[col-1])
                    elif row==2:
                        window.keyboardinput(keyboard,row,col,ButText2[col-1])
                    elif row==3:
                        window.keyboardinput(keyboard,row,col,ButText3[col-1])  
        else:
            tkmsg.showwarning(title='提示',message='下标键盘已被打开\n请检查屏幕!')
    def keyboardinput(keyboard,row,col,ButText):
        keyboardButName = locals()
        keyboardButName['keyboard_'+str(row)+'_'+str(col) ] = tk.Button(keyboard,text=ButText,font=('./font.ttf',15),height=4,width=8)
        keyboardButName['keyboard_'+str(row)+'_'+str(col) ].grid(row=row,column=col)
    def keyboardclose(keyboard):
        global keyboardopen
        keyboardopen=None
        keyboard.destroy()
        
    #子窗口-关于
    def aboutmake(win):
        about=tk.Toplevel(win)
        about.title('关于')
        width=380
        height=380
        screenwidth = about.winfo_screenwidth()
        screenheight = about.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        about.geometry(geometry)
        about.resizable(False,False)
        HeadPortraitImage=Image.open('./about.jpg')
        HeadPortrait=ImageTk.PhotoImage(HeadPortraitImage)
        HPlabel=tk.Label(about,image=HeadPortrait)
        HPlabel.pack()
        desp1=tk.Label(about,text='Html5syt',font=('./font.ttf',30)).pack()
        desp2=tk.Label(about,text='制作',font=('./font.ttf',25)).pack()
        desp3=tk.Label(about,text='V 1.0',font=('./font.ttf',20)).pack()
        desp4=tk.Label(about,text='GitHub链接',font=('./font.ttf',20)).pack()
        about.mainloop()#防止图片不显示
    #子窗口-元素周期表查询
    def qwertymake(win):
        global qwertydopen
        qwerty=tk.Toplevel(win)
        qwerty.title('元素周期表查询工具')
        qwerty.attributes('-topmost', True)
        qwerty.resizable(False,False)
        #原子序数
        NoQwerty=tk.Label(qwerty,text='原子序数:',font=('./font.ttf',22))
        NoQwerty.grid(row=1,column=1,padx=5,pady=5)
        NoQwertyInput=tk.Entry(qwerty,width=3,font=('./font.ttf',22))
        NoQwertyInput.grid(row=1,column=2,padx=5,pady=5)
        #元素符号
        NmQwerty=tk.Label(qwerty,text='元素符号:',font=('./font.ttf',22))
        NmQwerty.grid(row=2,column=1,padx=5,pady=5)
        NmQwertyInput=tk.Entry(qwerty,width=3,font=('./font.ttf',22))
        NmQwertyInput.grid(row=2,column=2,padx=5,pady=5)
        #相对原子质量
        MsQwerty=tk.Label(qwerty,text='相对原子质量:',font=('./font.ttf',22))
        MsQwerty.grid(row=3,column=1,padx=5,pady=5)
        MsQwertyInput=tk.Entry(qwerty,width=3,font=('./font.ttf',22))
        MsQwertyInput.grid(row=3,column=2,padx=5,pady=5)
        #获取
        QwertyGet=tk.Button(qwerty,text='获取',font=('./font.ttf',22))
        QwertyGet.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky='NWSE')

    #子窗口-帮助
    def HelpMake(win):
        Help=tk.Toplevel(win)
        Help.resizable(False,False)
     
     
    #彩蛋：窗口轰炸
    def EasterEggMake(event,win):
        global EasterEgg
        EasterEggwin=tk.Toplevel(win)
        EasterEgg+=1
    def EasterEggShow(event):
        global EasterEgg
        tkmsg.showinfo('彩蛋-EasterEgg','已弹出'+str(EasterEgg)+'个窗口！')
    def EasterEggReset(event):
        global EasterEgg
        EasterEgg=0
        tkmsg.showinfo('彩蛋-EasterEgg','已清空！')
        