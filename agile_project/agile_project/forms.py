from django import forms
from portfolio.models import Portfolio
from crispy_forms.helper import FormHelper

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = (
        'career',
        'about_me',
        'phone_number',
        'whatsapp',
        'telegram',
        'about_me',
        'project_links',
        'experience',
        'skills',
        'photo',
        'template',
        )
        widgets = {
                    'template': forms.RadioSelect,
                }
    
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.field_class = 'mb-3'