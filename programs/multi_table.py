def multi_table(a):

    # multi_table()関数を定義。
    # format()メソッドを利用して、
    # a x n = b
    # の形で出力する
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(a, i, a*i))
    
if __name__ == "__main__":
    a = input("Enter a number: ")
    multi_table(float(a))