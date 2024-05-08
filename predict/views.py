from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")



def Predict_crop(request):
    from joblib import load
    prediction=""
    # model = pickle.load(open("D:\Desktop\django-projects\crop_prediction\cropprediction\predict\model_saved.pkl", "rb"))
    model =load('cropprediction/predict/saved_model.joblib')
    
    if request.method=="POST":
        ip1=float(request.POST.get('nitrogen'))
        ip2=float(request.POST.get('phosphrous'))
        ip3=float(request.POST.get('potassium'))
        ip4=float(request.POST.get('ph'))
        ip5=float(request.POST.get('rainfall'))
        ip6=float(request.POST.get('temperature'))
        prediction= model.predict([[ip1,ip2,ip3,ip4,ip5,ip6]])[0]
    return render(request,"index.html",{"prediction":prediction})