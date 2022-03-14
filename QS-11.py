"""
Question: Write an Python program to print prime numbers in less then 20
"""

limit = int(input("Enter Limit: "))

for i in range(1, limit+1):
    if limit >= 20:
        print("Limits under 20 only valids")
        break

    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i)


"""
OUTPUT 1:
-----
Enter Limit: 10
1
2
3
5
7

OUTPUT 2:
-----
Enter Limit: 21
Limits under 20 only valids

"""