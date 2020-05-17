import sys
import math


def devide(li):
    m = math.floor(len(li) / 2)
    return li[:m], li[m:]

def merge(first, second):
    if len(first) == 0:
        return second
    i, j = 0, 0
    result = []
    while i < len(first) or j < len(second):
        f = first[i] if i < len(first) else float("inf")
        s = second[j] if j < len(second) else float("inf")
        if f <= s:
            result.append(f)
            i += 1
        else:
            result.append(s)
            j += 1
    return result

def merge_sort(li):
    if len(li) <= 1:
        return li
    first_half, second_half = devide(li)
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    return merge(first_half, second_half)

def main():
    input = sys.argv[1]
    output = merge_sort([int(i) for i in input.split(' ')])
    print(" ".join([str(o) for o in output]))


if __name__ == "__main__":
    main()
