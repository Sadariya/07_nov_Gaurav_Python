
def login_signup_data (request,signup_form,signup_model,messages,settings,send_mail,redirect):
    color = 'success'
    if request.method == 'POST':
        if request.POST.get('signup') == 'signup':
            signup_data = signup_form(request.POST)
            if signup_data.is_valid():
                username_verify = signup_data.cleaned_data.get('username')
                try:
                    unm = signup_model.objects.get(username=username_verify)
                    print('User Does Exits ! Please Use Another Username')
                    messages.error(
                        request, 'User Does Exits ! Please Use Another Username')
                    color = 'danger'
                except:
                    signup_data.save()
                    print('Account created successfully.')

                    # Mail Sending code :-
                    subject = 'Account Created successfully'
                    msg = 'Dear User, \n\nThank you for create an account on our site \nYou will get benefits in your farm \nAnd Your problem will be solved by our exert team \n\nFor More information Contact Us on \n+91 91234 56789'
                    Mail = settings.EMAIL_HOST_USER
                    user_mail = [request.POST['username']]

                    send_mail(subject=subject, message=msg,
                              from_email=Mail, recipient_list=user_mail)

                    color = 'success'
                    messages.success(request, 'Account created successfully.')
            else:
                print(signup_data.errors)
                messages.error(request, 'signup_data.errors')

        elif request.POST.get('login') == 'login':

            unm = request.POST['username']
            pas = request.POST['password']

            user = signup_model.objects.get(username=unm)
            login_var = signup_model.objects.filter(username=unm, password=pas)

            if login_var:
                print('login successfully.')
                messages.success(request, 'login successfully.')
                request.session['username'] = unm
                request.session['userid'] = user.id
                request.session['role'] = user.authorised
                color = 'success'

            else:
                print('Login ! Failed')
                messages.error(request, 'Login ! Failed')
                color = 'danger'

            return color


def contact_data (request,contactus_form,settings,send_mail,messages):
    color = 'success'
    if request.method == 'POST':
            con_var = contactus_form(request.POST)
            if con_var.is_valid():
                con_var.save()

                # Mail Sending code :-
                subject = 'Thank you'
                msg = 'Dear visitor, \n\nThank you for visit our site \nOur team will contact soon \nAnd Your Query will be solved by our exert team \n\nFor More information Contact Us on \n+91 91234 56789'
                Mail = settings.EMAIL_HOST_USER
                user_mail = [request.POST['email']]

                send_mail(subject=subject, message=msg,
                        from_email=Mail, recipient_list=user_mail)
                
                print ('Thank You for contact Us')
                messages.success(request,'Thank You for contact Us')
                color = 'success'
            else:
                print(con_var.errors)

            return color
