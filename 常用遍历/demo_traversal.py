# 常用遍历：展示 range、enumerate、zip 以及字典的 keys、values、items 遍历方法

# ==================== 1. range()：范围与步长遍历 ====================

print("--- 1. range() 基础与步长遍历 ---")

# 单参数：从 0 遍历到 4（不包含 5）
print("range(5) 输出：", end="")
for number in range(5):
    print(number, end=" ")
print()

# 双参数：指定起始值与终止值 [2, 7)
print("range(2, 7) 输出：", end="")
for number in range(2, 7):
    print(number, end=" ")
print()

# 三参数（正步长）：从 1 到 9，每次增加 2
print("range(1, 10, 2) 输出：", end="")
for odd_number in range(1, 10, 2):
    print(odd_number, end=" ")
print()

# 三参数（负步长）：从 10 倒数至 2（不包含 0）
print("range(10, 0, -2) 输出：", end="")
for even_number in range(10, 0, -2):
    print(even_number, end=" ")
print()


# ==================== 2. enumerate()：带索引与自定义起始计数的遍历 ====================

print("\n--- 2. enumerate() 带索引遍历 ---")

fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 默认 start=0 遍历列表
for index, fruit in enumerate(fruits):
    print(f"索引 {index}：{fruit}")

# 自定义 start=1，常用于排名或序号展示
for rank, fruit in enumerate(fruits, start=1):
    print(f"第 {rank} 名：{fruit}")

# 字符串同样支持 enumerate 遍历
greeting = "PYTHON"
for char_index, char in enumerate(greeting):
    print(f"字符 [{char_index}] -> {char}", end=" | ")
print()


# ==================== 3. zip()：多序列并行遍历 ====================

print("\n--- 3. zip() 多序列并行遍历 ---")

student_names = ["小明", "小红", "小刚"]
math_scores = [95, 88, 92]
english_scores = [90, 96, 85]

# 并行遍历两个列表并进行元组解包
for name, score in zip(student_names, math_scores):
    print(f"{name} 的数学成绩为：{score} 分")

# 并行遍历三个列表
for name, math, english in zip(student_names, math_scores, english_scores):
    print(f"{name} -> 数学：{math} 分，英语：{english} 分")

# 长度不一致时，以最短序列为准自动截断
short_labels = ["A", "B"]
long_values = [100, 200, 300, 400]
print("长度不一致时的 zip 遍历结果：")
for label, value in zip(short_labels, long_values):
    print(f"标签 {label} -> 数值 {value}")


# ==================== 4. 字典遍历：keys()、values() 与 items() ====================

print("\n--- 4. 字典遍历（keys, values, items） ---")

employee_salaries = {
    "张三": 12000,
    "李四": 15000,
    "王五": 18000
}

# 1. 遍历字典的键（keys）
print("员工姓名（键）：")
for name in employee_salaries.keys():
    print(f"- {name}")

# 直接遍历字典对象，默认遍历的就是所有的键
print("直接遍历字典（等同于 keys）：")
for name in employee_salaries:
    print(f"- {name}")

# 2. 遍历字典的值（values）
print("薪资列表（值）：")
for salary in employee_salaries.values():
    print(f"- {salary} 元")

# 3. 遍历字典的键值对（items）并解包
print("完整员工薪资信息（键值对）：")
for name, salary in employee_salaries.items():
    print(f"- 员工：{name}，月薪：{salary} 元")


# ==================== 5. for 循环支持的数据类型与 TypeError 报错演示 ====================

print("\n--- 5. for 循环支持的数据类型与 TypeError 报错 ---")

# 1. for 循环要求目标对象必须是可迭代对象（如 list, tuple, str, dict, set, range 等）
valid_collection = [10, 20, 30]
print("可迭代对象（列表）正常遍历：", end="")
for item in valid_collection:
    print(item, end=" ")
print()

# 2. 对非可迭代对象（如 int, float, bool, NoneType）执行 for 遍历会触发 TypeError
invalid_number = 100
try:
    for number in invalid_number:
        print(number)
except TypeError as error:
    print("对整数执行 for 遍历触发的报错：", type(error).__name__, "->", error)

invalid_none = None
try:
    for item in invalid_none:
        print(item)
except TypeError as error:
    print("对 NoneType 执行 for 遍历触发的报错：", type(error).__name__, "->", error)

"""
核心总结：
1. for 循环所需数据类型与报错：
   - 目标对象必须是可迭代对象（Iterable），如 list, tuple, str, dict, set, range, enumerate, zip 及文件对象等；
   - 若对非可迭代对象（如 int, float, bool, NoneType）执行 for 遍历，会触发 TypeError 类型错误（如 `TypeError: 'int' object is not iterable`）。
2. range(start, stop, step)：
   - 生成连续或等间隔的整数序列，区间遵循左闭右开 [start, stop)；
   - 支持负步长实现从大到小的逆向倒数。
3. enumerate(iterable, start=0)：
   - 在遍历可迭代对象的同时生成索引序号，每次迭代产出 (index, item) 元组；
   - 可通过 start 参数指定起始计数值（如 start=1）。
4. zip(*iterables)：
   - 并行聚合多个可迭代对象相同位置的元素并打包为元组；
   - 当多个序列长度不同时，以最短的序列为准自动结束遍历。
5. 字典遍历方法：
   - dict.keys()（或直接遍历字典）：仅遍历字典的所有键（Key）；
   - dict.values()：仅遍历字典的所有值（Value）；
   - dict.items()：遍历包含 (Key, Value) 的元组，通常配合多元赋值直接解包使用。
"""
