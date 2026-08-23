# 逻辑运算

## 概览

在编写判断式时，有时需要同时判断多个条件，或者对某个条件的结果进行取反。这时就需要用到逻辑运算符。

Python 中的逻辑运算符主要有三个：`and`（与）、`or`（或）和 `not`（非）。逻辑运算的结果为布尔值（`True` 或 `False`）。

## 逻辑运算符

- `and`：表示“且”。当且仅当两边的表达式都为 `True` 时，整个判断式才为 `True`。
- `or`：表示“或”。只要两边的表达式中有一个为 `True`，整个判断式就为 `True`。
- `not`：表示“非”（取反）。如果表达式为 `True`，则返回 `False`；如果表达式为 `False`，则返回 `True`。

## `and`：逻辑与

`and` 连接两个或多个条件，只有所有条件都成立时，判断式才成立：

```python
age = 20
has_id_card = True

if age >= 18 and has_id_card:
    print("年龄达标且持有证件，允许办理业务")
```

在以上代码中，只有当 `age >= 18` 和 `has_id_card` 同时为 `True` 时，才会执行 `print()`。

## `or`：逻辑或

`or` 连接两个或多个条件，只要其中任意一个条件成立，判断式就成立：

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("今天是休息日")
```

在以上代码中，只要 `is_weekend` 或 `is_holiday` 其中一个为 `True`，就会执行缩进内的代码。

## `not`：逻辑非

`not` 用于对布尔值进行取反：

```python
is_raining = False

if not is_raining:
    print("今天没有下雨，可以出行")
```

在以上代码中，`is_raining` 为 `False`，经过 `not` 取反后结果为 `True`，因此会执行 `print()`。

## 运算优先级

当多个逻辑运算符混合使用时，Python 的默认计算优先级为：

1. `not`（最高）
2. `and`
3. `or`（最低）

为了提高代码的可读性并避免歧义，建议使用括号 `()` 来明确计算顺序：

```python
user_age = 25
has_ticket = False
is_admin = True

if (user_age >= 18 and has_ticket) or is_admin:
    print("允许进入活动会场")
```

在以上代码中，会先计算括号内的 `user_age >= 18 and has_ticket`，再与 `is_admin` 进行 `or` 运算。
