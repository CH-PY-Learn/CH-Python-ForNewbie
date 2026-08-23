# 定义函数

## 概览

函数是将一段具有特定功能的代码组织在一起并命名的代码块。通过使用函数，可以将重复使用的逻辑封装起来，在需要时通过函数名进行调用，从而提高代码的复用性与结构清晰度。

在 Python 中，使用 `def` 关键字来定义一个函数。

### 基本语法结构

```python
def 函数名(参数1, 参数2: 类型 = 默认值, ...) -> 返回值类型:
    """函数文档说明（一般写项目时会写）"""
    函数体代码
    return 返回值  # 可选
```

- **`def`**：定义函数的关键字（define 的简写）。
- **函数名**：遵循 Python 标识符命名规范，通常使用小写字母和下划线组合（如 `calculate_total_price`）。
- **参数列表**：括号 `()` 内声明接收的参数；可设置默认值与类型注解；若不需要参数，保留空括号 `()`。
- **英文冒号 `:`**：函数头部末尾必须包含英文冒号。
- **函数体**：冒号后缩进的代码块，是函数被调用时实际执行的逻辑。

---

## 1. 无 `return` 的函数

无 `return` 语句的函数通常用于执行某种特定的操作（如打印输出、处理数据或修改可变对象），而不需要向调用者传递计算结果。

### 语法与执行特点

- 函数体内没有写 `return` 语句，或者单独写了 `return` 但未指定任何返回值。
- 在 Python 中，当函数执行完毕且没有显式返回值时，函数会**默认返回 `None`**。

### 代码示例

```python
# 1. 纯执行打印操作，无 return
def greet_user(username):
    print(f"欢迎，{username}！")


# 调用函数
result = greet_user("张三")
# 打印返回值，观察其默认返回 None
print("函数返回值：", result)  # 输出：函数返回值： None


# 2. 单独使用 return 用于提前终止函数执行
def check_temperature(temp_value):
    if temp_value < 0:
        print("温度低于零度，已结冰")
        return  # 提前结束函数执行，后续代码不再运行
    print(f"当前温度正常：{temp_value}℃")


check_temperature(-5)
check_temperature(25)
```

---

## 2. 有 `return` 的函数

有 `return` 语句的函数用于将函数内部的计算结果或处理后的数据返回给调用者，调用者可以使用变量接收该返回值并参与后续的计算或逻辑处理。

### 语法与执行特点

- **`return 表达式`**：执行到 `return` 语句时，计算表达式的值并将其作为函数的输出结果返回。
- **立即终止**：一旦执行到 `return` 语句，函数将立即结束执行，`return` 之后的代码将不会被运行。
- **支持多返回值**：`return` 可以同时返回多个值，各个值之间用逗号 `,` 分隔。Python 会自动将多个返回值打包成一个**元组（`tuple`）**返回，接收时可以直接解包。

### 代码示例

```python
# 1. 返回单个计算结果
def add_numbers(num_a, num_b):
    total = num_a + num_b
    return total


sum_result = add_numbers(15, 25)
print("计算相加结果：", sum_result)  # 输出：40


# 2. 结合条件分支返回不同结果
def get_absolute_value(number):
    if number < 0:
        return -number
    return number


print("绝对值：", get_absolute_value(-10))  # 输出：10
print("绝对值：", get_absolute_value(8))   # 输出：8


# 3. 返回多个值（自动打包为元组）
def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter  # 返回面积与周长两个值


# 接收打包的元组
rect_info = calculate_rectangle(5, 3)
print("返回的元组：", rect_info)  # 输出：(15, 16)

# 直接多元赋值（解包接收）
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"矩形面积：{rect_area}，矩形周长：{rect_perimeter}")
```

---

## 3. 默认参数值（如 `a=None`）

默认参数允许在定义函数时为某个形参指定一个默认值。当调用者未向该参数传递实参时，函数会自动使用设定的默认值。

### 语法与用途

- **语法结构**：`def 函数名(形参名=默认值):`
- **可选参数机制**：为参数赋予默认值后，该参数在调用时变为可选（Optional），调用者可传可不传。
- **`a=None` 的常见用途**：
  1. **占位与可选标记**：使用 `None` 作为未传参的空状态标记，函数内部可通过 `if a is None:` 分支判断调用者是否提供了有效数据。
  2. **避免可变默认参数共享**：在 Python 中，函数的默认参数在函数定义时仅被求值一次。若使用可变对象（如 `list`、`dict`）作为默认值（例如 `def func(lst=[]):`），多次调用会共享同一个对象。使用 `lst=None` 并在函数体内动态初始化（`if lst is None: lst = []`）可确保每次调用创建独立的新对象。
- **位置规则**：带有默认值的参数必须声明在所有无默认值参数的**右侧**，否则会触发语法错误 `SyntaxError`。

### 代码示例

```python
# 1. 基础默认参数
def show_welcome(username, role="普通用户"):
    print(f"用户：{username}，身份：{role}")


show_welcome("张三")               # 未传 role，使用默认值 "普通用户"
show_welcome("李四", "系统管理员")  # 传递实参，覆盖默认值


# 2. a=None 作为可选参数占位
def send_notification(content, title=None):
    if title is None:
        title = "系统提示"
    print(f"【{title}】{content}")


send_notification("您的订单已送达")
send_notification("账号异地登录", "安全告警")


# 3. a=None 避免可变默认参数共享
def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []  # 每次调用独立创建新列表
    task_list.append(task_name)
    return task_list


print(add_task("阅读文档"))  # 输出: ['阅读文档']
print(add_task("提交代码"))  # 输出: ['提交代码']（不会累积上一次的内容）
```

---

## 4. 类型注解与类型提示（如 `a: None`）

类型注解（Type Hints）是 Python 3 引入的语法特性，用于显式声明变量、函数参数以及返回值的预期数据类型。

### 语法与用途

- **形参类型注解**：`def func(a: int, b: str):` 在形参名后加 `: 类型`。
- **返回值类型注解**：`def func(...) -> 返回类型:` 在括号后加 `-> 类型`。
- **结合默认参数**：`def func(a: str = "默认值", b: int | None = None):` 先写冒号与类型，再写等号与默认值。
- **核心用途**：
  1. **提高代码可读性**：使调用者无需阅读函数内部细节即可知晓参数与返回值的预期结构。
  2. **IDE 智能提示与补全**：IDE（如 PyCharm）根据注解提供精准的代码自动补全和参数类型提示。
  3. **静态类型检查**：配合静态分析工具（如 `mypy`）在代码运行前排查潜在的类型不匹配错误。

### `a: None` 与 `-> None` 的具体含义

- **`a: None`**：声明形参 `a` 的预期类型为 `None`（即 `NoneType`）。通常用于要求或预期调用者传入 `None`，或与联合类型组合使用（如 `a: int | None = None`，表示参数可为整数或 `None`）。
- **`-> None`**：声明该函数没有显式返回值（执行完毕后默认返回 `None`）。

### 关键机制说明：非运行时强制性约束

Python 在运行时**不会**对类型注解做强制检查或类型拦截。即使传入与注解不符的类型，只要代码内部操作支持，Python 解释器依然会正常执行。类型注解本质上是附着在函数对象 `__annotations__` 属性上的**元数据（Metadata）**。

### 代码示例

```python
# 1. 基础类型注解与 -> None
def log_message(message: str, level: str) -> None:
    print(f"[{level}] {message}")


# 2. a: None 与 a: int | None 结合默认值
def reset_config(config_id: int, clear_flag: None = None, extra_data: str | None = None) -> bool:
    """
    clear_flag: None 声明该参数类型为 None
    extra_data: str | None 声明该参数可以是 str 或 None
    """
    print(f"重置配置 {config_id}，标记: {clear_flag}，附加信息: {extra_data}")
    return True


# 3. 类型注解的非强制性演示（运行时不拦截类型不一致）
def calculate_double(value: int) -> int:
    return value * 2


# 正常符合注解的调用
print(calculate_double(10))    # 输出: 20

# 传入字符串（与 int 注解不一致），Python 依然执行字符串乘法操作
print(calculate_double("Hi"))  # 输出: HiHi
```

---

## 5. `a=None` 与 `a: None` 对比

| 语法形式                    | 语法名称              | 作用层级              | 核心功能与机制                                                                 |
|:----------------------------|:----------------------|:----------------------|:-------------------------------------------------------------------------------|
| **`a = None`**              | 默认参数值            | 运行时逻辑            | 为形参 `a` 赋予默认值 `None`。未传参时实际生效，具备实际运行时赋值行为。       |
| **`a: None`**               | 类型注解（Type Hint） | 静态分析 / 元数据     | 标注形参 `a` 预期的类型为 `None`。仅作开发提示与静态检查，运行时不强制拦截。   |
| **`a: None = None`**        | 类型注解 + 默认参数   | 静态提示 + 运行时逻辑 | 既声明形参 `a` 预期类型为 `None`，又将其默认运行时取值设为 `None`。            |
| **`a: str \| None = None`** | 联合类型注解 + 默认值 | 静态提示 + 运行时逻辑 | 声明参数可为字符串或 `None`，未传参时默认值为 `None`，常用于定义可选数据参数。 |

---

## 6. 有无 `return` 对比

| 特性             | 无 `return`（或空 `return`）               | 有 `return 表达式`                   |
|:-----------------|:-------------------------------------------|:-------------------------------------|
| **主要用途**     | 专注于执行操作（打印、写文件、修改数据等） | 专注于数据计算与结果输出             |
| **返回值类型**   | 默认返回 `None`（类型注解为 `-> None`）    | 返回指定的表达式结果（单值或元组）   |
| **能否赋值使用** | 赋值后变量的值为 `None`                    | 赋值后变量保存函数返回的实际结果     |
| **退出机制**     | 执行完代码块或遇到空 `return` 退出         | 遇到 `return` 立即计算并携带结果退出 |
