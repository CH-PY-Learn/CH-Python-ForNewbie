# time 模块：提供时间戳获取、时间格式化、程序延时及性能计时等底层时间功能
from time import ctime, localtime, perf_counter, sleep, strftime, time

# ==================== 1. time：获取当前时间戳 ====================

current_timestamp = time()
print("当前时间戳（秒）：", current_timestamp)


# ==================== 2. ctime：将时间戳转换为易读字符串 ====================

human_readable_time = ctime(current_timestamp)
print("易读时间格式：", human_readable_time)


# ==================== 3. localtime：将时间戳转为本地时间结构体 ====================

current_local_time = localtime(current_timestamp)
print("年份：", current_local_time.tm_year)
print("月份：", current_local_time.tm_mon)
print("日期：", current_local_time.tm_mday)
print("小时：", current_local_time.tm_hour)
print("分钟：", current_local_time.tm_min)
print("秒数：", current_local_time.tm_sec)


# ==================== 4. strftime：自定义格式化时间字符串 ====================

formatted_date_time = strftime("%Y-%m-%d %H:%M:%S", current_local_time)
print("自定义格式化输出：", formatted_date_time)


# ==================== 5. perf_counter 与 sleep：高精度性能计时与程序延时 ====================

start_timer = perf_counter()

# 使用 sleep 暂停程序指定秒数
print("开始执行短暂停顿...")
sleep(0.05)
print("短暂停顿结束")

end_timer = perf_counter()
execution_duration = end_timer - start_timer
print(f"代码执行实际耗时：{execution_duration:.6f} 秒")

"""
time 模块核心总结：
1. 时间获取与结构体：
   - `time()`：获取当前时间戳（自 Unix 纪元起经过的秒数浮点数）。
   - `localtime()`：将时间戳转换为本地时间结构体对象（struct_time）。
2. 格式化与展示：
   - `strftime(format, t)`：根据自定义格式字符串（如 `%Y-%m-%d %H:%M:%S`）格式化时间。
   - `ctime()`：返回形如 'Thu Oct 1 08:30:00 2026' 的固定格式时间字符串。
3. 延时与计时：
   - `sleep(secs)`：挂起当前线程指定的秒数。
   - `perf_counter()`：高精度性能计数器，常用于测量代码执行耗时。
"""
