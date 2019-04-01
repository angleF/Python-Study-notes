from urllib import request
import re


class Spider():
    url = "https://www.panda.tv/cate/lol"

    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
    number_pattern = '<span class="video-number"><i class="ricon ricon-eye"></i>([\s\S]*?)</span>'

    def __fetch_content(self):
        """
             获取正文内容
            :return:  解码后的正文内容
        """
        request_obj = request.urlopen(Spider.url)
        request_body = request_obj.read()
        return str(request_body, encoding='utf-8')

    def __analysis(self, html_str):
        root_div_body = re.findall(Spider.root_pattern, html_str)
        data__list = list(map(Spider.__take_data, root_div_body))
        data__list = sorted(data__list, key=self.__take_number, reverse=True)
        self.__show(data__list)

    def __show(self, data__list):
        """
        对提取后的数据进行打印展示
        :param data__list: 提取出数据后的列表
        :return:
        """
        for i in range(0, len(data__list) - 1):
            i_ = data__list[i]
            print("第", i + 1, "名： ", i_['name'], "  :  ", i_['number'])

    def __take_number(self, ele):
        """
        获取每个主播的在线观看人数，
        :param ele: 提取出数据后的列表中的每个节点，也就是字典
        :return: 返回转换后的 number值
        """
        number_str = re.findall("\d*", ele["number"])
        number = float(number_str[0])
        if '万' in ele["number"]:
            number *= 10000
        return number

    @staticmethod
    def __take_data(div_):
        """
            提取主播名称和观看人数
        :param div_:  正文中每个主播展示的div节点字符串
        :return:  封装成字典后的主播名称和观看人数对象
        """
        name = re.findall(Spider.name_pattern, div_)
        number = re.findall(Spider.number_pattern, div_)
        dict_data = {"name": name.pop(), "number": number.pop()}
        return dict_data

    def go(self):
        content = self.__fetch_content()
        self.__analysis(content)


spider = Spider()
spider.go()
