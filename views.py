# pylint: skip-file
from django.shortcuts import Http404, HttpResponse, render
from .models import Url, generateCode

def home(request):
    return render(request, "index.html")

def createUrl(request):
    if request.method == "POST":
        url = request.POST['url']
        code = generateCode()
        new_url = Url(url=url, short_code=code)
        new_url.save()
        return HttpResponse(code)
    return Http404("Sorry!!")

def openUrl(request, code):
    url_obj = Url.objects.get(short_code=code)
    url = url_obj.url
    return render(request, "redirect.html", {'url': url})
