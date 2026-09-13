from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import portfolio_home

from main.views import (
    home,
    profile,
    complete_task,
    delete_task,
    edit_task,
    update_priority,
)

from accounts.views import (
    register,
    user_login,
    user_logout,
    change_password,
)


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    # ================= DASHBOARD =================

    path(
        '',
        home,
        name='home'
    ),

    # ================= REGISTER =================

    path(
        'register/',
        register,
        name='register'
    ),

    # ================= LOGIN =================

    path(
        'login/',
        user_login,
        name='login'
    ),

    # ================= LOGOUT =================

    path(
        'logout/',
        user_logout,
        name='logout'
    ),

    # ================= PROFILE =================

    path(
        'profile/',
        profile,
        name='profile'
    ),

    # ================= CHANGE PASSWORD =================

    path(
        'change-password/',
        change_password,
        name='change_password'
    ),

    # ================= COMPLETE / UNDO =================

    path(
        'complete/<int:task_id>/',
        complete_task,
        name='complete_task'
    ),

    # ================= DELETE =================

    path(
        'delete/<int:task_id>/',
        delete_task,
        name='delete_task'
    ),

    # ================= EDIT =================

    path(
        'edit/<int:task_id>/',
        edit_task,
        name='edit_task'
    ),
    
    path(
    'portfolio/',
    portfolio_home,
    name='portfolio'
),

    # ================= UPDATE PRIORITY =================

    path(
        'update-priority/<int:task_id>/',
        update_priority,
        name='update_priority'
    ),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)