from django import forms
from .models import Store
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
