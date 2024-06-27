from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
from apps.models import Product, Category
from django.shortcuts import render, get_object_or_404


# Create your views here.


def home(request):
    latest_post = Product.objects.latest('created_at')

    try:
        uzbekistan_category = Category.objects.get(name='uzbekistan')
        uzbekistan_posts = Product.objects.filter(category=uzbekistan_category).order_by('-created_at')
    except Category.DoesNotExist:
        uzbekistan_posts = Product.objects.none()

    other_posts = Product.objects.exclude(category=uzbekistan_category).order_by('-created_at')

    all_posts = uzbekistan_posts | other_posts

    return render(request, 'home.html', {
        'latest_post': latest_post,
        'uzbekistan_posts': uzbekistan_posts,
        'other_posts': other_posts,
        'all_posts': all_posts
    })


def about(request, id):
    post = get_object_or_404(Product.objects.all(), id=id)
    print(post)
    return render(request, 'about.html', {'post': post})


def uzb_view(request):
    posts = Product.objects.filter(category__name='uzbekistan')
    return render(request, 'uzbekistan.html', {'posts': posts})


def global_view(request):
    posts = Product.objects.filter(category__name='global')
    return render(request, 'global.html', {'posts': posts})


def sport_view(request):
    posts = Product.objects.filter(category__name__in=['uzbekistan', 'sport'])

    return render(request, 'sport.html', {'posts': posts})


def science_view(request):
    posts = Product.objects.filter(category__name='science')
    return render(request, 'science.html', {'posts': posts})


def techno_view(request):
    posts = Product.objects.filter(category__name='techno')
    return render(request, 'techno.html', {'posts': posts})


# views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f'Message from {name} ({email})',
            message,
            settings.EMAIL_HOST_USER,
            ["subhoniddinovnuriddin@gmail.com",], fail_silently=False
        )

    return render(request, 'contact.html')
