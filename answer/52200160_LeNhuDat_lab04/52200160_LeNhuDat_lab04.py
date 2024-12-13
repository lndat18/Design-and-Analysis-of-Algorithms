def binarySearch(arr, key):
    l = arr[0]
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            r = m - 1
        else:
            l = m + 1
    
    return None


def quickSort(arr, l, r):
    if l < r:
        s = HoarePartition(arr, l, r)
        quickSort(arr, l, s)
        quickSort(arr, s+1, r)


def HoarePartition(arr, l, r):
    p = arr[l]
    i = l - 1
    j = r + 1

    while True:
        i += 1
        while arr[i] < p:
            i += 1
        
        j -= 1
        while arr[j] > p:
            j -= 1

        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]


class Node:
     def __init__(self,data):
          self.left = self.right = None
          self.key = data


def height(node):
    if node is None:
        return -1
    
    left_height = height(node.left)
    right_height = height(node.right)
    
    return max(left_height, right_height) + 1


def preorder(node):
    if node:
        print(node.key, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=" ")


def main():
    # arr = [0,1,2,3,4,5,6,7,8,9,10]
    # arr1 = [7,2,6,5,1,3,4,8]


    # location = binarySearch(arr, 9)
    # quickSort(arr1, 0, len(arr1)-1)
    

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # print("Height of the binary tree is:", height(root))


    print("Pre-order traversal:")
    preorder(root)
    print("\nIn-order traversal:")
    inorder(root)
    print("\nPost-order traversal:")
    postorder(root)

if __name__ == '__main__':
    main()
