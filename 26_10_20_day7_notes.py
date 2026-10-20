#---- split 和 join ----
s = 'A,C,G,T'
print(s.split(','))                       # ['A', 'C', 'G', 'T']
print('-'.join(['A', 'C', 'G', 'T']))     # A-C-G-T
print(''.join(['A', 'C', 'G', 'T']))      # ACGT   空字符串当胶水



#---- split 三兄弟 ----
print(len('a\nb\n'.split('\n')))          # 3   末尾换行会多出一个空字符串
print(len('a\nb\n'.splitlines()))         # 2   没这个问题，读文件用它
print('a  b\nc'.split())                  # ['a', 'b', 'c']   按任意空白切，吞掉空串



#---- match 类型分支 ----
for x in (42, 'abc', [1, 2]):
    match x:
        case int():                       # 类模式，括号不能少
            print('整数')
        case str():
            print('字符串')
        case list():
            print('列表')
        case _:                           # 兜底
            print('其他')

# 整数 / 字符串 / 列表
# case int 不带括号 -> 捕获模式，匹配任何值；后面还有 case 会 SyntaxError



#---- 调用函数 ----
print(abs(-3))                            # 3
print(max([1, 5, 3]))                     # 5
print(int('123') + 1)                     # 124
print(float('1.5'))                       # 1.5
print(bool(0), bool(''))                  # False False
f = abs                                   # 函数名只是引用，能赋给变量
print(f(-7))                              # 7

# int('abc') -> ValueError: invalid literal for int() with base 10: 'abc'



#---- 定义函数 ----
def my_abs(n):
    if n >= 0:
        return n
    return -n                             # 前面已经 return，这里不用写 else
print(my_abs(-3), my_abs(0), my_abs(5))   # 3 0 5


def count_letters(s):
    d = {}                                # 必须在函数里！放外面第二次调用会翻倍
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d
print(count_letters('banana'))            # {'b': 1, 'a': 3, 'n': 2}
print(count_letters('banana'))            # 还是 {'b': 1, 'a': 3, 'n': 2}


def gc_content(seq):
    seq = seq.upper()                     # 统一大写，否则小写全丢
    count = 0
    for ch in seq:
        if ch in 'CG':                    # 只有 C 和 G，不带逗号
            count += 1
    return count / len(seq)
print(gc_content('ACGT'))                 # 0.5
print(gc_content('AAAA'))                 # 0.0
print(gc_content('acgt'))                 # 0.5


def empty():
    pass
print(empty())                            # None   没有 return 就返回 None


#---- 今天踩的坑 ----
# d = {} 写在函数外面     -> 第二次调用结果翻倍（在同一个字典上累加）
# 'C,G' 多了个逗号        -> 逗号被当成碱基算进 GC
# delta 写在 def 前面     -> 函数里看不到外面定义的变量
# 忘写 return             -> 函数返回 None
# return 缩进在 for 里面  -> 循环第一圈就返回，后面的没跑

