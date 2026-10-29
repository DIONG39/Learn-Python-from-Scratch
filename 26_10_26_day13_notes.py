#---- 生成器表达式 ----
g = (x * x for x in range(1, 11))      # 圆括号：只建一个"待办"，一个都不算
print(type(g))                         # <class 'generator'>
print(next(g), next(g))                # 1 4        要一个才给一个
print(list(g))                         # [9, 16, 25, 36, 49, 64, 81, 100]   把剩下的取完
print(list(g))                         # []         用完就空了，不能再来一次



#---- 生成器函数 yield ----
def squares(n):
    for i in range(1, n + 1):
        yield i * i                    # 给一个，停住；下次从这儿接着跑

q = squares(3)                         # 这一刻函数体一行都没跑
print(type(q))                         # <class 'generator'>
print(next(q))                         # 1
print(next(q))                         # 4
print(next(q))                         # 9
# 第四次 next(q) -> StopIteration



#---- Iterable 与 Iterator ----
from collections.abc import Iterable, Iterator
print(isinstance([1, 2], Iterable))    # True     能用 for 遍历
print(isinstance([1, 2], Iterator))    # False    不能直接 next
it = iter([1, 2, 3])                   # iter() 把列表转成迭代器
print(isinstance(it, Iterator))        # True
print(next(it), next(it), next(it))    # 1 2 3
# 第四次 next(it) -> StopIteration      for 循环就是靠接住它停下来的



#---- 今天踩的坑 ----
# next(g) 先吃掉一个        -> 后面的 for 从第二个开始，第一个丢了
# 生成器只能遍历一次        -> 第二次 list(g) 是空的，要重新生成
# iter(['a,b,c'])           -> 这是一个元素的列表，只能 next 一次（不是迭代器的问题）
# sorted(L, key=f())        -> key 要函数本身，不能带括号
