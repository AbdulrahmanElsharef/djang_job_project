from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ALL LIST FUNCTIONS  (1)
def Post_list(request):
    # Retrieve all records from the database
    posts = Post.objects.all()
    # Render a template with the records
    return render(request, 'blog/post_list.html', {'posts': posts})
# CBV


class PostList(ListView):
    model = Post

# ___________________________________________________

# FUNCTIONS    (2)


def Post_detail(request, slug):
    # Retrieve a specific record by ID
    post = get_object_or_404(Post, slug=slug)
    # Render a template with the record
    return render(request, 'blog/post_detail.html', {'post': post})

# CBV


class PostDetail(DetailView):
    model = Post
# ___________________________________________________

# FUNCTIONS    (3)


def Post_create(request):
    # Handle form submission for creating a new record
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    # Render a form for creating a new record
    else:
        form = PostForm()
        return render(request, 'blog/post_create.html', {'form': form})
# CBV

class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')
    
# ___________________________________________________

# FUNCTIONS (4)

def Post_update(request, slug):
    # Retrieve a specific record by ID
    post = get_object_or_404(Post, slug=slug)
    # Handle form submission for updating the record
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    # Render a form for updating the record
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', {'form': form})

# CBV

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blog:post_list')

# _____________________________________________________

# FUNCTIONS  (5)


def Post_delete(request, slug):
    # Retrieve a specific record by ID
    post = get_object_or_404(Post, slug=slug)
    # Handle form submission for deleting the record
    if request.method == 'POST':
            post.delete()
            return redirect('board:job_list')
    # Render a confirmation form for deleting the record
    else:
        return render(request, 'blog/post_delete.html', {'post': post})

# CBV

class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')
