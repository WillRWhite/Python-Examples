class A:
    pass
    a = 5
    b = 5
    sector = [['-' for x in range(a)] for y in range(b)]
    pass

class B:
    pass
    a = 1
    b = 2
    a = a+b
    pass

    def staticfn(p):
        return p+1
    a = staticfn(a)
    pass
    
    staticfn(3)
    pass


def main():
    print(A.a, A.b)
    print(B.a, B.b)

    a = 10
    b = 10
    sector = [['-' for x in range(a)] for y in range(b)]
 
if __name__ == "__main__":
    main()