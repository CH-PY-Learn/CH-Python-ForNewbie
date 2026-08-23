# datetime 模块：提供面向对象的日期、时间、时间间隔及格式化解析功能
from datetime import date, datetime, time, timedelta

# ==================== 1. datetime.now 与构造指定日期时间 ====================

current_moment = datetime.now()
print("当前日期与时间：", current_moment)
print(f"年: {current_moment.year}, 月: {current_moment.month}, 日: {current_moment.day}")
print(f"时: {current_moment.hour}, 分: {current_moment.minute}, 秒: {current_moment.second}")

custom_moment = datetime(2026, 10, 1, 8, 30, 0)
print("自定义构造的日期时间：", custom_moment)


# ==================== 2. date 与 time：单独处理日期与时间 ====================

today_date = date.today()
print("今天的日期：", today_date)

custom_date = date(2026, 12, 31)
print("自定义日期：", custom_date)

alarm_time = time(7, 30, 0)
print("闹钟时间：", alarm_time)


# ==================== 3. timedelta：时间跨度计算（加减天数与小时） ====================

span_one_week = timedelta(days=7)
next_week_date = current_moment + span_one_week
print("一周后的时间：", next_week_date)

span_three_hours = timedelta(hours=3, minutes=15)
earlier_time = current_moment - span_three_hours
print("3小时15分钟前的时间：", earlier_time)

# 计算两个日期之间的差值
target_date = datetime(2026, 12, 31, 23, 59, 59)
time_difference = target_date - current_moment
print(f"距离目标时刻还剩：{time_difference.days} 天，总计 {time_difference.total_seconds():.0f} 秒")


# ==================== 4. strftime：日期时间对象格式化为字符串 ====================

formatted_text = current_moment.strftime("%Y/%m/%d %H:%M:%S")
print("格式化字符串输出：", formatted_text)


# ==================== 5. strptime：字符串按格式解析为 datetime 对象 ====================

date_string = "2026-09-10 14:20:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("从字符串解析出的 datetime 对象：", parsed_datetime)
print("解析后的年份：", parsed_datetime.year)

"""
datetime 模块核心总结：
1. 核心类与对象：
   - `datetime.now()`：获取当前完整日期和时间对象。
   - `date.today()`：获取当前纯日期对象（年-月-日）。
   - `time(hour, minute, second)`：构造纯时间对象。
2. 时间计算（timedelta）：
   - `timedelta(days=..., hours=...)`：表示时间间隔，支持与 `datetime` / `date` 进行加减运算或两时间相减得到时间差。
3. 格式化与解析：
   - `strftime(format)`：将日期时间对象格式化为指定格式的字符串。
   - `strptime(date_string, format)`：将符合指定格式的日期时间字符串解析为 `datetime` 对象。
"""
