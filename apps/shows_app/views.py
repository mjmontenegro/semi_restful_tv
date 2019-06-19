from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Shows

# Create your views here.
def index(request):
    return redirect("/shows")


def shows(request):
    context = {
        "shows": Shows.objects.all()
    }
    return render(request, "shows_app/shows.html", context)


def new(request):
    return render(request, "shows_app/new.html")


def create(request):
    errors = Shows.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    new_show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect("/shows/" + str(new_show.id))


def show(request, num):
    context = {
        "show": Shows.objects.get(id=num)
    }
    return render(request, "shows_app/show.html", context)


def edit(request, num):
    show = Shows.objects.get(id=num)
    show.release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        "show": show,
    }
    return render(request, "shows_app/edit.html", context)


def destroy(request, num):
    Shows.objects.get(id=num).delete()
    return redirect("/shows")


def update(request, num):
    errors = Shows.objects.validate(request.POST)
    up = Shows.objects.get(id=num)
    if ('dup' in errors) and (up.title == request.POST['title']):
        del errors['dup']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{num}/edit')
    up.title = request.POST['title']
    up.network = request.POST['network']
    up.release_date = request.POST['release_date']
    up.description = request.POST['description']
    up.save()
    return redirect("/show/" + str(num))

def validate_name(request):
    errors = Shows.objects.validate(request.POST)
    if ('dup' in errors):
        output = "Title must be unique"
    else:
        output = ""
    return HttpResponse(output)

