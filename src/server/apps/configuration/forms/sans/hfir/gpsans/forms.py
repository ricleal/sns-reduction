from django.forms import ModelForm

from server.apps.configuration.models.sans.hfir.biosans import Configuration
from server.apps.configuration.forms import abstract


class ConfigurationForm(abstract.ConfigurationForm, ModelForm):
    class Meta(ConfigurationForm.Meta):
        model = Configuration
