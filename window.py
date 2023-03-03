'''
开源软件，使用GPLv3协议
请遵守开源规则！！！
窗口组件+按钮函数文件
'''

import tkinter as tk
import webbrowser
import function as func
import PTOElist as Plst
import tkinter.ttk
import tkinter.messagebox as tkmsg
from PIL import Image,ImageTk

#下标键盘是否存在
keyboardopen=None

inputarea_input=''
ShiLiang_output=''

#tkinter窗口部分
class window():
    def __init__(self):
        pass

    
    def mainwdmake(win):#制作主窗口
        win.title("化学式计算工具")
        #win和Linux不同的全屏指令
        try:
            width=888
            height=200
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
        win.minsize(540,200)
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
                    #关于
        aboutmenu=tk.Menu(mainmenu, tearoff=False)
        aboutmenu.add_command(label="关于(A)",command=lambda:window.aboutmake(win,False),underline=3)
        aboutmenu.add_separator()
        aboutmenu.add_command(label="关于参赛版本(C)",command=lambda:window.aboutmake(win,True),underline=7)
                #显示菜单
        mainmenu.add_cascade(label="关于(A)",menu=aboutmenu,underline=3)
        win.config(menu=mainmenu)

        
        #主窗口组件制作
            #缩放调整
                #行
        win.rowconfigure(1,weight=1)
        win.rowconfigure(2,weight=0)

        
                #列
        win.columnconfigure(1,weight=0)
        win.columnconfigure(2,weight=3)
        win.columnconfigure(3,weight=0)
        win.columnconfigure(4,weight=0)

        global inputarea_input,ShiLiang_output
            #制作输入区
        inputarea=tk.Label(win,text='输入区',font=('./font.ttf',22))
        inputarea.grid(row=1,column=1,padx=5,pady=5,sticky='NWSE')
        inputarea_input=tk.Text(win,font=('./font.ttf',55),height=2)
        inputarea_input.grid(row=1,column=2,padx=5,pady=5,sticky='NWSE')
        inputarea_scr=tk.Scrollbar(win,command=inputarea_input.yview)
        inputarea_input.config(yscrollcommand=inputarea_scr.set)
        inputarea_scr.grid(row=1,column=3,padx=(0,5),pady=5,sticky='NWSE')
        
            #制作输出区
                #式量
        ShiLiang=tk.Label(win,text='式量',font=('./font.ttf',22))
        ShiLiang.grid(row=2,column=1,rowspan=2,padx=5,pady=5,sticky='NWSE')
        ShiLiang_output=tk.Entry(win,font=('./font.ttf',30))
        ShiLiang_output.grid(row=2,column=2,padx=5,pady=5,sticky='NWSE')
        ShiLiang_get=tk.Button(win,text='⇚',font=('./font.ttf',20),height=3,command=lambda:func.function.ShiLiangCalc(input=inputarea_input,output=ShiLiang_output))
        ShiLiang_get.grid(row=2,column=3,padx=5,pady=5,sticky='NWSE')
                #ctrl+enter=计算
                    #中转函数
        def transferFunc(event):
            func.function.ShiLiangCalc(input=inputarea_input,output=ShiLiang_output)
        win.bind('<Control-KeyPress-Q>',transferFunc)
        win.bind('<Control-KeyPress-q>',transferFunc)
                
                #四个功能按钮
        FuncBut=tk.Frame(win)
        FuncBut.grid(row=1,column=4,columnspan=1,rowspan=2,sticky='NWSE')
                    #缩放设置（功能按钮）
                        #行
        FuncBut.rowconfigure(1,weight=1)
        FuncBut.rowconfigure(2,weight=1)
                        #列
        FuncBut.columnconfigure(1,weight=1)
              
                    #下标键盘
        FuncBut1=tk.Button(FuncBut,text='下标键盘',font=('./font.ttf',22),command=lambda:window.keyboardmake(win))
        FuncBut1.grid(row=1,column=1,padx=5,pady=5,sticky='NWSE')
                    #清空全部
        FuncBut4=tk.Button(FuncBut,text='清空全部',font=('./font.ttf',22),command=lambda:window.emptyAny(win))
        FuncBut4.grid(row=2,column=1,padx=5,pady=5,sticky='NWSE')
    
    def emptyAny(win):
        #清空全部的函数
        global inputarea_input,ShiLiang_output
        inputarea_input.delete("1.0", "end")
        ShiLiang_output.delete("0", "end")
    
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
            ButText1=['1','2','3']
            ButText2=['4','5','6']
            ButText3=['7','8','9']
            ButText4=['0',' ','*']
            for row in range(1,5):
                for col in range(1,4):
                    if row==1:
                        window.keyboardinput(win,keyboard,row,col,ButText1[col-1])
                    elif row==2:
                        window.keyboardinput(win,keyboard,row,col,ButText2[col-1])
                    elif row==3:
                        window.keyboardinput(win,keyboard,row,col,ButText3[col-1])  
                    elif row==4:
                        window.keyboardinput(win,keyboard,row,col,ButText4[col-1]) 
        else:
            tkmsg.showwarning(title='提示',message='下标键盘已被打开\n请检查屏幕!')
    def keyboardinput(win,keyboard,row,col,ButText):
        keyboardButName = locals()
        keyboardButName['keyboard_'+str(row)+'_'+str(col) ] = tk.Button(keyboard,text=ButText,font=('./font.ttf',15),height=4,width=8)
        keyboardButName['keyboard_'+str(row)+'_'+str(col) ].grid(row=row,column=col)
        def transferFunc2():
            nonlocal ButText,win
            window.keyboardinsert(win,str(ButText))
        keyboard.bind('<KeyPress-'+str(ButText)+'>',transferFunc2())
    def keyboardinsert(win,key):
        global inputarea_input
        if key=='1':
            inputarea_input.insert('INSERT','₁')
        elif key=='2':
            inputarea_input.insert('INSERT','₂')
        elif key=='3':
            inputarea_input.insert('INSERT','₃')
        elif key=='4':
            inputarea_input.insert('INSERT','₄')
        elif key=='5':
            inputarea_input.insert('INSERT','₅')
        elif key=='6':
            inputarea_input.insert('INSERT','₆')
        elif key=='7':
            inputarea_input.insert('INSERT','₇')
        elif key=='8':
            inputarea_input.insert('INSERT','₈')
        elif key=='9':
            inputarea_input.insert('INSERT','₉')
        elif key=='0':
            inputarea_input.insert('INSERT','₀')
        elif key=='*':
            inputarea_input.insert('INSERT','·')
    def keyboardclose(keyboard):
        global keyboardopen
        keyboardopen=None
        keyboard.destroy()
        
    #子窗口-关于
    def aboutmake(win,isComp):
        if isComp:
            about=tk.Toplevel(win)
            about.title('关于参赛版本')
            width=480
            height=110
            screenwidth = about.winfo_screenwidth()
            screenheight = about.winfo_screenheight()
            geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            about.geometry(geometry)
            about.resizable(False,False)
            desp1=tk.Label(about,text='宁波市海曙第二外国语学校',font=('./font.ttf',30)).pack()
            desp2=tk.Label(about,text='初中部',font=('./font.ttf',20)).pack()
            desp3=tk.Label(about,text='804班32号史宇涛',font=('./font.ttf',25)).pack()
        else:
            about=tk.Toplevel(win)
            about.title('关于')
            width=300
            height=300
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
            desp3=tk.Label(about,text='V 1.0 参赛版',font=('./font.ttf',20)).pack()
            desp4=tk.Label(about,text='GitHub链接',fg='blue',font=('./font.ttf',20,"underline"))
            desp4.pack()
            def github(event):
                webbrowser.open("https://github.com/html5syt/Chemical-formula-calculation-tool/tree/%E5%8F%82%E8%B5%9B%E7%89%88%E6%9C%AC", new=0)
            desp4.bind("<Button-1>",github)
        about.mainloop()#防止图片不显示

    #子窗口-帮助
    def HelpMake(win):
        Help=tk.Toplevel(win)
        Help.resizable(False,False)

