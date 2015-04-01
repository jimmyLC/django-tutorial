from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import StoreForm
from .models import Store
from .models import MenuItem
from django.core.urlresolvers import reverse
from events.forms import EventForm
from django.forms.models import inlineformset_factory
from .forms import MenuItemFormSet


def store_create(request):
  if request.method == 'POST':
    form = StoreForm(data=request.POST, submit_title='create')
    if form.is_valid():
      store = form.save(commit=False)
      if request.user.is_authenticated():
        store.owner = request.user
      store.save()
      return redirect(store.get_absolute_url())
  else:
      form = StoreForm(submit_title='create')
  return render(request, 'stores/store_create.html', {'form': form})

def store_update(request, pk):
  try:
    store = Store.objects.get(pk=pk)
  except Store.DoesNotExist:
    raise Http404
  if request.method == 'POST':
    form = StoreForm(data=request.POST, instance=store, submit_title='update')
    menu_item_formset = MenuItemFormSet(request.POST, instance=store)
    if form.is_valid() and menu_item_formset.is_valid():
      store = form.save()
      menu_item_formset.save()
      return redirect(store.get_absolute_url())
  else:
    form = StoreForm(instance=store, submit_title='update')
    form.helper.form_tag = False
    menu_item_formset = MenuItemFormSet(instance=store)
  return render(request, 'stores/store_update.html', {
    'form': form, 'store': store,
    'menu_item_formset': menu_item_formset,
    })

@login_required
# @require_http_methods(['POST', 'DELETE'])
def store_delete(request, pk):
  try:
    store = Store.objects.get(pk=pk)
  except Store.DoesNotExist:
    raise Http404
  if store.can_user_delete(request.user):
    store.delete()
    if request.is_ajax:
      return HttpResponse()
    return redirect('store_list')
  return HttpResponseForbidden()

def store_list(request):
  stores = Store.objects.all()
  return render(request, 'stores/store_list.html', {'stores': stores})

def store_detail(request, pk):
  try:
    store = Store.objects.get(pk=pk)
  except Store.DoesNotExist:
    raise Http404
  event_form = EventForm(initial={'store': store}, submit_title='create_event')
  event_form.helper.form_action = reverse('event_create')
  return render(request, 'stores/store_detail.html', {'store': store, 'event_form': event_form,})



