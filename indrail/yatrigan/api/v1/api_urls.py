from django.urls import path, include

from indrail.yatrigan.api.v1 import api_views as APIv1

urlpatterns = [
    path('station/<station>/stalls', APIv1.ShopListApi.as_view()),
]
