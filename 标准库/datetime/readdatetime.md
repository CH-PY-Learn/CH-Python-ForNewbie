# `datetime` 日期与时间模块

## 概览

`datetime` 是 Python 中用于处理日期（年、月、日）和时间（时、分、秒、微秒）的高级标准库。

与专注于时间戳和底层操作的 `time` 模块相比，`datetime` 提供了更加面向对象的类结构，支持直观的日期运算、时间差计算、格式化转换与解析。

---

## 核心类与常用方法

### 1. `datetime` 类：日期与时间结合

- **`datetime.now()`**：获取当前的本地日期与时间对象。
- **`datetime(year, month, day, hour, minute, second)`**：构造指定的日期时间对象。
- **属性提取**：可通过 `.year`、`.month`、`.day`、`.hour`、`.minute`、`.second` 直接读取各组成部分。
- **示例**：
  ```python
  from datetime import datetime

  now = datetime.now()
  print("当前完整时间：", now)
  print("当前年份：", now.year)
  print("当前小时：", now.hour)
  ```

### 2. `date` 类：纯日期处理

- **`date.today()`**：获取今天的日期（不包含时分秒）。
- **`date(year, month, day)`**：构造指定的日期对象。
- **示例**：
  ```python
  from datetime import date

  today = date.today()
  print("今天日期：", today)
  ```

### 3. `time` 类：纯时间处理

- **`time(hour, minute, second, microsecond)`**：构造一个独立的时间对象，表示一天中的具体时刻（不包含日期）。
- **示例**：
  ```python
  from datetime import time

  meeting_time = time(14, 30, 0)
  print("会议时刻：", meeting_time)
  ```

### 4. `timedelta` 类：时间间隔与日期加减计算

- **功能**：表示两个日期或时间之间的差值/跨度。支持 `days`（天）、`hours`（小时）、`minutes`（分钟）、`seconds`（秒）等参数。
- **日期运算**：日期对象与 `timedelta` 可以直接使用 `+` 或 `-` 进行加减运算，从而计算未来或过去的某个日期。
- **示例**：
  ```python
  from datetime import datetime, timedelta

  current_time = datetime.now()
  ten_days_later = current_time + timedelta(days=10)
  three_hours_ago = current_time - timedelta(hours=3)

  print("十天后：", ten_days_later)
  print("三小时前：", three_hours_ago)
  ```

### 5. `strftime` 与 `strptime`：字符串与对象的相互转换

- **`strftime(format)`**（String Format Time）：将 `datetime` 对象转换为指定格式的字符串。
- **`strptime(date_string, format)`**（String Parse Time）：将符合特定格式的文本字符串解析为 `datetime` 对象。
- **示例**：
  ```python
  from datetime import datetime

  # 对象 -> 字符串（格式化）
  now = datetime.now()
  text = now.strftime("%Y年%m月%d日 %H时%M分%S秒")
  print("格式化文本：", text)

  # 字符串 -> 对象（解析）
  parsed_date = datetime.strptime("2026-08-22 18:00:00", "%Y-%m-%d %H:%M:%S")
  print("解析得到的对象：", parsed_date)
  ```
