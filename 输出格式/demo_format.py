# 输出格式：通过格式说明符控制数字精度、通用格式、百分比、进制、千分位及对齐排版

# ==================== 1. 浮点数精度控制（:.2f 与 :.4f） ====================

pi_value = 3.141592653589793
print(f"原始数值：{pi_value}")
print(f"保留两位小数（:.2f）：{pi_value:.2f}")
print(f"保留四位小数（:.4f）：{pi_value:.4f}")
print(f"保留整数部分（:.0f）：{pi_value:.0f}")


# ==================== 2. 通用格式（:g 与 :G） ====================

# :g 会根据数值大小自动在定点表示与科学计数法之间切换，并自动去除末尾无意义的 0
standard_float = 28.50000
very_small_float = 0.000025
very_large_float = 9876543210.0

print(f"自动去除末尾多余的零（28.50000 -> :g）：{standard_float:g}")
print(f"极小数值自动转为科学计数法（:g）：{very_small_float:g}")
print(f"极大数值自动转为科学计数法（:g）：{very_large_float:g}")


# ==================== 3. 科学计数法格式（:.2e 与 :.2E） ====================

electron_mass = 0.00000009109
print(f"科学计数法小写 e（:.2e）：{electron_mass:.2e}")
print(f"科学计数法大写 E（:.2E）：{electron_mass:.2E}")


# ==================== 4. 百分比格式（:.1% 与 :.2%） ====================

# 会自动将原数值乘以 100 并附加 % 符号
completion_ratio = 0.8736
print(f"完成度百分比（保留1位小数）：{completion_ratio:.1%}")
print(f"完成度百分比（保留2位小数）：{completion_ratio:.2%}")


# ==================== 5. 千位分隔符（:, 与 :_） ====================

total_population = 1411780000
item_price = 129999.888
print(f"千位逗号分隔：{total_population:,}")
print(f"千位下划线分隔：{total_population:_}")
print(f"千位分隔符与小数位数结合（:,.2f）：{item_price:,.2f}")


# ==================== 6. 整数进制转换（:b, :o, :x 与前缀 :#b, :#o, :#x） ====================

decimal_number = 255
print(f"二进制（:b）：{decimal_number:b}，带前缀（:#b）：{decimal_number:#b}")
print(f"八进制（:o）：{decimal_number:o}，带前缀（:#o）：{decimal_number:#o}")
print(f"十六进制小写（:x）：{decimal_number:x}，带前缀（:#x）：{decimal_number:#x}")
print(f"十六进制大写（:X）：{decimal_number:X}，带前缀（:#X）：{decimal_number:#X}")


# ==================== 7. 对齐、宽度与字符填充（:<, :>, :^） ====================

course_name = "Python"
print(f"左对齐（:<10）：'{course_name:<10}'")
print(f"右对齐（:>10）：'{course_name:>10}'")
print(f"居中对齐（:^10）：'{course_name:^10}'")
print(f"自定义符号填充居中（:*^14）：'{course_name:*^14}'")

# 数字补零对齐（:0>5 或 :05d）
student_serial_id = 42
print(f"固定 5 位宽度补零（:0>5）：{student_serial_id:0>5}")


# ==================== 8. 正负号显示控制（:+ 与 :空格） ====================

temperature_positive = 18
temperature_negative = -6
print(f"强制显示符号（:+）：正温 {temperature_positive:+}, 负温 {temperature_negative:+}")
print(f"正数预留空格（: ）：正温 {temperature_positive: }, 负温 {temperature_negative: }")

"""
输出格式核心总结：
1. 小数与通用格式：
   - `:.nf`：定点小数格式，指定保留 n 位小数，四舍五入；
   - `:g`：通用数字格式，自动在定点与科学计数法间切换，并省略多余尾随零。
2. 科学计数与百分比：
   - `:.ne`：科学计数法表示；
   - `:.n%`：百分比格式，数值乘以 100 并保留 n 位小数且添加 %。
3. 千位分隔与进制转换：
   - `:,` / `:_`：千位分隔符；
   - `:b` / `:o` / `:x`：转换为二进制、八进制、十六进制表示（加 `#` 保留进制前缀）。
4. 对齐与填充控制：
   - `:<` / `:>` / `:^`：控制左、右、居中对齐及指定显示宽度和填充字符；
   - `:0>5`：数字前置补零对齐。
"""
