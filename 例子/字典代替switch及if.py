"""
switch ($day)
 {
     case 0:
       $dayName = "sunday";
       ......
       break;
     case 1:
        $dayName = "Monday"
        ......
        break;
     case 2:
        $dayName = "Tuesday"
     default:
        $dayName = "Unkown"
        ...
        break;
}
或转换为if  elseif
"""
# 使用字典代替
# 分支内容为字符串
day = 0
switcher = {
    0: 'sunday',
    1: 'Monday',
    2: 'Tuesday'
}
day_name = switcher[day]

# 分支内容为函数
day1 = 9
def get_sunday():
    # 业务逻辑
    return 'Sunday'


def get_monday():
    # 业务逻辑
    return 'Monday'


def get_tuesday():
    # 业务逻辑
    return 'Tuesday'


def get_default():
    # 业务逻辑
    return 'Unkown'


switcher1 = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}
day_name = switcher1.get(day1, get_default)()
print(day_name)
