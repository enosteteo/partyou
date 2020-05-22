from django.shortcuts import render
# Create your views here.


def store_list(request):
    return render(request, 'store/list_products.html')
