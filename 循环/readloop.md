# 循环

## 概览

循环分为 `for` 循环和 `while` 循环。

`for` 循环通常有固定的执行次数；`while` 循环则取决于结束循环的条件。

## `for` 循环

使用 `for` 循环时，一般使用 `for 循环变量 in range(整数值):` 表示缩进的内容需要执行多少遍：

```python
for _ in range(1):
    print("我来到了 Python!")  # 重复执行 1 遍缩进的内容
```

使用 `for` 循环时，可以通过循环变量的值知道当前是第几次循环：

```python
for i in range(18):
    print(f"这是第{i}次循环")
```

## `range()` 函数

可以修改 `range()` 括号中的内容来定义循环变量：

```python
for i in range(0, 20, 2):  # 表示 20 以内的偶数
    print(i)
```

在 `range(a, b, c)` 中：

- `a` 表示循环变量的起点
- `b` 表示循环变量的终点，但不包含 `b`
- `c` 表示循环变量每次增加的值

`a`、`b`、`c` 均只能为整数，负数也被允许，建议自行探索。

## `while` 循环

`while` 循环会在条件成立时不断执行缩进的内容：

```python
while 1 + 1 == 2:
    print("这是一个死循环")
```

上面的条件始终成立，因此会不断执行，形成死循环。使用 `while` 循环时，需要确保条件最终会变为不成立。

## `continue`

`continue` 用于跳过本次循环中剩余的代码，直接开始下一次循环：

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

当 `i` 的值为 `2` 时，`continue` 会跳过 `print(i)`，因此输出为 `0`、`1`、`3`、`4`。

## `break`

`break` 用于立即结束整个循环：

```python
for i in range(5):
    if i == 2:
        break
    print(i)
```

当 `i` 的值为 `2` 时，`break` 会结束循环，因此只会输出 `0` 和 `1`。
