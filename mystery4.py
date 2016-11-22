def mystery(n) :
    if n <= 0 : 
        return 0
    else:
        return n + mystery(n - 1)

def main():
    for i in range (1, 5):
        print("mystery (", i, ") is", mystery(i))

main()
