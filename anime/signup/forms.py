from django import forms

class SignupForm(forms.Form):
    email=forms.EmailField(label="Enter Your Email")
    name=forms.CharField(label="enter Your name",max_length=100)
    gender_choices=[
        ('male','MALE'),
        ('female','FEMALE'),
        ('transegender','TRANSGENDER'),
    ]
    gender=forms.CharField(widget=forms.RadioSelect(choices=gender_choices))
    dob=forms.DateField(widget=forms.DateInput())
    con_choices=[
        ('india','INDIA'),
        ('pakistan','PAKISTAN'),
        ('china','CHINA'),
    ]
    country=forms.ChoiceField(label='Select Your Country',choices=con_choices)
    password=forms.CharField(label="Enter Your password",widget=forms.PasswordInput())
