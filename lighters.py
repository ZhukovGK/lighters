# Фонарики (0055)
# 
# «Одна голова хорошо, а две лучше. Одна лампочка хорошо, а две лучше!» - подумал Миша, 
# и решил собрать фонарик с двумя лампочками. Теперь он хочет узнать, 
# насколько фонарик с двумя лампочками лучше, чем фонарик с одной. 
# Заметим, что лампочки в фонаре с двумя лампочками отличаются от лампочки в фонаре с одной лампочкой. 
# Для этого Миша посветил фонариком на стену, и каждая из лампочек осветила на ней круг.
#
# Эффективность фонарика Миша хочет оценить через площадь освещенной части стены. 
# Миша догадался измерить координаты центров освещенных кругов и их радиусы (которые оказались одинаковыми). 
# Причем, площадь, освещаемая фонариком с одной лампочкой известна, т.к. описана в документации, прилагаемой к фонарику. 
# Но что делать дальше он не знает. Напишите программу, которая поможет Мише.
#
# Входные данные
# В первых двух строчках входного файла INPUT.TXT содержатся координаты (x1,y1) и (x2,y2) 
# - центры кругов от лампочек собранного Мишей фонарика. В третьей строке задан радиус r описанных выше кругов, 
# а четвертая строка содержит площадь освещения s фонариком из одной лампочки. 
# Все числа целые и удовлетворяют следующим ограничениям: 1 ≤ x1,y1,x2,y2,r ≤ 100, 1 ≤ s ≤ 105.
# Так же заметим, что площади, освещаемые разными фонариками, отличаются друг от друга более чем на 10-3.
#
# Выходные данные
# В выходной файл OUTPUT.TXT выведите «YES», если Мишин фонарик лучше старого 
# (т.е. освещает большую площадь) и «NO» в противном случае.
# ----------------------------------------------------------------------------------------------------------------------------
from math import pi, sqrt, sin, acos, degrees, radians

input_data = open("input.txt", "r")
output_data = open("output.txt", "w")
data = input_data.readlines()

splitted_data = []
for i in data:
    splitted_data.append(i.split())

centre_1 = splitted_data[0]
centre_2 = splitted_data[1]
radius = int(splitted_data[2][0])
big_square = int(splitted_data[3][0])

# находим расстояние между центрами двух окружностей
# это нужно, чтобы определить взаимное расположение
# окружностей на плоскости
distance = sqrt(((int(centre_1[0]) - int(centre_2[0])) ** 2) + ((int(centre_1[1]) - int(centre_2[1])) ** 2))
small_squares = 2 * pi * (radius ** 2)

if distance >= 2 * radius:
    if small_squares > big_square:
        output_data.write("YES")
    else:
        output_data.write("NO")
elif distance == 0:
    if small_squares / 2 > big_square:
        output_data.write("YES")
    else:
        output_data.write("NO")
else:
    a = distance / 2
    h = sqrt((radius ** 2) - (a ** 2))
    angle = round(degrees(acos(a / radius)), 2)
    seqment_square = (radius ** 2) * (radians(angle) - sin(radians(angle)))
    small_squares = small_squares - seqment_square
    if small_squares > big_square:
        output_data.write("YES")
    else:
        output_data.write("NO")

print(distance)
print(centre_1)
print(centre_2)
print(radius)
print(big_square)
input_data.close()
output_data.close()