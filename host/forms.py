from django import forms
from .models import Courses,Trainers,Host,Attendence,ToDO

class Hostform(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Host
class CoursesForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Courses

class TrainersForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Trainers


class AttendenceForm(forms.ModelForm):
    class Meta:
        model = Attendence
        fields = "__all__"


class ToDoForms(forms.ModelForm):
    class Meta:
        model = ToDO
        fields = "__all__"