from django.shortcuts import render

def main(request):
    return render(request, 'books/base.html')
def support(request):
    return render(request, 'books/main.html')

