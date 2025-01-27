from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),

    path('list_b/', listbooks.as_view(), name='list_b'),
    path('create_b/', CreateBook.as_view(), name='create_b'),
    path('onebook/<int:book_id>/', onebook.as_view(), name='onebook' ),
    path('update_b/<int:book_id>/', updatebook.as_view(), name='update_b'),
    path('detale_b/<int:book_id>/', detalebook.as_view(), name='detale_b'),
    path('delete_b/<int:book_id>/', deletebook.as_view(), name='delete_b'),

    path('list_p/', listPosts.as_view(), name='list_p'),
    path('create_p/', CreatePost.as_view(), name='create_p'),
    path('onepost/<int:post_id>/', onePost.as_view(), name='onepost' ),
    path('update_p/<int:post_id>/', updatePost.as_view(), name='update_p'),
    path('detale_p/<int:post_id>/', detalepost.as_view(), name='detale_p'),
    path('delete_p/<int:post_id>/', deletePost.as_view(), name='delete_p')

]
