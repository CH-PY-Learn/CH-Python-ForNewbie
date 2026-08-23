# 基础算术运算：展示加、减、乘、除运算

# ==================== 1. 加法运算（+） ====================

summary_word = 120
essay_word = 180

total_word = summary_word + essay_word  # 加法用例
print(total_word)


# ==================== 2. 减法运算（-） ====================

max_of_list = 100
min_of_list = 10

maximum_difference = max_of_list - min_of_list  # 减法用例
print(maximum_difference)


# ==================== 3. 乘法运算（*） ====================

length_bed = 2
width_bed = 1.5

area_bed = length_bed * width_bed  # 乘法用例
print(area_bed)


# ==================== 4. 除法运算（/）与幂运算（**） ====================

height = 1.8
weight = 70

bmi = weight / height ** 2
print(bmi)

# 针对除法，无论被除数与除数两者类型为整数或浮点数，返回值类型默认为浮点数

"""
基础算术运算核心总结：
1. 四则运算符：
   - `+`（加法）、`-`（减法）、`*`（乘法）、`/`（除法）。
2. 除法类型特性：
   - 无论操作数是否为整数，常规除法 `/` 的计算结果始终为浮点数（float）。
"""
