def Partition(arr,low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1 
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[high] =arr[high],arr[i+1]
    return i+1

def Quick_Sort(arr,low, high):
    if low < high:
        pi = Partition(arr,low, high)
        Quick_Sort(arr,low,pi-1)
        Quick_Sort(arr,pi+1,high)

if __name__ == "__main__":
    arr= [5,4,3,2,1]
    size = len(arr)
    Quick_Sort(arr,0,size-1)
    print(arr)