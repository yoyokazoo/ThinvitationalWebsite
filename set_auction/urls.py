from django.urls import path
from . import views

urlpatterns = [
	path("", views.set_auction_index, name="set_auction_index"),
	path("<int:pk>/", views.set_auction_detail, name="set_auction_detail"),
	path("admin/", views.set_auction_admin, name="set_auction_admin"),
]