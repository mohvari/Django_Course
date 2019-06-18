from django.http import HttpResponse
from math import ceil, sqrt


def first_task(request, input_number):
    input_number = pow(input_number, 2)
    input_number = int(input_number)
    number_string = str(input_number)
    return HttpResponse(number_string)


def second_task(request, first_number, second_number):
    ret_val = first_number * second_number
    ret_val_string = str(ret_val)
    return HttpResponse(ret_val_string)


def third_task(request, first_number, second_number):
    ret_string = ''
    is_first = True
    for i in range(first_number, second_number + 1):
        if is_prime(i):
            if is_first:
                is_first = False
            else:
                ret_string += ','
            ret_string += str(i)
    return HttpResponse(ret_string)


def fourth_task(request, first_number, second_number, third_number):
    maximum = max(first_number, second_number, third_number)
    maximum_str = str(maximum)
    return HttpResponse(maximum_str)


def is_prime(x):
    if x == 2 or x == 3:
        return True
    for i in range(2, ceil(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def index(request):
    return HttpResponse("Hello World. You are at the math index.")
