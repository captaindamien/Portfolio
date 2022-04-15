from django import forms
from portfolio.models import Portfolio
from crispy_forms.helper import FormHelper


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.field_class = 'mb-3'