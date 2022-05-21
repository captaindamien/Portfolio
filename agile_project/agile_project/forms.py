from django import forms
from portfolio.models import Portfolio, Feedback
from crispy_forms.helper import FormHelper

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = (
        'text',
        )

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.field_class = 'mb-3'

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
                    'career': forms.Select,
                    'experience': forms.Select
                }

    
    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.field_class = 'mb-3'