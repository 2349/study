from django.conf.urls import url
from . import views

app_name = "images" 

urlpatterns = [
	url(
		regex=r'^explore/$',
		view=views.ListUsers.as_view(),
		name='list_user'
	),
    url(
		regex=r'(?P<user_id>[0-9]+)/follow/$',
		view=views.FollowUser.as_view(),
		name='follow_user'
	),
    url(
		regex=r'(?P<user_id>[0-9]+)/unfollow/$',
		view=views.UnFollowUser.as_view(),
		name='follow_user'
	),
	url(
		regex=r'^(?P<username>\w+)/$',
		view=views.UserProfile.as_view(),
		name='user_profile'
	),
	url(
		regex=r'^(?P<username>\w+)/followers/$',
		view=views.UserFollowers.as_view(),
		name='user_followers'
	)
]