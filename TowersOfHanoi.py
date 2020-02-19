# class TowersofHanoi(object):
#     def __init__(self):
#         pass

def move(source,target):
    print("Move {} to {}" .format(source,target))


def towerofhanoi(N,source,helper,target):
    if N == 0:
        pass
    else:    
        towerofhanoi(N-1,source,target,helper)
        move(source,target)
        towerofhanoi(N-1,helper,source,target)

towerofhanoi(3,'A','B','C')