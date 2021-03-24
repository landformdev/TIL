from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUerChangeForm(UserChangeForm):
    class Meta:

        model = get_user_model()
        fields = ('email', 'first-name', 'last-name',)