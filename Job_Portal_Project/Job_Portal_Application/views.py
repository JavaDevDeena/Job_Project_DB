from django.shortcuts import render
# from django.db import connection
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from Job_Portal_Application import utils,query,email

#-- Email Import --------
from django.core.mail import send_mail
# from django.conf import settings
import os

# desired_location = settings.MEDIA_ROOT 


con = connection.cursor()


# @csrf_exempt
# def image_copy(request):
#     if request.method == 'POST':
#         if request.method == 'POST':
#             name = request.POST.get('name')  # Accessing a text field value with key "name"
#             print(name," =======================================")
#             # email = request.POST.get('email')  # Accessing another text field

#             # Accessing uploaded file and saving it locally
#             if 'name' in request.FILES:
#                 image_file = request.FILES['name']
#                 # Save the image file to your desired location
#                 # ...5
#                 print(type(image_file),"---------------------------")

#             # Use the data further in your code

#             return JsonResponse('Form data processed successfully!',safe=False)
#         return JsonResponse('Form submission not allowed',safe=False)

# ----------------------------- Image and PDF Stores Start here ----------------------------------------

@csrf_exempt
def image_copy(request):
    try :
        if request.method == 'POST':
            image_file = request.FILES['name']
            desired_location = r'C:\Users\AdmiN\Desktop\Job Portal\Job_Portal_Project\images'
            print(image_file,"----------------------------------------")
            print("1 -----------------")
            full_file_path = os.path.join(desired_location, image_file.name)
            print("2 ------------------------")
            print(desired_location,"------------------ ",full_file_path)
            
            with open(full_file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
                    
            return JsonResponse("Success",safe=False)        
    except Exception:
        return JsonResponse("Failled",safe=False)


# --------------------------------------  SIGN-UP -----------------------------------------------
#post api-- Create your views here.
@csrf_exempt
def insert(request):
    print("Function working")
    try:
           if request.method == 'POST':
                data = json.loads(request.body)
                Company_Name = data.get('Company_Name')
                Official_Email = data.get('Official_Email')
                Mobile_No =data.get('Mobile_No')
                Contact_Person_Name = data.get('Contact_Person_Name')
                Password =data.get('Password')
                
                if Official_Email != None and Official_Email != '':
                    value = query.email_db_check(Official_Email)
                    if value:
                        print(value,"value printing here")
                        return utils.errorResponse("Email is already Present")
                    else :
                        if Company_Name != "" and Company_Name != None and Official_Email != "" and Official_Email != None and Mobile_No != "" and Mobile_No != None  and Contact_Person_Name != "" and Contact_Person_Name != None  and Password != "" and Password != None : 
                                query.mySqlQuery(Company_Name,Official_Email,Mobile_No,Contact_Person_Name,Password)
                                # --- Email - Send -----
                                name = 'Job Portal'
                                Message = 'Successfully SignUp .....................'
                                my_email = Official_Email
                                send_mail(name,Message,'settings.EMAIL_HOST_USER',[my_email],fail_silently=False)
                                return utils.handleSuccess("successFully Data Inserted")
                                 
                                
                        else:
                            return utils.errorResponse("data not inserted")
    except Exception as e :
            return utils.serverErrorResponse()

#----------------------------------------------- LOG-IN ---------------------------------------------------------

@csrf_exempt
def login(request):
    try:
 
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            if email != "" and  email != None and password !="" and password !=None :
                login_value = query.login_check(email,password)
                if login_value:
                    return utils.handleSuccess("successFully  login")   
                else:
                    return utils.errorResponse("failed to login")
                    
    except Exception :
        utils.serverErrorResponse()           
        
# ------------------ FORGET PASSWORD CODE START HERE ---------------------------------------     

# -- Password Changing Using This Variable 
email_changePassword = ""

@csrf_exempt
def forget_password(request):
    try :
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            global email_changePassword
            email_changePassword = email
            
            if email !="" and email != None :
                value = query.email_check(email)
                # Mail Send Here
                name = 'Change Password'
                Message = 'Click here to change password'
                my_email = 'p38802577@gmail.com'
                
                if value:
                    # send_mail(Subject,Message,From,To)
                    send_mail(name,Message,'settings.EMAIL_HOST_USER',[my_email],fail_silently=False)
                    
                    
                    return utils.handleSuccess("Success to Email")
                    
                    
                else:
                    return utils.errorResponse("Fail to Email")
    
    except Exception :
        return utils.serverErrorResponse()      
    
    
   # ------------------ CHANGE PASSWORD ------------------------
@csrf_exempt   
def change_password(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            if password !='' and password != None and confirm_password != '' and confirm_password != None:
                    check = query.changePassword(confirm_password,email_changePassword)
                    if check:
                         return utils.handleSuccess("Success to Password change")
                    else:
                        return utils.errorResponse("Failed Change Password")
    except Exception :
        return utils.serverErrorResponse()            

# -------------------------------------- Recruiter Register ------------------------------------------------
@csrf_exempt
def employe_registration(request):
    try:
        if request.method == 'POST':
            print("2 ----------------------------")
            data = json.loads(request.body)
            name = data.get('name')
            company_name = data.get('company_name')
            no_of_employees = data.get('no_of_employees')
            select_industry = data.get('select_industry')
            your_designation = data.get('your_designation')
            address = data.get('address')
            if name != None and company_name != None and no_of_employees != None and select_industry != None and your_designation != None and address != None :
                print("3 --------------------------------------")
                query.employeRegister(name,company_name,no_of_employees,select_industry,your_designation,address)
                return utils.handleSuccess("Successfully Registration")
            else :
                return utils.errorResponse("Data not Register")
    except Exception :
        return utils.serverErrorResponse()       
 
            
               
        
    # ---------------------------------------------------------------------------- END ----------------------------------------------------------------------------------    

        
           



               
            


            
            
        
                
            

   