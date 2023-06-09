from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Data
#user is table name

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pass1=request.POST['pass']
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login Successful")
            return render (request,'index.html')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html') 
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        username=request.POST['uname']
        last=request.POST['lname']
        mail=request.POST['email']
        p1=request.POST['pass']
        p2=request.POST['pass1']
        if p1==p2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exits")
                return render(request,'register.html')
        elif User.objects.filter(email=mail).exists():
            messages.info(request,"Email already exits")
            return render(request,'register.html')
        #create database connection for that create obj for db table
        user=User.objects.create_user(first_name=first,last_name=last,
             email=mail,password=p1,username=username)
        user.save()
        return redirect('login')
    else:
        # messages.info(request,"Password not matching")
        return render(request,'register.html')
    
def attrition(request):
     return render(request,'attrition.html') 
def attritionpredict(request):
        if (request.method == 'POST'):
            Age=request.POST['Age']
            BusinessTravel=request.POST['BusinessTravel']
            DailyRate=request.POST['DailyRate']
            Department=request.POST['Department']
            DistanceFromHome = request.POST['DistanceFromHome']
            Education=request.POST['Education']
            EducationField=request.POST['EducationField']
            EnvironmentSatisfaction=request.POST['EnvironmentSatisfaction']
            Gender=request.POST['Gender']
            HourlyRate= request.POST['HourlyRate']
            JobInvolvement=request.POST['JobInvolvement']
            JobLevel=request.POST['JobLevel']
            JobSatisfaction=request.POST['JobSatisfaction']
            MaritalStatus=request.POST['MaritalStatus']
            MonthlyIncome=request.POST['MonthlyIncome']
            MonthlyRate=request.POST['MonthlyRate']
            NumCompaniesWorked=request.POST['NumCompaniesWorked']
            OverTime=request.POST['OverTime']
            PercentSalaryHike=request.POST['PercentSalaryHike']
            PerformanceRating=request.POST['PerformanceRating']
            RelationshipSatisfaction=request.POST['RelationshipSatisfaction']
            StandardHours=request.POST['StandardHours']
            StockOptionLevel=request.POST['StockOptionLevel']
            TotalWorkingYears=request.POST['TotalWorkingYears']
            TrainingTimesLastYear=request.POST['TrainingTimesLastYear']
            WorkLifeBalance=request.POST['WorkLifeBalance']
            YearsAtCompany = request.POST['YearsAtCompany']
            YearsInCurrentRole=request.POST['YearsInCurrentRole']
            YearsSinceLastPromotion= request.POST['YearsSinceLastPromotion']
            YearsWithCurrManager= request.POST['YearsWithCurrManager']

            import pandas as pd;
            from sklearn.ensemble import RandomForestClassifier; 
            df = pd.read_csv(r"static/datasets/EmployeeData.csv")
            df.dropna(inplace=True)
            df.isnull().sum()
            # X=df.drop("Attrition",axis=1)
            # Y=df["Attrition"]
            X_train = df[['Age','BusinessTravel','DailyRate','Department','DistanceFromHome','Education','EducationField',
                         'EnvironmentSatisfaction','Gender','HourlyRate','JobInvolvement','JobLevel',
                          'JobSatisfaction','MaritalStatus','MonthlyIncome','MonthlyRate','NumCompaniesWorked','OverTime','PercentSalaryHike',
                          'PerformanceRating',
                          'RelationshipSatisfaction','StandardHours','StockOptionLevel','TotalWorkingYears',
                          'TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager']]
            y_train = df[['Attrition']]
            ran = RandomForestClassifier()
            ran.fit(X_train,y_train)
            prediction = ran.predict([[Age,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,
                                       
                                       EnvironmentSatisfaction,Gender,HourlyRate,JobInvolvement,JobLevel,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate
                                       ,NumCompaniesWorked,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,TotalWorkingYears,
                                       TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager]])
           #Storing user input prediction input data in DataBase
            data=Data.objects.create( Age=Age,BusinessTravel=BusinessTravel,DailyRate=DailyRate,Department=Department,DistanceFromHome=DistanceFromHome,Education=Education,
                  EducationField=EducationField,EnvironmentSatisfaction=EnvironmentSatisfaction,Gender=Gender,HourlyRate=HourlyRate,JobInvolvement=JobInvolvement,JobLevel=JobLevel,
                  JobSatisfaction=JobSatisfaction,MaritalStatus=MaritalStatus,MonthlyIncome=MonthlyIncome,MonthlyRate=MonthlyRate,NumCompaniesWorked=NumCompaniesWorked,
                  OverTime=OverTime,PercentSalaryHike=PercentSalaryHike,PerformanceRating=PerformanceRating,RelationshipSatisfaction=RelationshipSatisfaction,StandardHours=StandardHours,StockOptionLevel=StockOptionLevel,
                  TotalWorkingYears=TotalWorkingYears,TrainingTimesLastYear=TrainingTimesLastYear,WorkLifeBalance=WorkLifeBalance,YearsAtCompany=YearsAtCompany,YearsInCurrentRole=YearsInCurrentRole,
                  YearsSinceLastPromotion=YearsSinceLastPromotion,YearsWithCurrManager=YearsWithCurrManager)
            data.save()
        
            return render(request,'attritionpredict.html',
                      {"Attrition": prediction,'Age':Age,'BusinessTravel':BusinessTravel,'DailyRate':DailyRate,'Department':Department,'DistanceFromHome':DistanceFromHome,
                       'Education':Education,'EducationField':EducationField,
                       'EnvironmentSatisfaction':EnvironmentSatisfaction,'Gender':Gender,'HourlyRate':HourlyRate,'JobInvolvement':JobInvolvement,
                      'JobLevel':JobLevel,'JobSatisfaction':JobSatisfaction,'MaritalStatus':MaritalStatus,'MonthlyIncome':MonthlyIncome,
                      'MonthlyRate':MonthlyRate,'NumCompaniesWorked':NumCompaniesWorked,'OverTime':OverTime,'PercentSalaryHike':PercentSalaryHike,
                      'PerformanceRating':PerformanceRating,'RelationshipSatisfaction':RelationshipSatisfaction,'StandardHours':StandardHours,'StockOptionLevel':StockOptionLevel,
                      'TotalWorkingYears':TotalWorkingYears,'TrainingTimesLastYear':TrainingTimesLastYear,'WorkLifeBalance':WorkLifeBalance,
                      'YearsAtCompany':YearsAtCompany,'YearsInCurrentRole':YearsInCurrentRole,
                      'YearsSinceLastPromotion':YearsSinceLastPromotion,'YearsWithCurrManager':YearsWithCurrManager})
        else:
             return render(request, 'attritionpredict.html')