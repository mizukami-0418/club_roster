from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def trigger_500(request):
        # 500エラーを強制的に発生させる
    raise Exception("This is a test exception to trigger a 500 error")