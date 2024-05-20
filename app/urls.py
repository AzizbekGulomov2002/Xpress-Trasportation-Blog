from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, StatisticsViewSet, OfficeHoursViewSet, SocialNetworksViewSet, PartnersViewSet,
    StepsViewSet, StepDetailsViewSet, BlogsViewSet, FAQViewSet, FAQInfoViewSet
)
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as get_yasg_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'statistics', StatisticsViewSet)
router.register(r'officehours', OfficeHoursViewSet)
router.register(r'socialnetworks', SocialNetworksViewSet)
router.register(r'partners', PartnersViewSet)
router.register(r'steps', StepsViewSet)
router.register(r'stepdetails', StepDetailsViewSet)
router.register(r'blogs', BlogsViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'faqinfos', FAQInfoViewSet)

schema_view = get_yasg_view(
    openapi.Info(
        title="XPress Transportation",
        default_version='v1',
        description="API documentation for XPress Transportation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
