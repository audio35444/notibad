from django.shortcuts import render
from .models import Noticia

def notibad_list(request):
	qs_noticia = Noticia.objects.all()
	return render(request,r'notibad\notibad_list.html',{'qs_noticia':qs_noticia})

def noticia_detail(request,pk):
	noticia = Noticia.objects.get(pk=pk)
	return render(request,r'notibad\noticia_detail.html',{'noticia':noticia})
