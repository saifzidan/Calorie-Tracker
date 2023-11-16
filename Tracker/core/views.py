from django.shortcuts import render, redirect
from .models import Calorie
from .forms import CalorieAdd
import requests


def get_calorie(food):
    api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(food)
    response = requests.get(
        api_url, headers={"X-Api-Key": "TnItmloaMSGYADu4sDTD2w==Q4HF2yhJl2oJ2Won"}
    )
    resp = response.json()
    if response.status_code == requests.codes.ok:
        print(response.text)
        return resp[0]["calories"]
    else:
        print("Error:", response.status_code, response.text)
        return 0


def index(request):
    ca = Calorie.objects.all()
    total = 0
    for c in ca:
        total = total + c.calories
    if request.method == "POST":
        form = CalorieAdd(request.POST)
        if form.is_valid:
            calorie = Calorie(
                food=form["food"].value(),
                calories=float(get_calorie(form["food"].value())),
            )
            total = total + float(get_calorie(form["food"].value()))
            calorie.save()
    else:
        form = CalorieAdd()
    context = {
        "form": form,
        "ca": ca,
        "total": total,
    }
    return render(request, "core/index.html", context)


def delete(request, pk):
    food = Calorie.objects.get(id=pk)
    if request.method == "POST":
        food.delete()
        redirect("core:index")
    return render(request, "core/delete.html")
