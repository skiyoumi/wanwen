# def list_split(items, n):
#     return [items[i:n] for i in range(0, len(items), n)]


def list_split(items, n):
    data = []
    k = 0
    for i in range(0, len(items), n):
        j = -1
        item = []
        for m in range(k, i):
            j = m
            item.append(items[m])
        k = j + 1
        data.append(item)
    data.pop(0)
    return data
