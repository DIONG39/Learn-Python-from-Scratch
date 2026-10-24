#---- 列表生成式 ----
print([x * x for x in range(1, 11)])                    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])      # [4, 16, 36, 64, 100]
# 读法：[要什么  for x in 从哪来  if 什么条件下才要]

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])     # ['hello', 'world', 'apple']
# if 必须写在 .lower() 之前，否则 18 和 None 会先报错

seqs = ['ACGT', 'GGCC', 'A']
print([len(s) for s in seqs])                           # [4, 4, 1]
# 自己写的函数也一样：[gc(s) for s in seqs] -> [0.5, 1.0, 0.0]



#---- 切片 ----
nums = list(range(100))
print(nums[:10])          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]      前 10 个
print(nums[-10:])         # [90, 91, ..., 99]                  后 10 个
print(nums[10:20])        # [10, 11, ..., 19]                  第 11-20 个数是 [10:20]，索引从 0 开始
print(nums[:10:2])        # [0, 2, 4, 6, 8]                     第三个参数是步长
print(nums[::5])          # [0, 5, 10, 15, ..., 95]            全部里每 5 个取 1 个

print((0, 1, 2, 3, 4, 5)[:3])        # (0, 1, 2)      tuple 切片，结果还是 tuple
s = 'ACGTACGT'
print(s[:3], s[-3:], s[::-1])        # ACG CGT TGCATGCA       [::-1] 是反转



#---- 切片是拷贝，不是视图 ----
M = nums[:]               # 复制一份
M[0] = 990
print(M[0], nums[0])      # 990 0      改副本，原列表不变



#---- 迭代：遍历字典 ----
d = {'a': 1, 'b': 2, 'c': 3}

for k in d:               # 默认遍历的是 key，不是键值对
    print(k)              # a  b  c
for v in d.values():
    print(v)              # 1  2  3
for k, v in d.items():
    print(k, '->', v)     # a -> 1 / b -> 2 / c -> 3

print([k + '=' + str(v) for k, v in d.items()])     # ['a=1', 'b=2', 'c=3']



#---- enumerate：同时拿下标和元素 ----
for i, x in enumerate(['x', 'y', 'z']):
    print(i, x)           # 0 x / 1 y / 2 z

for i, base in enumerate('ACGTACGT'):
    if base == 'G':
        print(i)          # 2 6      找某个碱基在第几位，全靠它



#---- 今天踩的坑 ----
# nums[11:20] 想取"第 11 到 20 个数"  -> 少一个，应是 nums[10:20]（索引从 0 开始）
# 函数名和变量名都叫 GC_PCT            -> 结果被赋值后把函数覆盖成 list，再调用报 'list' object is not callable
# for x in d 以为是键值对               -> 默认只给 key，要 items() 才有两个
# findMinAndMax 把 max(L) 写在循环里    -> O(n²)，3000 个元素 0.17 秒；初值用 L[0]，不能用 0（全负数会出错）
