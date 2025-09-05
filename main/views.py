from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Cihuy United',
        'name': 'Muhammad Derriel Ramadhan',
        'class': 'PBP F',
    }
    
    return render(request, "main.html", context)