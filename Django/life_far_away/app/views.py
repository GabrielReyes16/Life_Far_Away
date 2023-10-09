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