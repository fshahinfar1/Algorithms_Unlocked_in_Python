def selection_sort(arr):
    length = len(arr)
    if length == 0:
        return arr
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if  arr[j] < arr[min_index]:
                min_index = j
        temp_value = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp_value

    return arr


def main():
    data = list(map(int, input('input numeric data: ').split()))
    selection_sort(data)
    print(data)

if __name__ == '__main__':
    main()
