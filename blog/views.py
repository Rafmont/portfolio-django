from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .models import Project
from .models import Formation
from .models import Latest
from django.shortcuts import get_object_or_404

# Create your views here.
def sobre(request):
    projects = Project.objects.filter(begin_date__lte=timezone.now()).order_by('begin_date')
    formations = Formation.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
    latests = Latest.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
    context = {'projects': projects, 'formations': formations, 'latests':latests}
    return render(request, 'sobre/sobre.html', context)

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blog/blog-index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})