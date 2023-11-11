from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, VersionForm
from catalog.utils import load_contacts_to_json
from catalog.models import Product, Feedback, Version
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class ProductListView(ListView):
    model = Product


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save
            load_contacts_to_json(feedback.name, feedback.phone, feedback.message)

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:list")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_edit', args=[self.kwargs.get(['pk'])])

    def get_contex_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        contex_data['formset'] = formset
        return contex_data

    def form_valid(self, form):
        contex_data = self.get_contex_data()
        formset = contex_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)
