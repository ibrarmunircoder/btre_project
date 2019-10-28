from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from btre import settings
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')

        #check if user has made an inquiry already for same listing
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, ("You have already made an inquiry for this listing"))
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, name=name, listing_id=listing_id, email=email, phone=phone,
         message=message, user_id=user_id)

        contact.save()
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. sign into the admin panel for more info.',
        #     'ibrarmunir009@gmail.com',
        #     [realtor_email, 'zeenatmunir97@outlook.com'],
        #     fail_silently=False
        # )

        messages.success(request, ("Your request has been submitted, a realtor will get back to you soon."))

        return redirect('/listings/'+listing_id)