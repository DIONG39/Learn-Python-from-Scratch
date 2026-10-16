#---- 切片 ----
s = 'Hello Python'
print(s[:5])    # 'Hello'           前 5 个
print(s[5:])    # ' Python'         从编号 5 到末尾（开头有个空格）
print(s[-6:])   # 'Python'          最后 6 个
print(s[1:3])   # 'el'              编号 1、2
print(s[::-1])  # 'nohtyP olleH'    整个反转
#编号含"起"不含"止"；s[:n] 前n个 / s[n:] 扔掉前n个 / s[-n:] 最后n个


#---- 三种拼接 ----
name = '小明'; n = 3
print(name,n)    #小明 3            逗号：自动加空格
print(name + ' 有 ' + str(n) + ' 份数据')    #陈可豪 有 3 份数据   加号：数字要 str() 包一层：+ 只能把字符串和字符串拼在一起，不能把字符串和整数拼在一起
print(f'{name} 有 {n} 份数据')      #陈可豪 有 3 份数据   f-string：以后统一用它


#---- list 增删 ----
nums = [3, 1, 4, 1, 5]
print(nums[-1])    #5            取最后一个
print(nums[:3])    #[3, 1, 4]    取前三个
nums.append(9)     #末尾追加
print(nums)        #[3, 1, 4, 1, 5, 9]
print(nums.pop())  #9            删末位并返回它，剩下 [3, 1, 4, 1, 5]
nums.remove(1)     #按"值"删第一个 1
print(nums)        #[3, 4, 1, 5]
nums.insert(2,99)  # 在索引2前插入： [3, 4, 99, 1, 5]
print(nums)
#记法：insert 加在指定位置 / append 加在末尾 / pop 删（不给参数删末位，给参数删指定位）/ remove 按值删

#---- list vs tuple ----
#list 用 []，能改；tuple 用 ()，不能改
#{[1, 2]: 'x'}             -> TypeError: unhashable type: 'list'
#{(1, 2): 'x'}             -> 可以，tuple 不可变，能当 dict 的 key


#---- if / elif / else ----
score = 67
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

#---- match（看懂即可，不要求会写）----
match score:
    case _ if score >= 90:
        print('A')
    case _ if score >= 80:
        print('B')
    case _ if score >= 60:
        print('C')
    case _:
        print('D')
#case _ 是通配符


#---- 今天的坑 ----
#if x = 1: 报错 -> = 是赋值语句、不产生值，if 后面要写 ==
#case x >= 80 不是合法语法，要写成 case x if x >= 80

