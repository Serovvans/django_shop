from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, VersionForm
from catalog.utils import load_contacts_to_json
from catalog.models import Product, Feedback, Version
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current=True).first()
            if active_version:
                product.active_version_number = active_version.num_version
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_edit', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        product_pk = self.kwargs['pk']
        product = Product.objects.get(pk=product_pk)
        if formset.is_valid():
            formset.instance = self.object
            Version.objects.filter(product=product).exclude(pk=product_pk).update(is_current=False)
            formset.save()

        return super().form_valid(form)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        product_pk = self.kwargs['pk']
        product = Product.objects.get(pk=product_pk)
        form.instance.product = product
        Version.objects.filter(product=product).exclude(pk=product_pk).update(is_current=False)
        return super().form_valid(form)
