# 变量赋值与复合赋值运算符

# ==================== 1. 变量定义与重新赋值 ====================

somebody = "小明"  # 第一次赋值，也是定义
print(somebody)

somebody = "小美"  # 重新赋值
print(somebody)


# ==================== 2. 复合赋值运算符（加法 += 与减法 -=） ====================

# 复合赋值运算符会先进行运算，再将结果重新赋值给左侧变量。

score = 60
score += 10  # 等价于 score = score + 10
print(score)

score -= 5  # 等价于 score = score - 5
print(score)


# ==================== 3. 复合赋值运算符（乘法 *=、整除 //=、幂运算 **=、取余 %=） ====================

number = 6
number *= 2  # 等价于 number = number * 2
print(number)

number //= 5  # 等价于 number = number // 5
print(number)

number **= 3  # 等价于 number = number ** 3
print(number)

number %= 5  # 等价于 number = number % 5
print(number)

"""
变量赋值与复合运算核心总结：
1. 变量赋值机制：
   - 使用 `=` 进行赋值绑定，首次赋值即完成变量定义，再次赋值会更新变量所指向的对象。
2. 复合赋值运算符：
   - `+=`、`-=`、`*=`、`/=`、`//=`、`%=`、`**=` 结合了运算与重新赋值，先计算表达式结果再赋值给左侧变量。
"""
