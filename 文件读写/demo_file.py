# 文件读写：展示 open/close 与 with open 的对比、字符编码 encoding 与 utf-8，以及 'w', 'r', 'a' 三种核心打开模式

import os

demo_file_path = "demo_test_file.txt"

# ==================== 1. 基础 open 与 close 写法（文件对象与方法调用） ====================

print("--- 1. 基础 open 与 close 写法 ---")

# 使用 open() 打开文件，返回一个文件对象并赋值给 manual_file 变量
# 对该文件对象调用 write() 方法写入内容，最后显式调用 close() 方法释放资源
manual_file = open(demo_file_path, mode="w", encoding="utf-8")
manual_file.write("第一行：通过 open() 返回的文件对象手动写入数据\n")
manual_file.write("第二行：手动调用 close() 方法前数据暂存于缓冲区\n")
manual_file.close()
print("已成功写入并手动关闭文件。")

# 打开文件返回只读文件对象，调用 read() 方法读取内容
read_file = open(demo_file_path, mode="r", encoding="utf-8")
manual_content = read_file.read()
read_file.close()
print("手动读取文件内容：\n" + manual_content)


# ==================== 2. with open 上下文管理器与 'w' 覆盖写入模式 ====================

print("--- 2. with open 上下文管理器与 'w' 模式 ---")

# 'w' 模式：with open(...) as file 将创建的文件对象绑定到变量 file
# 通过 file 对象调用 write() 方法，with 代码块结束时自动调用 close() 方法
with open(demo_file_path, mode="w", encoding="utf-8") as file:
    file.write("标题：学习 Python 文件读写\n")
    file.write("模式：'w' 覆盖写入模式已清空原有内容\n")

print("使用 with open('w') 写入完成（文件已自动关闭）。")


# ==================== 3. with open 与 'r' 只读模式 ====================

print("\n--- 3. with open 与 'r' 只读模式 ---")

# 方式 A：使用 read() 一次性读取全部内容
with open(demo_file_path, mode="r", encoding="utf-8") as file:
    full_text = file.read()
    print("【read() 一次性读取】\n" + full_text)

# 方式 B：使用 readline() 逐行读取
with open(demo_file_path, mode="r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
    print("【readline() 逐行读取】")
    print("第 1 行:", first_line.strip())
    print("第 2 行:", second_line.strip())

# 方式 C：直接遍历文件对象（内存友好，适合处理大文件）
with open(demo_file_path, mode="r", encoding="utf-8") as file:
    print("【遍历文件对象】")
    for line_number, line_content in enumerate(file, start=1):
        print(f"行 {line_number}: {line_content.strip()}")


# ==================== 4. with open 与 'a' 追加写入模式 ====================

print("\n--- 4. with open 与 'a' 追加写入模式 ---")

# 'a' 模式：文件指针位于末尾，保留已有内容并在末尾新增数据
with open(demo_file_path, mode="a", encoding="utf-8") as file:
    file.write("模式：'a' 追加模式添加的第一行记录\n")
    file.write("模式：'a' 追加模式添加的第二行记录\n")

print("追加写入完成。")

# 再次读取验证追加后的完整内容
with open(demo_file_path, mode="r", encoding="utf-8") as file:
    updated_content = file.read()
    print("追加后的文件完整内容：\n" + updated_content)


# ==================== 5. 编码 encoding="utf-8" 说明与演示 ====================

print("--- 5. encoding='utf-8' 跨平台编码演示 ---")

multilingual_file = "demo_multilingual.txt"

# 写入包含中文、特殊符号及英文字符的内容
with open(multilingual_file, mode="w", encoding="utf-8") as file:
    file.write("中文测试：你好，世界！\n")
    file.write("English: Python File I/O\n")
    file.write("符号与数字：★ 100% ￥ 2026\n")

# 以 utf-8 编码精确读取
with open(multilingual_file, mode="r", encoding="utf-8") as file:
    multilingual_text = file.read()
    print("utf-8 编码读取内容：\n" + multilingual_text)

# 清理演示过程中生成的临时文本文件
if os.path.exists(demo_file_path):
    os.remove(demo_file_path)
if os.path.exists(multilingual_file):
    os.remove(multilingual_file)
print("演示临时文件已清理完毕。")

"""
文件读写核心总结：
1. 文件对象概念：
   - 指向文件的变量是文件对象（File Object），读写操作本质上是通过该对象的方法（如 `write()`、`read()`、`readline()`、`close()`）对底层资源进行调用。
2. open/close vs with open：
   - 基础 `open` 需手动调用 `close()` 释放资源；
   - `with open(...) as file:` 上下文管理器在退出代码块时自动安全关闭文件并刷新缓冲区。
3. 字符编码（encoding）：
   - 明确指定 `encoding="utf-8"` 可确保跨平台兼容性，防止中文等非 ASCII 字符出现乱码或 `UnicodeDecodeError`。
4. 打开模式：
   - 'w'：覆盖写入，文件不存在则创建，存在则清空；
   - 'r'：只读模式，文件不存在时抛出 `FileNotFoundError`；
   - 'a'：追加写入，写入内容添加至文件末尾。
"""
