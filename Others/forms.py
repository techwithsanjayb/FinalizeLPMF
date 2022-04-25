from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  ,UserChangeForm
from .models import Category , SuccessStoriesCategory


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class UserProfileForm(forms.ModelForm):
    
#     class Meta:
#         model = UserProfile
#         field = "__all__"
#         exclude = ['userprofile_uid']

class EditUserProfileForm(UserChangeForm):
    
    password = None
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}

class EditAdminProfileForm(UserChangeForm):
    
    password = None
    class Meta:
        model = User
        fields= '__all__'
    

class CategoryDisplayForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class SuccessStoriesCategoryDisplayForm(forms.ModelForm):

    class Meta:
        model = SuccessStoriesCategory
        fields = "__all__"



class ContactForm(forms.Form):
    BUG = 'b'
    FEEDBACK = 'fb'
    NEW_FEATURE = 'nf'
    OTHER = 'o'
    purpose_choices = (
        (FEEDBACK, 'Feedback'),
        (NEW_FEATURE, 'Feature Request'),
        (BUG, 'Bug'),
        (OTHER, 'Other'),
    )

    name = forms.CharField()
    email = forms.EmailField()
    purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))