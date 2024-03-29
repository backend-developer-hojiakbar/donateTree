from django.shortcuts import render, get_object_or_404
from .models import PlantedTrees, MainPageStatic, AboutTrees, AllTreesCount
from datetime import datetime, timezone
from django.core.paginator import Paginator
from django.db.models import Q

def clickPayment(request):
    return render(request, 'clickPayment.html', context={})

def home(request):
    allTreesNumber = AllTreesCount.objects.all()[0]
    mainStatics = MainPageStatic.objects.all()

    treesToday = PlantedTrees.objects.filter(time=PlantedTrees.Time.Today)
    treesMonth = PlantedTrees.objects.filter(time=PlantedTrees.Time.Month)
    treesYear = PlantedTrees.objects.filter(time=PlantedTrees.Time.Year)

    time  = treesToday[0].deadline - datetime.now(timezone.utc)
    differToday = {
        "days": time.days,
        "hours": time.seconds//3600,
        "minutes": time.seconds // 60 % 60
    }

    time = treesMonth[0].deadline - datetime.now(timezone.utc)
    differMonth = {
        "days": time.days,
        "hours": time.seconds // 3600,
        "minutes": time.seconds // 60 % 60
    }

    time = treesYear[0].deadline - datetime.now(timezone.utc)
    differYear = {
        "days": time.days,
        "hours": time.seconds // 3600,
        "minutes": time.seconds // 60 % 60
    }

    context = {
        "treesToday": treesToday,
        "treesMonth": treesMonth,
        "treesYear": treesYear,
        "differToday": differToday,
        "differMonth": differMonth,
        "differYear": differYear,
        "mainStatics": mainStatics,
        "allTreesNumber": allTreesNumber
    }

    return render(request, 'index.html', context=context)

def donateProject(request):
    return render(request, 'donateProjects.html', context={})

def treeList(request):
    treesList = AboutTrees.objects.all()
    context = {
        "treesList": treesList
    }
    return render(request, 'treeList.html', context)

def faqList(request):
    return render(request, 'faqlist.html', context={})

def treeDetail(request, id):
    treesList = AboutTrees.objects.all()[:4]
    singleTree = get_object_or_404(AboutTrees, id=id)

    district = singleTree.Regions

    if district == 'ToshkentV':
        regions = ["Olmaliq", "Angren", "CHirchiq", "Parkent", "Yuqori CHirchiq", "Quyi chirchiq"]
    else:
        regions = []

    context = {
        "tree": singleTree,
        "treesList": treesList,
        "region": regions
    }
    return render(request, 'treeDetail.html', context=context)

def donate(request):
    return render(request, 'donation.html', context={})

def register(request):
    return render(request, 'register.html', context={})

def login(request):
    return render(request, 'account/login.html', context={})

def payment(request):
    return render(request, 'payment.html', context={})

def companyPlantedTree(request):
    return render(request, 'companyTreeList.html', context={})

def plantedTree(request):
    return render(request, 'daraxtpage.html', context={})

def toshkentVil(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.ToshkentV) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/toshkentVil.html', context=context)

def andijon(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Andijon) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/andijon.html', context)

def buxoro(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Buxoro) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/buxoro.html', context)

def namangan(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Namangan) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/namangan.html', context)

def navoiy(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Navoiy) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/navoiy.html', context)

def qoraqolpoq(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Qoraqolpoq) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }

    return render(request, 'regions/qoraqolpoq.html', context)

def samarqand(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.ToshkentV) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/samarqand.html', context)

def sirdaryo(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Sirdaryo) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/sirdaryo.html', context)

def xorazm(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Xorazm) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/xorazm.html', context)

def surxondaryo(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Surxondaryo) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/surxondaryo.html', context)

def qashqadaryo(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Qashqadaryo) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/qashqadaryo.html', context)

def fargona(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Fargona) | Q(region=AboutTrees.Regions.Barchasi))

    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/fargona.html', context)

def jizzax(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.Jizzax) | Q(region=AboutTrees.Regions.Barchasi))
    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)

    context = {
        "treesList": treeList
    }
    return render(request, 'regions/jizzax.html', context)

def toshshahar(request):
    objects = AboutTrees.objects.filter(Q(region=AboutTrees.Regions.ToshkentSH) | Q(region=AboutTrees.Regions.Barchasi))
    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)


    context = {
        "treesList": treeList
    }
    return render(request, 'regions/toshshahar.html', context)


def respublika(request):

    objects = AboutTrees.objects.all()
    paginator = Paginator(objects, 4)

    page_number = request.GET.get("page")
    treeList = paginator.get_page(page_number)


    context = {
        "treesList": treeList
    }
    return render(request, 'regions/respublika.html', context)

