from django import forms
from .models import Resume
from .import choice_state


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=choice_state.CHOICE_GENDER, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=choice_state.CHOICE_LOCATION, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'district', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        labels = {'naem':'Full name', 'dob':'Date of Birth', 'Locality':'Locality', 'city':'Ctiy', 'pin':'Pin Code/Zip', 'district':'District', 'mobile':'Mobile Number',
                  'email':'E-mail Address', 'profile_image':'Profile Image', 'my_file':'Document'  }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }