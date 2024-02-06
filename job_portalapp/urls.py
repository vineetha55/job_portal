from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('admin_login/', views.admin_login),
    path("admin_login_check/" ,views.admin_login_check),
    path("adminhome/",views.adminhome),
    path("addvacancy/",views.addvacancy),
    path("save_vacancy_first/",views.save_vacancy_first),
    path("job_vacancy_second/<id>",views.job_vacancy_second,name="job_vacancy_second"),
    path("save_vacancy_second/<id>",views.save_vacancy_second,name="save_vacancy_second"),
    path("job_vacancy_fourth/<id>", views.job_vacancy_fourth,name="job_vacancy_fourth"),
    path("save_vacancy_fourth/<id>",views.save_vacancy_fourth),
    path("job_vacancy_fifth/<id>", views.job_vacancy_fifth,name="job_vacancy_fifth"),
    path("save_vacancy_fifth/<id>",views.save_vacancy_fifth),
    path("job_vacancy_sixth/<id>", views.job_vacancy_sixth,name="job_vacancy_sixth"),
    path("save_vacancy_sixth/<id>",views.save_vacancy_sixth),
    path("job_vacancy_seventh/<id>", views.job_vacancy_seventh,name="job_vacancy_seventh"),
    path("addcategory/",views.addcategory),
    path("save_category/",views.save_category),
    path("viewcategory/",views.viewcategory),

    path("save_company/",views.save_company),
    path("viewcompany/",views.viewcompany),
    path("cmp_more_info/<id>",views.cmp_more_info),
    path("view_req_cmp/",views.view_req_cmp),
    path("request_approval/<id>",views.request_approval),
    path("save_approval/<id>",views.save_approval),
    path("create_mock/",views.create_mock),
    path("save_mockqns/",views.save_mockqns),
    path("addcompany/",views.addcompany),


    ######################Company######################

    path("company_login/",views.company_login),
    path("company_request/",views.company_request),
    path("save_cmp_request/",views.save_cmp_request),

    path("company_login_check/",views.company_login_check),
    path("company_home/",views.company_home),
    path("viewvacancy/",views.viewvacancy),
    path("vacancy_more_info/<id>",views.vacancy_more_info),
    path("user_login/",views.user_login),
    path("user_register/",views.user_register),
    path("save_register/",views.save_register),
    path("user_login_check/",views.user_login_check),
    path("user_home/",views.user_home),
    path("user_view_jobs/",views.user_view_jobs),
    path("view_more_job_user/<id>",views.view_more_job_user),
    path("apply_job/<id>",views.apply_job),
    path("save_job_application/<id>",views.save_job_application),
    path("my_applications/",views.my_applications),
    path("user_mock/",views.user_mock),
    path("search_mock/",views.search_mock),
    path("save_mock_answers/",views.save_mock_answers),
    path("mock_result/",views.mock_result),
    path("view_applications/",views.view_applications),
    path("cmp_shortlist/<id>",views.cmp_shortlist),
    path("cmp_reject/<id>",views.cmp_reject),
    path("view_shortlisted/",views.view_shortlisted)

 ]