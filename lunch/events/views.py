from django.views.generic import CreateView, DetailView
from .models import Event
from .forms import EventForm

class EventCreateView(CreateView):
  form_class = EventForm
  model = Event

class EventDetailView(DetailView):
  model = Event