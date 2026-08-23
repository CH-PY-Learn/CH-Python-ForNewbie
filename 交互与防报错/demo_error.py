# 异常处理：展示 try-except, try-except-else, try-except-finally 与裸 except

# ==================== 1. 基础 try-except：捕获指定类型的异常 ====================

user_age_str = "twenty"

try:
    age = int(user_age_str)
    print("年龄转换为：", age)
except ValueError:
    print("年龄必须为纯数字格式，转换失败")
# 当 int() 遇到无法转换的文本时触发 ValueError，程序由 except 捕获而不会崩溃


# ==================== 2. 多个 except 与 try-except-else 分支 ====================

number_text = "0"

try:
    divisor = int(number_text)
    result = 100 / divisor
except ValueError:
    print("请输入有效的数字字符串")
except ZeroDivisionError:
    print("除数不能为 0")
else:
    print("计算结果为：", result)
# 多个 except 会自上而下依次匹配异常类型；若未发生任何异常则执行 else


# ==================== 3. try-except-finally：必定执行的代码块 ====================

price_str = "50"

try:
    print("开始处理商品价格数据...")
    total_price = float(price_str) * 2
    print("计算折后总价：", total_price)
except ValueError:
    print("价格数据格式有误")
finally:
    print("数据处理流程结束（finally 必定执行）")
# finally 代码块常用于无论成功还是失败都需要进行的资源清理或收尾工作


# ==================== 4. 裸 except（bare except）：捕获所有异常 ====================

raw_data = "invalid"

try:
    processed_value = 10 / int(raw_data)
except:
    print("发生了未知错误")

"""
异常处理核心总结：
1. try-except 基础捕获：
   - `try` 块放置可能引发异常的代码，`except <ErrorType>:` 捕获并处理特定异常，防止程序崩溃。
2. 多分支与 else：
   - 支持多个 `except` 分支分别处理不同异常；当 `try` 块内未发生任何异常时，执行 `else` 块。
3. finally 最终执行：
   - 无论是否发生异常、无论是否被 `except` 捕获，`finally` 块内的代码均保证执行，常用于资源释放与状态清理。
4. 裸 except 特性：
   - 裸 `except:` 可捕获包括系统中断信号在内的所有异常（基于 `BaseException`），若仅需捕获常规业务异常，通常显式捕获 `Exception`。
"""
