#---- 函数当参数传 ----
print(sorted([36, 5, -12, 9, -21]))                    # [-21, -12, 5, 9, 36]
print(sorted([36, 5, -12, 9, -21], key=abs))           # [5, 9, -12, -21, 36]      按绝对值
print(sorted(['bob', 'About', 'Zoo'], key=str.lower))  # ['About', 'bob', 'Zoo']   忽略大小写
# key= 后面写的是"函数本身"，不带括号；写成 key=len() 会报错



#---- map / filter ----
seqs = ['ACGT', 'GGCC', 'A']
print(list(map(str.lower, seqs)))                      # ['acgt', 'ggcc', 'a']
print(list(filter(lambda s: len(s) > 2, seqs)))        # ['ACGT', 'GGCC']
# 两个返回的都是生成器，想看见结果要 list() 一下



#---- lambda：没有名字的小函数 ----
sq = lambda x: x * x
print(sq(5))                                           # 25
# 等价于  def sq(x): return x * x
# 限制：只能写一个表达式，不能写 if/for 这种语句

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda t: t[1]))                   # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
print(sorted(L, key=lambda t: t[1], reverse=True))     # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]



#---- 组合：数字列表 → 字符串 ----
print(''.join(map(str, [1, 2, 3])))                    # 123
# 拆开看：map 把每个数变成字符串 → '1' '2' '3' → join 用空串拼起来



#---- 今天踩的坑 ----
# key=lambda t: -t[1]      -> 只对数字有效；换成 reverse=True 才通用
# ''.join(list(map(...)))  -> list() 多余，join 直接接受 map 对象
# filter 里的函数用 yield  -> 必须返回 True/False，否则生成器对象永远为真，全部放行
