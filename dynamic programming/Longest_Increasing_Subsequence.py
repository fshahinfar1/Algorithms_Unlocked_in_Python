'''
DP
Longest Increasing Subsequence
https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
'''


def main():
    # LISs
    T = int(input()) # type: int
    while(T>0):
        T-=1
        n = int(input())
        seq = []
        subseq = []
        for i in range(n):
            seq.append(int(input()))
        dp_list = []
        dp_subseq_list = []  # this is for finding actual list
        max_j = 0
        max_length = 0
        max_index_j = 0
        max_index = 0
        for i in range(n):
            max_j = 0
            max_index_j = 0
            for j in range(i):
                if dp_list[j] > max_j:
                    if seq[i] > seq[j]:
                            max_j = dp_list[j]
                            max_index_j = j
            dp_list.append(max_j+1)
            if len(dp_subseq_list) > max_index_j:
                dp_subseq_list.append(dp_subseq_list[max_index_j]+[seq[i]])
            else:
                dp_subseq_list.append([seq[i]])
            if dp_list[-1] > max_length:
                max_length = dp_list[-1]
                max_index = i
        print (max_length)
        print(dp_subseq_list[max_index])


if __name__ == '__main__':
    main()
