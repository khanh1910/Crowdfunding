from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.Owner = kwargs.pop('Owner', None)
        self.RecentFund = kwargs.pop('RecentFund', 0)
        self.IsSuccessfull = kwargs.pop('IsSuccessfull', False)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        project = super().save(commit=False)
        project.Owner = self.Owner
        project.RecentFund = self.RecentFund
        project.IsSuccessfull = self.IsSuccessfull
        project.save()

    class Meta:
        model = Project
        fields = ["Title", "ShortDescribe", "Content" , "GoalFund",  "Location", "Price" ]#"Category", "Image", "Image_Content", ]
