class Array(object):
    def __init__(self,size):
        self._size=size
        self._items=[None]*size

    def __getitem(self,index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i]=value

    def __iter__(self):
        for item in self._items:
            yield item

def test_arry():
    size=10
    a=Array(size)
    a[0]=1
    assert a[0] == 1
    assert len(a) == 10

if __name__=='__main__':
    test_arry()
