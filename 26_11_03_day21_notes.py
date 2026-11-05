#---- print 调试：看见中间值，找到赋值覆盖 ----
# 原错误：循环里写 total = len(seq)，每轮覆盖，最后只剩最后一条长度。
# 输入 ['ACGT', 'GG', 'A'] 时，错误 total 依次为 4、2、1。
# 调试时把打印放在被观察语句之后，注意与循环体缩进对齐。
def total_length(seqs):
    total_length = 0
    for seq in seqs:
        total_length = total_length + len(seq)
    return total_length


running_total = 0
for seq in ['ACGT', 'GG', 'A']:
    running_total = running_total + len(seq)
    print(seq, running_total)           # ACGT 4 / GG 6 / A 7

print(total_length(['ACGT', 'GG', 'A']))  # 7
print(total_length([]))                 # 0
# 空列表不进入循环，但循环前已经赋值为 0，最后仍可返回 0。
# 自己最初用 i 和 I：合法，但容易看混；total_length/seq 更清楚。


#---- assert：检查预期，失败会抛出 AssertionError ----
assert total_length(['AT', 'G', '']) == 3, '总长度应为3'
assert total_length([]) == 0, '空列表总长度应为0'
print('两项检查通过')                    # 两项检查通过
# assert 条件, '失败提示'
# 条件成立：继续；条件不成立：抛错，没有捕获就中断后续正常流程。
# assert total_length(['ACGT', 'GG', 'A']) == 6, '总长度计算不正确'
# 上面是故意失败的示例，保留为注释，不自动执行。
# 开发时自检可用 assert；必须执行的输入检查使用 if ... raise ...。
# Python 的优化运行模式可以关闭 assert。


#---- logging：在单独 .py 文件中练习，日志门槛可统一调整 ----
# import logging
# logging.basicConfig(level=logging.INFO)
# seqs = ['AT', 'G', '']
# logging.debug('准备进入循环')          # INFO 门槛下不显示
# logging.info('开始检查序列')
# for seq in seqs:
#     if seq == '':
#         logging.warning('发现一条空序列')
# logging.info('序列检查结束')
# INFO 门槛下输出：
# INFO:root:开始检查序列
# WARNING:root:发现一条空序列
# INFO:root:序列检查结束
# 改成 level=logging.WARNING，保存并重新启动脚本，只显示 WARNING 那行。
# DEBUG < INFO < WARNING < ERROR < CRITICAL。
# 日志消息本身不会自动 raise；例如 logging.error(...) 只是记录消息。
# basicConfig 在已配置日志的交互进程中可能不生效，本次以新启动脚本验收。


#---- pdb：暂停后看变量，以屏幕箭头指向的位置为准 ----
# def debug_total_length(seqs):
#     x = 0
#     for seq in seqs:
#         total = len(seq)
#         breakpoint()
#         x = total + x
#     return x
# print(debug_total_length(['ACGT', 'GG', 'A']))
# 终端：python3 debug_practice.py
# (Pdb) p seq       # 查看当前序列
# (Pdb) p total     # 查看当前长度
# (Pdb) p x         # 查看累计长度
# (Pdb) n           # 下一步；再看箭头，确认刚刚执行了哪一行
# (Pdb) c           # 继续到下一个断点或程序结束
# (Pdb) q           # 退出调试，可能显示 BdbQuit；不是统计函数本身的错误
# 箭头指向尚未执行的行。首次可能仍停在 breakpoint() 所在行。
# 如果 n 后 x 仍为 0，先看是否才走到累加行，不要直接认定累加失效。
# 本次第二轮实际验证：seq='GG'，total=2，累加前 x=4，累加后 x=6。
# 调试完成后删除或注释 breakpoint()，避免日常运行反复暂停。


#---- 文本输入到统计输出：一行一条序列 ----
# 下面整段另存为 read_sequences.py；输入与运行位置需对应。
# with open('sequences.txt', 'r', encoding='utf-8') as f:
#     seqs = f.read().splitlines()
#
# total_length = 0
# for seq in seqs:
#     total_length = total_length + len(seq)
#
# with open('result.txt', 'w', encoding='utf-8') as f:
#     f.write('序列条数:' + str(len(seqs)) + '\n')
#     f.write('所有序列的总长度:' + str(total_length) + '\n')
# 输入 ACGT / GG / A / AT：条数 4，总长度 9。
# 闭卷整合改为 ACGT / GG / AT：条数 3，总长度 8。
# 真正空文件：条数 0，总长度 0；代码未额外过滤空行或清理序列。
# len(seqs) 是列表元素数，标签应写“序列条数”，不写“系列的长度”。
# f 是打开的文件对象；f.read() 得到字符串，再 splitlines() 得到列表。
# 离开 with 缩进范围后文件关闭，已读出的变量仍可使用。
# write 接收字符串，不会自动换行；str() 和 '\n' 分别负责转换与换行。
# 'UTF-8' 也能用；日常统一写 encoding='utf-8'。


#---- “看起来是空文件”不一定真正没内容 ----
for text in ['', '\n']:
    seqs = text.splitlines()
    print(repr(text), seqs, len(seqs))
# '' [] 0
# '\n' [''] 1‘’
# repr(text) 把换行符显示出来，便于定位看不见的字符。
# 本次“空文件条数1，总长0”实际读到 '\n'，所以统计逻辑没有出错。
# 临时造真正空文件可用：
# with open('empty.txt', 'w', encoding='utf-8') as f:
#     pass
# 不要把清空 sequences.txt 的这段临时代码留在正式统计脚本开头！
# w 每次都会清空已有文件，数据还没读取就会丢失。


#---- pathlib：描述路径、创建目录、写文件、列出名字 ----
# import pathlib
# base = pathlib.Path.cwd()
# folder = base / 'practice2'
# folder.mkdir(exist_ok=True)
#
# output_file = folder / 'note.txt'
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.write('第二次路径练习\n')
#
# for path in folder.iterdir():
#     print(path.name)                 # note.txt（若目录里仅有这个文件）
# 终端：cat practice2/note.txt          # 显示文件里的文字
# cwd = current working directory。相对路径按当前工作目录解释。
# Path.cwd() 获取当前目录；Path('sequences.txt').resolve() 解析为完整路径。
# / 用在路径对象上表示拼接，不是除法，也不会创建目录或文件。
# mkdir 中 dir 是 directory；exist_ok=True 允许同名目录已存在。
# 已存在的是同名普通文件时，不能靠 exist_ok=True 把它当目录使用。
# open(..., 'w') 创建或打开文件；父目录需要已经存在。
# iterdir() 返回目录直接内容的迭代器，不包含该目录自身，不递归进入子目录。
# path.name 是属性，不加括号；可取得文件或目录最后一级名字，保留扩展名。
# 文件类型由文件系统记录，.txt 后缀是命名习惯，不能决定实际类型。
# base 下的 result.txt 与 base/results/result.txt 是两个不同位置的文件。


#---- 廖雪峰13.3与本轮的对应：工具不同，核心目标相同 ----
# 教材主用 os/os.path，本轮主用 pathlib；两套均为 Python 标准库。
# 当前目录：os.path.abspath('.')      <-> pathlib.Path.cwd()（用途对应）
# 拼接路径：os.path.join(base, 'x')    <-> base / 'x'（base 为 Path 对象）
# 创建目录：os.mkdir(folder)          <-> folder.mkdir()
# 列目录：os.listdir(folder)          <-> folder.iterdir()
# os.listdir 给出名字列表；iterdir 给出路径对象，返回类型并不相同。
# os.mkdir 没有 exist_ok 参数；本轮用 Path.mkdir(exist_ok=True)。
# 完成的是清单要求的拼路径、建目录、列文件，未宣称教材整章全部学完。
# 系统信息、环境变量、删除、重命名、后缀筛选等内容未逐项实操。

#---- 这次踩的坑和学习记录 ----
# 1. 用赋值代替累加：只保留最后一条序列长度。
# 2. 把日志级别当成只显示“这一种”：实际上还会显示更严重的级别。
# 3. pdb 按一次 n 后变量未变：先确认箭头位置，再判断累加是否执行。
# 4. 忘记 read().splitlines()：先得到全文，再按行拆分，注意括号。
# 5. 忘记 encoding 的值：统一使用 'utf-8'，不用每次另想一种拼写。
# 6. f.wirte 拼错：正确是 f.write；iterdir = iter + dir。
# 7. 以为拼好了路径就会出现文件夹：实际创建要执行 mkdir。
# 8. mkdir 创建文件夹，open 的 w 模式创建/清空文件；名字不能决定类型。
# 9. 跟写成功不等于能独立组织：后来改成逐行回忆、提交未完成草稿、撤提示。
# 第19条最后短测：无名称提示答对 mkdir、exist_ok、write、iterdir。

