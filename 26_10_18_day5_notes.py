#---- 循环 ----
for x in range(1, 101):                   # 1 到 100（含头不含尾）
    print(x)

print(list(range(1, 101)))                # [1, 2, 3, ..., 100]   看看 range 到底生成了什么


#---- 累加器 ----
total = 0                                 # 先准备空盒子，这行不能少
for x in range(1, 101):
    total = total + x                     # 每圈往盒子里放
print(total)                              # 5050

total_len = 0
for s in ['ACGT', 'GGCC', 'A']:
    total_len += len(s)                   # 换个数据，结构一模一样
print(total_len)                          # 9


#---- 3 的倍数 ----
for x in range(1, 101):
    if x % 3 == 0:                        # % 取余，==0 表示能整除
        print(x)                          # 3 6 9 ... 99

for x in range(3, 101, 3):                # 另一种写法：第三个数是步长，不用 if
    print(x)                              # 3 6 9 ... 99


#---- while 猜数字 ----
while True:                               # True 就是一直转
    guess = int(input('猜一个数：'))        # input 返回字符串，int() 转整数
    if guess > 7:
        print('大了')
    elif guess < 7:
        print('小了')
    else:
        print('对了')
        break                             # 跳出整个循环


#---- 字典计数 ----
d = {}
for ch in 'banana':
    if ch in d:                           # 见过：原次数 + 1
        d[ch] = d[ch] + 1
    else:
        d[ch] = 1                         # 没见过：记成 1
print(d)                                  # {'b': 1, 'a': 3, 'n': 2}

d = {}
for ch in 'banana':
    d[ch] = d.get(ch, 0) + 1              # 短版本：取不到就给 0
print(d)                                  # {'b': 1, 'a': 3, 'n': 2}


#---- 取值和判断 ----
d = {'a': 3}
print(d['a'])                             # 3
print(d.get('x'))                         # None     取不到不报错，d['x'] 会 KeyError
print('a' in d)                           # True     判断 key 在不在


#---- set 去重 ----
print(set([1, 2, 2, 3, 3, 3]))            # {1, 2, 3}


#---- 字符串切行 ----
text = "第一行\n第二行\n第三行\n第四行\n第五行\n第六行\n第七行"
a = text.split('\n')                      # 按换行切开，得到 7 个元素的列表
print(len(a))                             # 7

print(len('a\nb\n'.split('\n')))          # 3   末尾有换行会多出一个空字符串
print(len('a\nb\n'.splitlines()))         # 2   splitlines 没这个问题

print(a[0:5])                             # 前 5 个（= a[:5]）
print('\n'.join(a[0:5]))                  # 用换行接回去，打印 5 行


#---- 今天写错的 ----
# for x in (1, 101)                      -> 元组不是 range，只输出 1、101，不报错
# sum = sum + x                          -> sum 是内置函数名，TypeError；且漏了 total = 0
# else: None                             -> if 不需要 else，这行是废代码
# range(1, 100)                          -> 到 99 就停，不是 100
