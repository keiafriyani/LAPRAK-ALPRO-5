def cek_angka(a, b, c):
    if a == b or a == c or b == c:
        return False
    if a+b == c or a+c == b or b+a == c:
        return True
    
    return False

print(cek_angka(2, 3, 2))
print(cek_angka(3, 5, 8))
