def cek_digit_belakang(a, b, c):
    last_a = a % 10
    last_b = b % 10
    last_c = c % 10


    return last_a == last_b or last_a == last_c or last_b == last_c


print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))


