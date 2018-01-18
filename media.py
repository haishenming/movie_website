#! /bin/python3

""" 类代码 """

import re


class Media:

    def __init__(self, name, post_url, media_url, stars):
        self.name = name                      # 名   称  str
        self.poster_image_url = post_url      # 海报链接  url
        self.trailer_url = media_url            # 视频链接  url
        self.stars = stars                      # 我的评分  float
        check_ret = self._check_attrs()
        if not check_ret:
            raise ValueError

    def _check_attrs(self):
        """ 检查传入的属性 """
        error = []
        print("上行参数检查：")
        self.title = str(self.name)

        # 判断url格式是否正确
        if not re.match(r'^https?:/{2}\w.+$', str(self.poster_image_url)):
            error.append("海报链接格式错误 {url}".format(url=self.poster_image_url))
        if not re.match(r'^https?:/{2}\w.+$', str(self.trailer_url)):
            error.append("视频链接格式错误 {url}".format(url=self.trailer_url))

        # 判断star值类型是否正确
        try:
            self.stars = float(self.stars)
        except ValueError as e:
            error.append("star类型错误： {err}".format(err=e))

        if error:
            print(error)
            return False
        else:
            print("ok")
            return True



if __name__ == '__main__':
    media = Media("123", "456", "789", "jsa")