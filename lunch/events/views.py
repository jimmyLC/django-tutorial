from django.views.generic import CreateView, DetailView
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from .models import Event
from .forms import EventForm
from .forms import OrderForm
from braces.views import LoginRequiredMixin

class EventCreateView(LoginRequiredMixin, CreateView):
  form_class = EventForm
  model = Event
  http_method_names = ('post',)

class EventDetailView(LoginRequiredMixin, DetailView):
  model = Event

  def post(self, request, *args, **kwargs):
    form = OrderForm(request.POST)
    if not form.is_valid():
      return HttpResponseBadRequest()
    order  = form.save(commit=False)
    order.event = self.get_object()
    order.save()
    return redirect(order.event.get_absolute_url())

  def get_context_data(self, **kwargs):
    data = super(EventDetailView, self).get_context_data(**kwargs)
    order_form = OrderForm()
    order_form.fields['item'].queryset = self.object.store.menu_items.all()
    data['order_form'] = order_form
    return data