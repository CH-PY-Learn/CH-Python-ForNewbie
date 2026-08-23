# 常见报错类型与原因

## 概览

在 Python 编程过程中，遇到报错是十分正常且必经的阶段。Python 的报错信息（Traceback）会清晰地指出 **出错的文件**、 **行号**、
**报错类型（Error Type） **以及**具体的错误原因描述**。

Python 中的错误通常分为两大类：

1. **语法错误（Syntax Errors）**：在代码解析/编译阶段被发现，代码根本无法开始运行。
2. **运行时异常（Exceptions）**：语法正确，但在程序运行过程中因非法操作、数据不符或外部环境问题引发中断。

熟练掌握常见的报错类型及其诱因，能够帮助我们快速定位并修复 Bug（调试）。

---

## 1. 语法与缩进错误

### `SyntaxError`（语法错误）

- **报错原因**：代码书写不符合 Python 的基本语法规则，解释器无法理解。
- **常见场景**：
    - `if`、`for`、`while`、`def`、`try` 等语句末尾漏写了英文冒号 `:`。
    - 单双引号、圆括号 `()`、方括号 `[]` 或花括号 `{}` 未成对闭合。
    - 误用了中文标点符号（如中文逗号 `，`、中文冒号 `：`、中文引号 `“”` 等）。
    - 变量名使用了 Python 的关键字（如 `class = 1`、`def = 2`）。
- **代码示例**：
  ```python
  # 错误示例 1：漏写冒号
  if 5 > 3
      print("5 大于 3")  # SyntaxError: expected ':'

  # 错误示例 2：中文字符/未闭合引号
  message = "Hello, world!  # SyntaxError: unterminated string literal
  ```

### `IndentationError`（缩进错误）

- **报错原因**：代码块的缩进层级不正确，属于 `SyntaxError` 的子类。
- **常见场景**：
    - 冒号 `:` 之后的下一行代码没有缩进。
    - 同一代码块内缩进空格数不一致（如有的行缩进 2 格，有的缩进 4 格）。
    - 在同一项目中混用了制表符（Tab）和空格（Space）。
    - 没有逻辑从属关系的代码行开头无故添加了缩进。
- **代码示例**：
  ```python
  # 错误示例 1：条件块内缺少缩进
  if True:
  print("未缩进")  # IndentationError: expected an indented block

  # 错误示例 2：意外的顶格缩进
  print("第一行")
    print("第二行")  # IndentationError: unexpected indent
  ```

---

## 2. 变量与名称错误

### `NameError`（未定义名称错误）

- **报错原因**：尝试使用一个尚未被定义或赋值的变量名、函数名或模块名。
- **常见场景**：
    - 变量名或函数名拼写错误（如将 `total_score` 误写为 `totoal_score`）。
    - 大小写不匹配（Python 严格区分大小写，如定义了 `name` 却使用了 `Name`）。
    - 字符串常量忘记加引号，被 Python 误当作变量名解析（如 `print(hello)`）。
    - 变量在使用之后才在后续代码中定义（执行顺序颠倒）。
- **代码示例**：
  ```python
  # 错误示例：使用了未定义的变量
  print(user_age)  # NameError: name 'user_age' is not defined

  # 字符串漏写引号
  greeting = hello  # NameError: name 'hello' is not defined
  ```

---

## 3. 类型与数值错误

### `TypeError`（类型错误）

- **报错原因**：对某个对象执行了该数据类型不支持的操作，或者传入了不兼容类型的参数。
- **常见场景**：
    - 将字符串和整数直接使用 `+` 拼接（如 `"年龄：" + 18`）。
    - 对不可调用的对象使用括号调用（如将非函数变量当作函数执行 `number()`）。
    - 函数调用时传入的参数个数与定义不符（过多或过少）。
    - 尝试修改不可变类型（如修改元组中的元素 `my_tuple[0] = 10`）。
- **代码示例**：
  ```python
  # 错误示例 1：字符串与数字直接拼接
  result = "分数：" + 95  # TypeError: can only concatenate str (not "int") to str

  # 错误示例 2：修改不可变的元组
  numbers = (1, 2, 3)
  numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment
  ```

### `ValueError`（值错误）

- **报错原因**：传入的操作或函数接收到了 **类型正确**但 **值不合法**的参数。
- **常见场景**：
    - 使用 `int()` 或 `float()` 强制转换无法解析为数字的字符串（如 `int("abc")`）。
    - 使用列表的 `.remove()` 方法移除一个在列表中不存在的元素。
    - 多元赋值（解包）时，左侧变量数量与右侧序列元素数量不一致。
- **代码示例**：
  ```python
  # 错误示例 1：无法转换的字符串
  age = int("十八")  # ValueError: invalid literal for int() with base 10: '十八'

  # 错误示例 2：列表中找不到要移除的元素
  fruits = ["苹果", "香蕉"]
  fruits.remove("西瓜")  # ValueError: list.remove(x): x not in list

  # 错误示例 3：解包变量数量不匹配
  a, b = [1, 2, 3]  # ValueError: too many values to unpack (expected 2)
  ```

---

## 4. 容器与索引错误

### `IndexError`（索引越界错误）

- **报错原因**：访问有序序列（列表、元组、字符串）时，指定的索引下标超出了序列的有效范围。
- **常见场景**：
    - 列表长度为 `3`（有效正向索引为 `0, 1, 2`），却尝试访问 `list[3]`。
    - 对空列表取首项 `empty_list[0]`。
- **代码示例**：
  ```python
  scores = [80, 90, 100]
  # scores 长度为 3，最大正向索引为 2
  print(scores[3])  # IndexError: list index out of range
  ```

### `KeyError`（键不存在错误）

- **报错原因**：在字典（`dict`）中通过键（`dict[key]`）取值时，该键并不存在于字典中。
- **常见场景**：
    - 字典键名拼写错误。
    - 访问了字典中不存在的键（如 `student["score"]`）。
- **代码示例**：
  ```python
  student = {"name": "小明", "age": 18}
  # 字典中不存在 "score" 键
  print(student["score"])  # KeyError: 'score'
  ```

---

## 5. 运算与属性错误

### `ZeroDivisionError`（除以零错误）

- **报错原因**：在数学除法（`/`）、整除（`//`）或取模/求余（`%`）运算中，除数（右侧操作数）为 `0`。
- **常见场景**：
    - 计算平均值等公式时，分母变量计算结果为 `0`。
- **代码示例**：
  ```python
  total_score = 100
  student_count = 0
  average = total_score / student_count  # ZeroDivisionError: division by zero
  ```

### `AttributeError`（属性/方法错误）

- **报错原因**：尝试访问某个对象不存在的属性或调用其不支持的方法。
- **常见场景**：
    - 记错或混淆了不同数据类型的方法（如对整数调用 `.append()`，对字符串调用 `.keys()`）。
    - 对象本身为 `None`（如函数未返回值却去调用结果的属性）。
- **代码示例**：
  ```python
  number = 100
  number.append(200)  # AttributeError: 'int' object has no attribute 'append'

  text = "Hello"
  text.push("World")  # AttributeError: 'str' object has no attribute 'push'
  ```

---

## 6. 文件与导入错误

### `FileNotFoundError`（文件未找到错误）

- **报错原因**：尝试打开（`open()`）、读取或操作一个不存在的文件或目录。
- **常见场景**：
    - 文件路径拼写错误、文件名后缀遗漏（如将 `data.txt` 写成 `data`）。
    - 相对路径的工作目录与预期不一致。
- **代码示例**：
  ```python
  with open("non_existent_file.txt", "r") as file:
      content = file.read()  # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
  ```

### `ModuleNotFoundError` / `ImportError`（模块未找到/导入错误）

- **报错原因**：
    - `ModuleNotFoundError`：尝试使用 `import` 导入未安装或不存在的第三方库/模块。
    - `ImportError`：模块存在，但从中导入的函数或变量名不存在。
- **代码示例**：
  ```python
  import non_existent_package  # ModuleNotFoundError: No module named 'non_existent_package'
  ```

---

## 7. 常见报错速查表

| 报错类型名称          | 中文含义       | 典型触发原因                               |
|:----------------------|:---------------|:-------------------------------------------|
| `SyntaxError`         | 语法错误       | 缺少冒号、括号未闭合、中英文标点混用等     |
| `IndentationError`    | 缩进错误       | 缺少缩进、缩进不对齐或空格与 Tab 混用      |
| `NameError`           | 未定义名称错误 | 变量名拼写错误、未定义先使用或漏加引号     |
| `TypeError`           | 类型错误       | 类型不匹配（如字符串加整数）、参数个数不符 |
| `ValueError`          | 值错误         | 类型正确但值不合法（如 `int("abc")`）      |
| `IndexError`          | 索引越界错误   | 访问列表/字符串时索引超出有效范围          |
| `KeyError`            | 键不存在错误   | 访问字典中不存在的键                       |
| `ZeroDivisionError`   | 除以零错误     | 除法、整除或求余时除数为 0                 |
| `AttributeError`      | 属性/方法错误  | 调用了该类型不存在的属性或方法             |
| `FileNotFoundError`   | 文件未找到错误 | 打开或读取不存在的文件路径                 |
| `ModuleNotFoundError` | 模块未找到错误 | 导入了未安装或不存在的模块                 |

---

## 8. 如何看懂报错追踪信息（Traceback）

当程序发生报错中断时，Python 控制台会输出调用栈追踪信息（Traceback），其主要结构如下：

1. **最后一行**：指明具体的报错类型名称（如 `ValueError`）以及原因描述。
2. **追踪路径与行号**：显示调用栈各层级的文件路径与出错所在的 **行号（如 line 99）**，便于定位代码位置。
3. **调用上下文**：展示引发异常处的具体代码片段。