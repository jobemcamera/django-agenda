from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    # get o name do input 'q' e strip remove os espaços vazios
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    # Q permite que a consulta seja com OR
    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value)).order_by('-id')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    # single_contact = get_object_or_404(Contact.filter(pk=contact_id).first())
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
