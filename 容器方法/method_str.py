# 字符串常用方法：展示 capitalize, title, upper, lower, split 与 join

# 由于字符串的方法过多，本节只介绍部分 md 文件中的部分字符串方法。

# ==================== 1. 大小写转换方法（capitalize, title, upper, lower） ====================

message = "hello world"
message = message.capitalize()  # capitalize 方法，将字符串的第一个字符转换为大写，其余字符转换为小写。
print(message)

book_name = "python basic"
book_name = book_name.title()  # title 方法，将字符串中的每个单词的首字母转换为大写，其余字符转换为小写。
print(book_name)

warning_text = "danger, dont touch!"
warning_text = warning_text.upper()  # upper 方法，将字符串中的所有字符转换为大写。
print(warning_text)

typo_message = "OOPS IM SORRY!"
typo_message = typo_message.lower()  # lower 方法，将字符串中的所有字符转换为小写。
print(typo_message)


# ==================== 2. split 与 join：字符串拆分与列表拼接 ====================

prime_number = "2 3 5 7 11 13"

# 当数据为字符串时，可以使用 split() 方法将字符串分割成列表。
prime_number = prime_number.split()  # split 方法，将字符串按照参数分割内容成列表。若参数为空默认为空白符
print(prime_number)

# 当有了一个列表需要以空格连接成字符串时，可以使用 join() 方法
prime_number = " ".join(prime_number)  # join 方法，将列表中的元素以参数连接成字符串。
print(prime_number)

"""
字符串方法核心总结：
1. 大小写转换：
   - `capitalize()`：首字母大写；`title()`：每个单词首字母大写；`upper()` / `lower()`：全大写 / 全小写。
2. 拆分与连接：
   - `split(sep)`：按指定分隔符将字符串拆分为列表。
   - `str.join(iterable)`：以指定字符串为连接符，将字符串序列拼接为单个新字符串。
3. 不可变性：
   - 字符串所有方法均返回新的字符串对象，不会修改原字符串。
"""
