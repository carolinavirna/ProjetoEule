# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .models import Questoes, Historico

from .models import Classificacao

from .forms import QuestoesForm


@login_required
def home(request):
	return render(request, 'apps/home.html')

@login_required
def inserir(request):
	if request.method == 'POST':
		form = QuestoesForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('http://127.0.0.1:8000')
	else:
		form = QuestoesForm()
		context = {
			'form': form,
		}
		return render(request, 'apps/inserir.html', context)

@login_required
def disciplinas(request):
	return render(request, 'apps/disciplinas.html')

@login_required
def perfil(request):
	return render(request, 'apps/perfil.html')

@login_required
def banco_de_questoes(request, cat):

	questoes = Questoes.objects.filter(id_class=0)
	
	if request.method == "POST":

		for q in request.POST:
			if q != 'csrfmiddlewaretoken':
				resp = request.POST[q]
				quest = Questoes.objects.get(id=q)

				hist = Historico(id_questao=quest, id_user=request.user, resposta=resp, acerto=False)
				hist.save()

		return redirect('/')
	else:
		classificacao = Classificacao.objects.filter(categoria=cat)

		

		for i in classificacao:
			var = i.id 
			if i==0:
				questoes = Questoes.objects.filter(id_class=var)
			else:
				q = Questoes.objects.filter(id_class=var)
				def unir(questoes, q):
					return (questoes | q)

				questoes = unir(questoes, q)

	context = {
		'questoes': questoes,
	}
	
	return render(request, 'apps/banco.html', context)	

# Create your views here.