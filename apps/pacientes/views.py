from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from pacientes.models import Consulta, Paciente, Tarefa

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
    tarefas = Tarefa.objects.all()
    consultas = Consulta.objects.filter(paciente=paciente)
    context = {
        'paciente': paciente, 
        'tarefas': tarefas,
        'consultas': consultas,
    }

    if request.method == "POST":
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')

        if not all([humor, registro_geral, video, tarefas]):
            messages.add_message(request, messages.WARNING, 'Preencha todos os campos.')
            return redirect(f'/pacientes/{id}')

        consulta = Consulta(
            humor=int(humor),
            registro_geral=registro_geral,
            video=video,
            paciente=paciente
        )

        try:
            consulta.save()

            for i in tarefas:
                tarefa = Tarefa.objects.get(id=i)
                consulta.tarefas.add(tarefa)

            consulta.save()
            messages.add_message(request, messages.SUCCESS, 'Registro de consulta adicionado com sucesso.')

        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Erro: {e}.')

        return redirect(f'/pacientes/{id}')
    
    else:
        return render(request, 'paciente.html', context)

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
