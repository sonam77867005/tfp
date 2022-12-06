from django.shortcuts import render
from joblib import load
import pandas as pd
from .models import PredResults, Feedback
from django.contrib import messages


# from .models import PredResults

# Create your views here.
model = load("taxifarepredictionmodel.joblib")


def home(request):
    return render(request, 'home.html',)


def database(request):
    data = {"dataset": PredResults.objects.all()}
    return render(request, 'DB.html', data)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = str(request.POST['name'])
        email = str(request.POST['email'])
        message = str(request.POST['message'])
        Feedback.objects.create(name=name, email=email, message=message)
        messages.success(request,
                         'Your feedback has been successfully submitted.Thank you, and Have a nice day!!')
    return render(request, 'contact.html')


def taxi(request):
    return render(request, 'taxi.html')


def predict(request):
    return render(request, 'predict.html')


def result(request):
    if request.method == 'POST':
        from_source = str(request.POST['from_source'])
        to_destination = str(request.POST['to_destination'])
        distance = float(request.POST['distance'])
        fuel_price = float(request.POST['fuel_price'])
        fuel_consumption = float(request.POST['fuel_consumption'])

    prediction = pd.DataFrame(data=({"Distance(km)": [distance], "Fuel Price": [
                              fuel_price], "Fuel Consumption": [fuel_consumption]}), index=[0])

    result = model.predict(prediction)
    ans = {
        's': from_source,
        'to': to_destination,
        'dis': distance,
        'fp': fuel_price,
        'fc': fuel_consumption,
        'r': float(result[0])
    }
    PredResults.objects.create(from_source=from_source, to_destination=to_destination, distance=distance,
                               fuel_price=fuel_price, fuel_consumption=fuel_consumption, result=result[0])

    return render(request, 'result.html', ans)
