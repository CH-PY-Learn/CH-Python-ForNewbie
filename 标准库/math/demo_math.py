# math 模块：提供数学常量、阶乘、开方、角度与弧度转换以及三角函数等数学运算
import math

# ==================== 1. 数学常量（pi 与 e） ====================

print("圆周率 pi：", math.pi)
print("自然常数 e：", math.e)

# ==================== 2. 阶乘计算（factorial） ====================

number_for_fact = 5
factorial_result = math.factorial(number_for_fact)
print(f"{number_for_fact} 的阶乘（5!）：", factorial_result)

# ==================== 3. 根号与平方根（sqrt 与 isqrt） ====================

target_number = 25
square_root_value = math.sqrt(target_number)
print(f"{target_number} 的浮点平方根：", square_root_value)

non_perfect_square = 20
exact_sqrt = math.sqrt(non_perfect_square)
integer_sqrt = math.isqrt(non_perfect_square)
print(f"{non_perfect_square} 的浮点平方根：{exact_sqrt}，整数平方根（向下取整）：{integer_sqrt}")

# ==================== 4. 弧度与角度转换（degrees 与 radians） ====================

# 180 度等于 pi 弧度
radian_sample = math.pi / 3  # pi/3 弧度即 60 度
degree_converted = math.degrees(radian_sample)
print("pi / 3 弧度转为角度：", degree_converted)

degree_sample = 45
radian_converted = math.radians(degree_sample)
print("45 度转为弧度：", radian_converted)

# ==================== 5. 三角函数计算（sin, cos, tan 默认弧度参数说明） ====================

# 注意：math 模块中的三角函数均默认接收“弧度”作为参数输入

# 计算 30 度的正弦值：需先将 30 度转换为弧度
angle_30_deg = 30
rad_30 = math.radians(angle_30_deg)
sin_30_val = math.sin(rad_30)
print(f"sin({angle_30_deg}°) 的计算结果：", sin_30_val)

# 计算 60 度的余弦值
angle_60_deg = 60
rad_60 = math.radians(angle_60_deg)
cos_60_val = math.cos(rad_60)
print(f"cos({angle_60_deg}°) 的计算结果：", cos_60_val)

# 计算 45 度的正切值
angle_45_deg = 45
rad_45 = math.radians(angle_45_deg)
tan_45_val = math.tan(rad_45)
print(f"tan({angle_45_deg}°) 的计算结果：", tan_45_val)

# ==================== 6. 取整、绝对值与最大公约数（ceil, floor, fabs, gcd） ====================

float_val = 3.14
print(f"{float_val} 向上取整（ceil）：", math.ceil(float_val))
print(f"{float_val} 向下取整（floor）：", math.floor(float_val))
print("-9.8 的浮点绝对值（fabs）：", math.fabs(-9.8))

# 计算最大公约数（gcd）
gcd_result = math.gcd(24, 36)
print("24 与 36 的最大公约数（gcd）：", gcd_result)

"""
math 模块核心总结：
1. 三角函数输入：
   - `math.sin()`, `math.cos()`, `math.tan()` 默认接收**弧度（Radian）**作为输入参数。
   - 若输入为角度，需先通过 `math.radians(deg)` 转为弧度；计算结果可用 `math.degrees(rad)` 转换为角度。
2. 阶乘与根号：
   - `math.factorial(n)`：计算非负整数 n 的阶乘。
   - `math.sqrt(x)`：计算浮点数平方根；`math.isqrt(n)`：计算非负整数平方根并向下取整。
3. 取整与绝对值：
   - `math.ceil(x)`：向上取整；`math.floor(x)`：向下取整；`math.fabs(x)`：返回浮点数绝对值。
4. 最大公约数：
   - `math.gcd(a, b)`：计算两整数的最大公约数。
"""
