from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('hostlogin',views.hostlogin,name='hostlogin'),

    # Course Section CRUD
    path('IT',views.IT,name='IT'),
    path('civil',views.civil,name='civil'),
    path('mech',views.mech,name='mech'),
    path('edit/<int:id>/<str:dept>',views.edit,name='edit'),
    path('delete/<int:id>/<str:dept>',views.delete,name='delete'),

    # Trainers 
    path('add_trainer',views.add_trainer,name='add_trainer'),
    path('edit_trainer/<int:id>',views.edit_trainer,name='edit_trainer'),
    path('delete_trainer/<int:id>',views.delete_trainer,name='delete_trainer'),
    path('back',views.host,name='host'),
    path('trainer_lgn/',views.trainer_lgn,name='trainer_lgn'),
    path('attendence/<str:department>',views.attendence,name='attendence'),
    path('add_attend/<int:id>',views.add_attend,name='add_attend'),


    # enquiry
    path('enquiry',views.enquiry,name='enquiry'),
    path('enroll/<int:id>',views.enroll,name='enroll'),

    # staff
    path('admsn_mang',views.admsn_mang,name='admsn_mang'),

    # students
    path('std_lgn',views.std_lgn,name='std_lgn'),
    path('upgrade',views.upgrade,name='upgrade'),
    path('upgrade_course/<str:department>/<str:email>',views.upgrade_course,name='upgrade_course'), 
    path('add_course/<int:id>/<str:email>',views.add_course,name='add_course'),
    path('dwn_atten/<str:email>',views.dwn_atten,name='dwn_atten'),

    # download Enquries CSV files
    path('down_all_enq',views.down_all_enq,name='down_all_enq'),
    path('down_tod_enq',views.down_tod_enq,name='down_tod_enq'),

    # ToDO app
    path('todo',views.todo,name='todo'),
    path('edit_todo/<int:id>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
]