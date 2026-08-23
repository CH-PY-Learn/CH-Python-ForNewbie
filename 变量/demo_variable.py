# 变量定义：展示各种数据类型变量的定义与引用

# ==================== 1. 基础数据类型变量定义 ====================

name = "小明"  # 字符串
age = 18  # 整数
retired = False  # 布尔值


# ==================== 2. 容器类型变量定义 ====================

school_friends = ["小张", "小豪", "小美", "小丽"]
game_friends = ["我会打破枷锁", "嘉豪", "Passion", "小张", "小美"]
# 列表

friends = set(school_friends + game_friends)  # 集合去重

score_subjects = {
    "Science": 60,
    "Math": 60,
    "Chinese": 60,
    "English": 60,
    "PE": 60,
    "Geography": 60,
    "History": 60,
    "Society": 60
}
# 字典


# ==================== 3. 函数对象引用与变量打印 ====================

printer0 = print  # 将内置 print 函数赋值给变量

printer0(f"名字: {name}, 年龄: {age}, 退休: {retired}")
printer0(f"学校朋友: {school_friends}, 游戏好友: {game_friends}")
printer0(f"朋友: {friends}")
printer0(f"学科分数: {score_subjects}")

"""
变量定义核心总结：
1. 变量命名与类型：
   - Python 是动态类型语言，无需声明变量类型，变量名直接引用内存中的对象。
   - 变量命名遵循 PEP 8 规范，使用小写字母和下划线组合。
2. 头等对象特性：
   - 函数在 Python 中是一等公民，可以将函数对象（如 `print`）赋值给变量并像函数一样直接调用。
"""
