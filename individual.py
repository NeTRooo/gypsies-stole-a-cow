def main():
    print(f"Введите возраст Тани и Мити")
    input1 = [0, 0]
    res = [0, 0, 0]
    for i in range(2):
        input1[i] = int(input())
    res[0] = ((int(input1[0]) + int(input1[1])) / 2)
    res[1] = abs(int(input1[0]) - int(res[0]))
    res[2] = abs(int(input1[1]) - int(res[0]))
    print(f"Средний возраст: {res[0]}\nРазница Тани: {res[1]}\nРазница Мити: {res[2]}")

if __name__ == "__main__":
    main()