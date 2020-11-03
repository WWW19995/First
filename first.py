#print('Hello World')
#print('人生苦短，我还用Python')
#变量：
#定义：   规则：变量名=数据
#a就是变量的名字，对应一个盒子，里面装的数据就是10
#变量是可以多次赋值的【在程序执行的过程中值可以改变的量】
#变量就是用来存储数据的
a=10      #a是一个变量
print(type(a))       #用print（type（ ））可以查看输入的变量是什么类型
b='Hello World'      #b也是一个变量
print(type(b))
print(a)  #使用变量  先定义变量，然后才能使用
print(b)

#高级类型
c=()    #元组类型
print(type(c))
print(c)
d=[]    #列表类型
print(type(d))
print(d)
e={}    #字典类型
print(type(e))
print(e)

#变量的命名规则
#变量必须以字母（a-z,A-Z）或者下划线（-）开头
#其他字符可以是字母，数字或者-
#变量区分大小写
#Python关键字不能用作变量名
#变量的命名不能以数字开头
Name='王'
name='王'
_age=21
#True=12.3 #不能这样定义，因为True是关键字
print(name,Name)
print(Name,_age)
#命名规范
#尽量使用可以表示含义的单词