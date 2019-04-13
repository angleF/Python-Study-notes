import csv

"""
使用writerow写入csv时有多余空行的处理办法,在打开文件时，手工指定newline参数为""即可避免空行
为避免使用文本方式写入csv时中文出现乱码，在open函数中指定编码为：utf-8-sig
open("copy.csv", "wt", encoding="utf-8-sig", newline='')
"""

with open("工作簿1.CSV", "r", encoding="gbk") as text_io:
    reader = csv.reader(text_io)
    with open("copy.csv", "w", encoding="gbk", newline='') as write_io:
        csv_writer = csv.writer(write_io)
        print(type(csv_writer))
        for text_row in reader:
            print(text_row)
            csv_writer.writerow(text_row)
