# 匿名函数（`lambda`）

## 概览

匿名函数是指没有具体名称的单行轻量级函数。在 Python 中，通过 `lambda` 关键字来创建匿名函数。

当需要执行一段简单且一次性的计算逻辑，或者需要将简短的函数作为参数传递给其他函数时，使用 `lambda` 表达式可以快速构建函数，而无需通过
`def` 编写完整的多行函数结构。

### 基本语法结构

```python
lambda 参数1, 参数2, ...: 表达式
```

- **`lambda` 关键字**：声明这是一个匿名函数。
- **参数列表**：可以声明 0 个、1 个或多个参数，多个参数之间用英文逗号 `,` 分隔，不需要加圆括号。
- **英文冒号 `:`**：用于分隔参数列表与主体表达式。
- **表达式**：冒号后只能是一个单行表达式。表达式的计算结果会 **自动作为该函数的返回值**，无需（也无法）写 `return` 关键字。

---

## 1. 基础直观示例

### 单参数与多参数计算

```python
# 1. 单参数：计算数字的平方
square = lambda x: x ** 2
print(square(5))  # 输出: 25
print(square(8))  # 输出: 64

# 2. 双参数：计算两数相加
add_numbers = lambda a, b: a + b
print(add_numbers(10, 20))  # 输出: 30

# 3. 多参数：计算三数乘积
multiply_three = lambda x, y, z: x * y * z
print(multiply_three(2, 3, 4))  # 输出: 24

# 4. 无参数：返回固定内容或状态
get_greeting = lambda: "你好，Python！"
print(get_greeting())  # 输出: 你好，Python！
```

---

## 2. 结合条件表达式（三元运算）

`lambda` 内部只能写单行表达式，但可以结合 Python 的条件表达式（三元运算符 `值1 if 条件 else 值2`）实现分支判断逻辑：

```python
# 1. 判断奇偶数
is_even = lambda num: "偶数" if num % 2 == 0 else "奇数"
print(is_even(10))  # 输出: 偶数
print(is_even(7))  # 输出: 奇数

# 2. 判断成绩是否及格
check_grade = lambda score: "及格" if score >= 60 else "不及格"
print(check_grade(85))  # 输出: 及格
print(check_grade(45))  # 输出: 不及格

# 3. 获取两数中的较大值
get_max = lambda x, y: x if x > y else y
print(get_max(18, 32))  # 输出: 32
```

---

## 3. 常见直观应用场景

`lambda` 函数最常见的用途是作为参数传递给需要接收函数（如 `key` 规则）的高阶内置函数。

### 1. 作为 `sorted()` 排序规则（`key` 参数）

通过 `lambda` 可以方便地指定复杂的排序依据：

```python
# 场景 A：按字典中的某个键值进行排序
students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72}
]

# 指定按照学生的 score 成绩从低到高排序
sorted_by_score = sorted(students, key=lambda item: item["score"])
print("按成绩升序排序：", sorted_by_score)

# 场景 B：按照字符串长度进行排序
words = ["python", "c", "javascript", "go"]
sorted_by_length = sorted(words, key=lambda s: len(s))
print("按单词长度排序：", sorted_by_length)

# 场景 C：按元组中的第二项（年龄）排序
users = [("张三", 25), ("李四", 18), ("王五", 30)]
sorted_by_age = sorted(users, key=lambda u: u[1])
print("按年龄排序：", sorted_by_age)
```

---

### 2. 配合 `map()` 与 `filter()` 处理序列数据

- **`map(func, iterable)`**：对序列中的每个元素应用 `func` 函数转换。
- **`filter(func, iterable)`**：根据 `func` 返回的真假值筛选序列中的元素。

```python
numbers = [1, 2, 3, 4, 5, 6]

# 配合 map()：对列表中所有数字乘以 10
scaled_numbers = list(map(lambda x: x * 10, numbers))
print("批量放大 10 倍：", scaled_numbers)  # 输出: [10, 20, 30, 40, 50, 60]

# 配合 filter()：筛选出列表中的所有偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("筛选偶数：", even_numbers)  # 输出: [2, 4, 6]
```

---

## 4. `def` 函数与 `lambda` 匿名函数对比

| 特性           | `def` 定义函数                              | `lambda` 匿名函数                         |
|:---------------|:--------------------------------------------|:------------------------------------------|
| **定义语法**   | `def name(args):`                           | `lambda args: expr`                       |
| **是否有名字** | 有显式函数名                                | 本身无名称（可赋值给变量）                |
| **支持的语句** | 支持任意复杂的多行逻辑、循环、异常处理等    | 仅支持单个单行表达式                      |
| **返回值处理** | 需显式通过 `return` 返回结果（默认 `None`） | 表达式计算结果自动作为返回值              |
| **适用场景**   | 复杂业务逻辑、长期维护与反复调用的模块      | 简短单行计算、临时回调、排序 `key` 等场景 |
