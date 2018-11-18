#!/usr/bin/python
import sys
# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
class AVL_Tree(object): 
    def insert(self, root, key): 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        elif key > root.val: 
            root.right = self.insert(root.right, key) 
        else:
            return root

  
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
        balance = self.getBalance(root) 
  
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
        y.left = z 
        z.right = T2 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
        y.right = z 
        z.left = T3 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
        result = []
        stack = []
        stack.append(root)

        while (len(stack) > 0):
            root = stack.pop()
            result.append(root.val)

            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result
	
#r = list(map(ord, "pm @tnek your complaints"))

def test_flag(r):
    arr = [40, 32, 5, 101, 38, 36, 46, 44, 41, 53, 43, 42, 48, 54, 55, 49, 60]
    tree = AVL_Tree()
    root = None
    for i in r:
        root = tree.insert(root, i)

    answer = tree.preOrder(root)
    answer = [ord(i) ^ 69 for i in answer]
    for i in range(len(answer)):
        if answer[i] != arr[i]:
            return False
    return True

def main():
    used_keys = set()
    print("give me serial keys and I'll hand them along")
    counter = 0
    while counter <= 30:
        inp = raw_input(">")
        if inp in used_keys:
            print("hey you already gave me that one!")
            continue
        if test_flag(inp):
            counter += 1
            used_keys.add(inp)

            print("thx for the copy of isengard2 anon")
            if counter == 30:
                print("here's a flag: flag{support_your_local_content_developers_piracy_is_bad}")
                sys.exit(0)
            else:
                print("gimmie %s more" %(30 - counter))
        else:
            print("Invalid serial key!")
            sys.exit(0)

if __name__ == "__main__":
    main()
