from django.contrib import messages
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.widgets import NumberInput

from django import forms
from django.http import Http404
from django.shortcuts import redirect
from django.utils import timezone

from upload.models import Upload, UploadResult


class UserUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'mealtimes','created_at']

        widgets = {
            "image": forms.ClearableFileInput(attrs={'id':'default-btn','hidden':''}),
            "mealtimes": forms.Select(choices=Upload.MEALTIME_CHOICE, attrs={'class': 'form-select'}),
            "created_at": NumberInput(attrs={'type': 'date'}),
        }

        labels = {
            'image':'',
            'mealtimes':'',
            'created_at':'',
        }

    def clean(self):  # 요청파라미터 값들 조회
        cleaned_data = super().clean()  # dictionary 반환.
        mealtimes = cleaned_data.get('mealtimes')
        created_at = cleaned_data.get('created_at')
        check_eaten = UploadResult.objects.filter(eaten_dt=created_at)\
            .select_related('upload_id').values_list('upload_id__mealtimes',flat=True)
        try:
            if mealtimes in check_eaten:
                if mealtimes == 1:
                    mealtimes = '아침'
                elif mealtimes == 2:
                    mealtimes = '점심'
                else:
                    mealtimes = '저녁'
                self.add_error('mealtimes',f'선택하신 날의 {mealtimes}은 등록이 되어있습니다 :) ')
        except:
            pass


class UserEatenForm(ModelForm):
    class Meta:
        model = UploadResult
        fields = ('eaten_dt',)
        widgets = {
            "eaten_dt": NumberInput(attrs={'type': 'date'})
        }
        labels = {
            'eaten_dt':'',
        }

SERVE = [
    ('','-----------'),
    (0.5, 0.5),
    (1, 1),
    (1.5, 1.5),
]

class ServedForm(forms.Form):
    food_served = forms.ChoiceField(choices=SERVE,
                                    label="",
                                    widget=forms.Select(attrs={'class':'form-select'}))


