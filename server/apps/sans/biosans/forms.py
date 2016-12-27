'''
Created on Jan 8, 2016
@author: rhf
'''
from django.forms import ModelForm
from django.forms import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, HTML, Div, Layout

from .models import BioSANSConfiguration, BioSANSReduction, BioSANSRegion

class ConfigurationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConfigurationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.layout.append(Submit('submit', 'Save'))
        self.helper.layout.append(Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()"))

    class Meta:
        model = BioSANSConfiguration
        exclude = ['user','instrument']

class ReductionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReductionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.render_required_fields = True
        # self.helper.layout = Layout(Submit('submit', 'Save'),
        #                      Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()"))
        self.helper.form_tag = False

    class Meta:
        model = BioSANSReduction
        exclude = ['user','instrument']


class RegionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.render_required_fields = True
        self.helper.layout = Layout(
            HTML('<div id="entries"></div>'),
            # Submit('submit', 'Save'),
            # Button('cancel', 'Cancel', css_class='btn-default', onclick="window.history.back()")
        )
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        
    class Meta:
        model = BioSANSRegion
        fields = '__all__'

 # New
RegionInlineFormSetCreate = inlineformset_factory(BioSANSReduction, BioSANSRegion, form=RegionForm, extra=3, can_delete=False)
# Edit
RegionInlineFormSetEdit = inlineformset_factory(BioSANSReduction, BioSANSRegion, form=RegionForm, extra=1, can_delete=True)