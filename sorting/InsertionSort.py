def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i-1
        while key < arr[j] and j > -1:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


def main():
    data = list(map(int, input('input numeric data: ').split()))
    insertion_sort(data)
    print(data)


if __name__ == '__main__':
    main()
