# `json` 数据序列化模块

## 概览

`json` 是 Python 标准库中用于处理 JSON（JavaScript Object Notation）数据格式的模块。

JSON 是一种轻量级、跨语言、纯文本的数据交换标准，被广泛应用于网络 API 传输、配置文件存储以及跨平台数据持久化等场景。

`json` 模块提供了在 **Python 内存对象**（如字典、列表等）与 **JSON 文本数据**（字符串或文件流）之间进行双向转换的能力：

- **序列化（Serialization / 编码）**：将 Python 原生对象转换为 JSON 格式文本。
- **反序列化（Deserialization / 解码）**：将 JSON 格式文本解析还原为 Python 原生对象。

---

## 核心机制：字符串处理（`s` 后缀）与文件流处理

`json` 模块的核心 API 由 4 个函数构成，其命名后缀体现了处理对象的类型差异：

- **带 `s` 后缀（`dumps` / `loads`）**：`s` 代表 **String（字符串）**。专门用于在 **内存中的 Python 对象**与 **JSON 格式字符串（
  `str`）**之间进行相互转换。
- **不带 `s` 后缀（`dump` / `load`）**：专门用于在 **内存中的 Python 对象**与**支持读写的文件对象（File-like Stream
  Object）**之间进行相互转换。

---

## 核心函数详解

### 1. `dumps(obj, ...)`：将 Python 对象序列化为 JSON 字符串

- **功能**：将传入的 Python 原生数据对象转换并返回为标准 JSON 格式的字符串。
- **参数说明**：
    - **`obj: Any`**：待转换的 Python 对象（通常为 `dict`、`list` 等）。
    - **`indent: int | None`**：格式化缩进空格数。不放该参数时默认值为 `None`，生成单行紧凑且无额外换行的 JSON 文本；若传入非负整数（如
      `indent=4`）或字符串，则生成按指定空格层级缩进与换行的美化 JSON 文本。
    - **`ensure_ascii: bool`**：是否将非 ASCII 字符全部转义。不放该参数时默认值为 `True`，会将所有非 ASCII 字符（如中文、表情符号）转义为
      `\uXXXX` 格式；若设为 `False`，则直接保留原生中文字符输出。
- **返回值**：标准 JSON 格式的字符串（`str` 类型）。
- **示例**：
  ```python
  from json import dumps

  user_info = {
      "name": "张三",
      "age": 25,
      "is_active": True,
      "skills": ["Python", "SQL"]
  }

  # 1. 默认紧凑单行格式（中文会被转义为 \uXXXX）
  compact_json = dumps(user_info)
  print("紧凑 JSON 字符串：", compact_json)

  # 2. 保留中文并带有 4 格缩进格式化
  pretty_json = dumps(user_info, indent=4, ensure_ascii=False)
  print("格式化 JSON 字符串：\n" + pretty_json)
  ```

---

### 2. `loads(s, ...)`：将 JSON 字符串解析为 Python 对象

- **功能**：解析包含合法 JSON 文本的字符串，并将其还原为对应的 Python 原生数据类型（通常为 `dict` 或 `list`）。
- **参数说明**：
    - **`s: str | bytes | bytearray`**：包含 JSON 数据的字符串或字节序列。
- **参数类型要求与常见异常**：
    - 参数必须为符合标准 JSON 规范的文本。
    - JSON 标准中键名和字符串值 **必须使用双引号 `"` 包裹**，不能使用 Python 的单引号 `'`。
    - 若传入格式非法字符串或末尾存在多余逗号，会抛出 `json.JSONDecodeError` 异常。
- **返回值**：解析还原后的 Python 原生对象（如 `dict`、`list`、`int`、`float` 等）。
- **示例**：
  ```python
  from json import loads

  json_text = '{"code": 200, "message": "请求成功", "data": [1, 2, 3]}'

  # 解析 JSON 字符串为 Python 字典
  parsed_dict = loads(json_text)
  print("解析后的 Python 字典：", parsed_dict)
  print("访问字典中的键：", parsed_dict["message"])
  print("数据类型：", type(parsed_dict))
  ```

---

### 3. `dump(obj, fp, ...)`：将 Python 对象序列化并写入文件对象

- **功能**：将 Python 原生对象直接序列化并写入到支持 `.write()` 方法的文本文件对象中。
- **参数说明**：
    - **`obj: Any`**：待序列化的 Python 对象。
    - **`fp: TextIO`**：指向目标文件的文本文件对象（由 `open(..., mode="w", encoding="utf-8")` 返回）。
    - **`indent: int | None`**：格式化缩进空格数。不放该参数时默认值为 `None`，向文件写入单行紧凑文本；若传入非负整数（如
      `indent=4`），则写入带格式化缩进与换行的美化文本。
    - **`ensure_ascii: bool`**：是否转义非 ASCII 字符。不放该参数时默认值为 `True`，将非 ASCII 字符转义为 `\uXXXX` 格式写入；若设为
      `False`，则直接保留原生中文字符写入。
- **返回值**：`None`。
- **示例**：
  ```python
  from json import dump

  config_data = {
      "app_name": "教学系统",
      "version": "1.0.0",
      "debug_mode": False
  }

  with open("config.json", mode="w", encoding="utf-8") as file:
      dump(config_data, file, indent=4, ensure_ascii=False)
  ```

---

### 4. `load(fp, ...)`：从文件对象中读取 JSON 并解析为 Python 对象

- **功能**：从支持 `.read()` 方法的文本文件对象中读取 JSON 文本，并直接解析还原为 Python 原生对象。
- **参数说明**：
    - **`fp: TextIO`**：指向包含有效 JSON 数据文件的文本文件对象（由 `open(..., mode="r", encoding="utf-8")` 返回）。
- **返回值**：解析还原后的 Python 原生对象（如 `dict` 或 `list`）。
- **示例**：
  ```python
  from json import load

  with open("config.json", mode="r", encoding="utf-8") as file:
      loaded_data = load(file)

  print("从文件加载的数据：", loaded_data)
  print("应用名称：", loaded_data["app_name"])
  ```

---

## Python 数据类型与 JSON 类型映射对照表

在进行序列化与反序列化时，Python 内置类型与 JSON 标准类型之间存在明确的对应关系：

| Python 原生数据类型     | JSON 数据类型 | 转换说明与示例                                 |
|:------------------------|:--------------|:-----------------------------------------------|
| **`dict`**              | **`object`**  | 键值对映射，JSON 语法形式为 `{"key": "value"}` |
| **`list`**、**`tuple`** | **`array`**   | 序列有序列表，JSON 语法形式为 `[1, 2, 3]`      |
| **`str`**               | **`string`**  | 文本字符串，JSON 中必须使用双引号 `"text"`     |
| **`int`**、**`float`**  | **`number`**  | 数值类型（包含整数与浮点数）                   |
| **`True`**              | **`true`**    | 布尔真值，JSON 中为小写 `true`                 |
| **`False`**             | **`false`**   | 布尔假值，JSON 中为小写 `false`                |
| **`None`**              | **`null`**    | 空值，JSON 中对应为 `null`                     |

> **注意**：
> 1. Python 中的元组（`tuple`）在序列化为 JSON 时会被统一转换为 JSON 的 `array`，反序列化回来时将成为 Python 的列表（
     `list`）。
> 2. JSON 对象的键名（Key）在规范中 **必须为字符串类型**。如果 Python 字典的键为整数（如 `{1: "a"}`），在序列化后键名会被自动转为字符串
     `"1"`。
> 3. 集合（`set`）、函数对象或自定义类实例无法直接被默认序列化器转换，若直接传入会抛出
     `TypeError: Object of type set is not JSON serializable`。

---

## `json` 四大核心函数速查表

| 函数名              | 输入源与参数类型                       | 输出目标与类型                            | 典型应用场景                                  |
|:--------------------|:---------------------------------------|:------------------------------------------|:----------------------------------------------|
| **`dumps(obj)`**    | `obj`: Python 内存对象                 | 返回 JSON 格式字符串（`str`）             | 网络 API 响应构建、文本日志打印、数据传输准备 |
| **`loads(s)`**      | `s`: JSON 格式字符串（`str`）          | 返回解析后的 Python 对象（`dict`/`list`） | 解析 API 返回结果、解析字符串配置             |
| **`dump(obj, fp)`** | `obj`: Python 对象，`fp`: 可写文件对象 | 直接写入文件（`None`）                    | 保存用户配置、持久化存储结构化数据到磁盘      |
| **`load(fp)`**      | `fp`: 可读文件对象                     | 返回解析后的 Python 对象（`dict`/`list`） | 读取本地 JSON 配置文件、加载离线数据文件      |
