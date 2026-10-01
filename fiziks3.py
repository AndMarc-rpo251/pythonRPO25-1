import math

#Шага индукции
k = int(input("Введите k: "))

#Угол в радианах
phi = float(input("Введите угол φ в радианах: "))

# Комплексное число cos(phi) + i*sin(phi)
a = math.cos(phi)
b = math.sin(phi)

#Состояние на шаге k
real_k = math.cos(k * phi)
imag_k = math.sin(k * phi)

print("\nШаг k:")
print(f"z_k = {real_k:.10f} + ({imag_k:.10f})i")

#Раскрываем скобки:
#(cos(kφ) + i sin(kφ)) * (cosφ + i sinφ)

real_next = real_k * a - imag_k * b
imag_next = real_k * b + imag_k * a

print("\nРаскрытие скобок:")

print(f"Re = cos(kφ)·cos(φ) - sin(kφ)·sin(φ)")
print(f"Im = sin(kφ)·cos(φ) + cos(kφ)·sin(φ)")

print("\nПолучаем:")
print(f"z_(k+1) = {real_next:.10f} + ({imag_next:.10f})i")

#Правая часть формулы Муавра для k+1
expected_real = math.cos((k + 1) * phi)
expected_imag = math.sin((k + 1) * phi)

print("\nПравая часть формулы Муавра:")
print(f"cos((k+1)φ) + i·sin((k+1)φ) = "f"{expected_real:.10f} + ({expected_imag:.10f})i")

#Проверяем равенство
epsilon = 1e-10

if (abs(real_next - expected_real) < epsilon and
        abs(imag_next - expected_imag) < epsilon):
    print("\nРезультат: равенство доказано для перехода k → k+1.")
else:
    print("\nРезультат: равенство не подтверждено.")
