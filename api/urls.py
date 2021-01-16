from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from .views import BlogView, TodoView, CurrentUserView, WorkLogView

router = SimpleRouter(trailing_slash=False)
router.register("blog", BlogView)
router.register("todo", TodoView)
router.register("worklog", WorkLogView)

urlpatterns = [
    url(r'^user$', CurrentUserView.as_view(), name='current_user'),
    url(r'^', include(router.urls, namespace='blog')),
]
