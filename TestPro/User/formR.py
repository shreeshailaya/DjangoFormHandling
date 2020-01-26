from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'username',
                  )


'''
class RegForm(UserCreationForm):
     email=forms.EmailField (required=True)

    class Meta:
        model = User
        fields =('first_name',
            'last_name',
            'email',
            'password',
            'username',
        )

     def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
            return user


'''