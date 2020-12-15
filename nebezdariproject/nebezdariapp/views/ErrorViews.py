from django.shortcuts import render


def error_400(request, exception):
    '''
    Рендерит страницу с кодом ошибки номер 400.
    '''
    data = {}
    return render(request, 'errors/400.html', data)

def error_403(request, exception):
    '''
    Рендерит страницу с кодом ошибки номер 403.
    '''
    data = {}
    return render(request, 'errors/403.html', data)

def error_404(request, exception):
    '''
    Рендерит страницу с кодом ошибки номер 404.
    '''
    data = {}
    return render(request, 'errors/404.html', data)

def error_500(request):
    '''
    Рендерит страницу с кодом ошибки номер 500.
    '''
    data = {}
    return render(request, 'errors/500.html', data)