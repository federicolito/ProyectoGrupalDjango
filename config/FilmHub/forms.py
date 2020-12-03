from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.http import request

class UserForm(ModelForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

    fields = ['basic_field']
'''class SubGroupForm(ModelForm):
    devices = Device.objects.all()

    devices_with_subgroup = forms.ModelMultipleChoiceField(devices)
    devices_without_subgroup = forms.ModelMultipleChoiceField(devices)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        instance = kwargs.get("instance")
        devices = Device.objects.filter(group=instance.group.pk)
        if instance:
            devices =  devices.filter(sub_group__isnull=True)
        self.fields['devices_without_subgroup'].queryset  = devices
        self.fields['devices_without_subgroup'].required = False
        subgroups = SubGroup.objects.filter(group=instance.group.pk)
        devices = Device.objects.filter(device_name="cacacaca")
        for subgroup in subgroups:
            devices_with = Device.objects.filter(sub_group=subgroup)
            devices_with = devices_with.exclude(sub_group__isnull=True)
            devices = ( devices | devices_with )
        if (len(subgroups) == 0):
            devices = Device.objects.filter(device_name="cacacaca")
        self.fields['devices_with_subgroup'].queryset  = devices
        self.fields['devices_with_subgroup'].required = False
        

            
        
        
        
            

            # if we're using this form to edit a post instance, we'll do this
        
    
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = SubGroup
        fields = ['sub_group_name','devices_without_subgroup','devices_with_subgroup']'''




        
class CreateUserForm(UserCreationForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True

class ComboComidaForm(ModelForm):
    #last_name = forms.CharField(blank=False)
    #first_name = forms.CharField(blank=False)
    class Meta:
        model = Combo_Comida
        fields = ['comida','cant_comida','bebida','cant_bebida']
    def __init__(self, *args, **kwargs):
        super(ComboComidaForm, self).__init__(*args, **kwargs)
        self.fields['comida'].required = False
        self.fields['bebida'].required = False

    fields = ['basic_field']