n = input()
N = n[0]
M = n[1]

A = input().rstrip().split(" ")


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data.pop(0)

    left = [i for i in data if i <= pivot]

    right = [i for i in data if i > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


new_A = quick_sort(A)

# 配列を小さい順に直した
