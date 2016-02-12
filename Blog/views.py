from django.shortcuts import render, get_object_or_404

from Blog.models import Post, Category

query_populer = Post.objects.order_by("updated")[:3]
query_kategori = Category.objects.all()[:5]


def anasayfa(request):
    query = Post.objects.all().order_by("-updated")
    context = {
        "objects": query,
        "populer": query_populer,
        "categories": query_kategori,
    }
    return render(request, "anasayfa.html", context)


def allposts(request):
    query = Post.objects.all().order_by("-updated")
    context = {
        "objects": query,
        "populer": query_populer,
        "categories": query_kategori,
    }
    return render(request, "allposts.html", context)


def detail(request, id):
    query = get_object_or_404(Post, id=id)
    context = {
        "objects": query,
        "populer": query_populer,
        "categories": query_kategori,
    }
    return render(request, "detay.html", context)


def categories(request):
    # query = Post.objects.values('category__name','category_id').annotate(count=Count('category'))
    query = Category.objects.all()
    context = {
        "objects": query,
        "populer": query_populer,
        "categories": query_kategori,
    }
    return render(request, "kategoriler.html", context)


def category_detail(request, id):
    query = get_object_or_404(Category, id=id)
    query_post = Post.objects.all().filter(category_id=id)
    context = {
        "objects": query,
        "obje": query_post,
        "populer": query_populer,
        "categories": query_kategori,
    }
    return render(request, "kategori_detail.html", context)
