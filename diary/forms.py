from django import forms

from diary.models import Memory


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = "__all__"
