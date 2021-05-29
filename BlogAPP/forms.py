from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Category
from ckeditor.fields import RichTextField

# getting Choises data form Categorys model....
choices = Category.objects.all().values_list('Category_Field','Category_Field')

# made a empty strings for collect the choises....
choice_list = []
# using loop we fetch data in choise_list to sow-up on html POST-creation page.
for i in choices:
  choice_list.append(i)



# post CreationFORM
class InstructionFORMS(forms.Form):
  TitleF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  DetailsF= forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  CategoryF= forms.ChoiceField(choices=choices, 
    widget= forms.Select(attrs={
      'class':'form-control',
      'id'   :'title',      
    }))

  Images= forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'placeholder': 'Thumbnail',
      'type':'file', 
      'id' : 'files',  
      'multiple': True
    }))



# category Form
class categoryFORMS(forms.Form):
  category = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
    }))



# Comment form
class commentFORMS(forms.Form):
  CommentF = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control'
    }))



class profileFORMS(forms.Form):
  panF = forms.CharField(max_length=10,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  adharF= forms.CharField(max_length=16,
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  mobileF= forms.CharField(max_length=10,
    widget= forms.TextInput(attrs={
      'type' :'text', 
      'class':'form-control',
      'id'   :'title'
    }))

  instaF = forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  fbF = forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))


  inF = forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))


  photoF= forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'type':'file', 
      'id' : 'files',  
      'multiple': True
    }))


  aboutUF= forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))




# sign-up form based class based view 
class SignupFORMS(UserCreationForm):
  email = forms.EmailField(
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  first_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  last_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  #For Attribute ordering
  class Meta:
    model = User
    fields = ('username','email','first_name','last_name','password1','password2')

  #For user-name and password designing
  def __init__(self, *args, **kwargs):
    super(SignupFORMS,self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control' 
    self.fields['password1'].widget.attrs['class'] = 'form-control' 
    self.fields['password2'].widget.attrs['class'] = 'form-control' 






