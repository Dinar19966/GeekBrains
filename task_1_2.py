def task_1_1_a():
    sum_a = 0
    list_of_cubes = []
    for i in range(1, 1000):
         if i % 2 == 1:
             list_of_cubes.append(i**3)
    for numb in list_of_cubes:
        digits_sum = 0
        numb = str(numb)
        digits_list = list(numb)
        j: int
        for j in digits_list:
            j = int(j)
            digits_sum += j
        if digits_sum % 7 == 0:
            numb = int(numb)
            sum_a += numb
    print(sum_a)

def task_1_1_b():
    sum_a = 0
    list_of_cubes = []
    for i in range(1, 1000):
         if i % 2 == 1:
             list_of_cubes.append(i**3)
    for numb in list_of_cubes:
        digits_sum = 0
        numb = numb + 17
        numb = str(numb)
        digits_list = list(numb)
        j: int
        for j in digits_list:
            j = int(j)
            digits_sum += j
        if digits_sum % 7 == 0:
            numb = int(numb)
            sum_a += numb
    print(sum_a)
task_1_1_a()
task_1_1_b()