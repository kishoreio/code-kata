N = int(input())
list1 = list(map(int,input().split()[:N]))
max1 = max(list1)
min1 = min(list1)
diff = list1.index(max1) - list1.index(min1)
print(diff)