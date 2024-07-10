from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PatientProfile, DoctorProfile

class PatientSignUpForm(UserCreationForm):
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=10)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            patient_profile = PatientProfile(user=user,
                                             address_line1=self.cleaned_data.get('address_line1'),
                                             city=self.cleaned_data.get('city'),
                                             state=self.cleaned_data.get('state'),
                                             pincode=self.cleaned_data.get('pincode'),
                                             profile_picture=self.cleaned_data.get('profile_picture'))
            patient_profile.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=10)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            doctor_profile = DoctorProfile(user=user,
                                           address_line1=self.cleaned_data.get('address_line1'),
                                           city=self.cleaned_data.get('city'),
                                           state=self.cleaned_data.get('state'),
                                           pincode=self.cleaned_data.get('pincode'),
                                           profile_picture=self.cleaned_data.get('profile_picture'))
            doctor_profile.save()
        return user
