from rest_framework_extensions.routers import ExtendedDefaultRouter

from . import viewsets

app_name = "TaskManager"
router = ExtendedDefaultRouter()

router.register(r"tags", viewsets.TagViewSet, basename="tags")
router.register(r"tasks", viewsets.TaskViewSet, basename="tasks")

urlpatterns = router.urls
