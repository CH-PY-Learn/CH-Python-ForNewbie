# 随机数模块：展示 randint, uniform, choice, choices (包含 k 与 weights), shuffle 以及 sample

from random import choice, choices, randint, sample, shuffle, uniform

# ==================== 1. randint：生成指定闭区间内的随机整数 ====================

print("--- 1. randint 随机整数 ---")

# randint(a, b) 要求参数为整数，返回 [a, b] 闭区间内的一个随机整数
random_int_1 = randint(1, 10)
random_int_2 = randint(100, 200)

print("生成 1 到 10 的随机整数：", random_int_1)
print("生成 100 到 200 的随机整数：", random_int_2)


# ==================== 2. uniform：生成指定区间的随机浮点数 ====================

print("\n--- 2. uniform 随机浮点数 ---")

# uniform(a, b) 返回 [a, b] 区间内的随机浮点数
random_float_1 = uniform(1.0, 5.0)
random_float_2 = uniform(0.0, 100.0)

print("生成 1.0 到 5.0 之间的随机浮点数：", random_float_1)
print(f"保留两位小数展示：{random_float_1:.2f}")
print("生成 0.0 到 100.0 之间的随机浮点数：", random_float_2)


# ==================== 3. choice：从非空序列中随机选取单个元素 ====================

print("\n--- 3. choice 从序列中单选元素 ---")

# 参数必须为支持索引的非空序列（如 list, tuple, str, range）
fruit_list = ["苹果", "香蕉", "西瓜", "草莓", "葡萄"]
picked_fruit = choice(fruit_list)
print("从列表序列中随机选取一个水果：", picked_fruit)

direction_tuple = ("东", "南", "西", "北")
picked_direction = choice(direction_tuple)
print("从元组序列中随机选取一个方向：", picked_direction)

alphabet_str = "ABCDEFGHJKLMNPQRSTUVWXYZ"
picked_char = choice(alphabet_str)
print("从字符串序列中随机选取一个字符：", picked_char)


# ==================== 4. choices：有放回随机抽样与 k 参数 ====================

print("\n--- 4. choices 有放回抽样与 k 参数 ---")

# 基础有放回抽样：参数 k 指定抽样次数，返回包含 k 个元素的列表（可能包含重复项）
color_pool = ["红", "蓝", "绿", "黄"]
sampled_colors = choices(color_pool, k=5)
print("从颜色池中有放回抽取 5 次（k=5）：", sampled_colors)

# 从字符集序列中抽取 8 个字符生成随机验证码
digits_pool = "0123456789"
code_chars = choices(digits_pool, k=6)
print("随机 6 位数字验证码列表：", code_chars)
print("拼接为字符串验证码：", "".join(code_chars))

# 带有权重（weights）的有放回抽样
lottery_levels = ["特等奖", "一等奖", "二等奖", "参与奖"]
lottery_weights = [1, 5, 14, 80]  # 相对概率比例：1%、5%、14%、80%
drawn_prizes = choices(lottery_levels, weights=lottery_weights, k=10)
print("按权重有放回抽取 10 次奖项：", drawn_prizes)


# ==================== 5. 扩展：shuffle（原地打乱）与 sample（无放回抽样） ====================

print("\n--- 5. 扩展：shuffle 与 sample ---")

# shuffle(x)：原地打乱可变列表序列（直接修改原列表，返回 None）
card_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("打乱前列表：", card_numbers)
shuffle(card_numbers)
print("shuffle 原地打乱后列表：", card_numbers)

# sample(population, k)：无放回抽样，抽取的 k 个元素互不重复
id_pool = range(1001, 1020)
lucky_winners = sample(id_pool, k=3)
print("无放回抽取 3 个互不重复的中奖编号：", lucky_winners)

"""
random 模块核心总结：
1. randint(a, b)：
   - 参数要求为整数，返回 [a, b] 闭区间内的一个随机整数（包含两端边界值）。
   - 要求 a <= b，若 a > b 则抛出 ValueError。
2. uniform(a, b)：
   - 生成并在 [a, b] 区间内返回一个均匀分布的随机浮点数（float）。
3. choice(seq)：
   - 参数必须为非空序列（Sequence），如 list, tuple, str, range。
   - 不支持 set 或 dict 等无序容器，若序列为空则抛出 IndexError。
   - 随机返回序列中的单个元素本身。
4. choices(population, weights=None, *, cum_weights=None, k=1)：
   - 进行有放回抽样（Sampling with replacement），抽出的多次结果可能出现重复元素。
   - 参数 population 为待抽取的候选序列/可迭代对象。
   - 参数 k 指定抽样次数/抽取结果的元素数量，默认 k=1。
   - 返回值始终为包含 k 个元素的列表（list）。
   - 可通过 weights 指定各元素的抽取权重比例。
5. 扩展函数：
   - shuffle(x)：直接原地打乱可变列表，返回 None。
   - sample(population, k)：无放回抽样，抽取 k 个互不重复的独立元素并返回列表。
"""
