# 字典专属方法：展示 keys, values, items, get, pop, popitem 与 update

seat_name = {
    0: "狗蛋",
    1: "小明",
    2: "小红",
    3: "小刚",
    4: "小强",
    5: "小华",
    6: "小丽",
    7: "小芳"
}

# ==================== 1. keys, values, items：读取键、值与键值对 ====================

print(seat_name.keys())  # keys 方法，以视图形式返回字典中所有键
print(seat_name.values())  # values 方法，以视图形式返回字典中所有值
print(seat_name.items())  # items 方法，以视图形式返回字典中所有键值对


# ==================== 2. get：安全获取键值与设置默认值 ====================

print(seat_name.get(0, None))  # get 方法，返回指定键的值，如果键不存在则返回默认值
# 在 get 方法中，左边是键，右边是默认值


# ==================== 3. pop 与 popitem：删除并返回键值对 ====================

remove_key = 0
removed_value = seat_name.pop(remove_key)  # pop 方法，删除指定键的键值对并返回该键值对的值
print(f"删除了{removed_value}")

last_join_seat = seat_name.popitem()  # popitem 方法，删除并返回字典中最后一个键值对
print(f"最后一个加入的座位是{last_join_seat}")

print(seat_name)  # 字典内被 pop 过的键值对都不存在了


# ==================== 4. update：覆盖与添加键值对 ====================

new_seat_name = {
    5: "王刚",
    6: "王五",
    7: "王六",
    8: "小豪"
}

seat_name.update(new_seat_name)  # update 方法，将字典中的键值对覆盖到另一个字典中
print(seat_name)

seat_name.update({0: "鸡蛋"})  # update 方法，修改字典中的键值对
print(seat_name)

# 在使用 update 方法时，如果字典中已经存在该键，则会覆盖原来的值；如果字典中不存在该键，则会添加该键值对。

"""
字典方法核心总结：
1. 视图与读取方法：
   - `keys()`、`values()`、`items()`：分别返回字典的所有键、值、键值对视图。
   - `get(key, default)`：安全读取键对应的值，若键不存在则返回指定的默认值。
2. 修改与删除方法：
   - `pop(key)`：删除指定键并返回对应值；`popitem()`：删除并返回最后插入的键值对。
   - `update(dict2)`：用新字典批量更新或新增键值对（若键已存在则覆盖对应值）。
"""
