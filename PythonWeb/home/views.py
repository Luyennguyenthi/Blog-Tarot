
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.http import HttpResponse


def index1(request):
   response = HttpResponse()
   response.write('<h1 style="color:green">HEADING</h1>')
   response.write('<img src="https://i.pinimg.com/474x/43/87/4a/43874a7dec0e3011308ec2b68585e7a6.jpg" alt="image1">')
   response.write('<img src="https://i.pinimg.com/474x/8d/fa/ee/8dfaee4c8e935d66cfdd5387f4e3cfcc.jpg" alt="image2">')
   response.write('<br/>')
   response.write('  <a href="viewscopy.py">Chuyển hướng tới trang </a>')
   response.write('<h1 style="color:brown">FOOTER</h1> ')

   return response   

# Create your views here.
def index(request):
     return render(request, 'pages/home.html')
   #   return render(request, 'blog/product.html')

def contact(request):
    return render(request, 'pages/contact.html')

def Blog(request):
    return render(request, 'pages/blog.html')



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})