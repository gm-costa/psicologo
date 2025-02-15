from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from pacientes.models import Paciente

def pacientes(request):
    template_name = 'pacientes.html'
    pacientes_list = Paciente.objects.all()

    context = {'queixas': Paciente.queixa_choices, 'pacientes': pacientes_list}

    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, messages.WARNING, 'Nome e foto são obrigatórios!')
            return redirect('pacientes')

        paciente = Paciente(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )
        try:
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Paciente cadastrado com sucesso.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Erro: {e}.')

        return redirect('pacientes')

    else:
        return render(request, template_name, context)

def paciente_view(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == "GET":
        return render(request, 'paciente.html', {'paciente': paciente})

def atualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    try:
        paciente.save()
        messages.add_message(request, messages.SUCCESS, 'Status atualizado com sucesso.')
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Erro: {e}.')
    return redirect(f'/pacientes/{id}')