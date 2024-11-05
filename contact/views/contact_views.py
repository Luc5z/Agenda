from django.shortcuts import render, get_object_or_404
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

    def get_object(self):
        contact_id = self.kwargs.get('pk')
        single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
        self.site_title = f'{single_contact.first_name} {single_contact.last_name} - '
        return single_contact


