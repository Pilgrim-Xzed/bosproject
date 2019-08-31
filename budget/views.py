from django.shortcuts import render

# Create your views here.
from .models import Setting, Document, Work, Publication, Category, Year


def index(request):
    settings = Setting.objects.get(active=True)
    budget2019 =Document.objects.filter(doc_year = 1).order_by('-id')[:3:1]
    budget2018 =Document.objects.filter(doc_year = 2).order_by('-id')[:3:1]
    budget2017 =Document.objects.filter(doc_year = 3).order_by('-id')[:3:1]
    governor_speech = Document.objects.get(governors_speech = True)
    categories =  Category.objects.all()
    works = Work.objects.all()
    years = Year.objects.all()
    context={
        "settings":settings,
        "budget2019":budget2019,
        "budget2018":budget2018,
        "budget2017":budget2017,
        "g_speech":governor_speech,
        "categories":categories,
        "works":works,
        "years":years
    }
    return render(request,'home.html',context)


def documents(request):
    documents =Document.objects.all()
    settings = Setting.objects.get(category_id="1")
    categories =  Category.objects.all()
    years = Year.objects.all()
    args = {
        "documents":documents,
        "categories":categories,
        "settings":settings,
        "years":years
    }

    return render(request,'documents.html',args)


def works(request):
    settings = Setting.objects.get(category_id="1")
    works = Work.objects.all()
    categories =  Category.objects.all()
    years = Year.objects.all()
    context = {
        "works":works,
        "categories":categories,
        "settings":settings,
        "years":years
    }

    return render(request,'works.html',context)


def publications(request):
     settings = Setting.objects.get(category_id="1")
     publications = Publication.objects.all()
     categories =  Category.objects.all()
     years = Year.objects.all()
     context = {
         "settings":settings,
         "categories":categories,
         "publications":publications,
         "years":years
     }

     return render(request,'publications.html',context)


def downloads(request,docid):
     settings = Setting.objects.get(category_id="1")
     document = Document.objects.get(id=docid)
     categories =  Category.objects.all()
     years = Year.objects.all()
     context = {
         "settings":settings,
         "categories":categories,
         "document":document,
         "years":years
     }

     return render(request,'download.html',context)
     



def budgetyr(request,year):
    documents =Document.objects.filter(doc_year = year)
    settings = Setting.objects.get(category_id="1")
    categories =  Category.objects.all()
    years = Year.objects.all()
    args = {
        "documents":documents,
        "categories":categories,
        "settings":settings,
        "years":years
    }

    return render(request,'budgetyr.html',args)
