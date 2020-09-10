class Heap(object):
    def __init__(self,*argv):
        self.array = []
        if argv :
            for i in argv:
                if type(i) == int :
                    self.array.append(i)
                else:
                    print("Heap accepts only numericals")
        else:
            self.array = list(input("Enter the input array in comma seperated type ex: 1,2,3,4").split(','))
        # self.length = len(Arr)
    #refer to the Donbader website for difference betewen __repr__ and __str__
    def __repr__(self):
        return '{self.__class__.__name__}({self.array})'.format(self = self)

    def max_heapify(self):
        length = len(self.array)
        for i in reversed(range(length//2)): #range(length//2,-1,-1):
            self.__maxheapify(self.array,i,length)

    def min_heapify(self):
        length = len(self.array)
        for i in reversed(range(length//2)):
            self.__minheapify(self.array,i,length)
         
    def __minheapify(self,array,i,length):
        # length = len(Arr) - 1
        left = 2 * i + 1 
        right = 2 * i + 2
        if(left < length and array[i] > array[left]):
            largest = left
        else:
            largest = i
        if(right < length and array[largest] > array[right]):
            largest = right
        if(largest != i):
            array[i],array[largest] = array[largest],array[i]
            self.__minheapify(array,largest,length)

    def __maxheapify(self,array,i,length):
        # length = len(Arr) - 1
        left = 2 * i + 1 
        right = 2 * i + 2
        if(left < length and array[i] < array[left]):
            largest = left
        else:
            largest = i
        if(right < length and array[largest] < array[right]):
            largest = right
        if(largest != i):
            array[i],array[largest] = array[largest],array[i]
            self.__maxheapify(array,largest,length)

    def heap_sort(self):
        self.max_heapify()
        length = len(self.array)
        for i in reversed(range(length)): #range(length,1,-1):
            self.array[0],self.array[i] = self.array[i],self.array[0]
            # length = length-1
            self.__maxheapify(self.array,0,i)
    
    def rev_heap_sort(self):
        self.min_heapify()
        length = len(self.array)
        for i in reversed(range(length)): #range(length,1,-1):
            self.array[0],self.array[i] = self.array[i],self.array[0]
            # length = length-1
            self.__minheapify(self.array,0,i)

    def extract_maximum(self):
        self.max_heapify()
        top = self.array[0]
        length = len(self.array)
        self.array[0] = self.array.pop() #self.array[length-1] 
        self.__maxheapify(self.array,0,length-2)
        return top
    
    def extract_manimum(self):
        self.min_heapify()
        top = self.array[0]
        length = len(self.array)
        self.array[0] = self.array.pop() #self.array[length-1] 
        self.__minheapify(self.array,0,length-2)
        return top

heap = Heap(1,2,3,4,5)
heap.max_heapify()
print(heap.array)
