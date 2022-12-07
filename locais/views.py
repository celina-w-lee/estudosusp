from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Local
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Local, Avaliacao
from .forms import LocalForm, RateForm
from django.contrib.auth.decorators import login_required

class LocalListView(generic.ListView):
    local = Local
    template_name = 'locais/index.html'

    def get_queryset(self):
        return Local.objects.order_by('id')

class LocalDetailView(generic.DetailView):
    local = Local
    template_name = 'locais/detail.html'

    def get_queryset(self):
        return Local.objects.all()

@login_required
def update_local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)

    if request.method == "POST":
        form = LocalForm(request.POST, request.FILES)
        if form.is_valid():
            local.nome = form.cleaned_data['nome']
            local.status = form.cleaned_data['status']
            local.tomada = form.cleaned_data['tomada']
            local.ruido = form.cleaned_data['ruido']
            local.coberto = form.cleaned_data['coberto']
            local.grupo = form.cleaned_data['grupo']
            local.permissoes = form.cleaned_data['permissoes']
            local.flexibilidade = form.cleaned_data['flexibilidade']
            local.imagem = form.cleaned_data['imagem']
            local.inicio_func = form.cleaned_data['inicio_func']
            local.fim_func = form.cleaned_data['fim_func']
            local.dias_func = form.cleaned_data['dias_func']
            local.save()
            return HttpResponseRedirect(
                reverse('locais:detail', args=(local.id, )))
    else:
        form = LocalForm(
            initial={
                'nome': local.nome,
                'status': local.status,
                'tomada': local.tomada,
                'ruido': local.ruido,
                'coberto': local.coberto,
                'grupo': local.grupo,
                'permissoes': local.permissoes,
                'flexibilidade': local.flexibilidade,
                'imagem': local.imagem,
                'inicio_func': local.inicio_func,
                'fim_func': local.fim_func,
                'dias_func': local.dias_func,
            })

    context = {'local': local, 'form': form}
    return render(request, 'locais/update.html', context)

@login_required
def rate_local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            avaliacao_local = form.cleaned_data['rating']
            avaliacao = Avaliacao(local=local,
                                rating = avaliacao_local)
            avaliacao.save()
            return HttpResponseRedirect(
                reverse('locais:detail', args=(local_id, )))
    else:
        form = RateForm()
    context = {'form': form, 'local': local}
    return render(request, 'locais/rate.html', context)
