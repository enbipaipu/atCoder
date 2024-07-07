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


print(list_merge([1, 2, 3], [2, 3, 4]))
