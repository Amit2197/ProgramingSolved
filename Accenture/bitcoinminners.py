import timeit
def BM(input_from_question):
    start = timeit.default_timer()
    total = 0
    input_from_question = input_from_question.split(' ')
    for i in range(1, int(input_from_question[0])+1):
        if i%2!=0:
            total += int(input_from_question[1])
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    return total

input_from_question = '7 15'
print(BM(input_from_question))