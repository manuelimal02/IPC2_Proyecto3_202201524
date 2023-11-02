from django.urls import path
from . import views

urlpatterns=[
    path('Tecnologias-Chapinas/',views.myform_view, name='Tecnologias-Chapinas'),
    path('consultaHashtag/',views.consulta_hashtag, name='consultaHashtag'),
    path('consultaMenciones/',views.consulta_menciones, name='consultaMenciones'),
    path('consultaSentimiento/',views.consulta_sentimiento, name='consultaSentimiento'),
    path('graficaHashtag/',views.grafica_hashtag, name='graficaHashtag'),
    path('graficaMenciones/',views.grafica_menciones, name='graficaMenciones'),
    path('graficaSentimiento/',views.grafica_sentimiento, name='graficaSentimiento'),
    path('resumenMensajes/',views.resumen_mensajes, name='resumenMensajes'),
    path('resumenConfiguraciones/',views.resumen_configuraciones, name='resumenConfiguraciones')
]