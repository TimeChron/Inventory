from django import forms
from .models import Store 

class WarehouseCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "store_code", "address", "city", "state", "pincode"]
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'store_code':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store Code'}),
            'address':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'pincode':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'})
        }
        labels = {
            "name":"",
            "store_code":"",
            "address":"",
            "city":"",
            "state":"",
            "pincode":"",
        }

    def save(self):
        warehouse = super().save(commit = False)
        if not warehouse.store_code:
            # Load the last object
            last_object = Store.objects.last()
            if last_object:
                # Load the last object code
                last_object_code = last_object.store_code
                code_constituent_list=last_object.split('-')
                next_code_number = int(code_constituent_list[-1]) + 1
            else:
                new_code_number = 1001
            store_code = 'WH-'+str(new_code_number)
            self.store_code = store_code
        warehouse.save()
