class Heap(object):
    def __init__(self,Arr):
        self.Array = Arr
        # self.N = len(Arr)


    def max_heapify(self):
        N = len(self.Array)
        for i in reversed(range(N//2)): #range(N//2,-1,-1):
            self._maxheapify(self.Array,i,N)

    def min_heapify(self):
        N = len(self.Array)
        for i in reversed(range(N//2)):
            self._minheapify(self.Array,i,N)
         
    def _minheapify(self,Array,i,N):
        # N = len(Arr) - 1
        left = 2 * i + 1 
        right = 2 * i + 2
        if(left < N and Array[i] > Array[left]):
            largest = left
        else:
            largest = i
        if(right < N and Array[largest] > Array[right]):
            largest = right
        if(largest != i):
            Array[i],Array[largest] = Array[largest],Array[i]
            self._minheapify(Array,largest,N)

    def _maxheapify(self,Array,i,N):
        # N = len(Arr) - 1
        left = 2 * i + 1 
        right = 2 * i + 2
        if(left < N and Array[i] < Array[left]):
            largest = left
        else:
            largest = i
        if(right < N and Array[largest] < Array[right]):
            largest = right
        if(largest != i):
            Array[i],Array[largest] = Array[largest],Array[i]
            self._maxheapify(Array,largest,N)

    def heap_sort(self):
        self.max_heapify()
        N = len(self.Array)
        for i in reversed(range(N)): #range(length,1,-1):
            self.Array[0],self.Array[i] = self.Array[i],self.Array[0]
            # N = N-1
            self._maxheapify(self.Array,0,i)
    
    def rev_heap_sort(self):
        self.min_heapify()
        N = len(self.Array)
        for i in reversed(range(N)): #range(length,1,-1):
            self.Array[0],self.Array[i] = self.Array[i],self.Array[0]
            # N = N-1
            self._minheapify(self.Array,0,i)

    def extract_maximum(self):
        self.max_heapify()
        top = self.Array[0]
        N = len(self.Array)
        self.Array[0] = self.Array.pop() #self.Array[N-1] 
        self._maxheapify(self.Array,0,N-2)
        return top
    
    def extract_manimum(self):
        self.min_heapify()
        top = self.Array[0]
        N = len(self.Array)
        self.Array[0] = self.Array.pop() #self.Array[N-1] 
        self._minheapify(self.Array,0,N-2)
        return top
