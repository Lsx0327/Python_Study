# -*-coding:utf-8 -*-
# -on my iMac-

# @File      : 字串.py
# @Time      : 2022/2/2 下午7:10
# @Author    : Ronchy
'''
问题描述

对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：
00000
00001
00010
00011
00100
'''

'''
1.bin() 二进制函数（type：str）
2.使用python字符串格式化
e.g.
# print('%字符串' %整数）
    print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
>>> 我叫 小明 今年 10 岁!
    %s	 格式化字符串
    %d	 格式化整数
    %u	 格式化无符号整型
    %o	 格式化无符号八进制数
    %x	 格式化无符号十六进制数
    格式化操作符辅助指令： 
    符号	功能
    * 	定义宽度或者小数点精度
    - 	用做左对齐
    + 	在正数前面显示加号( + )
    <sp> 	在正数前面显示空格
    # 	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
    0 	显示的数字前面填充'0'而不是默认的空格
    % 	'%%'输出一个单一的'%'
    (var) 	映射变量(字典参数)
    m.n. 	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
num =1
def number():
    global num
    print('%06d' %(int(bin(num)[2:])))
#0  显示的数字前面填充'0'而不是默认的空格
#6  是显示的最小总宽度
    num = num+1
    if num <=32:
        number()
if __name__ == '__main__':
    number()
    #print(num)