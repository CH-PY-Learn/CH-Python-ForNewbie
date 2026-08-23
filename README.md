# Python 教学与参考指南

## 概览

本项目是一套模块化、结构化的 Python 基础与实用教学资料库。每个知识模块均包含概念解析文档（`read*.md`）与可直接运行的代码示例（`demo_*.py` / `method_*.py`）。

## 学习路线指引

- **初学者起步**：初学者优先打开 `环境配置` 文件夹（查看 `readsetup.md` 与 `main.py`），完成 Python 运行环境的配置并了解代码基础编写与执行规则。
- **按需学习路线**：本项目采用模块化目录结构。在完成环境配置后，可以根据个人需求、具体应用场景或学习目标，自由选择对应模块进行按需学习与查阅，在自主实践中探索和形成自己的代码风格。

## 模块导航与内容索引

| 模块目录       | 主要内容与说明                                                                      | 核心文档与示例                                     |
|:---------------|:------------------------------------------------------------------------------------|:---------------------------------------------------|
| `环境配置`     | Python 安装、环境变量配置、基础规则与运行测试                                       | `readsetup.md`、`main.py`                          |
| `打印`         | `print()` 输出机制、分隔符 `sep` 与结束符 `end`                                     | `readprint.md`、`demo_print.py`                    |
| `变量`         | 变量命名、赋值机制与多元解包赋值                                                    | `readvariable.md`、`readassignment.md`             |
| `数据类型`     | 整数、浮点数、字符串、布尔值、列表、元组、字典、集合与 `None`                       | `readdatatype.md`、`demo_*.py`                     |
| `基础运算`     | 算术运算符与复合赋值运算符                                                          | `readoperator.md`、`demo_arithmetic.py`            |
| `判断式`       | 比较运算（`==`、`>` 等）与逻辑运算（`and`、`or`、`not`）                            | `readcomparison.md`、`readlogic.md`                |
| `循环`         | `for` 循环、`while` 循环、`break` 与 `continue`                                     | `readloop.md`、`demo_loop.py`                      |
| `索引`         | 正负索引、序列遍历（`enumerate`、`zip`）与切片提取（`[start:stop:step]`）           | `readindex.md`、`readtraversel.md`、`readslice.md` |
| `容器方法`     | 列表、集合、字符串、字典等容器的内置操作方法                                        | `readmethod.md`、`method_*.py`                     |
| `类型转换`     | 隐式类型转换、显式类型转换及 `type()` 类型检查                                      | `readconversion.md`、`readtypecheck.md`            |
| `交互与防报错` | `input()` 用户输入、`try-except-finally` 异常捕获与常见报错类型解析                 | `readinput.md`、`readerror.md`、`readerrortype.md` |
| `输出格式`     | 字符串格式化（`:.2f`、`:g`、对齐、填充与进制表示）                                  | `readformat.md`、`demo_format.py`                  |
| `函数`         | 函数定义（`def`、默认参数、类型注解、返回值）与匿名函数（`lambda`）                 | `readfunction.md`、`readlambda.md`                 |
| `文件读写`     | 文件对象概念、`open`/`close`、`with open` 及编码（`utf-8`）                         | `readfile.md`、`demo_file.py`                      |
| `标准库`       | `import` 机制与常用标准库（`time`、`datetime`、`math`、`string`、`random`、`json`） | `readimport.md`、各子目录模块                      |

## 项目使用说明

1. **阅读文档**：进入目标知识点文件夹，查看对应 `read*.md` 文档获取原理与用法解析。
2. **运行代码**：直接执行对应的 `demo_*.py` 示例文件观察实际输出与行为特性。
3. **自主练习**：根目录下的 `practice.py` 可用于编写和测试自己的代码。

## 提示

如果在编辑器中 Markdown（`.md`）文件显示异常，可以尝试使用快捷键 `Ctrl + Shift + V` 打开预览窗口。