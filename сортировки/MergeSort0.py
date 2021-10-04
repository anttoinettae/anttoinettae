def merge_sort(a, start=0, end = None):
    if end == None:
        end = len(a)
    if end - start <= 1:
        return 0
    middle = (start + end) // 2
    merge_sort(a, start, middle)
    merge_sort(a, middle, end)
    temp = []
    i, j = start, middle
    while i < middle or j < end:
        if i < middle and (j == end or a[i] <= a[j]):
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
    a[start:end] = temp
    return a


with open("sort.in") as data:
    n = int(data.readline())
    numbs = list(map(int, data.readline().split()))

with open("sort.out", "w") as otv:
    for i in merge_sort(numbs):
        print(i, file=otv, end=" ")

