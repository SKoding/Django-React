from rest_framework import routers
from .views import  farmViewSet, farmerViewSet, partnerViewSet

## Register Viewsets as APIs 
router = routers.DefaultRouter()
router.register(r"farms", farmViewSet)
router.register(r"farmers", farmerViewSet)
router.register(r"partners", partnerViewSet)
#router.register(r"search", SearchPost)


urlpatterns = router.urls