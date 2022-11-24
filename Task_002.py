# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

x1 = [True, False]
y1 = [True, False]
z1 = [True, False]

for x in x1:
    for y in y1:
        for z in z1:
            print(x, y, z)
            var1 = not (x or y or z)
            var2 = (not x) and (not y) and (not z)
            print(var1 == var2)
