# None：空值类型的表达方式

# ==================== 1. 直接赋值 None ====================

empty0 = None


# ==================== 2. 无返回值函数赋值得到 None ====================

def func1():
    ...


empty1 = func1()


# ==================== 3. 显式 return None ====================

def func2():
    return None


empty2 = func2()

print(empty0)
print(empty1)
print(empty2)
# 可以通过直接定义变量为 None，赋值为一个没有返回值的函数或者用函数返回 None 来表达

"""
None 空值类型核心总结：
1. None 特性：
   - `None` 是 `NoneType` 类型的唯一单例对象，表示“空”或“不存在的值”。
2. 常见来源：
   - 变量显式赋值 `None`；
   - 未显式指定返回值的函数默认返回 `None`。
"""
