# def Bubble_Sort(arr):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#                 print(arr)


#     return arr

def Bubble_Sort(arr):
    for i in range(len(arr)):
        swapped = False 
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True 

        if swapped == False:
            return arr  
    return arr  
if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(Bubble_Sort(arr))