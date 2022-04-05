
# def Selection_Sort(arr):
    
#     for i in range(len(arr)):
#         min = i 
#         for j in range(i+1,len(arr)):
#             if arr[min] > arr[j]:
#                 min = j 

#         arr[i],arr[min] = arr[min],arr[i] 
#         if i == min:
#             return arr  

#     return arr

# Iterate through the list changing the min 

def Selection_Sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j 

            arr[i],arr[min] = arr[min],arr[i]
            if i == min:
                return arr
    return arr

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(Selection_Sort(arr))


