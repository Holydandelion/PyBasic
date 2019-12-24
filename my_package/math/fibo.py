
def fib(n: int)-> None:
    a, b = 0, 1
    while (b < n):
        print(b, end= " ")
        a, b = b, a+b
    print()
    return None

def fibList(n: int)-> list:
    result = []
    a, b = 0, 1
    while(b < n):
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    fib(10)