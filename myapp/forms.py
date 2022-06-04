from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICE = [
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ahmedavad','Ahmedavad'),
    ('Surat','Surat'),
    ('Banglore','Banglore'),
    ('Mumbai','Mumbai')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Location',choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['id', 'name', 'dob', 'gender','locality','city','pin','state',
    'mobile','job_city','profile_image','my_file']
        labels = {'name':'Full Name','dob':'Date Of Birth','pin':'Pin Code',
        'mobile':'Mobile No','email':'Email Id','profile_image':'Profile Image','my_file':'Document'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }