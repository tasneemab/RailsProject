from django.urls import path
from .views import PasteList, PasteDetail, PasteDelete, PasteUpdate, PasteCreate

app_name = 'pastebin'

urlpatterns = [
	path('', PasteCreate.as_view(), name='create'),
	path('pastes/', PasteList.as_view(), name='paste_list'),
	path('paste/<int:pk>', PasteDetail.as_view(), name='paste_detail'),
	path('paste/delete/<int:pk>', PasteDelete.as_view(), name='paste_delete'),
	path('paste/edit/<int:pk>', PasteUpdate.as_view(), name='paste_edit'),
]