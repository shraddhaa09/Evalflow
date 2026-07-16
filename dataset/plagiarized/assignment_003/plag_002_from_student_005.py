list1 = [2,4,6,8,10]

num = 8

start = 0
end = len(list1)-1

while(start<=end):

    mid = int((start+end)/2)

    if(list1[mid]==num):
        print("element found")
        break

    elif(list1[mid]>num):
        end = mid-1

    else:
        start = mid+1