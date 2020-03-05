# Here the list is passed as a parameter,

li = [0,1]
n = 10

#Here "rec" is a recursive function where the list,int have been passed as the parameters.  In the recursive call l(immutable object) is being called by reference.
def rec(l,n):
    print(id(l))
    if(n == 0):
        return
    else:
        l.append(n)
        rec(l,n-1)

# In "rec_fib", parameter [li] is being called recursively however, the location will be created all the time
def rec_fib(l,n):
    print(id(l))
    if(n == 0):
        return
    else:
        t = l[0] + l[1]
        l.append(t)
        rec_fib(li[1:],n-1)

l = []
rec_fib(li,n)
rec(l,n)
