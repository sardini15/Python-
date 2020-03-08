def distinguish(a):
    nums = []
    for i in range(int(a)+2, int(a)+19, 2):
        nums.append(i)
    if a.is_integer():
        if a % 2 == 0:
            print("an even number")
            print(nums)
        else:
            print("an odd number")
            print(nums)
    else:
        print("Please enter a integer")


if __name__ == "__main__":
    a = input("Enter a integer: ")
    distinguish(float(a))