from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# dummy data for posts
posts = [
    {
        'author': 'Jimmy Lee',
        'title': 'CSCI3180',
        'content': 'Principles of Programming Languages',
        'date_posted': 'August 21, 2019',
    },
    {
        'author': 'Eric Lo',
        'title': 'CSCI3150',
        'content': 'Introduction to Operating Systems',
        'date_posted': 'August 25, 2019',
    },
    {
        'author': 'Andrej Bogdanov',
        'title': 'ENGG2430',
        'content': 'Probability and Statistics for Engineers',
        'date_posted': 'June 24, 2019',
    },
]

# /
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# /about
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
