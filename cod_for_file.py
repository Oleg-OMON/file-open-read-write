file_list = []
def count_file(input_file_1, input_file_2, input_file_3):

 with open('1.txt')as file_1:
    counter_1 = 0
    counter_1 += sum(1 for line in file_1)
    file_list.append(counter_1)

 with open('2.txt')as file_2:
    counter_2 = 0
    counter_2 += sum(1 for line in file_2)
    file_list.append(counter_2)

 with open('3.txt')as file_3:
    counter_3 = 0
    counter_3 += sum(1 for line in file_3)
    file_list.append(counter_3)


    print(sorted(file_list))

count_file('1.txt', '2.txt', '3.txt')

def write_file(input_file):
    with open('4.txt','w')as file:
        file.write("Файл 2.txt \n1 строка \n\nФайл 1.txt \n8 строк\n\nФайл 3.txt \n9 строк")


write_file('4.txt')

with open('4.txt') as file:
    print(file.read())