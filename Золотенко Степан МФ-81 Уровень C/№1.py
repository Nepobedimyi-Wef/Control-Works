length_1 = int(input("Введите длину 1 параллелепипеда: "))
width_1 = int(input("Введите ширину 1 параллелепипеда: "))
height_1 = int(input("Введите высоту 1 параллелепипеда: "))

length_2 = int(input("Введите длину 2 параллелепипеда: "))
width_2 = int(input("Введите ширину 2 параллелепипеда: "))
height_2 = int(input("Введите высоту 2 параллелепипеда: "))

length_3 = int(input("Введите длину 3 параллелепипеда: "))
width_3 = int(input("Введите ширину 3 параллелепипеда: "))
height_3 = int(input("Введите высоту 3 параллелепипеда: "))

volume_1 = length_1 * width_1 * height_1 #Считаем объём 1 параллелепипеда

volume_2 = length_2 * width_2 * height_2 #Считаем объём 2 параллелепипеда

volume_3 = length_3 * width_3 * height_3 #Считаем объём 3 параллелепипеда

total_volume = volume_1 + volume_2 + volume_3 #Считаем общий объём 3 параллелепипедов

print(f"Общий объём 3 параллелепипедов: {total_volume}")
