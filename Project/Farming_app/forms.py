from django import forms
from .models import signup_model, retailer_model, farmercomplain_model, farmertips_model, feedback_model,contactus_model


class signup_form (forms.ModelForm):

    class Meta:

        model = signup_model
        fields = '__all__'


class update_form (forms.ModelForm):

    class Meta:

        model = signup_model
        fields = [ 'firstname', 'lastname', 'username',
                  'password', 'number', 'city', 'state', 'pincode']


class retailer_form (forms.ModelForm):

    class Meta:

        model = retailer_model
        fields = '__all__'


class editpost_delete_form (forms.ModelForm):

    class Meta:

        model = retailer_model
        fields = ['option', 'crop_name', 'crop_file',
                  'crop_about', 'crop_quantity', 'confirmation']


class farmercomplaint_form (forms.ModelForm):

    class Meta:

        model = farmercomplain_model
        fields = '__all__'


class farmer_accept_form (forms.ModelForm):

    class Meta:

        model = farmercomplain_model
        fields = ['confirmation']


class farmertips_form (forms.ModelForm):

    class Meta:

        model = farmertips_model
        fields = '__all__'


class feedback_form (forms.ModelForm):

    class Meta:

        model = feedback_model
        fields = '__all__'


class contactus_form (forms.ModelForm):

    class Meta:

        model = contactus_model
        fields = '__all__'
