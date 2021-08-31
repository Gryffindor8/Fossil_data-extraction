from collections import OrderedDict

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def origin_extract(links):
    orig = requests.get(links).content
    pr = bs(orig, "lxml")
    dat = str(pr.find("dl", {"class": "dl-horizontal"}).text)
    author = (dat[dat.index("Author:"):dat.index("Year")].replace("Author:", ""))
    reference = (dat[dat.index("Reference:"):dat.index("Google")].replace("Reference:", "").strip())
    return author, reference


def extraction():
    with open("new.txt", "r") as f:
        links = (f.read())
    links = links.split("\n")
    links = list(OrderedDict.fromkeys(links))
    file_name = 0
    for j in links:
        pg = 1

        try:
            while True:
                content = requests.get(j + "?page=" + str(pg) + "").content
                print(j + "?page=" + str(pg) + "")
                pg += 1
                parse = bs(content, "lxml")
                try:
                    nm = str(parse.find("div", {"class": "col-lg-6"}).text)
                    name = nm.split("\n")[2]
                except:
                    name = " "
                table = parse.find("table", {"class": "table"})
                body = table.find("tbody")
                if len(body) < 5:
                    break
                table_row = (body.find_all("tr"))
                second_link = (body.find_all("a"))
                cnt = 0
                for k in table_row:
                    # data = []
                    table_data = (k.find_all("td"))
                    data = []
                    refe = "https://paleobotany.ru" + str(second_link[cnt]["href"])
                    cnt += 1
                    at, rf = origin_extract(refe)
                    i = 0
                    for k1 in table_data:
                        if i == 0:
                            data.append(name)
                            i += 1
                        else:
                            data.append(k1.text)
                    try:
                        data.append(at)
                        data.append(rf)
                        df = pd.DataFrame(data=data, index=["", "", "", "", "", "", "", ""])
                        df = df.T
                        name3 = "data" + str(file_name) + ".csv"
                        df.to_csv(name3, encoding="UTF-8", mode="a", index=False, header=False)
                    except:
                        pass
        except:
            pass
        file_name += 1


extraction()
