from django.urls import path

from microhr.views import company, worker


urlpatterns = [
    path('new/', company.work_new, name='work_new'),
    path('<int:work_id>/', company.work_detail, name='work_detail'),
    path('<int:work_id>/edit', company.work_edit, name='work_edit'),
    path('<int:work_id>/delete', company.work_delete, name="work_delete"),

    path('<int:work_id>/apply', worker.apply, name="work_apply"),
    path('applied_items/', worker.applied_items, name='applied_items'),
    path('select/', company.check_application, name='check_application'),
    path('<int:application_id>/detail', company.application_detail, name='application_detail'),
    path('favorite/', worker.favorite, name="favorite"),
    path('favorite/<int:favorite_id>/', worker.favorite_delete, name='favorite_delete'),
]
