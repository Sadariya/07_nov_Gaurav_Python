from django.shortcuts import render, redirect
from .models import signup_model, retailer_model, farmercomplain_model, farmertips_model, feedback_model
from .forms import signup_form, update_form, retailer_form, editpost_delete_form, farmercomplaint_form, farmertips_form, feedback_form, farmer_accept_form, contactus_form
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from Farming_assistant import settings
from Farming_app import module

# Create your views here.

# Main page views :-


def index(request):

    color = 'success'
    if request.method == 'POST':
        if request.POST.get('contactus') == 'contactus':
            color = module.contact_data(
                request, contactus_form, settings, send_mail, messages)
        else:
            color = module.login_signup_data(
                request, signup_form, signup_model, messages, settings, send_mail, redirect)
            if request.POST.get('login') == 'login':
                if color == 'success':
                    return redirect ('notes')

    username = request.session.get('username')
    role = request.session.get('role')

    return render(request, 'index.html', {'username': username, 'role': role, 'color': color})


def profile(request):

    color = ''
    username = request.session.get('username')
    role = request.session.get('role')

    userid = request.session.get('userid')
    userdata = signup_model.objects.get(id=userid)

    if request.method == 'POST':
        if request.POST.get('update') == 'update':
            update_var = update_form(request.POST)
            if update_var.is_valid():
                update_var = update_form(request.POST, instance=userdata)
                update_var.save()
                print('Your Profile has been updated successfully.')
                messages.success(
                    request, 'Your Profile has been updated successfully.')
                color = 'success'
            else:
                print(update_var.errors)
    return render(request, 'profile.html', {'username': username, 'userdata': userdata, 'role': role,'color':color})


def notes(request):

    color = 'success'

    if request.method == 'POST':
        if request.POST.get('contactus') == 'contactus':
            color = module.contact_data(
                request, contactus_form, settings, send_mail, messages)
        else:
            color = module.login_signup_data(
                request, signup_form, signup_model, messages, settings, send_mail, redirect)

    username = request.session.get('username')
    role = request.session.get('role')

    return render(request, 'notes.html', {'username': username, 'role': role, 'color': color})


def contact(request):

    color = ''
    if request.method == 'POST':
        if request.POST.get('contactus') == 'contactus':
            color = module.contact_data(
                request, contactus_form, settings, send_mail, messages)
        else:
            color = module.login_signup_data(
                request, signup_form, signup_model, messages, settings, send_mail, redirect)
            
    username = request.session.get('username')
    role = request.session.get('role')

    return render(request, 'contact.html', {'username': username, 'role': role, 'color': color})


def about(request):

    color = 'success'
    if request.method == 'POST':
        if request.POST.get('contactus') == 'contactus':
            color = module.contact_data(
                request, contactus_form, settings, send_mail, messages)
        else:
            color = module.login_signup_data(
                request, signup_form, signup_model, messages, settings, send_mail, redirect)

    username = request.session.get('username')
    role = request.session.get('role')

    return render(request, 'about.html', {'username': username, 'role': role, 'color': color})


def userlogout(request):

    logout(request)

    messages.success(request, 'Logout Successfull')

    return redirect('/')

def forget(request):

    if request.method == 'POST':
        unm = request.POST['username']
        userdata = signup_model.objects.get(username=unm)

        # send mail to user :-

        subject = 'Forget Password'
        message = f'Dear user, \n\nYour password is {userdata.password} \n\nNever Share Your password to any one.'
        mail = settings.EMAIL_HOST_USER
        maillist = [userdata.username]

        send_mail(subject=subject,message=message,from_email=mail,recipient_list=maillist)

        print ('Your Password has been Sent in Your registered E-Mail')
        messages.success(
            request, 'Your Password has been Sent in Your registered E-Mail')

    return render(request, 'forget.html')

# Admin page views :-

def adminpage(request):

    username = request.session.get('username')
    role = request.session.get('role')

    postdata = retailer_model.objects.all()
    color = 'success'

    if request.method == 'POST':
        if request.POST.get('confirm') == 'confirm':
            userid = request.POST.get('crop_id')
            userdata = retailer_model.objects.get(id=userid)

            retailer_var = editpost_delete_form(request.POST, request.FILES)
            status = request.POST.get('confirmation')
            print(request.POST.get('confirmation'))
            if status == 'Accept':
                if retailer_var.is_valid():
                    retailer_var = editpost_delete_form(
                        request.POST, request.FILES, instance=userdata)
                    retailer_var.save()
                    print(
                        'Add is Accepted successfully')

                    # Mail Sending code :- ('remain This code )
                    subject = 'New Advertisement'
                    msg = 'Dear User, \n\nDealer Publish a new add \nPlease visit for Your Profit \n\nIf Any Problem feel free to contact us On,\n+91 91234 56789 \tGmail:-xyz@gmail.com'
                    Mail = settings.EMAIL_HOST_USER
                    user_email = []

                    # Farmer Mail Id fetching :-
                    farmer_data = signup_model.objects.all()
                    for i in farmer_data:
                        if i.authorised == 'Farmer':
                            user_email.append(i.username)

                    send_mail(subject=subject, message=msg,
                              from_email=Mail, recipient_list=user_email)

                    messages.success(request, "'Add is Accepted successfully'")
                else:
                    print(retailer_var.errors)
                    messages.error(request, retailer_var.errors)
                    color = 'danger'
            elif status == 'Reject':
                if retailer_var.is_valid():
                    retailer_var = editpost_delete_form(
                        request.POST, request.FILES, instance=userdata)
                    retailer_var.save()
                    print(
                        'Add is Rejected ')
                    messages.error(request, "'Add is Rejected '")
                    color = 'danger'
                else:
                    print(retailer_var.errors)
                    messages.error(request, retailer_var.errors)
                    color = 'danger'

    return render(request, 'adminpage.html', {'username': username, 'role': role, 'postdata': postdata, 'color': color})


def farmertips(request):

    username = request.session.get('username')
    role = request.session.get('role')
    color = 'success'

    if request.method == 'POST':
        if request.POST.get('farmertips') == 'farmertips':
            tips_var = farmertips_form(request.POST)
            if tips_var.is_valid():
                tips_var.save()
                print('Your tips is submitted ')
                messages.success(request, 'Your tips is submitted ')
            else:
                print(tips_var.errors)
                messages.error(request, tips_var.errors)
                color = 'danger'

    return render(request, 'farmertips.html', {'username': username, 'role': role, 'color': color})


def farmerdata(request):

    username = request.session.get('username')
    role = request.session.get('role')

    farmer_data = signup_model.objects.all()

    return render(request, 'farmerdata.html', {'username': username, 'role': role, 'farmer_data': farmer_data})


def farmer_accept(request):

    username = request.session.get('username')
    role = request.session.get('role')

    color = 'success'

    # Farmer All data :-
    farmer_var = farmercomplain_model.objects.all()

    if request.method == 'POST':

        # userid and farmerdata :-
        id = request.POST.get('id')
        farmerdata = farmercomplain_model.objects.get(id=id)

        status = farmer_accept_form(request.POST)
        if status.is_valid():
            status = farmer_accept_form(request.POST, instance=farmerdata)
            status.save()
            messages.success(
                request, f'Stautus of Id No:- {id} has been successfully changed.')

        else:
            print(status.errors)
            color = 'danger'
            messages.error(request, 'Error ! Please try Again')

    return render(request, 'farmer_accept.html', {'username': username, 'role': role, 'farmer_var': farmer_var, 'color': color})


def feedback(request):

    username = request.session.get('username')
    role = request.session.get('role')
    color = 'success'

    if request.method == 'POST':
        feedback_var = feedback_form(request.POST)
        if feedback_var.is_valid():
            feedback_var.save()
            print('Feedback has been posteed')
            messages.success(request, 'Feedback has been posteed')
        else:
            print(feedback_var.errors)
            messages.error(request, feedback_var.errors)
            color = 'danger'

    return render(request, 'feedback.html', {'username': username, 'role': role, 'color': color})


def deleteadmin(request, id):

    post = retailer_model.objects.get(id=id)
    post.delete()
    messages.success(request, 'Data has been Deleted')

    return redirect('/adminpage')


# Farmer-Page views :-

def farmerpage(request):

    username = request.session.get('username')
    role = request.session.get('role')

    Dealer_data = retailer_model.objects.all()

    return render(request, 'farmerpage.html', {'username': username, 'role': role, 'Dealer_data': Dealer_data})


def farmercomplaint(request):

    username = request.session.get('username')
    role = request.session.get('role')
    color = 'success'

    if request.method == 'POST':
        if request.POST.get('POST_complaint') == 'POST_complaint':
            postcomplaint_var = farmercomplaint_form(request.POST)
            if postcomplaint_var.is_valid():
                postcomplaint_var.save()
                print('Your complaint is submitted we will contact soon.')
                messages.success(
                    request, 'Your complaint is submitted we will contact soon.')
                color = 'success'
            else:
                print(postcomplaint_var.errors)
                messages.error(request, 'Please Fill all the filled')
                color = 'danger'

    return render(request, 'farmercomplaint.html', {'username': username, 'role': role, 'color': color})


def complaint_status(request):

    username = request.session.get('username')
    role = request.session.get('role')

    complaint_data = farmercomplain_model.objects.all()

    return render(request, 'complaint_status.html', {'username': username, 'role': role, 'complaint_data': complaint_data})


def farming_tips(request):

    username = request.session.get('username')
    role = request.session.get('role')

    tipsdata = farmertips_model.objects.all()

    return render(request, 'farming_tips.html', {'username': username, 'role': role, 'tipsdata': tipsdata})


def Farmer_feedback(request):

    username = request.session.get('username')
    role = request.session.get('role')

    feedbackdata = feedback_model.objects.all()

    return render(request, 'Farmer_feedback.html', {'username': username, 'role': role, 'feedbackdata': feedbackdata})


# Retailer-Page views :-

def retailerpage(request):

    username = request.session.get('username')
    role = request.session.get('role')
    color = 'success'

    if request.method == 'POST':
        if request.POST.get('post') == 'post':
            retailer_var = retailer_form(request.POST, request.FILES)
            if retailer_var.is_valid():
                retailer_var.save()
                print(
                    'Your ad is posted successfully \n It wiil be accept by administrator.')
                messages.success(request, "Your ad is posted successfully")
            else:
                print(retailer_var.errors)
                messages.error(request, retailer_var.errors)
                color = 'danger'

    return render(request, 'retailerpage.html', {'username': username, 'role': role, 'color': color})


def editpost_delete(request):

    username = request.session.get('username')
    role = request.session.get('role')

    postdata = retailer_model.objects.all()

    if request.method == 'POST':
        if request.POST.get('editpost') == 'editpost':
            userid = request.POST.get('crop_id')
            userdata = retailer_model.objects.get(id=userid)

            retailer_var = editpost_delete_form(request.POST, request.FILES)
            if retailer_var.is_valid():
                retailer_var = editpost_delete_form(
                    request.POST, request.FILES, instance=userdata)
                retailer_var.save()
                print(
                    'Your ad is posted successfully \n It wiil be accept by administrator.')
                messages.success(request, "Your ad is posted successfully")
            else:
                print(retailer_var.errors)
                messages.error(request, retailer_var.errors)

    return render(request, 'editpost_delete.html', {'username': username, 'role': role, 'postdata': postdata})


def delete(request, id):

    post = retailer_model.objects.get(id=id)
    post.delete()

    return redirect('/editpost_delete')


def Dealer_feedback(request):

    username = request.session.get('username')
    role = request.session.get('role')

    feedbackdata = feedback_model.objects.all()

    return render(request, 'Dealer_feedback.html', {'username': username, 'role': role, 'feedbackdata': feedbackdata})


'''
# blog function 
def blog (request):
    username = request.session.get('username')
    role = request.session.get('role')

    return render (request,'blog.html', {'username': username, 'role':role})
'''
