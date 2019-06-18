from django.http import HttpResponse


def first_task(request, input_string):
    lower_string = input_string.lower()
    return HttpResponse(lower_string)


def second_task(request, leng, input_string):
    check = leng
    ret_string = ''
    for i in range(len(input_string)):
        if check == 0:
            ret_string += '-'
            check = leng
        check -= 1
        ret_string += input_string[i]
    return HttpResponse(ret_string)
