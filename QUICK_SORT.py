def quick_sort(arr,lb,ub):
    if(lb < ub):
        loc = partition(arr,lb,ub)

        quick_sort(arr,lb,loc-1)
        quick_sort(arr,loc+1,ub)

def partition(arr,lb,ub):
    pivot = arr[lb]
    start = lb
    end = ub

    while(start <= end):
        while(start <= end  and arr[start] <= pivot):
            start +=1

        while(start <= end and arr[end] > pivot):
            end -=1

        if(start < end):
            arr[start],arr[end] = arr[end],arr[start]

    arr[lb],arr[end] = arr[end],arr[lb]

    return end

arr = []
n = int(input("Enter number of elements : "))
for i in range(n):
    ele = int(input(f"Enter element {i+1} : "))
    arr.append(ele)

quick_sort(arr,0,n-1)
print("sorted array :",arr)