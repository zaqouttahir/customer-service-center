from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def healthcheck(_request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', healthcheck, name='healthcheck'),
    path('api/health/', healthcheck, name='api-healthcheck'),
    path('api/webhooks/', include('channels.urls')),
    path('api/messages/', include('conversations.urls')),
    path('api/agents/', include('agents.urls')),
    path('api/llm/', include('llm.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/customers/', include('customers.urls')),
]
