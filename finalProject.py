class Node:
    def __init__(self, ID, Name):
        self.ID = ID
        self.value = Name
        self.parent = None
        self.left = None  
        self.right = None 


class BST: 
    def __init__(self):
        self.root = None
    def insertRequest(self, ID, Name):
        preNode = Node(ID, Name)
        if self.root == None:
            self.root = preNode
            return None
        tempNode = self.root
        while True:
            if ID < tempNode.ID:
                if tempNode.left == None:
                    tempNode.left = preNode
                    break
                tempNode = tempNode.left
            else:  
                if tempNode.right == None:
                    tempNode.right = preNode
                    break
                tempNode = tempNode.right  
    '''               
    def insertRequest(self, ID, Name):
        tempNode = Node(ID, Name)
        preNode = Node(ID, Name)
        compareR = self.root
        if self.root.value == None:
           self.root = tempNode
        elif self.root.value != Name:
           while compareR.value != None:
                tempNode = compareR
                if ID < compareR.ID:
                    compareR = compareR.left
                else:
                    compareR = compareR.right
            preNode.parent = compareR
            if ID < compareR.ID:
                compareR.left = preNode
            else:
               compareR.right = preNode
    ''' 
    
    def deleteRequest(self, ID):
        tempNode = self.root
        parent = None

        while tempNode != None and tempNode.ID != ID:
            parent = tempNode
            if ID < tempNode.ID:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right

        if tempNode == None:
            return None
        
        if tempNode.left == None and tempNode.right == None:
            if tempNode == self.root:
                self.root = None  
            elif parent.left == tempNode:
                parent.left = None
            else:
                parent.right = None

        
        elif tempNode.left == None or tempNode.right == None:
            child = tempNode.left if tempNode.left != None else tempNode.right
            if tempNode.left != None:
                child = tempNode.left
            else:
                child = tempNode.right
            if tempNode == self.root:
                self.root = child  
            elif parent.left == tempNode:
                parent.left = child
            else:
                parent.right = child

        else:
            altP = tempNode
            alt = tempNode.right
            
            while alt.left != None:
                altP = alt
                alt = alt.left
                        
            tempNode.ID = alt.ID  
            tempNode.value = alt.value
                     
            if altP.left == alt:
                altP.left = alt.right
            else:
                altP.right = alt.right
            

    def searchRequest(self, ID):
        tempNode = self.root
        while tempNode != None:
            if tempNode.ID == ID:
                return tempNode.value 
            elif ID < tempNode.ID:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right
        return None
    
    '''    
    def min_value(self, Root):
        check = Root
        while check.left != None:
            check = check.left
        return check
    
    def deleteRequest(self,root, ID):
        if self.root == None:
            return self.root
        if ID < self.root.ID:
            self.root.left = self.delete(root.left, ID)
        elif ID > root.ID:
            root.right = self.delete(root.right, ID)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root
    '''    
    
    def printBST(self):
        self.__printBST(self.root)

    def __printBST(self, node):
        if node is not None:
            print(f"{node.ID} : {node.value}")
            self.__printBST(node.left)
            self.__printBST(node.right)
            


class MaxHeap:
    def __init__(self):
        self.heap = list()
    def insertHeap(self, ID, Priority):
        self.heap.append((Priority, ID))
        self.maxHeapify(len(self.heap) - 1)
        
    def maxHeapify(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent][0] < self.heap[index][0]:
                self.heap[parent] = self.heap[index]
                self.heap[index] = self.heap[parent]
                index = parent
            else:
                break
        '''
        n = len(self.heap)
        
        def heapify(l):
            largest = l
            left = 2 * l + 1 
            right = 2 * l + 2 
            
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
                
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
                
            if largest != l:
                self.heap[l], self.heap[largest] = self.heap[largest], self.heap[i]
                heapify(largest)
                
        for l in range(n // 2 - 1, -1, -1):
            heapify(l)
        '''
    def increasePriority(self, ID, nPrior):
        for i in range(len(self.heap)):
            if self.heap[i][1] == ID:
                Prior = self.heap[i][0]
                if nPrior > Prior:
                    self.heap[i] = (ID, nPrior)
                    self.maxHeapify(i)
                break

    def deleteMaxHeap(self):
        if len(self.heap) == 0:
            return None
                
        max = self.heap[0]
        last = self.heap.pop()
        
        if len(self.heap) != 0:
            self.heap[1] = last
            self.maxHeapify(1)
        return max
