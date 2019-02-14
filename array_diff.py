def max_dif(n,a):

    max=a[1]-a[0]
    min=a[0]

    if max<0:
        max=-1

    for i in range(1,n):
        if(a[i]-min>max):
            max=a[i]-min
        if(a[i]<min):
            min=a[i]
    return max


a=[7,9,5,6,3,2]
n=a.__len__()
print(n)
print("Method Call",max_dif(n,a))