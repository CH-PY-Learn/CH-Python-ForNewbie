# 定义函数：展示使用 def 关键字定义函数，包含无 return、有 return、默认参数（如 a=None）以及类型注解（如 a: None）的写法

# ==================== 1. 无 return 的函数写法 ====================


# 定义一个无 return 的打招呼函数，仅执行控制台输出
def print_greeting(user_name):
    print(f"你好，{user_name}！欢迎学习 Python 函数。")


# 调用无 return 的函数
print("--- 1. 调用无 return 函数 ---")
print_greeting("小明")

# 尝试接收无 return 函数的返回值
return_val = print_greeting("李华")
# Python 中未写 return 的函数默认返回 None
print("无 return 函数的返回值：", return_val)


# 单独使用 return（不带返回值），用于在满足特定条件时提前结束函数
def check_entry_age(age):
    if age < 18:
        print(f"年龄为 {age} 岁，未成年不可进入。")
        return  # 提前退出函数，后续代码不执行
    print(f"年龄为 {age} 岁，符合进入要求。")


print("\n--- 调用带提前退出 return 的函数 ---")
check_entry_age(15)
check_entry_age(22)


# ==================== 2. 有 return 的函数写法 ====================


# 定义一个返回计算结果的函数
def calculate_sum(number_a, number_b):
    result = number_a + number_b
    return result


print("\n--- 2. 调用带 return 的计算函数 ---")
sum_value = calculate_sum(12, 18)
print("两数相加结果：", sum_value)


# 结合条件判断返回不同的结果
def check_pass_status(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"


student_status = check_pass_status(75)
print("学生考试状态：", student_status)


# return 返回多个值：多个值用逗号分隔，Python 会将其打包为元组返回
def get_circle_properties(radius):
    pi_value = 3.14159
    circumference = 2 * pi_value * radius
    area = pi_value * (radius ** 2)
    return circumference, area


print("\n--- 调用返回多个值的函数 ---")
# 方式一：使用单个变量接收元组
circle_info = get_circle_properties(5)
print("返回的完整元组：", circle_info)

# 方式二：多元赋值直接解包接收
circle_circumference, circle_area = get_circle_properties(5)
print(f"圆周长：{circle_circumference:.2f}，圆面积：{circle_area:.2f}")


# ==================== 3. 默认参数值写法（如 a=None） ====================

print("\n--- 3. 默认参数与 a=None 用法 ---")


# 常规默认参数：未传参时使用预设值
def show_user_profile(username, user_role="普通用户"):
    print(f"用户名：{username}，身份：{user_role}")


show_user_profile("张三")
show_user_profile("李四", "管理员")


# a=None 作为可选参数占位符
def send_system_message(content, tag=None):
    # 通过判断 tag 是否为 None 区分是否传入实参
    if tag is None:
        tag = "默认通知"
    print(f"[{tag}] {content}")


send_system_message("系统将于今晚维护升级")
send_system_message("密码修改成功", "安全中心")


# a=None 避免可变默认对象（如列表/字典）在多次调用间共享
def append_student_record(name, records_list=None):
    if records_list is None:
        records_list = []
    records_list.append(name)
    return records_list


first_batch = append_student_record("小红")
second_batch = append_student_record("小蓝")
print("第一次调用生成记录：", first_batch)
print("第二次调用独立记录：", second_batch)


# ==================== 4. 变量类型注解写法（如 a: None） ====================

print("\n--- 4. 类型注解与类型提示用法 ---")


# 基础类型注解与 -> None 无返回值注解
def display_header(title: str, level: int) -> None:
    print(f"{'#' * level} {title}")


display_header("Python 教学", 1)


# a: None 注解、a: str | None 联合类型注解与默认值组合
def handle_session(session_id: int, placeholder: None = None, description: str | None = None) -> bool:
    """
    session_id: 预期 int 类型
    placeholder: 预期 None 类型（a: None），默认值为 None（= None）
    description: 预期 str 或 None 类型，默认值为 None
    -> bool: 预期返回布尔值
    """
    print(f"处理会话 {session_id}，占位符: {placeholder}，说明: {description}")
    return True


handle_session(1001)
handle_session(1002, None, "用户主动登录")


# 类型注解的非强制性：运行时不会强制拦截不匹配类型
def multiply_data(factor: int) -> int:
    return factor * 2


print("符合类型注解调用（整数）：", multiply_data(5))
# 传入字符串（与 int 注解不符），Python 解释器仍正常执行字符串翻倍
print("不符合类型注解调用（字符串）：", multiply_data("Python"))

"""
函数定义、返回值、默认参数与类型注解核心总结：
1. 返回值机制：
   - 没有 `return` 语句或仅有空 `return` 的函数，默认返回 `None`。
   - 函数通过 `return 值1, 值2` 返回多个值时，Python 会自动打包为一个元组（tuple）。
2. 默认参数规则：
   - 默认参数必须置于所有位置参数之后。
   - 推荐使用 `a=None` 作为默认值占位符，并在函数体内动态初始化可变对象（如列表/字典），防止多次调用共享同一对象状态。
3. 类型注解特性：
   - 形参注解 `a: int`、`a: None` 与返回值注解 `-> None` 属于类型提示元数据，Python 解释器在运行时不会强制拦截类型不匹配的传入。
"""
