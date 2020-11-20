
n = 20 #size of array
p = 4 #size of subset
array = []

for i in range(20):  
    l = list(map(int, input().split()))
    array.append(l)

def calc_product(sublist): #function that calculates product of each sublist aka every 4 elements
    product = 1
    for element in sublist:
        product = product*element
    return product

def linear(n, p, arr):
    lin = []
    limit = n-p+1 #calculating the number of iteration to be performed
    for i in range(n):
        idx_first_element = 0
        idx_last_element = p
        for _ in range(0,limit):
            lin.append(calc_product(arr[i][idx_first_element:idx_last_element]))
            idx_first_element += 1
            idx_last_element += 1   
    return max(lin)

def slash(n, p, arr):
    right = []
    start = p-1 
    limit = n-p+1
    for i in range(0,limit):
        for j in range(start, n):
            temp_list = []
            temp_list.extend((arr[i][j], arr[i+1][j-1], arr[i+2][j-2], arr[i+3][j-3]))
            right.append(calc_product(temp_list))
    return max(right)

def backslash(n, p, arr):
    left = []
    limit = n-p+1 #number of times the loop has to run
    for i in range(0,limit):
        for j in range(0,limit):
            temp_list = []
            temp_list.extend((arr[i][j], arr[i+1][j+1],arr[i+2][j+2],arr[i+3][j+3]))
            left.append(calc_product(temp_list))
    return max(left)

print(max(linear(n,p,array), slash(n,p,array),backslash(n,p,array)))