
# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print('Добрый день! Предлагаем Вам заполнить медицинскую анкету')
name = input('Ваше имя: ')
surname = input('Ваша фамилия :')
age = int(input('Ваш возраст. Введите число :'))
weight = int(input('Ваш вес. Введите число :'))

# def weightNormal(weight):
#     if weight >= 50 and weight <= 120:
#         weight = weightNormal
#     else:
#         return

while age <= 30:
    if weight >= 50 and weight <= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'хорошее состояние')
        break
    elif weight >= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'следует заняться собой')
        break
    else:
        break

while age >= 30 and age <= 40:
    if weight >= 50 and weight <= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'хорошее состояние')
        break
    elif weight <= 50 or weight >= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'следует заняться собой')
        break
    else:
        break

while age > 40:
    if weight >= 50 and weight <= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'хорошее состояние')
        break
    elif weight <= 50 or weight >= 120:
        print(name, surname, 'в возрасте ', age, 'и весе ', weight, 'следует обратиться к врачу')
        break
    else:
        break

