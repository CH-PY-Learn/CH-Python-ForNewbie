# `string` 字符常量与文本处理模块

## 概览

`string` 是 Python 标准库中用于提供预定义字符集常量与文本处理辅助功能的模块。

在处理字符判断、密码生成、输入过滤、文本排版等场景时，`string` 模块提供了常用的字符集合常量，无需手动书写长字符串。

---

## 核心字符集常量

### 1. `digits`：数字字符集

- **内容**：包含全部 10 个十进制数字字符 `'0123456789'`。
- **示例**：
  ```python
  from string import digits

  print("数字常量集：", digits)
  ```

---

### 2. `ascii_uppercase`：大写英文字母集

- **内容**：包含全部 26 个 ASCII 大写英文字母 `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`。
- **示例**：
  ```python
  from string import ascii_uppercase

  print("大写字母集：", ascii_uppercase)
  ```

---

### 3. `ascii_lowercase`：小写英文字母集

- **内容**：包含全部 26 个 ASCII 小写英文字母 `'abcdefghijklmnopqrstuvwxyz'`。
- **示例**：
  ```python
  from string import ascii_lowercase

  print("小写字母集：", ascii_lowercase)
  ```

---

### 4. `ascii_letters`：大小写英文字母全集

- **内容**：包含全部 52 个 ASCII 小写与大写英文字母，即 `ascii_lowercase + ascii_uppercase`。
- **示例**：
  ```python
  from string import ascii_letters

  print("大小写字母集：", ascii_letters)
  ```

---

### 5. `printable`：所有可打印字符集

- **内容**：包含所有被视为可打印的 ASCII 字符，包括数字、大小写字母、标点符号以及空白控制符（空格、`\t`、`\n`、`\r` 等）。
- **字符范围声明**：`printable` 仅包含标准 ASCII 字符集内的内容， **不包含**如中文、拼音、日文、俄罗斯文等任何非 ASCII 字符。
- **示例**：
  ```python
  from string import printable

  print("所有可打印字符：", repr(printable))  # repr 表示把表达式转换为 Python 中字符串表达式形式
  ```

---

## 扩展常量与文本函数

### 6. `punctuation` 与 `whitespace`

- **`punctuation`**：所有标准 ASCII 标点符号 `'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'`。
- **`whitespace`**：所有 ASCII 空白字符（空格、制表符 `\t`、换行符 `\n` 等）。

### 7. `capwords(s, sep=None)`：单词首字母大写处理

- **功能**：本质上是使用 `split` 将字符串拆分为单词，使用 `capitalize` 将每个单词首字母大写，最后使用 `join` 重新拼接。
- **示例**：
  ```python
  from string import capwords

  title_text = capwords("hello python standard library")
  print("每个单词首字母大写：", title_text)  # 输出 "Hello Python Standard Library"
  ```

---

## 常用应用场景

- **字符合法性校验**：结合集合或 `in` 运算符快速检测某个字符是否属于特定类型。
- **字符池构建**：生成随机验证码、令牌或临时密码时，将 `digits`、`ascii_letters` 等组合作为可选字符池。
- **数据清洗**：结合 `punctuation` 快速剔除文本中的标点符号。
