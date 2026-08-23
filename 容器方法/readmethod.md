# 容器方法

## 概览

当一个数据可以包含多个数据时，我们称该数据为容器。

身为容器的数据类型有：列表、元组、集合、字典、字符串。

## 常用的通用操作

对于每一个容器，有一些常用的通用操作与内置函数，用于读取或修改容器中的数据。

`count`、`index`、`len`、`in`、`reversed`、`clear`（其中 `index` 和 `reversed` 不包含在集合中，`clear` 不包含在元组、字符串中）：

- `count`：表示容器中某个元素出现的次数。
- `index`：表示容器中某个元素的索引。
- `len`：表示容器中元素的个数。
- `in`：表示判断某个元素是否在容器中（字典只会判断表达式是否在键中）。
- `reversed`：表示反转容器中的元素，这是一个有返回值的函数，其不直接反转容器。
- `clear`：表示清空容器中的所有元素。

针对每一个容器类型，除了以上通用的操作之外，还有各自独有的内置方法可供使用。

## `tuple`：元组

只能使用通用的容器操作与内置函数。

## `list`：列表

`append`、`extend`、`insert`、`remove`、`pop`、`sort`、`reverse` 等方法。

## `set`：集合

`add`、`discard`、`remove`、`pop`、`update` 等方法。

## `dict`：字典

`keys`、`values`、`items`、`get`、`pop`、`popitem`、`update` 等方法。

## `str`：字符串

`capitalize`、`title`、`upper`、`lower`、`strip`、`split`、`join`、`replace` 等方法。