from django.contrib import admin
from .models import Host,Trainers,Courses,Trainerslogin,Enquiry,Attendence
# Register your models here.


class TrainersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Trainers,TrainersAdmin)


class HostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Host,HostAdmin)


class CoursesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Courses,CoursesAdmin)


@admin.register(Trainerslogin)
class TrainersloginAdmin(admin.ModelAdmin):
    pass


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    pass