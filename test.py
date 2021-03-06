from collections.abc import Iterable

import pandas as pd


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item


arr = [[['8.5', '$949', '1'], ['10.5', '$300', '1'], ['13', '$296', '1'], ['13', '$250', '1'], ['15', '$224', '1'],
        ['9', '$211', '1'], ['9.5', '$202', '1'], ['11', '$201', '1'], ['5.5', '$200', '1'], ['10', '$200', '1'],
        ['6.5', '$190', '1'], ['10.5', '$185', '1'], ['11.5', '$170', '1'], ['13', '$170', '1'], ['7.5', '$170', '1'],
        ['10', '$170', '1'], ['8.5', '$170', '1'], ['12.5', '$170', '1'], ['9', '$170', '1'], ['11', '$170', '2'],
        ['9.5', '$170', '1'], ['8', '$170', '1'], ['10.5', '$170', '1'], ['12', '$170', '1'], ['10.5', '$160', '1'],
        ['6', '$150', '1'], ['9', '$150', '1'], ['8.5', '$100', '1'], ['9', '$69', '1'], ['7', '$50', '1'],
        ['9.5', '$25', '1'], ['11', '$25', '1']],
       [['10.5', '$450', '1'], ['12', '$400', '1'], ['11', '$278', '1'], ['15', '$224', '1'], ['9', '$215', '1'],
        ['8.5', '$190', '1'], ['8', '$190', '1'], ['10.5', '$185', '1'], ['9', '$177', '1'], ['5.5', '$177', '1'],
        ['13', '$177', '1'], ['11', '$177', '1'], ['6.5', '$177', '1'], ['4.5', '$177', '1'], ['5', '$177', '1'],
        ['8.5', '$177', '1'], ['6', '$177', '1'], ['10', '$177', '1'], ['8', '$177', '1'], ['7', '$177', '1'],
        ['4', '$177', '1'], ['10.5', '$177', '1'], ['11.5', '$177', '1'], ['12', '$177', '1'], ['9.5', '$177', '1'],
        ['12.5', '$177', '1'], ['7.5', '$177', '1'], ['4.5', '$103', '1'], ['4.5', '$100', '1'], ['5', '$100', '1'],
        ['8.5', '$100', '2'], ['6', '$100', '1'], ['10.5', '$100', '1'], ['10', '$100', '1'], ['8', '$100', '1'],
        ['7', '$100', '1'], ['4', '$100', '1'], ['11.5', '$100', '1'], ['12', '$100', '1'], ['9.5', '$100', '1'],
        ['12.5', '$100', '1'], ['7.5', '$100', '1'], ['9', '$100', '1'], ['5.5', '$100', '1'], ['11', '$100', '1'],
        ['6.5', '$100', '1'], ['14', '$26', '1'], ['10', '$24', '1']]]
arr1 = list(flatten(arr))
item1 = []
item2 = []
item3 = []
i = 0
for k in arr1:
    if i == 0:
        item1.append(k)
    if i == 1:
        item2.append(k)
    if i == 2:
        item3.append(k)
        i = 0
        continue
    i += 1

dat = [item1, item2, item3]
dfs = pd.DataFrame(data=dat, index=["item1", "item2", "item3"])
dfs = dfs.T
dfs.to_csv("data.csv")
