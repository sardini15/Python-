def multi_table(a, n):
    
    for i in range(1, 1+int(n)):
        print("{0} x {1} = {2}".format(a, i, a*i))
    
if __name__ == "__main__":
    a = input("Enter a number: ")
    n = input("Enter the number of multiples")
    multi_table(float(a), float(n))