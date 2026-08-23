# 异常处理与防报错（`try-except-finally`）

## 概览

在程序运行过程中，某些操作可能会因为意外输入或外部因素导致错误（在 Python 中称为**异常**，Exception）。当异常发生时，如果没有处理机制，程序会直接报错并中断退出。

为了保证程序的健壮性，防止程序崩溃（即“防报错”），Python 提供了 `try-except` 异常捕获机制。其运行逻辑类似于条件判断式：尝试执行可能出错的代码，并在出错时执行备用补救代码。

```python
try:
    number = int("abc")  # 这行代码会引发 ValueError 异常
except ValueError:
    print("输入格式错误，无法转换为整数")

print("程序未崩溃，继续正常执行")
```

## `try-except`：基础防报错

`try-except` 是最基本的异常处理结构：
- `try` 代码块：包含可能会发生异常的代码。
- `except` 代码块：当 `try` 中的代码发生指定的异常时执行；若没有发生异常，则跳过 `except` 代码块。

```python
try:
    divisor = 0
    result = 10 / divisor
except ZeroDivisionError:
    print("除数不能为 0！")
```

在以上代码中，`10 / 0` 会引发 `ZeroDivisionError`（除以零异常），程序被 `except ZeroDivisionError` 捕获并执行对应处理，避免了程序崩溃。

## 多个 `except` 与 `try-except-else`

类似于判断式中的 `if-elif-else`，一段代码可能会产生多种不同类型的异常，可以使用多个 `except` 代码块分别进行捕获和处理。

同时，还可以添加 `else` 代码块：当 `try` 代码块**没有发生任何异常**时，执行 `else` 代码块。

```python
user_input = "10"

try:
    number = int(user_input)
    result = 100 / number
except ValueError:
    print("输入的不是有效的整数！")
except ZeroDivisionError:
    print("计算失败：除数不能为 0！")
else:
    print("计算成功，结果为：", result)
```

在以上代码中：
- 若 `user_input` 为 `"abc"`，触发 `ValueError`；
- 若 `user_input` 为 `"0"`，触发 `ZeroDivisionError`；
- 若 `user_input` 为 `"10"`，无异常发生，执行 `else` 代码块。

## `try-except-finally`：最终执行代码块

`finally` 代码块的特点是：**无论 `try` 中是否发生异常，也无论异常是否被捕获，`finally` 中的代码块都一定会执行**。

这通常用于资源清理、文件关闭或输出结束提示等无论成功与否都必须完成的操作：

```python
try:
    print("正在连接数据库或打开资源...")
    data = 10 / 2
    print("数据处理成功：", data)
except ZeroDivisionError:
    print("处理失败：出现除以零错误")
finally:
    print("清理连接资源，操作结束（无论成功与否均会执行）")
```

在 `try-except-else-finally` 完整结构中：
1. 先执行 `try`；
2. 若出错，执行匹配的 `except`；
3. 若无错，执行 `else`；
4. 最后**一定会执行** `finally`。

## 裸 `except`（`bare except`）及其利弊

裸 `except` 指的是在 `except` 关键字后不指定任何具体的异常类型，直接写 `except:`：

```python
try:
    value = int("文本")
except:
    print("发生了某种未知错误")
```

### 裸 `except` 的利弊分析

- **利（特点）**：
  - **简单快捷**：不需要预先指定具体的异常类型。
  - **防崩溃保底**：能够拦截所有错误与异常，确保程序在面对未知情况时不会中断退出。

- **弊（局限与影响）**：
  - **捕获范围较宽**：裸 `except` 会拦截所有异常，包括代码中的拼写错误、变量名写错（`NameError`）、类型错误（`TypeError`）等，可能增加定位具体代码问题的难度。
  - **拦截系统控制信号**：裸 `except` 同样会捕获 `KeyboardInterrupt`（用户按下 `Ctrl + C` 终止程序）和 `SystemExit`（系统退出请求）等底层信号。

### 捕获基类 `Exception`

若希望捕获所有常规运行时异常（而不拦截系统退出等控制信号），可以使用 `Exception`（常规异常的基类）：

```python
try:
    result = 10 / 0
except Exception as e:
    print(f"捕获到异常：{e}") #e表示报错类型，也可直接 except Excepttion
```
