#————字符 vs 字节----
print(len('中文'))                        # 2  字符数
print(len('中文'.encode('utf-8')))        # 6  字节数（每个中文3字节）


#---- str vs bytes 转换----
print('中文'.encode('utf-8'))             # b'\xe4\xb8\xad\xe6 \x96\x87'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))    # '中文'


# --- 编码编号 ---
print(ord('中'))    #20013
print(chr(20013))    #'中'


# --- 格式化 ---
x = 0.18055
print(f'{x:.2f}')    # 0.18    只看小数
print(f'{x:.1%}')    # 18.1%   自动x100＋%
print(f'{x*100:.1f}')    #18.1%    自己x100

