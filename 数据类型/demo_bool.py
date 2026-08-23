# bool：布尔值类型与假值转换

# ==================== 1. 空容器与假值对象定义 ====================

empty_list = []
zero_list = list()

empty_dictionary = {}
zero_dictionary = dict()

empty_string = ""
zero_string = str()
# 针对字符串也可以用空内容的 单/双/三 引号，str() 括号里面同样可以用空字符串表示

empty_set = set()

bool_false1 = False
bool_false2 = not True
bool_false3 = None

int_false = 0


# ==================== 2. bool() 转换与布尔假值验证 ====================

print(bool(empty_list))
print(bool(zero_list))
print(bool(empty_dictionary))
print(bool(zero_dictionary))
print(bool(empty_string))
print(bool(zero_string))
print(bool(empty_set))
print(bool(bool_false1))
print(bool(bool_false2))
print(bool(bool_false3))
print(bool(int_false))

# 只要确保 bool() 括号内的内容为空或 False，那么输出为 False
# 基于以上代码，其他非空/非零表达式均为 True 表达式

"""
bool 布尔类型核心总结：
1. 布尔值范围：
   - 只有 `True` 与 `False` 两个布尔常量。
2. 假值（Falsy）对象：
   - 空容器（`[]`, `()`, `{}`, `set()`, `""`）、数字零（`0`, `0.0`）、`None` 与 `False` 在布尔上下文中求值均为 `False`。
   - 其余非空、非零对象求值均为 `True`。
"""
