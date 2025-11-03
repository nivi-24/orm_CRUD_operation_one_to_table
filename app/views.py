from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# inserting the data to  parent table(topic)
def insert_into_topic(request):
    tn=input("enter the topic:")
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    else:
        return HttpResponse("Topic is already present")
    
#display data into frontend for topic table
def display_topic(request):
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)

# retriveing the data from child table(webpage) by using get method 
def insert_into_webpage(request):
    tn=input("enter the topic:")
    PTO=Topic.objects.get(topic_name=tn)
    na=input("enter the name:")
    ur=input("enter the url:")
    WTO=Webpage.objects.get_or_create(topic_name=PTO,name=na,url=ur)
    if WTO:
        QLWO=Webpage.objects.all()
        d={'QLWO':QLWO}
        return render(request,'display_webpage.html',d)
    else:
         return HttpResponse("webpage is already present")

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name='hardhik')
    QLWO=Webpage.objects.exclude(name='rahul')
    QLWO=Webpage.objects.all()[::-1]
    QLWO=Webpage.objects.all()[:3:2]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(id__in=(3,4))
    QLWO=Webpage.objects.filter(id__range=(2,4))
    QLWO=Webpage.objects.filter(id__gte=3)
    QLWO=Webpage.objects.filter(id__gt=3)
    QLWO=Webpage.objects.filter(id__lt=4)
    QLWO=Webpage.objects.filter(name__startswith='r') 
    QLWO=Webpage.objects.filter(name__endswith='o')
    QLWO=Webpage.objects.filter(name__regex='^r')
    QLWO=Webpage.objects.filter(id__gt=3)
    QLWO=Webpage.objects.filter(id=2,topic_name='Cricket')
    QLWO=Webpage.objects.filter(Q(id=2)|Q(topic_name='Cricket'))

 
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

    
def update_webpage(request):
    #Webpage.objects.filter(name='hardhik').update(url='https://hardhik.com')
    #Webpage.objects.filter(name='rahul').update(url='https://son_of_dancing_mani.com')
    TTO=Topic.objects.get(topic_name='Cricket')
    Webpage.objects.update_or_create(name='loosecutie' ,defaults={'topic_name':TTO,'url':'https://im_rahul.com'})
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)    
# insert the data to child table(webpage) by using filter method D
def insert_into_webpage_filter(request):
    tn=input("Enter the topic:")
    PTO=Topic.objects.filter(topic_name=tn)
   
    if PTO:
        TO=PTO[0]
        na=input("Enter the name:")
        url=input("Enter the url:")
        WTO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url)
        if WTO:
            return HttpResponse('webpage is created..')
        else:
            return HttpResponse("webpage is already present ")
    else:
        return HttpResponse("webpage is not available...")

# inserting the data to child table(access_record) by using filter method                        
def insert_into_access_record(request):
    wid=input("Enter the id:")
    LWTO=Webpage.objects.filter(id=wid)
    if LWTO:
        WO=LWTO[0]
        auth=input("enter the author:")
        date=input("enter the date:")
        ATO=Accessrecord.objects.get_or_create(name=WO,author=auth,date=date)
        if ATO:
            return HttpResponse('accessrecord is created..')
        else:
            return HttpResponse("accessrecord is already present.. ")
    else:
        return HttpResponse("page not available")
    

#display the accessrecord table
def display_access(request):
    QLAO=Accessrecord.objects.all()
    QLAO=Accessrecord.objects.filter(date__year=1980)
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)



    

#insertion using forms 

#insert into topic 
def insert_topic_form(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TTO=Topic.objects.get_or_create(topic_name=tn)
        if TTO[1]:
            return HttpResponse('topic created')
        else:
            return HttpResponse('topic already present')

    return render(request,'insert_topic_form.html')

#display_topic_form
def display_topic_form(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic_form.html',d)

#insert into webpage 
def insert_into_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn) 
        na=request.POST['na']
        ur=request.POST['ur']

        TWO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)
        if TWO[1]:
            return HttpResponse('webpage created')
        else:
            return HttpResponse('webpage already created')


    return render(request,'insert_into_webpage.html',d)

#display webpage 

def display_webpage_form(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage_form.html',d)

#insert into accessrecord
def insert_into_access_record_form(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}

    if request.method=='POST':
        na=request.POST['na']
        WO=Webpage.objects.get(pk=na)
        au=request.POST['au']
        da=request.POST['da']
        TAO=Accessrecord.objects.get_or_create(name=WO,author=au,date=da)
        if TAO[1]:
              QLWO=Webpage.objects.all()
              d={'QLWO':QLWO}
              return render(request,'display_access_form.html',d)
        else:
            return HttpResponse('accessrecord already present')
    
    return render(request,'insert_into_access_record_form.html',d)

def display_access_form(request):
    QLAO=Accessrecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_access_form.html',d)

def select_multiple_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method=='POST':
        STL=request.POST.getlist('tn')
        EWQS=Webpage.objects.none()
        
        for TO in STL:
            EWQS=EWQS|Webpage.objects.filter(topic_name=TO)
        d1={'EWQS':EWQS}
        return render (request,'display_webpage_form.html',d1)


    return render(request,'select_multiple_topic.html',d)

