from django.shortcuts import render
from django.core.mail import EmailMessage

from .forms import ContatoForm


def contato(request):
    send = False
    form = ContatoForm(request.POST or None)
    
    if form.is_valid():
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')

        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {} <{}>\n\nEscreveu:\n{}".format(nome, email, mensagem),
            "no-reply@inbox.mailtrap.io",
            ["rogliofabricio@gmail.com"],
            reply_to=[email]
        )

        try:
            email.send()
            send = True
        except: 
            send = False

    return render(request, 'contato/contato.html', {'form': form,
                                            'success': send})