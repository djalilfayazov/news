from django.shortcuts import render
from .models import Post


def index(request):

    return render(
        request, 'index/index.html', {
            'posts': Post.objects.order_by('-created')
        }
    )

