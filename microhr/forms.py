from django import forms

from microhr.models import Work
from accounts.models import WorkerProfile


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title', 'salary_min', 'salary_max', 'text')
        
    title = forms.CharField(
        label='求人タイトル',
        max_length=128,
        required=True,
        help_text='必須',
    )
    salary_min = forms.IntegerField(
        label='給与下限(万円)',
        required=True,
        min_value=13,
        help_text='必須',
        )
    salary_max = forms.IntegerField(
        label='給与上限(万円)',
        required=True,
        help_text='必須',
        )        
    text = forms.CharField(
        label='委細',
        widget=forms.Textarea,
        required=False,
        help_text='*任意',
    )

class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ('resume', 'self_pr',)
        labels = {
            'resume': '経歴',
            'self_pr': '自己PR',
        }
