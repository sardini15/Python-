def factors(b):

    # factor()関数を定義。
    # b以下の全ての自然数iについて、b/i の余りを調べ、
    # 余りが1の場合(iがbの因数である場合)に
    # iを出力する
    for i in range(1, b+1):
        if b % i == 0:
            print(i)


if __name__ == "__main__":
    # input()を用いて、ユーザーに数を入力させる
    b = input("Your Number Please: ")
    b = float(b)

    if b > 0 and b.is_integer():
        # 引数bが自然数であれば、factor()関数を適用する
        factors(int(b))
    else:
        # 自然数でなければ、自然数を入力するようにメッセージを出力する
        print("Please enter a positive integer")