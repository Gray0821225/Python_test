#coding:utf-8

from __future__ import division
from json_ana import *
import urllib2
import os
from baidu_map import *
import json

keyword = [u"小姐姐",u"小哥哥",u"自闭",u"恋爱",u"结婚",u"男朋友",u"女朋友",u"相亲"]
dir="E:\Python Project\Sou_analysis\json"
image_dir = "E:\Python Project\Sou_analysis\image"
dictt = GetJsonContent(dir,GetJsonList(dir))
s = []

#根据json字典，下载每个瞬间的图片至指定文件夹中。传入参数为json字典和指定文件夹路径
def DownloadPicture(dictt,image_dir):
    pict_count = 1
    for item in dictt:
        print item
        if len(dictt[item]["image_url"]) != 0:
            for url in dictt[item]["image_url"]:
                image_name = url.split("/")[-1].split(".")[0]
                name = image_dir + "\\" + image_name + ".png"
                conn = urllib2.urlopen(url)
                try:
                    f = open(name,"wb")
                    f.write(conn.read())
                    f.close()
                    print "图片已保存," + str(pict_count) + "张图片已下载"
                    pict_count += 1
                except:
                    print "Pciture Download Error"
        else:
            print "No Image Url"


#根据json字典，获取每个瞬间的经纬度，并保存为字典。格式为{id:[longitude,latitude],id:[longitude,latitude]....}
def GetPosition(dictt):
    position_dict = {}
    for item in dictt:
        if dictt[item]["longitude"] == 0.0 and dictt[item]["latitude"] == 0.0:
            continue
        if dictt[item]["longitude"] == None and dictt[item]["latitude"] == None:
            continue
        else:
            position_dict[item] = []
            position_dict[item].append(dictt[item]["longitude"])
            position_dict[item].append(dictt[item]["latitude"])
    return position_dict

#根据json字典，将所有瞬间的content内容保存为list
def GetContent(dictt):
    content_list = []
    for item in dictt:
        content_list.append(dictt[item]["content"])
    return content_list

#根据给定的keyword，计算keyword在所有瞬间content中出现的频率
def KeywowdFrequency(keyword_list):
    conten_list = GetContent(dictt)
    frequency_dict ={}
    for keyword in keyword_list:
        count = 0
        frequency_dict[keyword] = count
        for content in conten_list:
            if keyword in content:
                count += 1
                frequency_dict[keyword] = count
            else:
                continue
    return frequency_dict

#根据json字典，计算瞬间的type占比
def TypePrecent(dictt):
    type_precent_dict = {}
    total_list = []
    for item in dictt:
        total_list.append(dictt[item]["type"])
    base_list = list(set(total_list))
    total_num = len(total_list)
    for item in base_list:
        count = 0
        type_precent_dict[item] = 0
        for info in total_list:
            if info == item:
                count +=1
                type_precent_dict[item] = count/total_num
            else:
                continue
    return type_precent_dict


def LocateProvince(position_dict):
    province_list = []
    for item in position_dict:
        try:
            t_province = locatebyLatLng(position_dict[item][1],position_dict[item][0])
            province_list.append(t_province)
        except:
            print "get baidu info error"
            print position_dict[item][1],position_dict[item][0]
    return province_list

position_dict = GetPosition(dictt)
pro_list = LocateProvince(position_dict)

uni_list = list(set(pro_list))
provi_dict = {}
for item in uni_list:
    count = 1
    for province in pro_list:
        if item == province:
            provi_dict[item] = count
            count += 1
        else:
            continue

input_list = []
for item in provi_dict:
    t_dict = {"name":"","value":0}
    t_dict["name"] = item
    t_dict["value"] = provi_dict[item]
    input_list.append(t_dict)

print json.dumps(input_list, encoding='UTF-8', ensure_ascii=False)