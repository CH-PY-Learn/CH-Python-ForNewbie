# 赋值运算符

## 概览

对变量进行赋值时使用的符号，称为赋值运算符。

## `=` 赋值运算符

等号 `=` 用于将右侧的值赋给左侧的变量：

```python
name = "小明"
```

在 `name = "小明"` 中，`=` 就是赋值运算符。

## 复合赋值运算符

有时需要在变量原有的值上进行数学运算。如果变量名很长，重复书写变量名会比较麻烦：

```python
the_very_long_variable_name = 10
the_very_long_variable_name = the_very_long_variable_name + 10
```

上面的代码只是让变量增加 `10`，却需要重复写出很长的变量名。

对变量进行数学运算时，可以使用复合赋值运算符。`+=`、`-=`、`*=`、`/=`、`//=`、`**=` 和 `%=` 都属于复合赋值运算符。

```python
the_very_long_variable_name = 10
the_very_long_variable_name += 10  # 在原有的 10 上增加 10
```

`the_very_long_variable_name += 10` 等价于：

```python
the_very_long_variable_name = the_very_long_variable_name + 10
```
