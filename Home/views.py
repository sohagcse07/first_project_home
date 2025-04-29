from django.shortcuts import render , HttpResponse
from datetime import date
from Home.models import Contact
# Create your views here.

def index(request):

    # context={
    #     "variable" : " this is sent"
    # }
    return render(request, 'index.html' )


def about(request):
    #return HttpResponse("<h1>About Us</h1><p>Welcome to our website. We are here to provide the best services and information. Stay connected!</p>")
    return render(request, 'about.html',  )



def services(request):
    # return HttpResponse("""
    #     <h1>Our Ice Cream Services</h1>
    #     <ul>
    #         <li>Fresh Ice Cream Production</li>
    #         <li>Home Delivery</li>
    #         <li>Custom Ice Cream Cakes</li>
    #         <li>Party & Event Orders</li>
    #         <li>Seasonal Specials</li>
    #     </ul>
    #     <p>We make your days sweeter! 🍨🍓🍫</p>
    # """)
    return render(request, 'services.html'  )

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("this is contact  page")
