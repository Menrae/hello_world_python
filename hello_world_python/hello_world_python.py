print("hello world");

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5));
print(sum(15));
print(sum(151));


def array_test():
    ar = [3, 2, 4, 5]

    ar.pop()

    ar.append(6)

    print(ar)
    print("Index of 4: ", ar.index(4)) # index of given value

    ar.remove(4) # remove the first occurence of the item with the given value
    print("Removed 4: ", ar)

    ar.reverse()
    print("reversed: ", ar)
    print("sorted return: ", sorted(ar))

    ar.sort()
    print("sorted in place: ", ar)


def main():
    array_test()


if __name__ == "__main__":
    main()