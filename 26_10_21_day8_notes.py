#---- 可变参数 *args ----
def mul(*numbers):                        # 参数前加 *，调用时可以传任意多个
    if len(numbers) == 0:                 # 空参数要报错
        raise TypeError('参数不能为空')
    product = 1                           # 盒子必须放在循环外面！
    for n in numbers:
        product = product * n
    return product

print(mul(1, 2, 3, 4))                    # 24
print(type((1, 2, 3)))                    # <class 'tuple'>   numbers 拿到的是元组

# mul() -> TypeError: 参数不能为空



#---- 参数检查 ----
def mul2(*numbers):
    if len(numbers) == 0:
        raise TypeError('参数不能为空')
    product = 1
    for n in numbers:
        if not isinstance(n, (int, float)):   # 判断单个元素，必须放在循环里
            raise TypeError('参数必须是数字')
        product = product * n
    return product

print(mul2(1, 2, 3))                      # 6

# mul2('a', 2) -> TypeError: 参数必须是数字
# isinstance(*numbers, int) -> TypeError: isinstance expected 2 arguments, got 4




#---- 默认参数 ----
def gc(seq, upper=True):                  # upper=True 是默认值，调用时可以不传
    if len(seq) == 0:
        return 0.0
    if upper:                             # 这个开关必须真的用上，否则传了也没反应
        seq = seq.upper()
    GC_count = 0
    for x in seq:
        if x in 'GC':
            GC_count = GC_count + 1
    return GC_count / len(seq)

print(gc('ACGT'))                         # 0.5
print(gc('acgt'))                         # 0.5   upper 默认 True，先转大写
print(gc('acgt', False))                  # 0.0   关掉开关，小写不算



#---- 关键字参数 ----
def info(name, age, city='开封'):
    print(name, age, city)

info('小明', 23)                         # 小明 23 开封     位置参数：按顺序传
info(age=23, name='小明')                # 小明 23 开封     关键字参数：按名字传，顺序可以乱



#---- 默认参数不要用可变对象 ----
def add(x, L=[]):                         # 这个 [] 只在定义时创建一次
    L.append(x)
    return L

print(add(1))                             # [1]
print(add(2))                             # [1, 2]   不是 [2]！两次共用同一个列表


def add_ok(x, L=None):                    # 正确写法：默认值给 None，进函数再新建
    if L is None:
        L = []
    L.append(x)
    return L

print(add_ok(1))                          # [1]
print(add_ok(2))                          # [2]      每次都是新的



#---- 今天踩的坑 ----
# product = 1 写在循环里        -> 每圈清零，mul(1,2,3,4) 返回 4，且不报错
# isinstance(*numbers, int)     -> * 是拆包，isinstance 收到 4 个参数 -> TypeError
# isinstance(numbers, int)      -> numbers 是元组，永远 False
# 签名写了 upper=True 但函数体没用 -> gc('acgt', False) 也照样返回 0.5
# return = 0.0                  -> 语法错，return 后面不能有 =
# def f(x, L=[]) 连续调用两次    -> 共用同一个列表，第二次结果带上第一次
