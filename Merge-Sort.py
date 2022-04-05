def Merge_Sort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]

        Merge_Sort(l)
        Merge_Sort(r)

        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1 
            else:
                arr[k] = r[j]
                j+=1

            k+=1

        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1 
            k+=1

    return arr
if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(Merge_Sort(arr))
        
