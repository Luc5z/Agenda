from django.urls import path
from contact.views import ContactListView, ContactDetailView

app_name = 'contact'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
]
