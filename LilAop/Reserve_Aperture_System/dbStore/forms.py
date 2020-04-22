from django import forms
from management.models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name', 'store_pic', 'branch', 'phone', 'cost_total', 'repaired', 'other_notes', )