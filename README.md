# Chemical-formula-calculation-tool
# 欢迎！

### [转到Wiki](https://github.com/html5syt/Chemical-formula-calculation-tool/wiki/%E5%8F%82%E8%B5%9B%E7%89%88%E3%81%AEHome)
# ***离线版帮助文件可在开始菜单/程序安装目录中查看。***

---
---
# ***安装部分***
---
---

# 安装包安装（仅支持Windows）
---
按照提示安装即可。
# 源码安装
---
1. 安装Python解释器（***版本大于3***，最好是最新版本）、PIL库  `pip install pillow` ***(如是Linux，还需安装Tkinter，并且Linux系统安装了图形界面。)***
2. 运行main.py即可。


---
---
# ***使用部分***
---
---

# 1. 部件功能介绍
---
## 1.1 主窗口
---
介绍一下各个部件的功能：

![(o_230307150825_1.png (889×451) (cnblogs.com)](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230307150825_1.png)

### A、C区：
算式输入区与计算结果输出区。
### B：
[下标键盘](#12-下标键盘)
### D：
计算（与在主窗口按下Ctrl+Q等效）。
### E：
清空输入区与输出区的所有文字。
### F：
可以置顶主窗口。
### G：
帮助与关于。

---
## 1.2 下标键盘
---
> 它是为了方便输入化学式下那一串小小的数字（下标）而设计，使程序可以尽可能还原化学式书写时的样子。

![](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230307151809_image.png)

### 0-9数字：
在这里按下这些按钮，会在输入区的光标处插入对应的小数字，也可以按下键盘上数字键直接输入 ***(请先点击“下标键盘”窗口，使其右上角的“x”变成红色，再输入！(也就是把焦点移到此窗口上)***
### “+”号：
功能与数字键相同，但是在输入区中插入的是一个点 “·”。

---
# 2. 如何使用
---

> 以 `CuSO₄·5H₂O`为示范。

## 2.1 输入化学式
把化学式输入进去。

![](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230307155226_%E5%8A%A8%E7%94%BB.gif)

## 2.2 计算
点击按钮计算或在主界面按Ctrl+Q计算。

![js](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230307160100_%E5%8A%A8%E7%94%BB55.gif)

## 2.3 复制结果
选择结果Ctrl+C复制。

---
# 3. 特别提醒：
---
> 1. 支持多化学式计算：
>
> ![duo](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230308121948_%E5%8A%A8%E7%94%BB11.gif)
>
>  ***(请以英文逗号分割每个化学式，最后不能有逗号，可以在输入框中随意插入空格与回车以方便阅读。)*** 
> 例：
> ```
>   CuSO₄·5H₂O,CuSO₄,5H₂O,
>      
>     5H₂O,   5H₂O
>
> 结果：250,160,90,90,90,
> ```

>2. 式量结果超出框
>
>可以选中部分结果按下Ctrl+A全选复制，也可以拖动光标选择。
>
>![sl](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230308124554_%E5%8A%A8%E7%94%BB2222.gif)

---
# 4. 各种错误提示
---

![ERR](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230308130140_image.png)

## A：
输入框中没有化学式，请检查输入框中是否存在化学式。
## B：
由于技术条件限制，暂不支持类似“***555***CuSO₄₄₄₄₄₄·***555***H₂₄₄₄₄₄₄O”等带有多位数字的化学式，下标数字***不***受此影响。
## C：
请检查化学式是否输入错误，如：
1. 在最后一个化学式之后加上了逗号：“CuSO₄·5H₂O,CuSO₄·5H₂O,”
2. 使用中文括号与逗号：“CuSO₄·5H₂O ***，*** CuSO₄·5H₂O ***（*** H₂ ***）***”
3. 输入非化学式内容/大小写/数字下标错误：“fdhgdshds”  /   “cuh₂o”  /  “CuSO4”
## D：
请检查是否输入类似于“Cu555SO”或“CuSO555”等数字不在最前面的情况
> 如化学式中遇到 “·”，以 “·”为分界可以在 “·”后面输入数字。
>
> ***什么？没有理解？看下面的例子。***
>
> ***999*** CuSO₄· ***599*** H₂O
>
> ***特别提醒：暂不支持类似CuSO₄(***99***H)等括号中带有数字的化学式！***
---
# 5. 完整使用示例
---

![ex](https://images.cnblogs.com/cnblogs_com/blogs/767021/galleries/2283943/o_230309022033_%E5%8A%A8%E7%94%BB2222KJ.gif)

[回到顶部](#欢迎)
