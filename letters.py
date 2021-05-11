massage = input("Введите текст : ")
new_massage = " "
VOWELS = "aeiou"
print()
for letter in massage:
    if letter.lower() not in VOWELS:
        new_massage += letter
        #print("Создана новая строка:", new_massage)

print("\nВот ваш текст с изъятыми гласными буквами : ", new_massage,len(new_massage))
print("\nПривет Мир")