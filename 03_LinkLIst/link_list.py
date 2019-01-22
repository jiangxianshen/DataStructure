class Node(object):
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

    def __str__(self):
        """方便你打出来调试，复杂的代码可能需要断点调试"""
        return'<Node:value:{},next={}>'.format(self.value.self.next)

    __repr__=__str__

""" 
链接表 ADT
[root] -> [node0] -> [node1] -> [node2]
"""
class LinkedList(object):
    """初始化，定义根节点"""
    def __init__(self,maxsize=None): # 如果是 None，无限扩充
        self.maxsize=maxsize
        self.root=Node() # 默认 root 节点指向 None
        self.tailnode=None
        self.length=0
     """定义长度"""
    def __len__(self):
        return self.length
    """末尾增加新元素"""
    def append(self,value):
        if self.maxsize is not None and len(self) >= self.maxsize
            raise Exception('LinkedList is full')
        node=Node(value)


