from django.shortcuts import render,redirect,get_object_or_404
from .models import Noticia
from .forms import NoticiaForm

def notibad_list(request):
	qs_noticia = Noticia.objects.all()
	return render(request,r'notibad\notibad_list.html',{'qs_noticia':qs_noticia})

def noticia_detail(request,pk):
	noticia = Noticia.objects.get(pk=pk)
	return render(request,r'notibad\noticia_detail.html',{'noticia':noticia})

def noticia_new(request):
	if request.method == 'POST':
		form = NoticiaForm(request.POST)
		if form.is_valid():
			noticia = form.save(commit=False)#para no guardar aun, indicando que vamos a agregar datos
			noticia.author = request.user
			noticia.save()
			return redirect(r'notibad.views.noticia_detail',pk=noticia.pk)
	else:
		form = NoticiaForm()
	return render(request,r'notibad\noticia_edit.html',{'form':form})

def noticia_edit(request,pk):
	noticia = get_object_or_404(Noticia,pk=pk)
	if request.method == 'POST':
		form = NoticiaForm(request.POST,instance=noticia)
		if form.is_valid():
			noticia = form.save(commit=False)#para no guardar aun, indicando que vamos a agregar datos
			noticia.author = request.user
			noticia.save()
			return redirect(r'notibad.views.noticia_detail',pk=noticia.pk)
	else:
		form = NoticiaForm(instance=noticia)
	return render(request,r'notibad\noticia_edit.html',{'form':form})


