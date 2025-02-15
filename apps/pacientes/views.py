from django.shortcuts import redirect, render
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
        paciente.save()

        messages.add_message(request, messages.SUCCESS, 'Paciente cadastrado com sucesso.')
        return redirect('pacientes')

    else:
        return render(request, template_name, context)
