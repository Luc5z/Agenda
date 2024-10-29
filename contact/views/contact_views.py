from django.shortcuts import render
from contact.models import Contact
from django.views.generic import ListView, DetailView

class ContactListView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        return Contact.objects.filter(show=True).order_by('-id')


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact.html'
    context_object_name = 'contact'
