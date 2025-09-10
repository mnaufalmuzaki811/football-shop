from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'NOPALZ SPORTY',
        'name': 'Muhammad Naufal Muzaki',
        'npm': '2406428794'
    }

    return render(request, "main.html", context)
