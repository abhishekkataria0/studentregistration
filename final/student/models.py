from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MaxValueValidator

# Create your models here.

def user_directory_path(instance,filename):
    return 'user_{id}/{file}'.format(id=instance.user.id ,file=filename)



class Student_form1(models.Model):
    First_name= models.CharField(max_length = 100)
    Middle_name= models.CharField(max_length = 100,blank=True,null=True)
    Last_name = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length=12,unique= True)
    email = models.EmailField(max_length=70,unique= True)
    Nationality = (
        ('India', 'India'),
        ('Foreign', 'Foreign'),
    )
    Nationality = models.CharField(max_length = 7, choices = Nationality)

    STATUS = (
        ('Male', 'Male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )

    Gender = models.CharField(max_length = 6, choices = STATUS)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Student_form2(models.Model):
    Mother_name= models.CharField(max_length = 100)
    Father_name= models.CharField(max_length = 100)
    marks_in_tenth= models.CharField(max_length = 5)
    tenth_marksheet= models.FileField(null=True,blank=True,upload_to=user_directory_path)
    Status_of_twefth_result= (
        ('Awaited', 'Awaited'),
        ('Passed', 'Passed'),
    )

    Status_of_twefth_result = models.CharField(max_length = 7, choices =Status_of_twefth_result)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class Student_form3(models.Model):
    marks_in_twelfth= models.CharField(max_length = 5,blank=True)
    Subject1_marks= models.CharField(max_length = 5,blank=True)
    Subject2_marks= models.CharField(max_length = 5,blank=True)
    Subject3_marks= models.CharField(max_length = 5,blank=True)
    Subject4_marks= models.CharField(max_length = 5,blank=True)
    twelfth_marksheet= models.FileField(null=True,blank=True,upload_to=user_directory_path)
    user=models.OneToOneField(User,on_delete=models.CASCADE)






class Student_form4(models.Model):
    candidate_photo= models.ImageField(null=True,blank=True,upload_to=user_directory_path)
    thumb_impression= models.ImageField(null=True,blank=True,upload_to=user_directory_path)
    candidate_signature= models.ImageField(null=True,blank=True,upload_to=user_directory_path)
    user=models.OneToOneField(User,on_delete=models.CASCADE)







class Prob_form(models.Model):
    Name= models.CharField(max_length = 100,blank=True)
    Subject= models.CharField(max_length = 200,blank=True)
    Description= models.CharField(max_length = 500,blank=True)
    Error_number= models.CharField(max_length = 5,blank=True)