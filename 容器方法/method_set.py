# 集合专属方法：展示 add, remove, discard, pop 与 update

prime = {2, 4, 3, 5, 7, 11, 13, 17}

# ==================== 1. add：向集合添加元素 ====================

prime.add(19)  # add 方法，向集合中添加元素
print(prime)


# ==================== 2. remove 与 discard：删除元素与容错差异 ====================

prime.remove(4)
prime.discard(4)
print(prime)
"""
remove 和 discard 方法，从集合中移除元素：
- discard 方法如果元素不存在，不会报错
- remove 方法如果元素不存在，则会抛出 KeyError
"""


# ==================== 3. pop：随机移除并返回集合元素 ====================

prime.pop()  # pop 方法，移除并返回集合中的某个元素，但不保证具体是哪一个
print(prime)


# ==================== 4. update：批量合并多个可迭代对象 ====================

coding_language = {"Python", "C"}

basic_language = ["Python", "Java"]

hard_language = ("C++", "C")

coding_language.update(basic_language, hard_language)  # update 方法，将其他可迭代对象中的元素添加到集合中

print(*coding_language, sep=", ")

"""
集合方法核心总结：
1. 添加与更新：
   - `add(x)`：向集合添加单个元素（自动去重）。
   - `update(iterable)`：批量添加可迭代对象中的元素。
2. 移除元素：
   - `discard(x)`：移除元素 x，若元素不存在不会报错。
   - `remove(x)`：移除元素 x，若元素不存在则抛出 KeyError。
   - `pop()`：随机弹出一个元素并返回该元素。
"""
