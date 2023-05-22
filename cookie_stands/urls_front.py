from django.urls import path
from .views import CookieStandList, CookieStandDetail


# from .views_front import (
#     ThingCreateView,
#     ThingDeleteView,
#     ThingDetailView,
#     ThingListView,
#     ThingUpdateView,
# )

urlpatterns = [
    path('', CookieStandList.as_view(), name='cookie_stand_list'),
    path('<int:pk>', CookieStandDetail.as_view(), name='cookie_stand_detail'),
]


    # path("create/", ThingCreateView.as_view(), name="thing_create"),
    # path("<int:pk>/update/", ThingUpdateView.as_view(), name="thing_update"),
    # path("<int:pk>/delete/", ThingDeleteView.as_view(), name="thing_delete"),
