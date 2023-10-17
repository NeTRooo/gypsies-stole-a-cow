def main():
    print(f"Введите 4 числа.")
    args = [0, 0, 0, 0]
    res = [0, 0, 0]
    for i in range(0,4):
        args[i] = input(f"Введите число №{i+1}: ")
    res[0] = int(args[0]) + int(args[1])
    res[1] = int(args[2]) + int(args[3])
    res[2] = res[0] / res[1]
    print("{:.2f}".format(res[2]))

if __name__ == "__main__":
    main()