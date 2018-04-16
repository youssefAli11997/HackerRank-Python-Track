if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        line = input().split(" ")
        if line[0] == "insert":
            L.insert(int(line[1]), int(line[2]))
        if line[0] == "print":
            print(L)
        if line[0] == "remove":
            L.remove(int(line[1]))
        if line[0] == "append":
            L.append(int(line[1]))
        if line[0] == "sort":
            L.sort()
        if line[0] == "pop":
            L.pop()
        if line[0] == "reverse":
            L.reverse()
