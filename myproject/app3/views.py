from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def home(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    return render(request, 'app3/home.html', {
        'contacts': contacts,
        'form': form,
    })


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تمت إضافة جهة الاتصال بنجاح إلى قاعدة البيانات!')
    return redirect('app3:home')


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث بيانات جهة الاتصال "{contact.name}" بنجاح!')
            return redirect('app3:home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'app3/edit.html', {
        'form': form,
        'contact': contact,
    })


def delete_contact(request, contact_id):
    if request.method == 'POST':
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        messages.success(request, f'تم حذف جهة الاتصال "{contact.name}" بنجاح!')
    return redirect('app3:home')
