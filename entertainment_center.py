""" 逻辑代码 """

import csv

from fresh_tomatoes import open_movies_page

from media import Media


def get_medias_by_yourself():
    """ 手动输入medias """
    name = input("请输入名称：")
    post_url = input("请输入海报url：")
    media_url = input("请输入视频链接地址：")
    stars = input("请输入你的评分：")

    return Media(name=name, post_url=post_url, media_url=media_url,
                 stars=stars)

def get_medias_by_csv(filename):
    """ 从csv文件中获取medias """

    medias_list = []
    with open(filename, "r", encoding="utf-8") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)   # 第一行是标题，不读
        for row in f_csv:
            print(row)
            media = Media(row[0], row[1], row[2], row[3])
            medias_list.append(media)
    return medias_list

def main():
    medias_list = []
    go_on = True

    while go_on:
        print("""
        请输入录入电影的方式：
        0、结束录入
        1、手动录入
        2、从csv文件录入
        >>>
        """)
        way_to_input = input()
        if int(way_to_input) == 1:
            try:
                medias_list.append(get_medias_by_yourself())
            except Exception as e:
                print("输入错误，请重新输入 {}".format(e))
        elif int(way_to_input) == 2:
            try:
                filename = input("请输入文件名:\n>>>")
                medias_list.extend(get_medias_by_csv(filename))
            except Exception as e:
                print("输入错误，请重新输入 {}".format(e))
        elif int(way_to_input) == 0:
            go_on = False
        else:
            print("指令错误，请重新输入")

    open_movies_page(medias_list)



if __name__ == '__main__':
    main()
