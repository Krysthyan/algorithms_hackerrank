def counterPlusMinus(arr):
    return [
        sum(1 for number in arr if number > 0),
        sum(1 for number in arr if number < 0),
        arr.count(0)
    ]


def plusMinus(arr):
    [print("{:.6f}".format(number / len(arr))) for number in counterPlusMinus(arr)]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
