"""
1:过滤字符串' nick2008@gmail.com ' 前后空白字符
2:过滤字符串 ‘hello world\r\n’ \r符号
3：去除文本中unicode组合符号(音调)

解决方案：
1：使用strip(),lstrip(),rstrop()去除两端字符
    strip:去除前后空格
    lstrip：去除左侧空格
    rstrop：去除右侧空格
2：删除单个固定位置的字符，可是使用切片+拼接的方式
3：使用replace()或者正则表达式的re.sub删除任意位置字符
4：translate()可以同时删除多个不同字符
"""

