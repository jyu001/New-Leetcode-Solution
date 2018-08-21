'''
146. LRU Cache
DescriptionHintsSubmissionsDiscussSolution
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
'''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}                # key:index
        self.listvalue = []             # value
        self.listkey = []               # key
        self.capacity = capacity
        self.listpop = []               # order of index to pop

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dic = self.dic 
        listvalue = self.listvalue
        listkey = self.listkey 
        listpop = self.listpop
        print('get', key)
        if key in dic:
            listpop.remove(dic[key])
            listpop.append(dic[key])
            print (listpop,listkey,listvalue,dic.keys(),dic.values())
            return listvalue[dic[key]]
        else: return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        dic = self.dic
        listvalue = self.listvalue
        listkey = self.listkey
        capacity = self.capacity
        listpop = self.listpop
        
        ninsert = 0
        if len(listvalue) == capacity:          # in case over capacity
            print('over', listpop)
            del dic[listkey[listpop[0]]]
            listkey[listpop[0]] = 0
            listvalue[listpop[0]] = 0
            ninsert = listpop[0]
            listpop = listpop[1:]
            print('over', listpop)
            print (listpop,listkey,listvalue,dic.keys(),dic.values())
        else:
            ninsert = len(listpop)
        if key not in dic: 
            dic[key] = ninsert
            listpop.append(ninsert)
            if len(listvalue) == capacity:
                listkey[ninsert] = key
                listvalue[ninsert] = value
            else:
                listkey.append(key)
                listvalue.append(value)
            print('put', key, value, 'n:',ninsert)
            print (listpop,listkey,listvalue,dic.keys(),dic.values())
        else:
            return "key already exists"
            
        

'''
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
 
 
class DoubleLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
 
    def pop(self, node=None):
        if not node:
            node = self.tail
        pre, next = node.pre, node.next
        if pre and next:
            pre.next = next
            next.pre = pre
        
        if node == self.tail:
            self.tail = self.tail.pre
        if node == self.head:
            self.head = self.head.next
        return node
 
    def insert_head(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            node.pre = self.tail
            self.head.pre = node
            self.tail.next = node
            self.head = node
 
 
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.linklist = DoubleLinkList()
 
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key)
        if not node: return -1
        self.linklist.pop(node)
        self.linklist.insert_head(node)
        return node.value
 
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            node = self.linklist.pop(self.map[key])
            node.value = value
        else:
            if len(self.map) == self.capacity:
                node = self.linklist.pop()
                del self.map[node.key]
            node = Node(key, value)
            self.map[key] = node
        self.linklist.insert_head(node)