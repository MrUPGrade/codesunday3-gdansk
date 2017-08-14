from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from datetime import datetime

from contacts.forms import ContactForm
from contacts.models import Contact


# Create your views here.

def index(request):
    now = str(datetime.now())
    c = {
        'data': now,
        'msg': 'Witaj swiecie !!!!!!',
    }
    return render(request, 'contacts/main.html', context=c)


def date(request):
    now = datetime.now()
    return HttpResponse(str(now))


def contact_list(request):
    cl = Contact.objects.all()
    a = {
        'lista_kontaktow': list(cl)
    }
    return render(request, 'contacts/contact_list.html', context=a)


def contact_add(request):
    if request.method == 'POST':
        # obsluga posta
        c = {'post': request.POST}
        return render(request, 'contacts/add.html', context=c)
    else:
        return render(request, 'contacts/add.html', context={})


def contact_add2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # zapisanie obiektu w bazie
            form.save()
            # przejscie do listy kotaktow
            return HttpResponseRedirect('/contacts/list')
        c = {'form': form}
        # obsluga posta gdy sa bledy
        return render(request, 'contacts/add2.html', context=c)
    else:
        form = ContactForm()
        c = {'form': form}
        return render(request, 'contacts/add2.html', context=c)
