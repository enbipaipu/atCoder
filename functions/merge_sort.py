def list_merge(a: list, b: list) -> list:
    a_len, b_len = len(a), len(b)
    a_index = b_index = 0
    result = []

    while (a_index < a_len) and (b_index < b_len):
        if a[a_index] <= b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    result.extend(a[a_index:])
    result.extend(b[b_index:])

    return result


def merge_sort(x: list) -> list:
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list_merge(left, right)


lis = [0, 3, 1, -1, 5]
print(merge_sort(lis))
