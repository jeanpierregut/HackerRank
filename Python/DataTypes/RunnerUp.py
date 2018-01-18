n = int(input())
arr = map(int, input().split())

numberList = list(arr)
numberList = sorted([i for i in numberList if (i != max(numberList))],reverse=True)

print(numberList[0])