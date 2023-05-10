from django import forms
from web import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号',validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机号格式错误'),])
    password = forms.CharField(label='密 码',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    code = forms.CharField(label='验证码')
    class Meta:
        model = models.UserInfo
        fields = '__all__'

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入'+field.label