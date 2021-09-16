from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import HiddenInput

from .models import ShopUser
from django.core.exceptions import ValidationError


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''  # FIXME все равно показывает вспомогательные сообщения


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'date_birthday', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_date_birthday(self):
        import datetime
        data = str(self.cleaned_data['date_birthday'])
        today = datetime.datetime.now().date()
        # get date from data for python
        date_birth = datetime.date(*[int(i) for i in data.split('-')])
        if int((today - date_birth).days) < 365 * 18 + 4:  # FIXME неточное количество дней
            raise ValidationError("Вы слишком молоды!")
        return data


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'email', 'date_birthday', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()

    def clean_date_birthday(self):
        import datetime
        data = str(self.cleaned_data['date_birthday'])
        today = datetime.datetime.now().date()
        # get date from data for python
        date_birth = datetime.date(*[int(i) for i in data.split('-')])
        if int((today - date_birth).days) < 365 * 18 + 4:  # FIXME неточное количество дней
            raise ValidationError("Вы слишком молоды!")
        return data