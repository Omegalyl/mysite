from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Project, ProjectCategory, ProjectSeries
from .forms import NewUserForm
# Create your views here.

def slug(request, single_slug):
    categories = [c.slug for c in ProjectCategory.objects.all()]
    if single_slug in categories:
        macthing_series = ProjectSeries.objects.filter(category__slug=single_slug)

        series_urls={}
        for m in macthing_series.all():
            p_one = Project.objects.filter(project_series__series=m.series).earliest("project_published")
            series_urls[m] =p_one.project_slug

        return render(
            request,
            "main/category.html",
            {"p_ones": series_urls}
        )
    
    projects_slug = [p.project_slug for p in Project.objects.all()]
    if single_slug in projects_slug:
        this_project = Project.objects.get(project_slug=single_slug)
        project_from_series = Project.objects.filter(project_series__series=this_project.project_series).order_by('project_published')

        this_project_idx = list(project_from_series).index(this_project)
        return render(
            request,
            "main/project.html",
            {'project': this_project,
             'sidebar': project_from_series,
             'this_project_idx': this_project_idx
            },
        )

    return HttpResponse(f"{single_slug} does not correspond to anything.")


def homepage(request):
    return render(
        request=request,
        template_name="main/categories.html",
        context={"categories": ProjectCategory.objects.all},
    )


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request,
                f"Account Created: {username}"
            )
            login(request, user)
            messages.info(
                request,
                f"Your are now logged in as: {username}"
            )
            return redirect("/")
        else:
            for msg in form.error_messages:
                messages.error(
                    request,
                    f"{msg}: {form.error_messages[msg]}"
                )

    form = NewUserForm 
    return render(
        request,
        template_name="main/register.html",
        context={"form": form}
    )


def logout_request(request):
    logout(request)
    messages.info(
        request,
        "Logged out successfully!"
    )
    return redirect("/")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                request,
                f"Your are now logged in as: {username}"
                )
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm
    return render(
        request,
        "main/login.html",
        {"form": form}
    )