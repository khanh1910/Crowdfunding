
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            'invalid':'Tài khoản không hợp lệ', 
            'required': 'Vui lòng nhập tên',
            "unique": "Tài khoản đã tồn tại",
            })
    first_name = forms.CharField(error_messages={'invalid':'Tên không hợp lệ', 'required': 'Vui lòng nhập tên'})
    last_name = forms.CharField(error_messages={'invalid':'Họ không hợp lệ'})
    email = forms.EmailField(error_messages={'invalid':'Email không hợp lệ'})
    error_messages = {
            'password_mismatch': "Mật khẩu xác nhận không khớp",
        }
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

        # new_user = User.objects.create_user(username, email, password)
        # new_user.is_active = False
        # new_user.first_name = first_name
        # new_user.last_name = last_name
        # new_user.save()