from django.urls import path, include
from acheve_mgt import views
# from acheve_mgt.views import StudentListView


app_name = 'acheve_mgt'

urlpatterns = [
    path('person/<int:pk>/', views.person, name='person'),
    path('person_data/<int:pk>/', views.person_data, name='person_data'),
    path('single_course/', views.view_course, name='view_course'),
    path('single_course/<int:pk>', views.single_course, name='single_course'),
    path('score_together/', views.score_together, name='score_together'),
    path('score_rating/', views.score_rating, name='score_rating'),
]