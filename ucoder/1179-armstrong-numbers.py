def get_digits(n):
    digit_list = []

    while n > 0:
        digit_list.append(n % 10)
        n //= 10

    return digit_list

while True:
    n = int(input())
    if n == 0:
        break
    digit_list = get_digits(n)
    power_list = [x for x in digit_list]

    power = 2
    while power < 10:
        for i in range(len(digit_list)):
            power_list[i] *= digit_list[i]
        sum_list = sum(power_list)
        if sum_list == n:
            break
        power += 1
    print(power if power < 10 else 'N')
