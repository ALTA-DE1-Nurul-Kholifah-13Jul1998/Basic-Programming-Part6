def find_max_sum_sub_array(k, arr):
    list_max_sum = []
    for i in range(0,len(arr)):
        if k<=len(arr):
            subarray = sum(arr[i:k])
            list_max_sum.append(subarray)
            i+=1
            k+=1
            
    return max(list_max_sum)

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8