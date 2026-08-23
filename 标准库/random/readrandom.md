# `random` 随机数与随机抽样模块

## 概览

`random` 是 Python 标准库中用于生成伪随机数（Pseudo-random Numbers）、实现序列随机抽样、打乱以及概率选择的核心模块。

在模拟仿真、数据打乱、随机抽取样本、游戏开发以及生成测试数据等场景中，`random` 模块提供了丰富且直观的函数工具。

---

## 核心函数与机制

### 1. `randint(a, b)`：生成指定范围内的随机整数

- **功能**：返回闭区间 $[a, b]$ 内的一个随机整数，满足 $a \le n \le b$（包含两端边界值 $a$ 和 $b$）。
- **参数说明**：
  - `a: int`：区间的下界整数（包含）。
  - `b: int`：区间的上界整数（包含）。
- **参数类型要求**：
  - 参数 `a` 和 `b` 必须为整数类型。若传入浮点数或非数值类型会抛出 `TypeError`。
  - 参数必须满足 $a \le b$，若 $a > b$ 会抛出 `ValueError: empty range for randrange()`。
- **示例**：
  ```python
  from random import randint

  # 模拟掷骰子（点数 1 到 6 之间，包含 1 和 6）
  dice_point = randint(1, 6)
  print("骰子点数：", dice_point)

  # 生成指定范围的年份
  random_year = randint(2000, 2030)
  print("随机年份：", random_year)
  ```

---

### 2. `uniform(a, b)`：生成指定范围内的随机浮点数

- **功能**：生成并在区间 $[a, b]$ 内返回一个随机浮点数（实数）。
- **参数说明**：
  - `a: float | int`：区间的一个端点数值。
  - `b: float | int`：区间的另一个端点数值。
- **参数类型与行为说明**：
  - 参数可接收整数或浮点数，返回值类型统一为 `float`。
  - 端点大小无严格顺序限制：无论 $a \le b$ 还是 $a > b$，`uniform(a, b)` 均能在两端点之间生成均匀分布的浮点数。
- **示例**：
  ```python
  from random import uniform

  # 生成 0.0 到 10.0 之间的随机浮点数
  score = uniform(0.0, 10.0)
  print("随机评分：", score)
  print(f"保留两位小数格式化：{score:.2f}")
  ```

---

### 3. `choice(seq)`：从序列中随机选取单个元素

- **功能**：从给定的非空序列中随机返回**一个**元素。
- **参数说明**：
  - `seq: Sequence[T]`：待选择的序列对象。
- **参数类型与序列要求**：
  - **必须是序列类型（Sequence）**：即支持索引访问（`__getitem__`）与长度计算（`__len__`）的数据类型，包括列表（`list`）、元组（`tuple`）、字符串（`str`）、`range` 对象等。
  - **不支持无序容器**：若传入集合（`set`）或字典（`dict`），会直接抛出 `KeyError` 或 `TypeError`。若需要从集合中选择，需先将其转换为 `list` 或 `tuple`。
  - **序列不能为空**：若传入空序列（如 `[]`、`""`、`()`），会抛出 `IndexError: Cannot choose from an empty sequence`。
- **示例**：
  ```python
  from random import choice

  # 从列表序列中随机抽取一个元素
  colors = ["红色", "蓝色", "绿色", "黄色"]
  picked_color = choice(colors)
  print("抽取颜色：", picked_color)

  # 从字符串序列中随机抽取一个字符
  letters = "abcdefg"
  picked_char = choice(letters)
  print("抽取字符：", picked_char)

  # 从元组序列中随机抽取一个元素
  options = ("同意", "反对", "弃权")
  picked_option = choice(options)
  print("抽取选项：", picked_option)
  ```

---

### 4. `choices(population, weights=None, k=1)`：有放回随机抽样

- **功能**：从候选群体中进行**有放回抽样（Sampling with Replacement）**，并返回包含抽取元素的**列表**。
- **参数说明**：
  - **`population: Sequence[T] | Iterable[T]`**：待抽取的候选元素群体（序列或可迭代对象）。
  - **`k: int`**：抽样的次数（即返回列表的长度），默认为 `1`。
  - **`weights: Sequence[float | int] | None`**（可选）：候选元素对应的相对权重序列，长度必须与 `population` 一致。
  - **`cum_weights: Sequence[float | int] | None`**（可选）：候选元素的累加权重序列。注意 `weights` 与 `cum_weights` 不能同时传入。
- **`k` 参数的功能与抽样机制**：
  - **`k` 的作用**：指定从群体中独立抽取元素的总数量。若指定 `k=5`，则执行 5 次独立抽取，将这 5 个结果组合为一个列表返回。
  - **有放回抽样机制**：每次抽取后候选元素并不会从原池子中移除，下一次抽取依然面对完整的群体。因此在返回的列表中，**同一个元素可能被多次重复抽中**。
  - **返回值类型**：无论 `k` 值为多少（即使 `k=1`），`choices()` 的返回值始终是一个**列表（`list`）**。
- **示例**：
  ```python
  from random import choices

  # 1. 基础有放回抽样（指定 k 抽取多个元素）
  fruits = ["苹果", "香蕉", "橘子", "西瓜"]
  sampled_fruits = choices(fruits, k=3)
  print("抽取 3 次水果列表（可能重复）：", sampled_fruits)

  # 2. 从字符串序列中抽取字符组成列表
  char_samples = choices("0123456789ABCDEF", k=6)
  print("抽取 6 个字符列表：", char_samples)
  print("拼接为随机字符串：", "".join(char_samples))

  # 3. 带有权重的有放回抽样（weights 参数）
  prizes = ["一等奖", "二等奖", "参与奖"]
  prize_weights = [5, 15, 80]  # 相对概率比例：5:15:80
  draw_results = choices(prizes, weights=prize_weights, k=5)
  print("按权重抽取 5 次奖项：", draw_results)
  ```

---

## 扩展：打乱序列与无放回抽样

除上述核心函数外，`random` 模块中常用的还有序列打乱与无放回抽样功能：

### 1. `shuffle(x)`：原地打乱序列

- **功能**：将可变序列（如列表 `list`）中的元素次序原地随机打乱。
- **注意**：该函数直接修改原列表，返回值为 `None`。只能作用于可变序列，不能用于元组或字符串。

```python
from random import shuffle

card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(card_deck)
print("打乱后的卡牌顺序：", card_deck)
```

### 2. `sample(population, k)`：无放回抽样

- **功能**：从候选群体中抽取 $k$ 个**互不重复**的独立元素。
- **与 `choices` 的区别**：`sample` 为无放回抽样，抽出的每个元素在结果中只出现一次；且要求 $k$ 不能超过候选群体的总长度。

```python
from random import sample

lottery_pool = range(1, 36)
lucky_numbers = sample(lottery_pool, k=7)
print("无放回抽取 7 个不重复号码：", lucky_numbers)
```

---

## `random` 常用函数速查表

| 函数名                  | 输入参数类型                     | 抽样/生成机制                               | 返回值类型   | 典型应用                              |
|:------------------------|:---------------------------------|:--------------------------------------------|:-------------|:--------------------------------------|
| **`randint(a, b)`**     | `a: int, b: int`                 | 生成区间 $[a, b]$ 内的随机整数（闭区间）    | `int`        | 掷骰子、随机索引、生成整数编号        |
| **`uniform(a, b)`**     | `a: float/int, b: float/int`     | 生成区间 $[a, b]$ 内的均匀分布浮点数        | `float`      | 随机坐标、权重系数、模拟测量值        |
| **`choice(seq)`**       | `seq: Sequence`（非空序列）      | 从序列中随机选取 1 个元素                   | 元素本身类型 | 随机选人、随机决定分支选项            |
| **`choices(pop, k=1)`** | `pop: Sequence/Iterable, k: int` | 从群体中有放回抽取 $k$ 次（允许重复）       | `list`       | 随机生成字符串/验证码、带权重随机事件 |
| **`sample(pop, k)`**    | `pop: Sequence/Iterable, k: int` | 从群体中无放回抽取 $k$ 个独立元素（不重复） | `list`       | 抽奖不重复中奖者、划分测试数据集      |
| **`shuffle(x)`**        | `x: list`（可变序列）            | 原地打乱序列内元素的排列次序                | `None`       | 洗牌、打乱训练数据样本                |
