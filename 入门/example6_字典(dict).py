# 字典中的元素按照key加入字典的顺序排序（相当于java中的LinkedHashMap）
d = {"name": "张三", "age": 19, "gender": "男"}
print("姓名：", d.get("name"))
print("年龄：", d["age"])
print("性别：", d["gender"])
print(type(d))

my_dict = dict(name="孙悟空", age=18)
print(my_dict)
print(len(my_dict))  # 个数

# in 检查字典中是否包含指定的key
# not in 检查字典中是否不包含指定的key
print("h" in d)
print("h" not in d)

d_items = d.items()  # [('name', '张三'), ('age', 19), ('gender', '男')]
print(d_items)  # dict_items([('name', '张三'), ('age', 19), ('gender', '男')])
for k, v in d_items:  # 遍历
    print("key:", k, "\tvalue:", v)
