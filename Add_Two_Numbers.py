# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = l1
        len1 = 0
        len2 = 0
        while(c != None):
            len1+=1
            c = c.next
       
        c = l2
        while(c != None):
            len2+=1
            c = c.next 
        
        t = l1
        n1 = 0
        for i in range(len1):
            n1 =n1+ t.val * (10**i)
            t=t.next
       
        t = l2
        n2 = 0
        for i in range(len2):
            n2 =n2+ t.val * (10**i)
            t=t.next
               
        n = n1+n2
        #print(n)
        flag = True
        Head = None
        if n==0:
            Head =  ListNode(0,None)
            return Head
        while(n!=0):
            if flag:
                r = n%10
               #print(r)
                previous  = ListNode(r,None)
                Head = previous
                flag = False
                n = n//10
            else :
                r = n%10
               # print(r)
                newNode = ListNode(r,None)
                
                previous.next = newNode
                previous = newNode
                n = n//10
            
        return Head
