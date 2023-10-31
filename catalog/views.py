from django.urls import reverse_lazy

from catalog.utils import load_contacts_to_json
from catalog.models import Product, Feedback
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = Product


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save
            load_contacts_to_json(feedback.name, feedback.phone, feedback.message)

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
