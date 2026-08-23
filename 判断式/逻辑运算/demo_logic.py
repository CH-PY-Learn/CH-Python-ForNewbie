# 逻辑运算符：展示 and, or, not 以及优先级规则

# ==================== 1. 逻辑与（and）：多条件同时成立 ====================

age = 20
has_id_card = True

if age >= 18 and has_id_card:
    print("年龄达标且持有证件，允许办理业务")
# 当 age >= 18 和 has_id_card 两个条件同时成立时，执行代码块

score_math = 90
score_english = 85

if score_math >= 90 and score_english >= 90:
    print("两门学科均为优秀")
else:
    print("未同时达到双优秀")
# 只有在两门学科的得分均超过 90 分时，方可认定为双优。


# ==================== 2. 逻辑或（or）：满足任一条件 ====================

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("今天是休息日")
# 只要 is_weekend 或 is_holiday 其中一个为 True，就会执行代码块

has_coupon = False
is_vip = True

if has_coupon or is_vip:
    print("享有优惠资格")
# 持有优惠券或者是 VIP 用户，即可享受优惠


# ==================== 3. 逻辑非（not）：布尔值取反 ====================

is_raining = False

if not is_raining:
    print("今天没有下雨，可以出行")
# 当 is_raining 为 False 时，not is_raining 为 True，执行代码块

is_logged_in = False

if not is_logged_in:
    print("请先登录账号")
# 当未登录时，提示用户登录


# ==================== 4. 逻辑运算符优先级与括号组合 ====================

# 逻辑运算符的优先级为：not > and > or；可以使用括号明确或调整优先级

user_age = 25
has_ticket = False
is_admin = True

if (user_age >= 18 and has_ticket) or is_admin:
    print("允许进入活动会场")
else:
    print("未达到进入活动会场的条件")

"""
逻辑运算核心总结：
1. 逻辑运算符：
   - `and`：逻辑与，所有条件均为真时结果为真；
   - `or`：逻辑或，至少一个条件为真时结果为真；
   - `not`：逻辑非，对布尔值进行取反。
2. 运算优先级：
   - 优先级顺序为：`not` > `and` > `or`。可以使用小括号 `()` 明确或调整运算次序。
3. 短路求值机制：
   - `and` 遇到首个假值即停止计算；`or` 遇到首个真值即停止计算。
"""
