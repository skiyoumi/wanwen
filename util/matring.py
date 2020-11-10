# def list_split(items, n):
#     return [items[i:n] for i in range(0, len(items), n)]


def list_split(items, n):
    print(len(items),n)
    data = []
    k = 0
    for i in range(0, len(items), n):
        print(i)
        j = -1
        item = []
        i = i + n
        if len(items)<=i:
            i=len(items)-1
        for m in range(k, i):
            j = m
            item.append(items[m])
        k = j + 1
        data.append(item)
    return data
