# string 模块：提供数字、大小写字母、标点符号、可打印字符集常量及文本处理函数
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    capwords,
    digits,
    hexdigits,
    printable,
    punctuation,
    whitespace,
)

# ==================== 1. 数字常量（digits） ====================

print("数字字符集（digits）：", digits)


# ==================== 2. 大写英文字母常量（ascii_uppercase） ====================

print("大写英文字母集（ascii_uppercase）：", ascii_uppercase)


# ==================== 3. 小写英文字母常量（ascii_lowercase） ====================

print("小写英文字母集（ascii_lowercase）：", ascii_lowercase)


# ==================== 4. 大小写字母集合常量（ascii_letters） ====================

print("大小写字母全集（ascii_letters）：", ascii_letters)


# ==================== 5. 可打印字符集常量（printable 范围说明） ====================

# 注意：printable 仅包含 ASCII 字符，不包含中文、拼音、日文、俄罗斯文等非 ASCII 字符
print("可打印字符集（printable）：", repr(printable))


# ==================== 6. 标点符号与空白字符常量（punctuation, whitespace, hexdigits） ====================

print("标点符号集（punctuation）：", punctuation)
print("空白字符集（whitespace）：", repr(whitespace))
print("十六进制字符集（hexdigits）：", hexdigits)


# ==================== 7. capwords 函数：单词首字母大写 ====================

raw_title = "python standard library string module"
formatted_title = capwords(raw_title)
print("首字母大写处理（capwords）：", formatted_title)


# ==================== 8. 实际应用场景示例（字符判断、密码池、标点过滤） ====================

# 场景一：字符集判断（检测字符是否为纯数字或纯字母）
user_char = "8"
is_digit_char = user_char in digits
print(f"字符 '{user_char}' 是否为数字：", is_digit_char)

# 场景二：构建密码字符候选池
password_pool = ascii_letters + digits + "!@#$"
print("密码候选字符池长度：", len(password_pool))

# 场景三：过滤文本中的标点符号
sample_text = "Hello, world! Python is powerful."
cleaned_text = "".join(char for char in sample_text if char not in punctuation)
print("去除标点后的文本：", cleaned_text)

"""
string 模块核心总结：
1. 字符常量集：
   - `digits`：包含 '0123456789'。
   - `ascii_lowercase`：包含 'abcdefghijklmnopqrstuvwxyz'。
   - `ascii_uppercase`：包含 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'。
   - `ascii_letters`：包含大小写字母全集。
   - `punctuation`：包含 ASCII 标点符号集。
   - `whitespace`：包含所有空白字符（空格、制表符、换行符等）。
   - `printable`：可打印字符全集（仅包含 ASCII 字符，不包含中文、日文、俄文等非 ASCII 字符）。
2. 工具函数：
   - `capwords(s)`：将字符串中每个由空格分隔的单词首字母转换为大写。
"""
