n = int(input())
integer_list = map(int, input().split())

tuple = tuple(integer_list)

print(int(hash(tuple)))
