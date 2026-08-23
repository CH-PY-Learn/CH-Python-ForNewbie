# function：函数定义与返回值机制

# 除了 Python 自带的内置函数以外，程序员也可以自行定义一个函数

# ==================== 1. 无返回值函数定义与默认返回 None ====================

def say_hello():
    print("hello")


# 这是一个没有返回值的函数，若将一个变量赋值为该函数被调用后的值，那么该变量的值为 None
hello = say_hello()
print(hello)


# ==================== 2. 有返回值函数定义与 return 语句 ====================

def division():
    return 5 / 5


# 这是一个有返回值的函数
result_of_5_divide_5 = division()  # 被调用后的值会赋值给变量
print(result_of_5_divide_5)

"""
function 函数类型核心总结：
1. 函数定义与调用：
   - 使用 `def` 关键字定义函数，通过 `()` 传入参数并触发调用执行。
2. 返回值特性：
   - 函数可通过 `return` 返回计算结果；若无 `return` 或仅写 `return`，则默认返回 `None`。
"""
