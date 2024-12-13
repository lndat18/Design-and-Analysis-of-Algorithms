import numpy as np

def ex1(n):
    sum = 0
    for i in range(2,n+1):
        sum += 1/(1-i**i)
    return sum

def ex2(n, m):
    sum = 0
    for i in range(1, n+1):
        sum += ((-1)**(i+1))*1/(1+m**i)
    return sum

def ex3(n):
    sum = 0
    for i in range(1, n+1): 
        sum += i**3
    return sum

def ex4(n):
    #  find the factorial
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial if n != 0 else 1

def ex5(arr):
    # check whether all elements in an array are distinct.
    # return true if all elements are distinct otherwise
    s = set()
    for element in arr:
        s.add(element)
    return True if len(s) == len(arr) else False

def ex6(arr):
    # find max element in array (all elements in the array are unique)
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def ex7(matrix1, matrix2):
    result = []
    if len(matrix1[0]) == len(matrix2):
        for i in range(len(matrix1)):
            line = []
            for j in range(len(matrix2[0])):
                sum = 0
                for k in range(len(matrix1)):
                    sum += matrix1[i][k] * matrix2[k][j]
                line.append(sum)
            result.append(line)
        return result
    else:
        return 'Dimension error: can not multiply'

def ex8(n, matrix):
    new_matrix = np.array(matrix).copy()
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = n*matrix[i][j]
    return new_matrix

def ex9(matrix1, matrix2):
    new_matrix1 = np.array(matrix1)
    new_matrix2 = np.array(matrix2)
    result = np.zeros((new_matrix1.shape))

    if new_matrix1.shape == new_matrix2.shape:
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                result[i][j] = new_matrix1[i][j] - new_matrix2[i][j]
        return result
    else:
        return 'Dimension error: can not subtract'

def ex10(matrix1, matrix2):
    new_matrix1 = np.array(matrix1)
    new_matrix2 = np.array(matrix2)
    result = np.zeros((new_matrix1.shape))

    if new_matrix1.shape == new_matrix2.shape:
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                result[i][j] = new_matrix1[i][j] + new_matrix2[i][j]
        return result
    else:
        return 'Dimension error: can not add'
    
def print_result(n,m=2):
    arr_str = ['hello','name','date','class']
    arr1 = [1,5,6,2,7,2,5,9,8]
    arr2 = [1,2,3,4,5,6,7,8,9]

    matrix1 = [[1,1,1],
               [2,2,2],
               [3,3,3]]
    matrix2 = [[1,1,1],
               [1,1,1],
               [1,1,1]]
    
    print('Ex1 ',ex1(n))
    print('Ex2 ',ex2(n,m))
    print('Ex3 ',ex3(n))
    print('Ex4 ',ex4(n))
    print('Ex5 ',ex5(arr_str))
    print('Ex6 ',ex6(arr2))
    print('Ex7 ',ex7(matrix1,matrix2))
    print('Ex8 ',ex8(n,matrix2))
    print('Ex9 ',ex9(matrix1, matrix2))
    print('Ex10 ',ex10(matrix1, matrix2))

def main():
    n = 3
    print_result(n)
    

if __name__ == '__main__':
    main()