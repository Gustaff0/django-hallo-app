from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def home_view(request):

    print(request.GET.getlist('title'))
    return render(request, 'home.html')


def math_create_view(request):
    if request.method == "GET":
        return render(request, 'calculate_input.html')
    elif request.method == "POST":
        context = {
            'f_num': int(request.POST.get("f_num")),
            's_num': int(request.POST.get("s_num")),
            'math': request.POST.get("math"),
            }
        math_result = 0
        sumbol = ''
        if context['math'] == 'add':
            math_result += context['f_num'] + context['s_num']
            sumbol = '+'
        elif context['math'] == 'subtract':
            math_result += context['f_num'] - context['s_num']
            sumbol = '-'
        elif context['math'] == 'multiply':
            math_result += context['f_num'] * context['s_num']
            sumbol = '*'
        else:
            math_result += context['f_num'] / context['s_num']
            sumbol = '/'
        context['sumbol'] = sumbol
        context['math_result'] = math_result
        return render(request, 'result.html', context)
