
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import pyrebase 
from django.shortcuts import render


config = {
    "apiKey": "AIzaSyAL6y7jvIY1win9H9XGy1BcQpqj7MyNSYg",
    "authDomain": "minnano-df3a0.firebaseapp.com",
    "databaseURL": "https://minnano-df3a0.firebaseio.com",
    "projectId": "minnano-df3a0",
    "storageBucket": "minnano-df3a0.appspot.com",
    "messagingSenderId": "538306671431",
    "appId": "1:538306671431:web:853596b85c3f3a6ff55262",
    "measurementId": "G-208ZMQNRMP"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()

def homepage(request):
    return render(request, "accounts/superuser.html")

def signin(request):
    return render(request, "accounts/login.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
       # return render(request,"login_error.html",{"messg":message})
    #print(user['idToken'])
     
    session_id=user['idToken']
    idtoken= request.session['uid']=str(session_id)
    #a = auth.get.account_info(idtoken)
    a = auth.get_account_info(idtoken)
    a = a['users']
    print (a)
    a = a[0]
    a = a['localId']
    print (a)
    
    name = database.child('users').child(a).child('details').child('First Name').get().val()
    return render(request, "accounts/dashboard.html",{"e":name})



def register_counselor(request):
    return render(request, "accounts/counselor_reg.html")

def postregister_counselor(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    url=request.POST.get('url')
    skills=request.POST.get('skills')
    experience=request.POST.get('experience')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Id Proof":url,"Mentoring Skills":skills,"Years of Experience":experience}
    database.child("users").child(uid).child("details").set(data)
    return render(request, "accounts/login.html")


def register_parent(request):
    return render(request, "accounts/parent_reg.html")

def postregister_parent(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    skills=request.POST.get('skills')
    experience=request.POST.get('experience')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Mentoring Skills":skills,"Years of Experience":experience}
    database.child("Parent").child(uid).set(data)
    return render(request, "accounts/login.html")




def register_school(request):
    return render(request, "accounts/school_reg.html")

def postregister_school(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    skills=request.POST.get('skills')
    experience=request.POST.get('experience')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Mentoring Skills":skills,"Years of Experience":experience}
    database.child("School").child(uid).set(data)
    return render(request, "accounts/login.html")





def register_activist(request):
    return render(request, "accounts/activist_reg.html")

def postregister_activist(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    skills=request.POST.get('skills')
    experience=request.POST.get('experience')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Mentoring Skills":skills,"Years of Experience":experience}
    database.child("Counselor").child(uid).set(data)
    return render(request, "accounts/login.html")





def register_mentor(request):
    return render(request, "accounts/mentor_reg.html")

def postregister_mentor(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    url=request.POST.get('url')
    skills=request.POST.get('skills')
    experience=request.POST.get('experience')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Id Proof":url,"Mentoring Skills":skills,"Years of Experience":experience}
    database.child("users").child(uid).child("details").set(data)
    return render(request, "accounts/login.html", {"form": form, "msg" : msg })