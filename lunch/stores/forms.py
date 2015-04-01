from django import forms
from .models import Store
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.models import inlineformset_factory
from .models import MenuItem

BaseMenuItemFormSet = inlineformset_factory(
  parent_model=Store, model=MenuItem, fields=('name', 'price'), extra=1,
)

class StoreForm(forms.ModelForm):

  class Meta:
    model = Store
    fields = ('name', 'notes',)

  def __init__(self, submit_title='Submit', *args, **kwargs):
    super(StoreForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', submit_title))
    # if submit_title:
    #     self.helper.add_input(Submit('submit', submit_title))

class MenuItemFormSet(BaseMenuItemFormSet):
  def __init__(self, *args, **kwargs):
    super(MenuItemFormSet, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_tag = False
    self.helper.disable_csrf = True