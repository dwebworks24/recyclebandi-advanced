from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.xlsx', '.xls')):
            raise forms.ValidationError("Only Excel files are allowed.")
        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError("File size must be under 5MB.")
        return file
