# 数据序列化模块：展示 dumps, loads, dump, load 的功能与字符串/文件对象/Python数据类型的转换

import os
from json import dump, dumps, load, loads

# ==================== 1. dumps：Python 对象转换为 JSON 格式字符串 ====================

print("--- 1. dumps 序列化为字符串 ---")

student_profile = {
    "student_id": 1001,
    "name": "李雷",
    "is_graduated": False,
    "scores": [95.5, 88.0, 92.0],
    "contact": {
        "email": "lilei@example.com",
        "phone": None
    }
}

# 默认转换：单行紧凑字符串，非 ASCII 字符（如中文）转义为 \uXXXX
default_json_str = dumps(student_profile)
print("默认 dumps 结果（单行且转义中文）：")
print(default_json_str)

# 格式化转换：indent=4 设置 4 格缩进，ensure_ascii=False 原样输出中文
pretty_json_str = dumps(student_profile, indent=4, ensure_ascii=False)
print("\n格式化 dumps 结果（带缩进并保留中文）：\n" + pretty_json_str)


# ==================== 2. loads：JSON 格式字符串解析为 Python 原生对象 ====================

print("--- 2. loads 字符串反序列化 ---")

incoming_json_data = '{"status": 200, "message": "查询成功", "active": true, "tags": ["学生", "优秀"]}'

# 解析为 Python 原生字典对象
parsed_response = loads(incoming_json_data)
print("解析后的 Python 对象：", parsed_response)
print("对象类型：", type(parsed_response))
print("访问解析后的状态码：", parsed_response["status"])
print("访问解析后的布尔值（JSON true -> Python bool）：", parsed_response["active"], type(parsed_response["active"]))
print("访问解析后的列表项：", parsed_response["tags"][0])


# ==================== 3. dump：Python 对象序列化并写入文件对象 ====================

print("\n--- 3. dump 序列化写入文件 ---")

app_settings = {
    "project_name": "Python 教学项目",
    "version": "2.0.0",
    "port": 8080,
    "enabled_modules": ["random", "json", "math", "time"]
}

temp_json_path = "temp_settings.json"

# 使用 open(...) 获取文件对象，dump 直接将 Python 对象序列化并写入文件流
with open(temp_json_path, mode="w", encoding="utf-8") as json_file:
    dump(app_settings, json_file, indent=4, ensure_ascii=False)

print(f"数据已成功通过 dump 写入文件：{temp_json_path}")


# ==================== 4. load：从文件对象读取并反序列化为 Python 对象 ====================

print("\n--- 4. load 从文件读取并解析 ---")

# 使用 open(...) 获取只读文件对象，load 直接从文件流中读取 JSON 并解析为 Python 字典
with open(temp_json_path, mode="r", encoding="utf-8") as json_file:
    loaded_settings = load(json_file)

print("从文件 load 解析出的 Python 字典：", loaded_settings)
print("项目名称：", loaded_settings["project_name"])
print("启用模块列表：", loaded_settings["enabled_modules"])

# 清理演示临时文件
if os.path.exists(temp_json_path):
    os.remove(temp_json_path)
print("演示临时文件已清理完毕。")

"""
json 模块核心总结：
1. dumps 与 loads（内存字符串转换）：
   - `json.dumps(obj)`：将 Python 原生对象序列化为 JSON 格式的字符串（str）。
   - `json.loads(s)`：将 JSON 格式字符串解析为 Python 原生数据结构。
2. dump 与 load（文件流持久化读写）：
   - `json.dump(obj, fp)`：将 Python 对象序列化并直接写入支持 `.write()` 的文件对象中。
   - `json.load(fp)`：从支持 `.read()` 的文件对象中直接读取并反序列化为 Python 对象。
3. 格式化与中文编码控制：
   - `indent=4`：使输出的 JSON 字符串按层级缩进排版，提高可读性。
   - `ensure_ascii=False`：保留中文字符原生输出，避免被转义为 `\\uXXXX` 格式。
4. 数据类型映射规则：
   - dict -> object, list/tuple -> array, str -> string, int/float -> number, True/False -> true/false, None -> null。
"""
