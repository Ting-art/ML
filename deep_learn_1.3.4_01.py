# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:48:31 2019

@author: 清矿轩
"""
#列表
a=[1,2,3,4,5]#创建列表
print(a)#输出列表的内容
print(len(a))#获取列表的长度
print(a[0])#访问列表的第一个值
a[4]=99#赋值
print(a)
print(type(a))
print(a[0:2])
print(a[:3])
print(a[:-1])
#字典
me={'height':180}#生成字典
print(me['height'])#访问元素
me['weight']=70#添加新元素
print(me)
print(type(me))
#布尔型
hungry=True#饿了
sleepy=False#困了
print(type(hungry))
print(not hungry)
#if 语句
hungry=True
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    pass
#for 语句
for i in [1,2,3]:
    print(i)
    pass
#函数
def hello(object):
    print("Hello "+object+"!")
    pass
hello("cat")
#类
class Man:
    def __init__(self,name):
        self.name=name
        print("Initializaed")
        
    def hello(self):
        print("Hello "+self.name+"+")
        
    def goodbye(self):
        print("Good-bye "+self.name+"+")

m=Man("David")
m.hello()
m.goodbye()
#Numpy数组
import numpy as np
x=np.array([1.0,2.0,3.0])
print(x)
print(type(x))
y=np.array([2.0,4.0,6.0])
print(x*y)
A=np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)
A=np.array([[1,2],[3,4]])
B=np.array([10,20])
print(A*B)
#访问元素
X=np.array([[51,55],[14,19],[0,4]])
print(X[0])
print(X[0][1])
for row in X:
    print(row)
#将X转换为一维数组
X=X.flatten()
print(X)
print(X>15)
print(X[X>15])
#画图
import matplotlib.pyplot as plt
from matplotlib.image import imread
#生成数据
x=np.arange(0,6,0.1)
y1=np.sin(x)
y2=np.cos(x)

#绘制图形
plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")#用虚线绘制
plt.xlabel("x")#x轴标签
plt.ylabel("y")#y轴标签
plt.title('sin&cos')#标题
plt.legend()
plt.show()
img=imread('lena.jpg')
plt.imshow(img)
plt.show()