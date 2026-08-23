# Python 教学与参考指南

## 概览

本项目是一套模块化、结构化的 Python 基础与实用教学资料库。每个知识模块均包含概念解析文档（`read*.md`）与可直接运行的代码示例（`demo_*.py` / `method_*.py`）。

## 学习路线指引

> **新手阅读提示**：
> 无论阅读哪个文件夹或代码文件前，**请务必提前或搭配对应的 `.md` 文档一起阅读**，以便更好地理解概念原理与代码逻辑。

### 新手定制学习路线（循序渐进）

本路线**专为零基础与新手学习者定制**。按照知识体系的前后依赖关系，将从“环境配置”开始直到“标准库”之前的基础知识点细化排列为逐级递进的学习顺序。若当前文件夹内容未被其他模块交叉拆分，请在完整阅读并掌握该文件夹全部内容后，再进入下一个文件夹：

1. **`环境配置`**
   - 需完整掌握该文件夹内容：阅读 `readsetup.md`（完成 Python 环境安装与配置，掌握基础代码编写与执行规则），完成后进入下一文件夹。
2. **`打印`**
   - 需完整掌握该文件夹内容：阅读 `readprint.md` 并运行 `demo_print.py`（掌握控制台输出、`sep` 分隔符与 `end` 结束符，了解打印中引入的变量概念），完成后进入下一文件夹。
3. **`变量`**
   - 依次学习：先阅读 `readvariable.md` 并运行 `demo_variable.py`（掌握变量定义与命名规范），再阅读 `readassignment.md` 并运行 `demo_assignment.py`（掌握赋值机制与解包赋值）。阅读完该文件夹全部内容后进入下一文件夹。
4. **`基础运算`**
   - 需完整掌握该文件夹内容：先阅读 `readoperator.md` 掌握运算符概念，随后依次运行与学习 `demo_arithmetic.py` -> `demo_multiplication_and_exponentiation.py` -> `demo_modulo.py` -> `demo_floor_division.py`。阅读完该文件夹全部内容后进入下一文件夹。
5. **`数据类型`**
   - 需完整掌握该文件夹内容：先阅读 `readdatatype.md` 建立全局数据类型认知，随后依次学习各项类型示例代码：`demo_int.py` -> `demo_float.py` -> `demo_str.py` -> `demo_bool.py` -> `demo_list.py` -> `demo_tuple.py` -> `demo_set.py` -> `demo_dict.py` -> `demo_none.py` -> `demo_function.py`。阅读完该文件夹全部内容后进入下一文件夹。
6. **`类型转换`**
   - 需完整掌握该文件夹内容：先阅读 `readconversion.md` 并运行 `demo_conversion.py`（掌握隐式与显式数据类型转换），再阅读 `readtypecheck.md`（掌握 `type()` 类型检查）。阅读完该文件夹全部内容后进入下一文件夹。
7. **`判断式`**
   - 需完整掌握该文件夹内容：先进入 `比较运算` 目录（阅读 `readcomparison.md` 并运行 `demo_comparison.py`），再进入 `逻辑运算` 目录（阅读 `readlogic.md` 并运行 `demo_logic.py`）。阅读完该文件夹全部内容后进入下一文件夹。
8. **`循环`**
   - 需完整掌握该文件夹内容：阅读 `readloop.md` 并运行 `demo_loop.py`（掌握 `for` 与 `while` 循环、`range()` 计数以及 `break` 与 `continue` 流程控制）。阅读完该文件夹全部内容后进入下一文件夹。
9. **`索引`**
   - 需完整掌握该文件夹内容：先阅读 `readindex.md` 掌握正负索引基础概念，接着进入 `遍历` 目录（阅读 `readtraversel.md` 并运行 `demo_traversel.py` 学习基础序列遍历），最后进入 `切片` 目录（阅读 `readslice.md` 并运行 `demo_slice.py` 学习正负步长切片提取与序列反转）。阅读完该文件夹全部内容后进入下一文件夹。
10. **`常用遍历`**
    - 需完整掌握该文件夹内容：阅读 `readtraversal.md` 并运行 `demo_traversal.py`（掌握 `range()` 范围与步长遍历、`enumerate()` 带索引遍历、`zip()` 多序列并行遍历以及字典的 `keys()`、`values()`、`items()` 遍历）。阅读完该文件夹全部内容后进入下一文件夹。
11. **`容器方法`**
    - 需完整掌握该文件夹内容：先阅读 `readmethod.md` 掌握通用操作与各容器独有方法概览，随后依次学习 `method_general.py`（常用通用操作） -> `method_list.py`（列表方法） -> `method_str.py`（字符串方法） -> `method_dict.py`（字典方法） -> `method_set.py`（集合方法）。阅读完该文件夹全部内容后进入下一文件夹。
12. **`交互与防报错`**
    - 需完整掌握该文件夹内容：先学习用户输入交互（阅读 `readinput.md` 并运行 `demo_input.py`），再学习异常捕获机制（阅读 `readerror.md` 并运行 `demo_error.py`），最后查阅 `readerrortype.md` 掌握常见报错类型与排查方法。阅读完该文件夹全部内容后进入下一文件夹。
13. **`输出格式`**
    - 需完整掌握该文件夹内容：阅读 `readformat.md` 并运行 `demo_format.py`（掌握浮点数定点 `:.2f`、通用格式 `:g`、科学计数法、千位分隔符以及对齐填充等输出格式化方法）。阅读完该文件夹全部内容后进入下一文件夹。
14. **`函数`**
    - 需完整掌握该文件夹内容：先进入 `定义函数` 目录（阅读 `readfunction.md` 并运行 `demo_function.py` 掌握 `def`、默认参数、类型注解与返回值），再进入 `匿名函数` 目录（阅读 `readlambda.md` 并运行 `demo_lambda.py` 掌握 `lambda` 表达式与应用场景）。阅读完该文件夹全部内容后进入下一文件夹。
15. **`文件读写`**
    - 需完整掌握该文件夹内容：阅读 `readfile.md` 并运行 `demo_file.py`（掌握文件对象概念、`open`/`close` 与 `with open` 上下文管理、打开模式以及 `encoding="utf-8"` 字符编码）。阅读完该文件夹全部内容后，即可完成所有 Python 核心基础储备。
16. **`标准库` 及后续按需拓展**
    - 完成上述基础知识积累后，可进入 `标准库` 模块：先阅读 `readimport.md` 掌握模块导入机制（`import a`、`from a import b` 与 `from a import *`），随后根据实际学习与开发需求，按需探索各个常用标准库（`time`、`datetime`、`math`、`string`、`random`、`json`）或在根目录 `practice.py` 中进行自由编程实践。

### 按需学习路线（进阶查阅）

对于已有编程基础或希望针对特定主题快速查阅的学习者，可以在完成环境配置后，根据个人需求、具体应用场景或学习目标，直接从下方“模块导航与内容索引”中自由选择对应模块进行查阅与针对性练习。

## 模块导航与内容索引

| 模块目录 | 主要内容与说明 | 核心文档与示例 |
| :--- | :--- | :--- |
| `环境配置` | Python 安装、环境变量配置、基础规则与运行测试 | `readsetup.md` |
| `打印` | `print()` 输出机制、分隔符 `sep` 与结束符 `end` | `readprint.md`、`demo_print.py` |
| `变量` | 变量命名、赋值机制与多元解包赋值 | `readvariable.md`、`readassignment.md`、`demo_*.py` |
| `基础运算` | 算术运算符与复合赋值运算符 | `readoperator.md`、`demo_*.py` |
| `数据类型` | 整数、浮点数、字符串、布尔值、列表、元组、字典、集合与 `None` | `readdatatype.md`、`demo_*.py` |
| `类型转换` | 隐式类型转换、显式类型转换及 `type()` 类型检查 | `readconversion.md`、`readtypecheck.md`、`demo_conversion.py` |
| `判断式` | 比较运算（`==`、`>` 等）与逻辑运算（`and`、`or`、`not`） | `比较运算/`、`逻辑运算/` |
| `循环` | `for` 循环、`while` 循环、`break` 与 `continue` | `readloop.md`、`demo_loop.py` |
| `索引` | 正负索引、基础遍历与切片提取（`[start:stop:step]`） | `readindex.md`、`遍历/`、`切片/` |
| `常用遍历` | `range`、`enumerate`、`zip` 及字典 `keys`/`values`/`items` 遍历 | `readtraversal.md`、`demo_traversal.py` |
| `容器方法` | 列表、集合、字符串、字典等容器的内置操作方法与通用操作 | `readmethod.md`、`method_*.py` |
| `交互与防报错` | `input()` 用户输入、`try-except-finally` 异常捕获与常见报错类型解析 | `readinput.md`、`readerror.md`、`readerrortype.md`、`demo_*.py` |
| `输出格式` | 字符串格式化（`:.2f`、`:g`、对齐、填充与进制表示） | `readformat.md`、`demo_format.py` |
| `函数` | 函数定义（`def`、默认参数、类型注解、返回值）与匿名函数（`lambda`） | `定义函数/`、`匿名函数/` |
| `文件读写` | 文件对象概念、`open`/`close`、`with open` 及编码（`utf-8`） | `readfile.md`、`demo_file.py` |
| `标准库` | `import` 机制与常用标准库（`time`、`datetime`、`math`、`string`、`random`、`json`） | `readimport.md`、各子目录模块 |

## 项目使用说明

1. **阅读文档**：进入目标知识点文件夹，查看对应 `read*.md` 文档获取原理与用法解析。
2. **运行代码**：直接执行对应的 `demo_*.py` 或 `method_*.py` 示例文件观察实际输出与行为特性。
3. **自主练习**：根目录下的 `practice.py` 可用于编写和测试自己的代码。

## 提示

如果在编辑器中 Markdown（`.md`）文件显示异常，可以尝试使用快捷键 `Ctrl + Shift + V` 打开预览窗口。