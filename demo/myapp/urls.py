from django.urls import path
from . import views

urlpatterns = [

    #Main Page
    path("", views.main, name="main"),
    path('course/', views.course, name='course'),
    path('contact/',views.contact_page,name="contact"),
    path('userfull_websites/',views.usefull_webs,name="usefullwebs"),

    #Main Section
    path('articles/STL/string/', views.string_page, name='string_page'),
    path('articles/STL/', views.stl_page, name='stl_page'),
    path('articles/grafuri_arbori/', views.grafuri_arbori_page, name='grafuri_arbori_page'),
    path('articles/structuri_avansate/', views.structuri_avansate_page, name='structuri_avansate_page'),
    path('articles/concursuri/', views.concursuri_page, name='concursuri_page'),
    path('articles/archive/', views.archive_page, name='archive_page'),
    path('articles/measure_time/', views.measure_time_page, name='measure_time_page'),

    #STL
    path('articles/STL/diverse/', views.diverse_stl_page, name='diverse_stl_page'),
    path('articles/STL/map/', views.map_page, name='map_page'),
    path('articles/STL/pair_tuple/', views.pair_tuple_page, name='pair_tuple_page'),
    path('articles/STL/queue/', views.queue_page, name='queue_page'),
    path('articles/STL/set/', views.set_page, name='set_page'),
    path('articles/STL/stack/', views.stack_page, name='stack_page'),
    path('articles/STL/string/', views.string_page, name='string_page'),
    path('articles/STL/vector/', views.vector_page, name='vector_page'),
    
    #Algo contests
    path("articles/algo_concurs/lee/", views.lee_page, name="lee_page"),
    path("articles/algo_concurs/dijkstra/", views.dijkstra_page, name="dijkstra_page"),
    path("articles/algo_concurs/kruskal/", views.kruskal_page, name="kruskal_page"),

    # Arhivă personală
    path("articles/arhiva/kth1/", views.kth1_page, name="kth1_page"),

    # Grafuri și Arbori
    path("articles/grafuri/graphs/", views.graphs_page, name="graphs_page"),
    path("articles/grafuri/arbori/", views.arbori_page, name="arbori_page"),

    # Structuri de Date Avansate (SDA)
    path("articles/sda/aib/", views.aib_page, name="aib_page"),
    path("articles/sda/aint/", views.aint_page, name="aint_page"),
    path("articles/sda/avl/", views.avl_page, name="avl_page"),
    path("articles/sda/dsu/", views.dsu_page, name="dsu_page"),
    path("articles/sda/heap/", views.heap_page, name="heap_page"),
    path("articles/sda/red_black/", views.red_black_page, name="red_black_page"),
    path("articles/sda/splay/", views.splay_page, name="splay_page"),
    path("articles/sda/trie/", views.trie_page, name="trie_page")

]
