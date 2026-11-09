#---- Counter：字符串逐字符数，列表逐元素数 ----
import collections

seq = 'AAGGGCT'
counts = collections.Counter(seq)
print(counts['A'])                       # 2
print(counts['G'])                       # 3
print(counts['C'])                       # 1
print(counts['N'])                       # 0：未出现的元素

antibodies = ['IgG', 'IgM', 'IgG', 'IgA', 'IgG']
counts = collections.Counter(antibodies)
print('IgG的数量' + str(counts['IgG']))    # IgG的数量3
print('IgM的数量' + str(counts['IgM']))    # IgM的数量1
print('IgE的数量' + str(counts['IgE']))    # IgE的数量0

# Counter(...) 用圆括号调用工具，生成一个计数对象。
# counts['IgG'] 用方括号按键查询数量；counts('IgG') 会尝试调用该对象。
# IgG是完整的列表元素，按一次计数，不拆成I、g、G三种字符。
# 模块名collections与Counter的C是固定写法；counts是自取的变量名。


#---- datetime：创建指定时间，读取属性 ----
import datetime

sample_time = datetime.datetime(2026, 12, 8, 14, 20)
print(sample_time)                       # 2026-12-08 14:20:00
print(sample_time.year)                  # 2026
print(sample_time.month)                 # 12
print(sample_time.day)                   # 8
# 依次传年、月、日、时、分；本例未传秒，默认为0。
# 前一个datetime是模块名，后一个datetime是其中的日期时间类型。
# year/month/day是属性，读取时不加括号。


#---- 日期时间 -> 指定格式的字符串 ----
label = sample_time.strftime('%Y%m%d_%H%M')
print(label)                            # 20261208_1420
# strftime可记作str + f(format) + time。
# %Y年份，%m月份，%d日期，%H小时，%M分钟；月份与分钟大小写不同。
# 横线、斜杠、空格、下划线按格式串原样输出。
# 返回值label是字符串，sample_time仍是日期时间对象。
# 曾混用sample与sample_time：变量名应与自己的赋值保持一致。


#---- 字符串 -> 日期时间：格式要描述输入文字 ----
text = '2026/12/08 14:20'
dt = datetime.datetime.strptime(text, '%Y/%m/%d %H:%M')
print(dt)                               # 2026-12-08 14:20:00
# strptime可记作str + p(parse) + time。
# 第一个参数是文字，第二个参数说明原文字的格式。
# 原文有斜杠，格式串也写斜杠。print(dt)显示日期时间对象的默认样子。
# 若再解析'2026/12/08'，仅有日期，新对象的时间部分默认是00:00:00。
# dt是自己取的变量名。上次会话变量丢失时，要重新导入并赋值。


#---- timedelta：时间点加上一段时长 ----
end_time = dt + datetime.timedelta(hours=12)  #也可以加浮点数
print(end_time)                         # 2026-12-09 02:20:00
# timedelta可记成time + delta（变化量）。常用参数有days/hours/minutes。


#---- datetime调用位置：本轮疑问与能运行的写法 ----
# end_time.strftime(格式) 调用已获得的对象的方法。
# datetime.datetime.strftime(end_time, 格式) 也能运行，是显式传入该对象。
# strptime是类型提供的类方法，常用datetime.datetime.strptime(文字, 格式)。
# end_time.strptime(文字, 格式)也能调用类方法，结果由输入文字和格式决定。
# 实际书写先固定为：datetime.datetime.strptime(...) / 时间对象.strftime(...)。
# text.datetime.strptime(...)：字符串上没有datetime属性，会报AttributeError。
# import datetime后直接datetime.strptime(...)：模块里没有这个直接属性。
# 只写timedelta(...)需先单独导入它；本轮统一datetime.timedelta(...)。


#---- itertools：组合、排列、两组条件搭配 ----
import itertools

sites = ['A', 'B', 'C']
times = ['24h', '48h']
pairs = list(itertools.combinations(sites, 2))
order = list(itertools.permutations(sites, 2))
orders = list(itertools.product(sites, times))
print(pairs)                            # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(order)                            # 6种先后顺序，含A-B和B-A
print(orders)                           # 每个位点分别搭配两个时间点
print(len(pairs), len(order), len(orders))  # 3 6 6
# combinations不区分顺序。permutations区分顺序。product从各组输入分别取项。
# 本例输入列表元素彼此不同。r=2表示每组选两个位置。
# 函数产生迭代器，用list收集后可查看、重复访问和求len。


#---- hashlib：计算一段序列文本的MD5摘要 ----
import hashlib

seq = 'ACGA'
data = seq.encode('utf-8')
print(data)                             # b'ACGA'
md5_obj = hashlib.md5(data)
result = md5_obj.hexdigest()
print(result)                           # f59bf72975d1a8b9e7ee393e14e05ad6
# encode把字符串变成字节。hashlib.md5处理字节，返回哈希对象。
# hexdigest返回32个十六进制字符组成的字符串。
# 同一算法处理同样的字节得到同样摘要；哈希可用于数据内容核对。
# 【关于比特(Bit)】 计算机底层由二进制的 0 和 1 组成，1个比特就是 1个二进制位。
#   只要数据里有哪怕“1个比特（bit）”发生翻转（0变成1，或1变成0），
# 【雪崩效应】     MD5 具有极端敏感性。原文哪怕只改动一个字符或一个比特，
#   算出来的 32 位哈希值也会彻底面目全非、完全不相关。
# 【应用场景对比】肉眼肉身辨别仅限“几个字符”的极小文本；
#   而在现实中，哈希主要用于核对几十GB的大文件、软件防篡改、数据库查重。
# 记法：hash + lib；m、d加数字5；hex（十六进制）+ digest（摘要）。


#---- 类和实例：先按样品记录理解 ----
# 最初的练习是class Sample: pass，再用Sample()创建实例，手动绑定name。
# 下面统一用初始化方法填编号。类名Sample自取，首字母大写是命名习惯。
class Sample:  	#Sample 是你给这个模具起的名字
    def __init__(self, name):
        self.name = name

    def label(self):
        return '样品编号' + self.name


sample_a = Sample('A01')
sample_c = Sample('C03')
sample_d = Sample('D04')
print(sample_a.name)                    # A01
print(sample_c.name)                    # C03
print(sample_d.label())                 # 样品编号D04
# __init__前后各两个下划线，在创建实例的初始化过程中自动运行。
# 右侧name是传入的值，左侧self.name是该实例的属性。
# 创建sample_d时self指向这份新记录；调用label时self指向点号左侧实例。


#---- self的传入位置：先找到名字，再执行调用 ----
print(Sample.label(sample_c))            # 样品编号C03：手动传入实例
print(sample_c.label())                  # 样品编号C03：自动传入实例
# 对这里定义的普通实例方法，这两种写法得到相同结果。
# sample_c.label(sample_c) 会额外再传一次实例，引发TypeError。
# 类里的label保存在Sample中；单独写label(sample_c)要能找到类外同名函数。


#---- 类外函数：顶格定义后，可以用习惯的F(x)调用 ----
def label(sample):
    return '样品编号' + sample.name


print(label(sample_c))                   # 样品编号C03：调用顶格定义的函数
# Sample.label和外面的label是两个独立定义的函数，分别在不同位置查找。
# 如果交互环境中旧的类外label还在，裸名调用会找到那个已存在的定义。


#---- 继承：子类沿用父类的初始化和方法 ----
# class AntibodySample(Sample):
#     pass
# ab2 = AntibodySample('Ab2')
# print(ab2.label())                     # 样品编号Ab2
# 以上是覆盖前的原练习，放在注释里保留。


#---- 覆盖与多态：子类提供更具体的label ----
class AntibodySample(Sample):
    def label(self):
        return '抗体样品' + self.name


sample = Sample('S01')
antibody = AntibodySample('Ab2')
for item in [sample, antibody]:
    print(item.label())                 # 样品编号S01 / 抗体样品Ab2
# class头部括号里的Sample表示父类；AntibodySample是子类。
# 子类沿用父类__init__，同时提供自己的label方法。
# 同一句item.label()随实际对象调用不同实现，本轮正确预测并验证了输出。

#---- 本次踩的坑 ----
# counts['A']用方括号查询，Counter(seq)用圆括号调用。
# 日期输入斜杠由strptime格式说明，print日期对象的默认显示使用横线。
# strftime返回字符串，start_time/end_time本身保留日期时间类型。
# datetime.datetime.strptime有模块、类型、方法三层；timedelta直接在模块下。
