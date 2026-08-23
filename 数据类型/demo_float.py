# float：浮点数类型存储、运算与转换

# ==================== 1. 浮点数直接定义与 float() 转换 ====================

simple_num = 0.5
basic_num = float(0.5)

print(simple_num)
print(basic_num)


# ==================== 2. 除法运算产生浮点数与整除行为 ====================

old_highest_temperature = 28
old_lowest_temperature = 25

# 只要是做除法 '/' ，Python 也会把数据类型转变为浮点数
old_average_temperature = old_highest_temperature / old_lowest_temperature

new_highest_temperature = float(old_highest_temperature)
new_lowest_temperature = float(old_lowest_temperature)

# 但对于整数除法 "//"，只要两者为整数，返回的才是整数，一旦某一项或两者为浮点数，返回的也是浮点数
new_average_temperature = new_highest_temperature // new_lowest_temperature

print(old_highest_temperature)
print(old_lowest_temperature)
print(old_average_temperature)
print(new_highest_temperature)
print(new_lowest_temperature)
print(new_average_temperature)


# ==================== 3. 字符串转浮点数与过滤空字符 ====================

# 在 float() 括号中的内容只要是一个数字就会被转译为浮点数，float() 会自动过滤空字符如换行符和空格
direction = float("180\n")
print(direction)

"""
float 浮点数类型核心总结：
1. 浮点数表示：
   - 用于表示带有小数部分的实数；可通过 `float()` 函数从整数或符合格式的字符串进行转换。
2. 运算类型行为：
   - 常规除法 `/` 始终返回浮点数；
   - 整除 `//` 若有浮点数参与，返回带 `.0` 的浮点数。
"""
