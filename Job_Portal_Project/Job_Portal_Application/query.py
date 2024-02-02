from Job_Portal_Application import utils

from django.db import connection


con = connection.cursor()

# -------------------- SIGHN-UP ----------------------------------------

# ----- INSER CHECK TO DB - ALREADY PRESENT OR NOT PRESENT - EMAIL --------
def email_db_check(email):
    sql = "select * from  recruiter_signup where Official_Email = %s"
    value = con.execute(sql,(email))
    print(" 2 -------------------------")
    return value




# Insert mySql query function starts here------->
def mySqlQuery(Company_Name,Official_Email,Mobile_No,Contact_Person_Name,Password):
    myquery = "INSERT INTO recruiter_signup(Company_Name,Official_Email,Mobile_No,Contact_Person_Name,Password) values(%s,%s,%s,%s,%s)"
    value = (Company_Name,Official_Email,Mobile_No,Contact_Person_Name,Password)    # values = (first_name, last_name, mobile, password, confirm_password)
    print("value",value)
    con.execute(myquery,value)
    print("success------>")
    return True

# ----------------------- LOGIN ---------------------------------
def login_check(email,password):
    sql = "select id from  recruiter_signup where Official_Email =%s and Password =%s"
    # value = con.execute("select id from  recruiter_signup where email =%s and password =%s",[email,password])
    # value = con.fetchall()
    values = (email,password)
    con.execute(sql,values)
    
    
    data = con.fetchone()
    print(data,"-------------------------------------")
    return data
        
        
# --------------------- FORGET - EMAIL - RETRIVAL ------------------------
def email_check(email):
    sql = "select * from recruiter_signup where  Official_Email = %s"        
    return con.execute(sql,(email))
    
        
# ------------------------- CHANGE PASSWORD START HERE ----------------------------
def changePassword(confirm_password,email_changePassword):
    sql = "Update  recruiter_signup set  Password =%s  where Official_Email = %s"
    values = (confirm_password,email_changePassword)
    return con.execute(sql,values)
        
#------------------------------Employers Registration Page -------------------------------------------------
        
def employeRegister(name,company_name,no_of_employees,select_industry,your_designation,address):
    myquery = "INSERT INTO employers_registration(name,company_name,no_of_employees,select_industry,your_designation,address) values(%s,%s,%s,%s,%s,%s)"
    value = (name,company_name,no_of_employees,select_industry,your_designation,address)    # values = (first_name, last_name, mobile, password, confirm_password)
    print("value",value)
    con.execute(myquery,value)
    print("success------>")
         
   
   
    
    
  
    





# Select mySql query function
# def selectQuery():
#      con.execute("select * from  recruiter_signup")
#      return  con.fetchall()
 
 
# def update_query(id,password):
#     con.execute("Update  recruiter_signup set password=%s where id = %s",[password,id]) 
    
    
# def delete_query(id):
#     con.execute("DELETE from recuirter_signup  where id = %s",[id])
#     return True
        
    
