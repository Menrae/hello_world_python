print("hello world");

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5));
print(sum(15));
print(sum(151));