from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from api.models import Post

PPP = 10  # POSTS_PER_PAGE
PML = 11  # PAGINATOR_MAX_LENGTH
PHL = (PML - 1) // 2 # PAGINATOR_HALF_LENGTH


# TODO: Return csrf token and do not replace delete and put method with middleware
# TODO: Django forms
# TODO: Bootstrap form group to align buttons together
# TODO: Length limit for title and body text
class BlogView(LoginRequiredMixin, View):
    def get(self, request):
        all_posts = Post.objects.all().order_by("date")
        paginator = Paginator(all_posts, PPP)
        active_page = request.GET.get('page')

        try:
            active_page = int(active_page)
            posts = paginator.page(active_page)
        except (ValueError, TypeError, EmptyPage): # get the last page in case of wrong active page
            active_page = paginator.num_pages
            posts = paginator.page(active_page)

        if paginator.num_pages <= PML: # num_pages less than maximum
            page_numbers = range(1, paginator.num_pages + 1)
        elif active_page <= PHL:
            page_numbers = range(1, PML + 1)
        elif active_page >= paginator.num_pages - PHL:
            page_numbers = range(paginator.num_pages - PML + 1, paginator.num_pages + 1)
        else:
            page_numbers = range(active_page - PHL, active_page + PHL + 1)

        # next and prev button references on the pagination bar
        if active_page == 1:
            prev_page = None
        elif active_page <= PML:
            prev_page = 1
        else:
            prev_page = active_page - PML
        if active_page == paginator.num_pages:
            next_page = None
        elif active_page >= paginator.num_pages - PML:
            next_page = paginator.num_pages
        else:
            next_page = active_page + PML

        return render(request, 'blog/home.html',
                      {'posts': posts,
                       'active_page': active_page,
                       'page_numbers': page_numbers,
                       'prev_page': prev_page,
                       'next_page': next_page
                       })

    def post(self, request):
        title = request.POST.get('title')
        post = request.POST.get('body')
        db_post = Post(title=title, body=post)
        db_post.user = request.user
        db_post.save()
        return self.get(request)

    def put(self, request):
        post_id = request.PUT['post_id']
        oPost = Post.objects.get(id=post_id)
        oPost.title = request.PUT['title']
        oPost.body = request.PUT['body']
        oPost.save()
        return self.get(request)

    def delete(self, request):
        # TODO: make deleted flag in database
        post_id = request.DELETE['post_id']
        Post.objects.get(id=post_id).delete()
        return self.get(request)
