# 切片操作：展示 [start:stop:step] 语法、默认值规则与负步长技巧

# ==================== 1. 切片的基本用法（左闭右开区间） ====================

fruits = ["苹果", "香蕉", "橙子", "西瓜", "葡萄", "芒果"]

# 提取索引 1 到 4（不包含 4）的元素，即索引 1、2、3
selected_fruits = fruits[1:4]
print("截取结果：", selected_fruits)

# 字符串切片同样适用
greeting = "Hello, Python!"
sub_text = greeting[0:5]
print("截取结果：", sub_text)


# ==================== 2. 省略参数的默认值规则 ====================

scores = [60, 72, 85, 90, 95, 100]

# 省略 start：默认从序列开头（索引 0）开始截取
first_three_scores = scores[:3]
print("前三项成绩：", first_three_scores)

# 省略 stop：默认截取到序列末尾（包含最后一项）
after_two_scores = scores[2:]
print("索引 2 之后的成绩：", after_two_scores)

# 省略 start 和 stop：截取完整序列，生成浅拷贝副本
scores_copy = scores[:]
print("完整副本：", scores_copy)


# ==================== 3. 步长（step）、负步长与序列快速反转 ====================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 正步长：step = 2，每隔 1 个元素提取一个（提取偶数索引）
even_index_numbers = numbers[::2]
print("每隔一项提取：", even_index_numbers)

# 负步长：step = -1，从右向左逆向截取
# 从索引 7 逆向截取到索引 2（不包含 2）
reverse_partial = numbers[7:2:-1]
print("逆向切片结果：", reverse_partial)

# 经典技巧：利用负步长 [::-1] 快速反转序列
reversed_numbers = numbers[::-1]
print("完整列表反转：", reversed_numbers)

word = "上海自来水来自海上"
reversed_word = word[::-1]
print("回文字符串反转：", reversed_word)

"""
切片核心总结：
1. 基本语法与区间：
   - `sequence[start:stop:step]`，提取区间为 [start, stop) 左闭右开。
2. 缺省默认值规则：
   - 正步长时：start 默认为 0，stop 默认为 len(sequence)；
   - 负步长时：start 默认为 -1（序列末尾），stop 默认为序列开头之前。
3. 常用技巧：
   - `[:]`：创建浅拷贝副本；
   - `[::-1]`：快速反转序列。
4. 容器支持与安全性：
   - 支持 list, tuple, str 等有序序列；切片越界时自动截断至边界而不会抛出 IndexError。
"""
