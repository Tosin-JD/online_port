from django.urls import path

from .views import (dock_overview,
                    DockDetail,
                    user_profile,
                    CreateDockManifest,
                    DockManifestList,
                    DockManifestUpdate,
                    DockManifestDelete,
                    DockManifestDetail,
                    ShipList,
                    offload,
                    print_manifest,)

app_name = 'ship'


urlpatterns = [
        path('dock-overview/', dock_overview, name='overview'),
        path('dock/<int:pk>/detail/', DockDetail.as_view(), name='dock_detail'),
        path('user-profile/', user_profile, name='user_profile'),
        path('manifest/create/', CreateDockManifest.as_view(), name='manifest_create'),
        path('ships/', ShipList.as_view(), name='ships'),
        path('manifest/list/', DockManifestList.as_view(), name='manifest_list'),
        path('dock/<int:pk>/manifest/detail/', DockManifestDetail.as_view(), name='manifest_detail'),
        path('dock/<int:pk>/manifest/update/', DockManifestUpdate.as_view(), name='manifest_update'),
        path('dock/<int:pk>/manifest/delete/', DockManifestDelete.as_view(), name='manifest_delete'),
        path('<int:pk>/offload/', offload, name='offload'),
        path('<int:pk>/manifest/print/', print_manifest, name='print_manifest'),
    ]
