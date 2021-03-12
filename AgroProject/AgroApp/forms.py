from django import forms
from .  models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def save(self, commit=True, **kwargs):
        item = super().save(commit=False)
        item.Images = kwargs.get('images', [])
        # item.kelishilgan = kwargs.get('kelishilgan', False)
        if commit:
            item.save()
        return item