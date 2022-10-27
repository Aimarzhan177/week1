lang = input('язык программирования:python,java,javasript ').lower()
age = int(input('Введите ваш возраст пожалуйста: '))
op = int(input('Введите ваш опыт работы: '))
are = int(input('Введите вашу желаемую зарплату: '))
if age > 65:
    print("К сожалению вы нам не подходите")
if op > 3:
    print('Вы нам  подходите')
if are > 60000:
    print('Вы нам  Neподходите')