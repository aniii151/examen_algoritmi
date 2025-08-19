#merge sort- divid lista
# O(n log n) in cel mai bun caz
#caz rau 0(n)
def merge_sort(arg):
    if len(arg) >1:
        mij = len(arg)//2
        l= arg[:mij]
        r= arg[mij:]          #impart lista
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i] < r[j]:
                arg[k]= l[i]
                i+=1
            else:
                arg[k] = r[j]
                j+=1
            k+=1
        while i< len(l):
            arg[k] = l[i]
            i+=1
            k+=1
        while j< len(r):
            arg[k] = r[j]
            j+=1
            k+=1

arg=[5,2,8,1,3]
merge_sort(arg)
print("Merge Sort:", arg)
