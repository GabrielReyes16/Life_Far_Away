from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'planet.html')

def planet (request):
# def planet (request,codigo):
    # planeta=Planeta.objects.get(id=codigo)
    # context={
    #     'planeta':planeta
    # }
    return render(request,"planet.html")
    # return render(request,"planet.html",context)

def data(request):
    return render(request, 'planet_data.html')

def our_exoplanet(request):
    name = "OGL-2023-1524L b"
    exoplanet = planet.objects.get(name_planet = name)
    context={ 
        'exoplanet':exoplanet
    }
    return render(request,"our_exoplanet.html", context)

