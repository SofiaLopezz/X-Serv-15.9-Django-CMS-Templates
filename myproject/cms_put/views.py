from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.


@csrf_exempt
def index(request, peticion):

	if request.method == "POST":
		recurso = request.POST['name']
		contenido = request.POST['page']
		p = Pages(name=recurso, page=contenido)
		p.save() 

	try:
		requerimiento = Pages.objects.get(name=peticion)
		Response = "I am the page " + requerimiento.name + " y mi descripcion es " + requerimiento.page
		template = get_template('Simple_Beauty/index.html')
		c = Context({'name': recurso, 'content': contenido})
		renderizado = template.render(c)
		return HttpResponse(renderizado)

	except Pages.DoesNotExist:
		Response = "The page does not exist. Please, create it" 
		Response += '<form action"" method="POST">'
		Response += '<br>' + 'Name: <input type="text" name="name">' + '<br>' + '<br>'
		Response += 'Description: <input type="text" name="page">' + '<br>' + '<br>'
		Response += '<input type="submit" value="Enviar">' 
		return HttpResponse(Response)