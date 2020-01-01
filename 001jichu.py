# !/user/bin/python
# -*- coding:utf-8 -*-    Python 3 源码文件默认以 UTF-8 编码，所有字符串都是 unicode 字符串
# _author: wenrouge

# 基础知识
# 单行注释以 # 开头，多行注释用 ''' 和 """
# 通过pycharm软件操作python代码时一次性操作多行注释 :Ctrl+/
print('\n')            # 打印回车，显示出来好像空了两行
print(end="\n")        # 空一行，等同于print("", end="\n")

# 系统保留关键字
import keyword
print("系统保留关键字：",keyword.kwlist)  # kwlist 就是key word list
# 输出结果 ：
# 系统保留关键字： ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif',  'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
# 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 变量的命名规范
# 模块名和包名：小写字母，单词之间用_分割 ad_stats.py
# 类名：单词首字母大写（驼峰命名法）AdStats，ConfigUtil
# 全局变量名：大写字母，单词之间用_分割 NUMBER，COLOR_WRITE
# 普通变量或函数：小写字母，单词之间用_分割 this_is_a_var
# 实例变量：以_开头 _price，_instance_var
# 私有实例变量（外部访问会报错）：以__开头（2个下划线） __private_var
# 专有变量：__开头，__结尾，一般为python的自有变量 doc，class

# 代码书写规范(基础)
# Indentation 缩进：每一级缩进使用4个空格，不用使用Tab
# Whitespace in Expressions and Statements 表达式和语句中的空格：二元运算符前后各加一个空格；在逗号、冒号、分号后加空格；紧贴函数或索引的左括号前不加空格
# Comments 注释：#后要加一个空格；文档字符串用"""注释"""

# python代码一行写不下，换行写就是每行后面加个\，还是一个整体
s1 = "abcdefghijklmnopqrstuvwxyz"
print(s1)     # 输出结果 ：abcdefghijklmnopqrstuvwxyz
s2 = "abcdefg\
hijklmn\
opqrst\
uvwxyz"
print(s2)  # 输出结果 ：abcdefghijklmnopqrstuvwxyz  \可以在一行写不下的时候连接多行

age = 18
age1 = age
age2 = age1
print(id(age),id(age1),id(age2))  # 查看内存地址： 这里指向同一个内存地址，age2与age1相当于都是指向了18
age = 20
age1 = 19
print(age,age1,age2)       # 输出结果 ：20 19 18
print(type(age))  # 输出结果 ：<class 'int'>  type 用来判断类型 int表示整形（数字）
print(id(age),id(age1),id(age2))  # 输出内存地址，这里age与age分别指向了新的内存地址，用来存放20与19。

# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，紧跟的数字为复制的次数, 2**3表示3个2相乘
print('eat' + '=', 1+2)       # 输出结果：eat= 3
print('eat', '=', 1+2)       # 输出结果：eat = 3
print('eat' + '=' + str(1+2))  # 输出结果：eat=3
print('eat'*3)             # 输出结果：eateateat
print(2**3)                # 输出结果：8
# print中，使用逗号连接有空格，使用加号连接无空格。

eat=1+2
water=2-3
bread=3/5
total=eat+water+bread
print(total)                   # 输出结果：2.6
print('total','=',total)       # 输出结果：total = 2.6
print('total','=',eat+water+bread)  # 输出结果：total = 2.6

# 字符串的拼接：
# 凡是被引号引起来的都是字符串
a = "alex"
b = "三哥"
print(a + b)    # 输出结果：alex三哥
print(a,b)      # 输出结果：alex 三哥
c = a + "嘿嘿嘿" + b
print(c)          # 输出结果：alex嘿嘿嘿三哥
# 其实不推荐使用+来拼接字符串，推荐使用join函数（后面会学到），
# 因为join函数在拼接字符串之前会计算所有字符串的长度，然后逐一拷贝，仅新建一次对象。


# 字符串的相乘/倍增：
a = "坚强"
print(a * 8)       # 输出结果：坚强坚强坚强坚强坚强坚强坚强坚强

# 字符串的相加和乘法：
a = "坚持"
b = "python"
print((a + b)*3)   # 输出结果：坚持python坚持python坚持python

# 格式化输出
# 用print打印出下面内容：
# 文能提笔安天下,
# 武能上马定乾坤.
# 心存谋略何人胜,
# 古今英雄唯世君.
# 方法一：
print("文能提笔安天下,")
print("武能上马定乾坤.")
print("心存谋略何人胜,")
print("古今英雄唯世君.")
# 方法二：
print("文能提笔安天下,\n" "武能上马定乾坤.\n" "心存谋略何人胜,\n" "古今英雄唯世君.\n")
# 方法三
msg = """
文能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯世君.
"""
print(msg)

# 占位符
# %s  s = string
# %d  d = digit 整数
# %f  f = float 浮点数，约等于小数
print('我的名字叫%s' % ('楼怡麟'))
print('我的年龄是 %d 岁'% (12))
print('我的身高是 %f m' % (1.49))    # 输出：我的身高是 1.490000 m
print('我的身高是 %.2f m' % (1.49))   # 保留2位小数 ，我的身高是 1.49 m
print('姓名:%10s，年龄:%10d，身高:%5.2f' % ('楼怡麟',12,1.49))   # 指定占位符宽度
print('姓名:%-10s，年龄:%-10d，身高:%-5.2f' % ('楼怡麟',12,1.49))   # 指定占位符宽度且左对齐

name = input("姓名?:")
addr = input("地址?:")
hobby = input("爱好:")
msg = "敬爱可亲的%s,最喜欢在%s干%s"
print(msg%(name,addr,hobby))
# 输出结果：
# 姓名?:楼怡麟
# 地址?:操场
# 爱好:打篮球
# 敬爱可亲的楼怡麟,最喜欢在操场干打篮球

name=input("你的名字是什么？")
age=int(input('你的年龄是多少？'))
job=input('你的工作是什么？')
sex=input('你的性别是什么？')
msg='''___________个人信息____________
name:%s
age:%s
job:%s
sex:%s
__________信息结束_________'''%(name,age,job,sex)
print(msg)
# 输出结果：
# ___________个人信息____________
# name:楼怡麟
# age:12
# job:学生
# sex:男
# __________信息结束_________

'''
format用法
 相对基本格式化输出采用‘%’的方法，format()功能更强大，
 该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’
 使用方法有两种：b.format(a)和format(a,b)。
'''
print('以下是用.format格式化输出')
print('{} {}'.format('hello','world'))  # 不带字段  hello world
print("{:.2f}".format(3.141592653589))  # 不带字段，3.14
print('{0} {1}'.format('hello','world'))  # 带数字编号,通过位置匹配参数 hello world
print('{0} {1} {0}'.format('hello','world'))   # hello world hello
print('{a} {tom} {a}'.format(tom='hello',a='world'))  # 带关键字,通过名字匹配参数 world hello world
print("姓名：{name}, 性别 ：{sex}".format(name="楼怡麟", sex="男"))
# .format 用于格式化输出 姓名：楼怡麟, 性别 ：男

print('------------------------------')

print('{} and {}'.format('hello','world'))  # 默认左对齐
print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
print('{:^10s} and {:^10s}'.format('hello','world'))  # 取10位中间对齐
print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数  1.123 is 1.12
print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
print('{:%}'.format(8))    # 800.000000%
#'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。

# 两个%% 才是百分号   ，%s只是占位符
msg = "山哥,目前的学习进度为%s%%"
print(msg % (2))
msg = "my name is %s I'm %s years old"  # 单双引号配合使用
print(msg % (input("name:"), input("age:")))
msg = f"my name is {input('name:')} I'm {input('age:')} years old"
print(msg)

# 另外可在字符串前加f以达到格式化的目的，在{}里加入对象，此为format的另一种形式
name = 'jack'
age = 18
sex = 'man'
job = "IT"
salary = 9999.99
print(f'my name is {name.capitalize()}.')  # capitalize 表示首字母大写
print(f'I am {age:*^10} years old.')  # *^10表示10个*，{:^10}表示居中，{:<10s}表示左对齐，宽度10
print(f'I am a {sex}')
print(f'My salary is {salary:10.3f}')
# 输出结果：
# my name is Jack.
# I am ****18**** years old.
# I am a man
# My salary is   9999.990


# 条件控制
# 提示用户输入的麻花藤. 判断用户输入的是否正确.
user = input("请输入用户名:")
if user == "麻花藤":
    print("真聪明")
else:
    print("输入错误")

# 用户输入一个月份.然后判断月份是多少月.
# 根据不同的月份,打印出不用的饮食(根据个人习惯和老家习惯随意编写)
month = input("请输入月份:")
if int(month) == 1:
    print("刀削面")
elif int(month) == 2 :
    print("米饭")
else:
    print("不知道你吃的啥")

# 用户输入一个分数.根据分数来判断用户考试成绩的输出不同的档次
fraction = input("请输入分数：")
if int(fraction) == 90 :
    print("A")
elif int(fraction) == 60 :
    print("D")
elif int(fraction) < 60 :
    print("不及格")

# 利用if语句写出猜大小的游戏：
num = input("请输入数字:")
if int(num) > 66:
    print("猜大了")
elif int(num) < 66 :
    print("猜小了")
else:
    print("结果正确")

# 用户输入他的年龄, 通过程序进⾏判断.如果小于10,提示小屁孩,
# 如果大于10,小于20,提示青春期叛逆的小屁孩.
# 如果大于20,小于30.提示开始定性,开始混社会小屁孩儿,
# 如果大于30,小于40.提示看老老大不了,赶紧结婚小屁孩儿.
# 如果大于40,小于50.提示家里有个不听话的小屁孩儿.
# 如果大于50,小于60.提示自己马上变成不听话的老屁孩儿.
# 如果大于60,小于70.提示活着还不错的老屁孩儿.
# 如果大于70,小于90.提示人生就快结束了的一个老屁孩儿.
# 如果大于90以上.提示再见了这个世界.
age = input("请输入年龄:")
if int(age) < 10:
    print("小屁孩")
elif 20 > int(age) > 10:
    print("青春期叛逆的小屁孩")
elif 30 > int(age) > 20:
    print("开始定性")
elif 40 > int(age) > 30:
    print("看老大不小了")
elif 50 > int(age) > 40 :
    print("家里有不听话的小屁孩")
elif 60 > int(age) > 50 :
    print("不听话小屁孩")
elif int(age) > 90 :
    print("再见世界")

#  %要用%%表示 ； %s表示占位符，一般用于格式化输出
print("版本一：")
s1 = 82
s2 = 95
tisheng = 100*((s2-s1)/s1)
print('%s，恭喜你，你的成绩提高了%.3f%%' % ('三小603班楼怡麟同学',tisheng))
print("", end="\n")    #  表示打印显示空一行
print("版本二：")
name = input('请输入您的名字：')
s1 = float(input("请输入您的第一次成绩:"))
s2 = float(input("请输入您的第二次成绩:"))
s3 = 0
s4 = 0
s5 = 0
if s2>=s1:
    s4=s2-s1
    s3="提升"
    s5=(s4/s1)*100
else:
    s4=s1-s2
    s3="降低"
    s5=(s4/s1)*100
print("嗨,%s同学,你的成绩%s了%s分,%s了%s%%" %(name,s3,s4,s3,s5))

# if嵌套：举例如下：
sex = input("请输入性别：男|女:")
if sex == "女":
    age = int(input("请输入年龄：:"))
    if age == 18:
        print("进来坐坐")
    else:
        print("隔壁找三哥")
else:
    print("去对门找Alex")

'''#  数字中不是零的都为True?  是的
逻辑运算符：与（ and ）或（ or ）非（not）
True and False - -False
True or False - -True
True and not False - -True
优先级：（） > not > and > or --首先是括号大于not、然后not大于and、然后and大于or
查找顺序：从左向右查找：True and False or True and not False and True - -True
成员运算符： in （在）、not in （不在）
'''
name = "zd"
msg = input("请输入名字：")
if name in msg:
    print(111)
else:
    print(222)

#小数据池--驻留机制  （注意只有字符串和数值有这个概念）
# 在一定范围之内的，共用同一个内存地址。数字 -5~256 节省空间（内存），共用的都是一个小数据池（指向的是同一个内存地址）
# 小整数对象[-5, 257]在python中是共享的
# （注，用列表表示是因为python中含首不含尾，所以［-5，257］表示的范围也就是数字 -5~256。）
# 整数对象都是从缓冲池中获取的。
# 整数对象回收时，内存并不会归还给系统，而是将其对象的ob_type指向free_list，供新创建的整数对象使用
name1 = "meet"
name2 = "meet"
print(id(name1))     # 内存地址：1991535223856
print(id(name2))     # 内存地址一样：1991535223856
name3=name1
print(id(name3))     # 内存地址一样：1991535223856

s5 = 'tiele'
s6 = 'mao'
print('tiele' + 'mao' is 'tielemao')  #  True
print(s5 + s6 is 'tielemao')   # False


# “==” 和 “is” 的区别:
# 前者是相等性比较，比较的是两个对象中的值是否相等. 后者是一致性比较，比较的是两个对象的内存空间地址是否相同。
# 如果内存地址相同，那么它们的值肯定也是一样的，因此，如果 “is” 返回 True，那么 “==” 一定也返回 True，反之却不成立。
# 查看内存地址我们使用的是id()方法：
a = 1000
b = 1000
print(a == b)    # 返回 True  ,  == 比较的是数值
print(a is b)    # 返回的是False
print(id(a))     # 返回的是内存地址，id门牌号之类
print(id(b))

a = 1000
b = a
print(a is b)     # 返回 True

c = 256
d = 256
print(c is d)   # 返回 True

c = 257
d = 257
print(c is d)   # 返回 False
# 将c赋值整型值256，d也为256，e为257，f为257。当把c与d，e与f进行is操作时，却发现两者的布尔值结果不同。
# 为什么呢？这是由python中的整型对象的缓冲池机制引起的。在python中几乎所有的内建对象，都会有自己所特有的对象池机制。

# True and False是来判断选择True还是False
print(True and False)  # False
# True or False  是来判断选择True还是False
print(True or False)  # True
# 1 and 3是为了验证都为真时会选择and那边的内容
print(1 and 3)  # 3
#  1 or 3 是为了验证都为真时会选择or那边的内容
print(1 or 3)  # 1
#  判断下列逻辑语句的结果,一定要自己先分析 (3<4这种是一体)?
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # True
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # False
#  求出下列逻辑语句的值
print(8 or 3 and 4 or 2 and 0 or 9 and 7)  # 8
print(0 or 2 and 3 and 4 or 6 and 0 or 3)  # 4
print(1 and 0 or 8 and 9 and 5 or 2)  # 5
print(4 or 8 and not False and 8 or 9)  # 4
#  下列结果是什么? (2>1这种是一体)
print(6 or 2 > 1)  # 6
print(3 or 2 > 1)  # 3
print(0 or 5 < 4)  # False
print(5 < 4 or 3)  # 3
print(2 > 1 or 6)  # True
print(3 and 2 > 1)  # True
print(0 and 3 > 1)  # 0
print(2 > 1 and 3)  # 3
print(3 > 1 and 0)  # 0

# 编码知识：
# 所有编码底层都是ascii码
# scii编码：支持英文、数字、符号，不支持中文
# 　　 1个英文字母占用空间：1个字节（8位）
# gbk编码：支持英文、数字、符号、中文
# 　　1个英文字母英文占用空间：1个字节（8位）
# 　　1个中文字符占用空间：2个字节（16位）
# Unicode编码：支持英文、数字、符号、中文
# 　　1个英文字母英文占用空间：4个字节、32位
# 　　1个中文字符占用空间：4个字节、32位
# utf-8编码：支持英文、数字、符号、中文
# 　　英文：1个字节、8位
# 　　欧洲文字：2个字节、16位
# 　　亚洲文字（包含中文）：3个字节、24位
# python3内存中使用的就是Unicode(俗称万国码)、不断的使用回收。硬盘中存储时选择的编码方式gbk和utf-8。
# 以什么编码就以什么解码：
s = 'tiele'    # python3默认是Unicode编码
s1 = s.encode('utf-8')      #  unicode ---> utf-8 转码   字符串编码（encode）
s2 = s1.decode('utf-8')     #  utf-8 --->unicode   字符串解码（decode）
# gbk ----> utf-8  两者不能直接进行转换， 都需要借助unicode
s = 'tiele'       # python3默认是Unicode编码
s1 = s.encode('gbk')
s2 = s1.decode('gbk')
s3 = s2.encode('utf-8')
# 或 s2 = s1.decode('gbk').encode('utf-8')
s='中文'
# 如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。
# 这种情况下，要进行编码转换，都需要先用decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。
# 通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件。
# 如果字符串是这样定义：s=u'中文' ，则该字符串的编码就被指定为unicode了