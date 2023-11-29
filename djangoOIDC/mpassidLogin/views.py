from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return redirect('success_page')

    return render(request, 'mpassidLogin/index.html')