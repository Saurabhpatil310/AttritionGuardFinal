from django.db import models

# Create your models here.

# class Register(models.Model):
#     firstname=models.CharField(max_length=100)
#     lastname=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     moblie=models.CharField(max_length=10)
#     password=models.CharField(max_length=100)

# class login(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
    

class Data (models.Model):
            Age=models.CharField(max_length=100)
            BusinessTravel=models.CharField(max_length=100)
            DailyRate=models.CharField(max_length=100)
            Department=models.CharField(max_length=100)
            DistanceFromHome = models.CharField(max_length=100)
            Education=models.CharField(max_length=100)
            EducationField=models.CharField(max_length=100)
            EnvironmentSatisfaction=models.CharField(max_length=100)
            Gender=models.CharField(max_length=100)
            HourlyRate= models.CharField(max_length=100)
            JobInvolvement=models.CharField(max_length=100)
            JobLevel=models.CharField(max_length=100)
            JobSatisfaction=models.CharField(max_length=100)
            MaritalStatus=models.CharField(max_length=100)
            MonthlyIncome=models.CharField(max_length=100)
            MonthlyRate=models.CharField(max_length=100)
            NumCompaniesWorked=models.CharField(max_length=100)
            OverTime=models.CharField(max_length=100)
            PercentSalaryHike=models.CharField(max_length=100)
            PerformanceRating=models.CharField(max_length=100)
            RelationshipSatisfaction=models.CharField(max_length=100)
            StandardHours=models.CharField(max_length=100)
            StockOptionLevel=models.CharField(max_length=100)
            TotalWorkingYears=models.CharField(max_length=100)
            TrainingTimesLastYear=models.CharField(max_length=100)
            WorkLifeBalance=models.CharField(max_length=100)
            YearsAtCompany =models.CharField(max_length=100)
            YearsInCurrentRole= models.CharField(max_length=100)
            YearsSinceLastPromotion=models.CharField(max_length=100)
            YearsWithCurrManager=models.CharField(max_length=100)