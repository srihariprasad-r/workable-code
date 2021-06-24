class Node():
    def __init__(self, data):
        self.data =  data
        self.next = None
        

class List():
    def __init__(self):
        self.head = None
        
        
    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        last_node = self.head
            
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node
        
    def prepend(self, node, data):
        new_node = Node(data)
        
        cur_node = self.head
        prev_node = None
        
        while cur_node and cur_node.data != node:
            prev_node = cur_node
            cur_node = cur_node.next

        if prev_node is None:
            self.head = new_node
            new_node.next = cur_node
        else:
            prev_node.next = new_node
            new_node.next = cur_node
            
    
    def reverse(self):
        cur_node = self.head
        prev_node = None
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            
        self.head = prev_node

    def delete(self, data):
        cur = self.head
        prev_node = None
        
        while cur and cur.data != data:
            prev_node = cur
            cur = cur.next
            
        prev_node.next = cur.next
        cur = None

    def swap_node(self, data1, data2):
        
        prev1 = None
        cur1 = self.head
        
        while cur1 and cur1.data != data1:
            prev1 = cur1
            cur1 = cur1.next
            
            
        prev2 = None
        cur2 = self.head
        
        while cur2 and cur2.data != data2:
            prev2 = cur2
            cur2 = cur2.next

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
            
        cur1.next, cur2.next = cur2.next, cur1.next

    def merge_sorted_list(self, l2):
        p = self.head
        q = l2.head
        s = None
        new_head = None
        
        if p.data < q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
            
        new_head = s
        
        while p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next
 
        if not p:
            s.next = q
            
        if not q:
            s.next = p
            
        return new_head

    def odd_even(self):
        odd, even = Node(-1), Node(-1)
        o = odd
        e = even
        tmp = Node(-1)
        
        fnl = tmp
        
        cur = self.head
        
        while cur:
            if cur.data % 2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
        
        odd.next = None
        even.next = None
        
        odd = o.next
        even = e.next
        
        while odd:
            tmp.next = odd
            tmp = tmp.next
            odd = odd.next
            
        while even:
            tmp.next = even
            tmp = tmp.next
            even = even.next
                
        tmp.next = odd if odd else even
                
        return fnl.next

    def clockwise_rotate(self,k):
        cnt = i = 0
        t = k
        
        front = Node(-1)
        back = Node(-1)
        
        tmp = Node(-1)
        
        f = tmp
        
        ft = front
        bk = back
        
        cur_node = self.head
        
        while cur_node:
            cur_node = cur_node.next
            cnt += 1
        
        m = cnt
        
        cur_node = self.head
        c = cur_node
        
        while i < cnt - k and cur_node.next:
            cur_node = cur_node.next
            i += 1
            
        while k > 0 and cur_node:
            back.next = cur_node
            back = back.next
            cur_node = cur_node.next
            k -= 1
            
        i = 0
        cur_node = c

        while m - t > i:
            front.next = cur_node
            front = front.next
            cur_node = cur_node.next
            i += 1

        front.next = None
        back.next = ft.next
            
        return bk.next
                

l = List()
l.append('A')
l.append('B')
l.append('C')
l.append('D')
l.prepend('D','E')
# l.print_list()
l.reverse()
# l.print_list()
l.delete('C')
# l.print_list()
# l.swap_node('A', 'B')
# l.print_list()
# 1st List
l1 = List()
l1.append(1)
l1.append(3)
l1.append(4)
l1.append(5)
# 2nd List
l2 = List()
l2.append(2)
l2.append(6)
l2.append(7)
l2.append(8)
l1.merge_sorted_list(l2)
# l1.print_list()
l1.odd_even()
# l1.print_list()
f = l1.clockwise_rotate(1) 