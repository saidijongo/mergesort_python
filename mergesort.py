from random import randint
def randno(lengthx =15, max = 50):
    
    arr_lst = [randint(0,max) for _ in range(lengthx)]
    return arr_lst
#print(randno())

def merge(a, b):
    c = []
    ai,bi = 0,0
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            c.append(a[ai])
            ai+=1
        else:
            c.append(b[bi])
            bi+=1
    if ai == len(a):
        c.extend(b[bi:])
    else:
        c.extend(a[ai:])
    return c

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    midp = len(arr)//2
    left, right = merge_sort(arr[midp:]), merge_sort(arr[:midp])
    return merge(left,right)

arr = randno()
print(arr)
print(merge_sort(arr))








