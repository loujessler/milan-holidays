from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        # fields = ['from_transfer','time_from', 'to_transfer','class_transport','passenger','children','return_transfer','children_passenger','name','email','comment']
        exclude = ["created","updated","paid","status"]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['from_transfer'].widget.attrs['placeholder'] = 'Откуда'
        self.fields['class_transport'].widget.attrs['class'] = 'form-control'
        self.fields['class_transport'].widget.attrs['value'] = '1'
        self.fields['to_transfer'].widget.attrs['placeholder'] = 'Куда'
        self.fields['class_transport'].widget.attrs['class'] = 'hidden'
        # self.fields['passenger'].widget.attrs['placeholder'] = 'Кол-во'

        self.fields['passenger'].widget.attrs['type'] = 'number'
        self.fields['passenger'].widget.attrs['step'] = '1'
        self.fields['passenger'].widget.attrs['min'] = '1'
        self.fields['passenger'].widget.attrs['max'] = '50'
        self.fields['passenger'].widget.attrs['value'] = '1'

        # self.fields['passenger'].widget.attrs['required'] = ''
        self.fields['children'].widget.attrs['onchange'] = 'showOrHide("id_children", "have_children_div");'
        self.fields['return_transfer'].widget.attrs['onchange'] = 'showOrHide("id_return_transfer", "return_transfer_div");'

        self.fields['children_passenger'].widget.attrs['type'] = 'number'
        self.fields['children_passenger'].widget.attrs['step'] = '1'
        self.fields['children_passenger'].widget.attrs['min'] = '0'
        self.fields['children_passenger'].widget.attrs['max'] = '50'
        self.fields['children_passenger'].widget.attrs['value'] = '0'

        self.fields['chair_small'].widget.attrs['type'] = 'number'
        self.fields['chair_small'].widget.attrs['step'] = '1'
        self.fields['chair_small'].widget.attrs['min'] = '0'
        self.fields['chair_small'].widget.attrs['max'] = '50'
        self.fields['chair_small'].widget.attrs['value'] = '0'

        self.fields['chair_middle'].widget.attrs['type'] = 'number'
        self.fields['chair_middle'].widget.attrs['step'] = '1'
        self.fields['chair_middle'].widget.attrs['min'] = '0'
        self.fields['chair_middle'].widget.attrs['max'] = '50'
        self.fields['chair_middle'].widget.attrs['value'] = '0'

        self.fields['chair_large'].widget.attrs['type'] = 'number'
        self.fields['chair_large'].widget.attrs['step'] = '1'
        self.fields['chair_large'].widget.attrs['min'] = '0'
        self.fields['chair_large'].widget.attrs['max'] = '50'
        self.fields['chair_large'].widget.attrs['value'] = '0'

        self.fields['name'].widget.attrs['placeholder'] = 'Имя и фамилия*'
        self.fields['email'].widget.attrs['placeholder'] = 'Email*'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['phone'].widget.attrs['type'] = 'tel'
        self.fields['phone'].widget.attrs['placeholder'] = 'Телефон*  +7 (945) 123 45 67'
        self.fields['phone'].widget.attrs['class'] = 'input100'
        self.fields['comment'].widget.attrs['placeholder'] = 'Ваш комментарий...'
        self.fields['time_from'].widget.attrs['class'] = 'datepicker-here'
        # self.fields['time_from'].widget.attrs['type'] = 'date'readonly="readonly"
        self.fields['time_from'].widget.attrs['readonly'] = 'readonly'
        self.fields['time_from'].widget.attrs['data-timepicker'] = 'true'
        self.fields['time_from'].widget.attrs['autocomplete'] = 'off'
        self.fields['time_from'].widget.attrs['data-position'] = 'bottom center'
        self.fields['time_from'].widget.attrs['placeholder'] = 'Выбрать дату'
        self.fields['time_return_transfer'].widget.attrs['class'] = 'datepicker-here'
        # self.fields['time_return_transfer'].widget.attrs['type'] = 'date'
        self.fields['time_return_transfer'].widget.attrs['readonly'] = 'readonly'
        self.fields['time_return_transfer'].widget.attrs['data-timepicker'] = 'true'
        self.fields['time_return_transfer'].widget.attrs['autocomplete'] = 'off'
        self.fields['time_return_transfer'].widget.attrs['data-position'] = 'top center'
        self.fields['time_return_transfer'].widget.attrs['placeholder'] = 'Выбрать дату'
        # time_from = forms.DateTimeField(required=False, widget=DateInput(attrs={'type': 'datetime-local'}),
        #                              initial=datetime.date.today(), localize=True)
