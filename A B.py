
def comparing_arguments():
    try:
         number_a = int(input('Напиши перше число :'))
         number_b = int(input('Напиши друге число :'))
         if number_a == number_b:
             print("Ці числа рівні.")
         elif number_a < number_b:
             print("Перше число менше за друге.")
         elif number_a > number_b:
             print("Перше число більше за друге.")
    except:
           print("Помилка!!!Ви ввели не число.")

comparing_arguments()



