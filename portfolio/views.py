from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def portfolio_home(request):

    profile = request.user.profile

    return render(
        request,
        "portfolio.html",
        {
            "profile": profile,
            "user": request.user,
        }
    )