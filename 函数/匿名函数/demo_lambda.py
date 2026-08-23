# 匿名函数：展示使用 lambda 关键字定义单行匿名函数及其常见应用场景

# ==================== 1. 基础 lambda 运算 ====================

# 单参数：计算数值的平方
calculate_square = lambda num: num ** 2
print("5 的平方：", calculate_square(5))
print("9 的平方：", calculate_square(9))

# 双参数：计算两数之和
add_two_numbers = lambda a, b: a + b
print("15 + 25 =", add_two_numbers(15, 25))

# 多参数：计算长方体体积（长 * 宽 * 高）
calculate_volume = lambda length, width, height: length * width * height
print("长 4, 宽 5, 高 6 的体积：", calculate_volume(4, 5, 6))

# 无参数：返回固定字符串
get_greeting_message = lambda: "你好，欢迎使用 lambda 匿名函数！"
print("无参数 lambda 调用：", get_greeting_message())


# ==================== 2. 结合条件表达式（三元运算） ====================

# 判断数字是偶数还是奇数
check_even_or_odd = lambda value: "偶数" if value % 2 == 0 else "奇数"
print("\n8 是：", check_even_or_odd(8))
print("13 是：", check_even_or_odd(13))

# 判断考试成绩是否及格
evaluate_score = lambda score: "及格" if score >= 60 else "不及格"
print("85 分状态：", evaluate_score(85))
print("52 分状态：", evaluate_score(52))


# ==================== 3. 经典直观应用：自定义排序（key 参数） ====================

print("\n--- lambda 应用于 sorted() 排序 ---")

# 示例 1：按字典中的某个字段进行排序
student_list = [
    {"name": "小明", "score": 82},
    {"name": "小红", "score": 95},
    {"name": "小华", "score": 76},
    {"name": "小强", "score": 89}
]

# 按成绩升序排序
sorted_students = sorted(student_list, key=lambda student: student["score"])
print("按成绩升序排序：", sorted_students)

# 示例 2：按单词的字符长度排序
word_list = ["banana", "pie", "apple", "watermelon", "fig"]
sorted_words = sorted(word_list, key=lambda word: len(word))
print("按单词长度排序：", sorted_words)

# 示例 3：按元组中的第二项（年龄）排序
user_tuples = [("张三", 28), ("李四", 19), ("王五", 35), ("赵六", 22)]
sorted_users = sorted(user_tuples, key=lambda user: user[1])
print("按年龄升序排序：", sorted_users)


# ==================== 4. 配合序列处理内置函数（map 与 filter） ====================

print("\n--- lambda 配合 map 与 filter ---")

number_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 map() 配合 lambda 对列表中的每个数字进行翻倍
doubled_numbers = list(map(lambda x: x * 2, number_sequence))
print("全员翻倍：", doubled_numbers)

# 使用 filter() 配合 lambda 筛选出大于 5 的所有数字
filtered_numbers = list(filter(lambda x: x > 5, number_sequence))
print("筛选大于 5 的数字：", filtered_numbers)

"""
lambda 匿名函数核心总结：
1. 基本语法与特性：
   - 语法格式：`lambda [参数1, 参数2, ...]: 表达式`。
   - 只能包含单行表达式，无需 `return` 关键字，该表达式的计算结果即为返回值。
2. 应用场景：
   - 常作为高阶函数（如 `sorted`、`map`、`filter`、`min`、`max`）的 `key` 参数传入。
   - 适合用于一次性、逻辑简短的轻量级函数，避免繁琐的 `def` 命名。
3. 条件表达式支持：
   - 支持在表达式中使用三元运算符：`x if condition else y`。
"""
