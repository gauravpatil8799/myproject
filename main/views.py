from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Task, Profile


@login_required(login_url="login")
def home(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        # Profile photo upload
        if request.FILES.get("photo"):

            profile.photo = request.FILES["photo"]
            profile.save()

            return redirect("home")

        # Add Task
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority", "medium")

        if title:

            Task.objects.create(
                user=request.user,
                title=title,
                due_date=due_date if due_date else None,
                priority=priority
            )

        return redirect("home")

    tasks = Task.objects.filter(
        user=request.user
    )

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        completed=True
    ).count()

    pending_tasks = tasks.filter(
        completed=False
    ).count()

    return render(
        request,
        "home.html",
        {
            "tasks": tasks,
            "profile": profile,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
        }
    )


# =====================================================
# PROFILE PAGE
# =====================================================

@login_required(login_url="login")
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        profile.full_name = request.POST.get(
            "full_name", ""
        )

        joining_date = request.POST.get(
            "joining_date"
        )

        profile.joining_date = (
            joining_date
            if joining_date
            else None
        )

        profile.education = request.POST.get(
            "education", ""
        )

        profile.skills = request.POST.get(
            "skills", ""
        )

        profile.about_me = request.POST.get(
            "about_me", ""
        )

        profile.projects = request.POST.get(
            "projects", ""
        )

        profile.achievements = request.POST.get(
            "achievements", ""
        )

        profile.certifications = request.POST.get(
            "certifications", ""
        )

        if request.FILES.get("photo"):

            profile.photo = request.FILES["photo"]

        profile.save()

        return redirect("profile")

    return render(
        request,
        "profile.html",
        {
            "profile": profile
        }
    )


# =====================================================
# COMPLETE TASK
# =====================================================

@login_required(login_url="login")
def complete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.completed = not task.completed

    task.save()

    return redirect("home")


# =====================================================
# DELETE TASK
# =====================================================

@login_required(login_url="login")
def delete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect("home")


# =====================================================
# EDIT TASK
# =====================================================

@login_required(login_url="login")
def edit_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == "POST":

        title = request.POST.get("title")

        due_date = request.POST.get(
            "due_date"
        )

        priority = request.POST.get(
            "priority",
            task.priority
        )

        if title:

            task.title = title

            task.due_date = (
                due_date
                if due_date
                else None
            )

            task.priority = priority

            task.save()

            return redirect("home")

    return render(
        request,
        "edit.html",
        {
            "task": task
        }
    )


# =====================================================
# UPDATE PRIORITY
# =====================================================

@login_required(login_url="login")
def update_priority(request, task_id):

    if request.method == "POST":

        task = get_object_or_404(
            Task,
            id=task_id,
            user=request.user
        )

        priority = request.POST.get(
            "priority"
        )

        if priority in [
            "high",
            "medium",
            "low"
        ]:

            task.priority = priority

            task.save()

            return JsonResponse(
                {
                    "success": True,
                    "priority": task.priority
                }
            )

    return JsonResponse(
        {
            "success": False
        }
    )