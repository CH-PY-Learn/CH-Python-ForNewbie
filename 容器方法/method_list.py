# 列表专属方法：展示 extend, insert, remove, pop, sort 与 reverse

class_seats = [1, 2, 3, 4]


# ==================== 1. extend：添加列表至末尾 ====================

new_members_seat = [6, 7, 8, 9, 10]

class_seats.extend(new_members_seat)  # extend 方法，将被选中的列表添加到列表末尾，在本行代码中为 new_members_seat 被添加至 class_seats
print(class_seats)


# ==================== 2. insert：指定索引插入元素 ====================

new_member_seat = 5

class_seats.insert(4, new_member_seat)  # insert 方法，将元素添加到列表指定的索引值
print(class_seats)


# ==================== 3. remove：删除指定元素 ====================

quit_member_seat = 10

class_seats.remove(quit_member_seat)  # remove 方法，删除列表中指定的元素
print(class_seats)


# ==================== 4. pop：删除指定索引元素 ====================

quit_member_index = 0

class_seats.pop(quit_member_index)  # pop 方法，删除列表中指定索引值的元素
print(class_seats)


# ==================== 5. sort 与 reverse：排序与反转 ====================

class_seats = [7, 30, 15, 5, 17, 13, 27, 18, 1, 4]
class_seats.sort()  # sort 方法，对列表进行从由小到大的排序
print(class_seats)

class_seats.reverse()  # reverse 方法，反转列表中的元素
print(class_seats)

"""
列表方法核心总结：
1. 添加元素：
   - `append(x)`：在列表末尾添加单个元素。
   - `extend(iterable)`：将可迭代对象的所有元素逐一追加到列表末尾。
   - `insert(index, x)`：在指定索引位置插入元素。
2. 删除元素：
   - `remove(x)`：删除列表中首次出现的指定元素 x。
   - `pop([index])`：移除并返回指定索引处的元素（默认最后一个）。
3. 排序与反转：
   - `sort()`：原地升序排序列表；`reverse()`：原地反转列表元素顺序。
"""
