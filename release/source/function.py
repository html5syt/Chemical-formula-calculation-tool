'''
开源软件，使用GPLv3协议
请遵守开源规则！！！
计算函数文件
'''


import tkinter as tk
import window as wd
import PTOElist as Plst
import tkinter.messagebox as tkmsg
import tkinter.ttk
import re

#数字括号标识
numberbracket=False
#数字是否在最前面
numberlocation=True
#多位数字
numbersss=False

#上一个元素
lastelement=''
#数字括号乘标识
numberbracketcross=False
#数字括号乘元素
numberbracketEM=''
numbernegativeone=False



class function():
    def __init__(self):
        pass
    
    def funcAdaptor(fun, **kwds):
        #按键绑定适配器（中介）
        return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
    #查询相关
    def list_to_str(lst):
        #警告：仅可用于多元素列表！！！
        lststr = ""
        for i in lst:
            lststr = lststr + str(i) + " "
        return lststr.replace(' ','')
    def get_key(dct, value):
        lst=list(filter(lambda k:dct[k] == value, dct))
        return function.list_to_str(lst)
    #分割
    def Cut(input):
    #分割
        def CutHandle(input):
            CutRule =r"([A-Z][a-z]*|[0-9]|[₀-₉]|·|[(]|[)])"
            output=re.split(CutRule,input)
            return output
        if input.find(',')>=0:
            out=re.split(r",",input)
            cutout=[]
            for i in out:
                cutouttemp=CutHandle(str(i))
                while '' in cutouttemp:
                    cutouttemp.remove('')
                cutout.append(cutouttemp)
            return cutout
        else:
            cutout=[]
            cutouttemp=CutHandle(str(input))
            while '' in cutouttemp:
                cutouttemp.remove('')
            cutout.append(cutouttemp)
            return cutout
        
    def ShiLiangCalc(input,output):
        #式量计算
        global numberbracket,numberlocation,numbersss
            #获取
        intext=input.get('1.0','end').replace('\n','').replace('\r','')
        if not intext :
            tkmsg.showerror('错误','请先输入化学式！')
            return
            #切割
        cut=function.Cut(intext)
            #核心：计算
                #制作算式
        Arithmetic=[]
        subscriptnumberdic={'₀':'0',
                            '₁':'1',
                            '₂':'2',
                            '₃':'3',
                            '₄':'4',
                            '₅':'5',
                            '₆':'6',
                            '₇':'7',
                            '₈':'8',
                            '₉':'9'}
        output.delete('0','end')
        for BigGroup in range(0,len(cut)):
            numberbracket=False  #数字的括号标识
            subscriptnumber=[]
            def subscriptnumberadd():
                nonlocal subscriptnumber
                global numberlocation,numbersss
                Arithmetic.append('*'+function.list_to_str(subscriptnumber))
                subscriptnumber=[]
                numberlocation=False
                numbersss=False
            Arithmetic.append('(')
            numberlocation=True
            for SmallGroup in range(0,len(cut[BigGroup])):
                # SmallGroup+=1
                if str(cut[BigGroup][SmallGroup]).isalpha()==True:
                    if subscriptnumber!=[]:
                        subscriptnumberadd()
                    Arithmetic.append('+'+str(Plst.PTOE2.get(str(function.list_to_str(cut[BigGroup][SmallGroup])))))
                    numberlocation=False
                    numbersss=False
                elif str(cut[BigGroup][SmallGroup]).isdigit()==True:
                    try:
                        number=int(str(cut[BigGroup][SmallGroup]))
                    except:
                        subscriptnumber.append(str(subscriptnumberdic.get(str(cut[BigGroup][SmallGroup]))))
                        numbersss=False
                    else:
                        if numberlocation:
                            if numbersss==False:
                                Arithmetic.append(str(number)+'*'+'(')
                                numberbracket=True
                                numbersss=True
                            else:
                                tkmsg.showerror('抱歉','暂不支持多位数字\n具体请查看帮助')
                                return
                        else:
                            tkmsg.showerror('错误','数字必须在最前面！\n具体请查看帮助')
                            return
                elif str(cut[BigGroup][SmallGroup])=='·':
                    if subscriptnumber!=[]:
                        subscriptnumberadd()
                    if numberbracket==True:
                        Arithmetic.append(')')
                    Arithmetic.append(')+(')
                    numberbracket=False
                    numberlocation=True
                    numbersss=False
                elif str(cut[BigGroup][SmallGroup])=='(':
                    if subscriptnumber!=[]:
                        subscriptnumberadd()
                    Arithmetic.append('+(')
                    numberlocation=False
                    numbersss=False
                elif str(cut[BigGroup][SmallGroup])==')':
                    if subscriptnumber!=[]:
                        subscriptnumberadd()
                    Arithmetic.append(')')
                    numberlocation=False
                    numbersss=False
                #Arithmetic.append('||')
            if subscriptnumber!=[]:
                subscriptnumberadd()
            if numberbracket==True:
                Arithmetic.append(')')
            Arithmetic.append(')')
            numberbracket=False
            try:
                if '(),' in str(eval(function.list_to_str(Arithmetic)))+',':
                    raise TypeError
                output.insert('end',str(eval(function.list_to_str(Arithmetic)))+',')  
            except:
                tkmsg.showerror('错误','计算错误\n请检查化学式是否输入正确!')
            Arithmetic=[]    
            numbersss=False


    def menuCmd():
        tkmsg.showerror('错误','尚未实现')


