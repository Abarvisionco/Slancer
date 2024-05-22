from django import forms
from chat.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control border-0 p-3 shadow-none right text_right'
            self.fields[field].widget.attrs['placeholder'] = "پیغام شما"
            self.fields[field].widget.attrs['rows'] = '2'
            self.fields[field].widget.attrs['dir'] = 'auto'