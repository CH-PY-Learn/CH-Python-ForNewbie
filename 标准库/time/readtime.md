# `time` 时间模块

## 概览

`time` 是 Python 提供的用于处理时间、时间戳、时间结构体以及程序延时等底层时间操作的标准库。

在计算机系统中，时间通常以**时间戳（Timestamp）**的形式表示，即从纪元时间（Epoch，1970 年 1 月 1 日 00:00:00 UTC）开始经过的总秒数（浮点数）。

---

## 常用函数与方法

### 1. `time()`：获取当前时间戳

- **功能**：返回当前时刻的时间戳（浮点数，单位为秒）。
- **示例**：
  ```python
  from time import time

  current_timestamp = time()
  print("当前时间戳：", current_timestamp)
  ```

### 2. `sleep(seconds)`：程序延时暂停

- **功能**：让程序挂起/暂停执行指定的秒数（支持整数或浮点数）。
- **示例**：
  ```python
  from time import sleep

  print("准备开始...")
  sleep(1.5)  # 程序暂停 1.5 秒
  print("1.5 秒后继续执行")
  ```

### 3. `localtime([secs])`：将时间戳转换为本地时间结构体

- **功能**：将传入的时间戳（缺省时为当前时间）转换为本地时区的时间元组/结构体（`struct_time`）。
- **结构体字段**：包含 `tm_year`（年）、`tm_mon`（月）、`tm_mday`（日）、`tm_hour`（时）、`tm_min`（分）、`tm_sec`（秒）、`tm_wday`（星期，0 代表周一）等。
- **示例**：
  ```python
  from time import localtime

  local_info = localtime()
  print("当前年份：", local_info.tm_year)
  print("当前月份：", local_info.tm_mon)
  ```

### 4. `strftime(format[, t])`：格式化时间输出

- **功能**：将时间结构体（如 `localtime()` 的返回值）按照指定的格式字符串转换为自定义格式的文本。
- **常见格式占位符**：
  - `%Y`：四位年份（如 `2026`）
  - `%m`：两位月份（`01`-`12`）
  - `%d`：两位日期（`01`-`31`）
  - `%H`：24 小时制小时（`00`-`23`）
  - `%M`：两位分钟数（`00`-`59`）
  - `%S`：两位秒数（`00`-`59`）
- **示例**：
  ```python
  from time import localtime, strftime

  formatted_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
  print("格式化时间：", formatted_time)
  ```

### 5. `perf_counter()`：高精度性能计时器

- **功能**：返回一个具有最高可用分辨率的浮点数时钟值，专门用于精确测量一段代码的执行耗时。
- **示例**：
  ```python
  from time import perf_counter, sleep

  start_time = perf_counter()
  sleep(0.1)
  end_time = perf_counter()

  elapsed_time = end_time - start_time
  print("执行耗时：", elapsed_time, "秒")
  ```

### 6. `ctime([secs])`：转换为易读的字符串

- **功能**：将时间戳直接转换为本地易读的固定格式时间字符串（例如 `"Sat Aug 22 17:24:00 2026"`）。
- **示例**：
  ```python
  from time import ctime

  time_string = ctime()
  print("当前时间字符串：", time_string)
  ```
