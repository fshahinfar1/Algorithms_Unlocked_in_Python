def min_edit_dist(base, compr):
    """
    operations: remove, insert, substidue
    cost: remove = insert = susbtidue = 1
    """
    cost_r = 1
    cost_i = 1
    cost_s = 1
    height = len(base) + 1
    width = len(compr) + 1
    table = [[j for j in range(width)] for i in range(height)]
    for i in range(height):
        table[i][0] = i
    for row, b in enumerate(base):
        for col, c in enumerate(compr):
            rem = table[row + 1][col] + cost_r
            ins = table[row][col + 1] + cost_i
            sub = table[row][col]
            if b != c:
                sub += cost_s
            dist = min(rem, ins, sub)
            table[row + 1][col + 1] = dist 
    # print(table)
    dist = table[height - 1][width - 1]
    return dist


def main():
    base_str = input("base string: ")
    compr_str = input("compared string: ")
    distance = min_edit_dist(base_str, compr_str)
    print(f"distance is {distance}")



if __name__ == '__main__':
    main()
