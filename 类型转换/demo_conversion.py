# 类型转换：展示隐式转换、显式转换（int, float, str, bool）与容器互转

# ==================== 1. 隐式类型转换（自动转换） ====================

# 当整数与浮点数进行运算时，Python 会自动将整数转换为浮点数
count_students = 10
average_score = 85.5

total_score = count_students * average_score
print("隐式转换结果：", total_score, "类型：", type(total_score))

# 除法运算 / 的结果默认转换为浮点数
division_result = 10 / 2
print("除法运算结果：", division_result, "类型：", type(division_result))


# ==================== 2. 显式类型转换：转换为整数 int() ====================

# 浮点数转整数：直接丢弃小数部分
price = 19.99
int_price = int(price)
print("浮点数转整数：", int_price)

# 字符串转整数：内容必须为整数格式（自动过滤首尾空格和换行符）
score_text = "  95 \n"
int_score = int(score_text)
print("字符串转整数：", int_score)

# 布尔值转整数：True 为 1，False 为 0
int_true = int(True)
int_false = int(False)
print("布尔值转整数：", int_true, int_false)


# ==================== 3. 显式类型转换：转换为浮点数 float() ====================

# 整数转浮点数
base_number = 42
float_number = float(base_number)
print("整数转浮点数：", float_number)

# 字符串转浮点数
pi_text = "3.1415926"
float_pi = float(pi_text)
print("字符串转浮点数：", float_pi)


# ==================== 4. 显式类型转换：转换为字符串 str() ====================

# 将数字和布尔值转换为字符串，便于文本拼接或格式化输出
user_id = 1001
is_active = True
message = "用户 ID：" + str(user_id) + "，状态：" + str(is_active)
print("字符串拼接：", message)


# ==================== 5. 显式类型转换：转换为布尔值 bool() ====================

# 假值转换为 False：0、0.0、空字符串、空容器、None
print("空字符串转布尔：", bool(""))
print("数字 0 转布尔：", bool(0))
print("空列表转布尔：", bool([]))
print("None 转布尔：", bool(None))

# 非假值转换为 True
print("非空字符串转布尔：", bool("hello"))
print("非零数字转布尔：", bool(10))
print("非空列表转布尔：", bool([1, 2, 3]))


# ==================== 6. 容器类型之间的转换 ====================

# 字符串转列表与元组：逐字符拆分
word = "Python"
char_list = list(word)
char_tuple = tuple(word)
print("字符串转列表：", char_list)
print("字符串转元组：", char_tuple)

# 列表与集合互转：利用 set() 进行数据去重
duplicated_numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers_set = set(duplicated_numbers)
unique_numbers_list = list(unique_numbers_set)
print("列表去重结果：", unique_numbers_list)

# 二元键值对序列转字典
user_info_pairs = [("name", "小明"), ("age", 18), ("city", "北京")]
user_dict = dict(user_info_pairs)
print("键值对转字典：", user_dict)

"""
类型转换核心总结：
1. 隐式类型转换：
   - Python 在混合运算中自动提升精度（如整数与浮点数运算自动转换为浮点数）。
2. 显式类型转换：
   - 数值与文本：`int()`、`float()`、`str()`、`bool()` 进行显式强制转换。
   - 容器互转：`list()`、`tuple()`、`set()` 可互相转换（如通过 `set()` 去重后再转回 `list()`）。
   - 字典构造：`dict()` 可将键值对元组/列表直接构造为字典。
"""
