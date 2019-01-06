

import os
import json

dir="E:\PythonProject\Sou_analysis\json"



def GetJsonList(dir):
    json_list = []
    file_list = os.listdir(dir)
    for item in file_list:
        if ".json" in item:
            json_list.append(item)
            continue
        else:
            continue
    return json_list

def GetJsonContent(dir,json_list):
    json_dict = {}
    for item in json_list:
        #item_dir = os.path.join(dir,item)
        item_dir = dir + "//" + item
        content = json.load(open(item_dir))
        content_list = content["data"]["postList"]
        for info in content_list:
            id = info["id"]
            json_dict.setdefault(id,{})
            json_dict[id]["likes"] = info["likes"]
            json_dict[id]["shares"] = info["shares"]
            json_dict[id]["comments"] = info["comments"]
            json_dict[id]["latitude"] = info["latitude"]
            json_dict[id]["longitude"] = info["longitude"]
            json_dict[id]["image_url"] = []
            json_dict[id]["content"] = info["content"]
            json_dict[id]["soulmate"] = info["soulmate"]
            json_dict[id]["type"] = info["type"]
            try:
                for attachment in info["attachments"]:
                    if attachment["type"] == "IMAGE":
                        json_dict[id]["image_url"].append(attachment["fileUrl"])
                        continue
                    else:
                        continue
            except:
                print "no attachments"

    return json_dict



