from django import forms
from .models import CustomUser, LoginForm, Feedback




# class SignupForm(UserCreationForm):
#   username = forms.CharField(max_length=30, min_length=8)
#   email = forms.EmailField(max_length=40, min_length=6, help_text='Required')
#   agree_terms = forms.BooleanField()



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['login', 'password']




class FeedbackCreateForm(forms.ModelForm):
    """
    Форма отправки обратной связи
    """

    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'content')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})