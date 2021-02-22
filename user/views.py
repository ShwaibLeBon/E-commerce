from django.shortcuts import render

# Create your views here.
def AccountView(request):
    return render(request, 'user/account.html')