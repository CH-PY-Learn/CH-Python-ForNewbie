# 常用遍历

## 概览

在 Python 中，遍历的核心机制是通过 `for ... in ...` 逐项获取数据。除了使用基础的 `for item in sequence` 进行单变量顺序遍历之外，针对不同场景还提供了多种高效的遍历工具与方法：

- **`range()`**：按指定数值范围与步长进行循环与计数遍历。
- **`enumerate()`**：在遍历元素的同时自动生成对应的索引序号。
- **`zip()`**：将多个序列对应位置的元素“打包”并进行多序列并行遍历。
- **字典遍历（`keys()`、`values()`、`items()`）**：分别按键、按值或按键值对遍历字典内容。

---

## 1. `for` 循环支持的数据类型与报错类型

### 支持的数据类型（可迭代对象）

`for` 循环语句的基本语法结构为 `for 变量 in 目标对象:`，其中 **目标对象必须是可迭代对象（Iterable）**。

Python 中支持 `for` 循环遍历的常见数据类型包括：
- **序列类型**：列表（`list`）、元组（`tuple`）、字符串（`str`）、`range` 对象等。
- **映射与集合**：字典（`dict`，默认遍历其所有的键）、集合（`set`）。
- **迭代生成对象**：`enumerate` 对象、`zip` 对象、打开的文件对象（File Object）等。

### 不支持的数据类型与报错类型

当尝试对 **非可迭代对象（Non-iterable）** 使用 `for` 循环进行遍历时，Python 解释器在运行时会抛出 **`TypeError`** 类型错误。

常见触发 `TypeError` 的非可迭代类型与控制台报错信息：

| 目标数据类型 | 遍历代码示例 | 触发的报错类型与信息 |
| :--- | :--- | :--- |
| 整数（`int`） | `for i in 100:` | `TypeError: 'int' object is not iterable` |
| 浮点数（`float`） | `for i in 3.14:` | `TypeError: 'float' object is not iterable` |
| 布尔值（`bool`） | `for i in True:` | `TypeError: 'bool' object is not iterable` |
| 空值（`NoneType`） | `for i in None:` | `TypeError: 'NoneType' object is not iterable` |

---

## 2. `range()`：范围与计数遍历

`range()` 函数用于生成一个不可变的整数序列，常用于控制循环执行次数、按步长跳跃访问或生成数值范围。

### 语法形式

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

- **`stop`**：终止数值（不包含该值，遵循左闭右开区间 `[0, stop)`）。
- **`start`**：起始数值，默认值为 `0`。
- **`step`**：步长，即每次递增（正数）或递减（负数）的间隔，默认值为 `1`。

### 示例代码

```python
# 1. 单参数：从 0 遍历到 4（不包含 5）
for i in range(5):
    print(i, end=" ")  # 输出：0 1 2 3 4
print()

# 2. 双参数：从 2 遍历到 6（不包含 7）
for i in range(2, 7):
    print(i, end=" ")  # 输出：2 3 4 5 6
print()

# 3. 三参数（正步长）：从 1 开始，步长为 2
for i in range(1, 10, 2):
    print(i, end=" ")  # 输出：1 3 5 7 9
print()

# 4. 三参数（负步长）：从 10 倒数到 2（不包含 0）
for i in range(10, 0, -2):
    print(i, end=" ")  # 输出：10 8 6 4 2
print()
```

---

## 3. `enumerate()`：带索引的遍历

当在遍历序列的同时需要获取每个元素对应的 **索引序号（Index）** 时，使用 `enumerate()` 可以直接生成 `(索引, 元素)` 元组。

### 语法形式

```python
enumerate(iterable, start=0)
```

- **`iterable`**：任何可迭代对象（如列表、元组、字符串等）。
- **`start`**：索引计数的起始值，默认值为 `0`；若传入其他整数（如 `1`），则序号从该数值开始递增。

### 示例代码

```python
fruits = ["apple", "banana", "cherry"]

# 默认从索引 0 开始
for index, fruit in enumerate(fruits):
    print(f"索引 {index} 处的元素是 {fruit}")
# 输出：
# 索引 0 处的元素是 apple
# 索引 1 处的元素是 banana
# 索引 2 处的元素是 cherry

# 自定义从序号 1 开始计数
for rank, fruit in enumerate(fruits, start=1):
    print(f"第 {rank} 名：{fruit}")
# 输出：
# 第 1 名：apple
# 第 2 名：banana
# 第 3 名：cherry
```

---

## 4. `zip()`：多序列并行遍历

`zip()` 函数用于将多个可迭代对象（如多个列表、元组）中 **相同索引位置** 的元素依次组合打包成元组，从而实现多个序列的同时遍历。

### 语法形式

```python
zip(*iterables)
```

- **`*iterables`**：一个或多个可迭代对象。
- **长度对齐机制（短板效应）**：当传入的多个序列长度不同时，`zip()` 会在 **最短的序列耗尽时立即停止遍历**，多余的元素会被忽略。

### 示例代码

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]
cities = ["Beijing", "Shanghai", "Guangzhou"]

# 并行遍历两个列表并进行元组解包
for name, score in zip(names, scores):
    print(f"{name} 的得分是 {score}")
# 输出：
# Alice 的得分是 95
# Bob 的得分是 88
# Charlie 的得分是 92

# 并行遍历三个列表
for name, score, city in zip(names, scores, cities):
    print(f"{name} 来自 {city}，得分为 {score}")

# 序列长度不同时的行为：以最短序列为准
short_list = [1, 2]
long_list = ["a", "b", "c", "d"]
for num, char in zip(short_list, long_list):
    print(num, char)
# 输出：
# 1 a
# 2 b
```

---

## 5. 字典遍历：`keys()`、`values()` 与 `items()`

字典（`dict`）由键值对（Key-Value Pair）构成，Python 提供了三种视图方法来满足不同的遍历需求：

### 遍历方式对比

| 方法 / 语法 | 每次迭代返回的内容 | 常见应用场景 |
| :--- | :--- | :--- |
| `dict.keys()` / 直接遍历 `dict` | 字典的所有 **键（Key）** | 仅需要获取属性名、键名，或根据键查询对应值 |
| `dict.values()` | 字典的所有 **值（Value）** | 仅需要数据本身，如对所有数值求和、求极值或平均数 |
| `dict.items()` | 包含 **`(键, 值)` 的元组** | 同时需要使用键和值，通常配合多元赋值解包使用 |

### 示例代码

```python
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}

# 1. 遍历所有的键（keys）
# 注：直接遍历字典对象 `for name in student_scores:` 与遍历 `.keys()` 效果一致
for name in student_scores.keys():
    print("学生姓名（键）：", name)

# 2. 遍历所有的值（values）
for score in student_scores.values():
    print("学生成绩（值）：", score)

# 3. 遍历所有的键值对（items）并解包
for name, score in student_scores.items():
    print(f"学生 {name} 的成绩为 {score} 分")
```

---

## 常用遍历速查表

| 遍历方式 / 函数 | 语法示例 | 每次迭代获取的内容 | 核心特点 |
| :--- | :--- | :--- | :--- |
| `for ... in` | `for item in iterable:` | 单个元素 `item` | 遍历可迭代对象；若用于非可迭代对象（如 `int`、`None`）则触发 `TypeError` |
| `range()` | `for i in range(start, stop, step):` | 整数数值 `i` | 左闭右开区间 `[start, stop)`，支持指定正负步长 |
| `enumerate()` | `for index, item in enumerate(seq, start=0):` | `(index, item)` 元组 | 原生获取下标与元素，支持自定义起始序号 `start` |
| `zip()` | `for a, b in zip(seq_a, seq_b):` | `(a, b, ...)` 元组 | 多序列并行对齐打包，长度以最短序列为准 |
| `dict.keys()` | `for key in my_dict.keys():` | 字典的键 `key` | 仅读取字典键，直接遍历 `my_dict` 效果相同 |
| `dict.values()` | `for val in my_dict.values():` | 字典的值 `val` | 仅读取字典值，常用于数值汇总统计 |
| `dict.items()` | `for key, val in my_dict.items():` | `(key, val)` 键值对元组 | 同时获取键与值，配合解包直接使用两个变量 |
