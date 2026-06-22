# from django.shortcuts import render, get_list_or_404
# from django.http import HttpResponse

# # Create your views here.
# def members(request):
#     return HttpResponse('<h1>Hello Django!</h1>')



# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())



from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers =Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id): 
  mymember = Member.objects.get(id=id) 
  template = loader.get_template('details.html') 
  context = { 
   'mymember': mymember, 
  } 
  return HttpResponse(template.render(context, request))

def main(request): 
    template = loader.get_template('main.html') 
    return HttpResponse(template.render()) 


# def testing(request): 
#     template = loader.get_template('template.html') 
#     context = { 
#         'fruits': ['Apple', 'Banana', 'Cherry'], 
#     } 
#     return HttpResponse(template.render(context, request))


# def testing(request): 
#     template = loader.get_template('template.html') 
#     context = { 
#         'firstname': 'Linus',
#     } 
#     return HttpResponse(template.render(context, request))



def testing(request): 
    mymembers = Member.objects.all().values() 
    template = loader.get_template('template.html') 
    context = { 
        'mymembers': mymembers, 
        } 
    return HttpResponse(template.render(context, request))

