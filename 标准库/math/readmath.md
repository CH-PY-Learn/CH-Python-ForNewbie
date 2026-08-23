# `math` 数学运算模块

## 概览

`math` 是 Python 标准库中用于执行基础与高级数学运算的模块。

该模块提供了丰富的数学常量（如 $\pi$、$e$）、代数运算函数（开方、阶乘、对数等）、取整函数以及几何三角函数。

---

## 核心方法与功能

### 1. 常用数学常量

- **`pi`**：圆周率常数 $\pi \approx 3.141592653589793$
- **`e`**：自然对数的底数 $e \approx 2.718281828459045$

```python
from math import pi, e

print("圆周率 pi：", pi)
print("自然常数 e：", e)
```

---

### 2. 阶乘计算（`factorial`）

- **`factorial(n)`**：计算非负整数 $n$ 的阶乘（即 $n! = n \times (n-1) \times \dots \times 1$）。$0! = 1$。
- **示例**：
  ```python
  from math import factorial

  result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
  print("5 的阶乘：", result)
  ```

---

### 3. 根号与开方（`sqrt`、`isqrt`）

- **`sqrt(x)`**：计算非负实数 $x$ 的平方根（返回浮点数 $\sqrt{x}$）。
- **`isqrt(n)`**：计算非负整数 $n$ 的整数平方根（向下取整的整数值）。
- **示例**：
  ```python
  from math import isqrt, sqrt

  print("16 的平方根：", sqrt(16))      # 输出 4.0
  print("20 的浮点平方根：", sqrt(20))  # 输出 4.47213595499958
  print("20 的整数平方根：", isqrt(20)) # 输出 4
  ```

---

### 4. 角度与弧度转换（`degrees`、`radians`）

在数学与计算机几何中，角度有**度数（Degree）**和**弧度（Radian）**两种衡量体系：$180^\circ = \pi \text{ 弧度}$。

- **`degrees(x)`**：将弧度 $x$ 转换为角度值。
- **`radians(x)`**：将角度 $x$ 转换为弧度值。
- **示例**：
  ```python
  from math import degrees, pi, radians

  # 将 pi 弧度转为角度
  angle = degrees(pi)
  print("pi 弧度对应的角度：", angle)  # 输出 180.0

  # 将 90 度转为弧度
  rad = radians(90)
  print("90 度对应的弧度：", rad)      # 输出 1.5707963267948966 (即 pi / 2)
  ```

---

### 5. 三角函数与默认弧度机制

#### 默认弧度参数的重要说明

**在 Python 的 `math` 模块中，所有三角函数（如 `sin`、`cos`、`tan` 等）接收的参数均默认以“弧度（Radian）”为单位，而非日常生活中常用的“角度（Degree）”。**

如果直接传入度数值（例如 `sin(30)`），Python 会将其视为“30 弧度”进行计算，而非“30 度”。

若要计算特定角度的三角函数值，需先将角度转换为弧度（通过 `radians(角度)` 或 `角度 * pi / 180`），再传入三角函数中。

#### 常用三角函数

- **`sin(x)`**：计算弧度 $x$ 的正弦值。
- **`cos(x)`**：计算弧度 $x$ 的余弦值。
- **`tan(x)`**：计算弧度 $x$ 的正切值。
- **示例**：
  ```python
  from math import cos, pi, radians, sin, tan

  # 计算 30 度的正弦值（sin(30°) = 0.5）
  # 步骤：先将 30 度转为弧度，再调用 sin()
  rad_30 = radians(30)
  sin_value = sin(rad_30)
  print("sin(30°)：", sin_value)  # 输出约 0.49999999999999994 (即 0.5)

  # 计算 60 度的余弦值（cos(60°) = 0.5）
  rad_60 = radians(60)
  cos_value = cos(rad_60)
  print("cos(60°)：", cos_value)

  # 计算 45 度的正切值（tan(45°) = 1.0）
  rad_45 = radians(45)
  tan_value = tan(rad_45)
  print("tan(45°)：", tan_value)
  ```

---

### 6. 其他常用基础运算

- **`ceil(x)`**：向上取整（返回大于等于 $x$ 的最小整数）。
- **`floor(x)`**：向下取整（返回小于等于 $x$ 的最大整数）。
- **`fabs(x)`**：返回浮点数绝对值。
- **`gcd(a, b)`**：计算两整数的最大公约数。
