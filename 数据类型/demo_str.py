# str：字符串不可变类型与字符串替换

# ==================== 1. 字符串定义（单引号、双引号、三引号） ====================

# 单引号写法
game_mode = 'c'  # 引用"我的世界"中 Aternos 收编的essentials插件中的指令/gmc 表示原版"我的世界"的 /gamemode creative
# 单引号一般用于储存单个或极少字符的字符串

# 双引号写法
quote = "Be yourself; everyone else is already taken."

# 三引号写法
lyrics = """
你我在人群中，试着抓紧你的手
请不要甩开我，不会让你走
可能余温太久，没给你感动
...
"""

# 不仅如此，双引号和三引号一般也用于显眼的代码注释
"""
比如我想说这段代码很重要，千万别删！
千万别删！
千万别删！千万别删！
千万别删！千万别删！千万别删！
千万别删！千万别删！千万别删！千万别删！
"""

# python虽然会去解读这些字符串，但因为没有被赋值，所以实际上它们不参与任何代码块。

print(game_mode)
print(quote)
print(lyrics)


# ==================== 2. replace 方法：生成替换后的新字符串 ====================

# 针对字符串，虽然它是不可变的，但是Python开发者为程序设置了内置函数 replace来得到一个返回值用于修改字符串

simple_text = "000000000000000000000000000000000000000"
print(simple_text)
mask_text = simple_text.replace("0", "1")  # 这一行会返回simple_text被修改后的值（simple_text本身不会被修改）并返回给mask_text
simple_text = mask_text  # 把mask_text变量赋值给simple_text变量，从而达到修改字符串的效果
print(simple_text)

basic_text = "2222222222222222222222222222222222222222"
print(basic_text)
basic_text = basic_text.replace("2", "3")  # 当然replace会有一个返回值，可以直接赋值给原本指向很多"2"的变量自己。
# 通俗来说就是计算replace后得到的值，重新赋值给自己

print(basic_text)

"""
str 字符串类型核心总结：
1. 字符串定义：
   - 使用单引号 `'`、双引号 `"` 或三引号 `'''` / `\"\"\"` 定义文本。三引号支持跨行字符串。
2. 不可变性：
   - 字符串为不可变序列，不能通过索引直接修改字符。
3. 替换与转换：
   - `replace(old, new)` 方法返回替换后的新字符串对象，原字符串保持不变。
"""
