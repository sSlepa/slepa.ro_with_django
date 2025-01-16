from django.shortcuts import render

# Pagini principale
def main(request):
    return render(request, "main.html")

def course(request):
    return render(request, "course.html")

def contact_page(request):
    return render(request, "contact.html")

def usefull_webs(request):
    return render(request, "usefull_websites.html")

# Articole generale
def string_page(request):
    return render(request, "articles/STL/string.html")

def stl_page(request):
    return render(request, "articles/STL.html")

def grafuri_arbori_page(request):
    return render(request, "articles/grafuri_arbori.html")

def structuri_avansate_page(request):
    return render(request, "articles/structuri_avansate.html")

def concursuri_page(request):
    return render(request, "articles/concursuri.html")

def archive_page(request):
    return render(request, "articles/archive.html")

def measure_time_page(request):
    return render(request, "articles/measure_time.html")

# Diverse STL
def diverse_stl_page(request):
    return render(request, "articles/STL/diverseSTL.html")

def map_page(request):
    return render(request, "articles/STL/map.html")

def pair_tuple_page(request):
    return render(request, "articles/STL/pair&tuple.html")

def queue_page(request):
    return render(request, "articles/STL/queue.html")

def set_page(request):
    return render(request, "articles/STL/set.html")

def stack_page(request):
    return render(request, "articles/STL/stack.html")

def vector_page(request):
    return render(request, "articles/STL/vector.html")

# Algoritmi pentru concursuri
def lee_page(request):
    return render(request, "articles/algo_concurs/lee.html")

def dijkstra_page(request):
    return render(request, "articles/algo_concurs/dijkstra.html")

def kruskal_page(request):
    return render(request, "articles/algo_concurs/kruskal.html")

# Arhivă personală
def kth1_page(request):
    return render(request, "articles/arhiva/kth1.html")

# Grafuri și Arbori
def graphs_page(request):
    return render(request, "articles/grafuri/graphs.html")

def arbori_page(request):
    return render(request, "articles/grafuri/arbori.html")

# Structuri de Date Avansate (SDA)
def aib_page(request):
    return render(request, "articles/sda/aib.html")

def aint_page(request):
    return render(request, "articles/sda/aint.html")

def avl_page(request):
    return render(request, "articles/sda/avl.html")

def dsu_page(request):
    return render(request, "articles/sda/dsu.html")

def heap_page(request):
    return render(request, "articles/sda/heap.html")

def red_black_page(request):
    return render(request, "articles/sda/red_black.html")

def splay_page(request):
    return render(request, "articles/sda/splay.html")

def trie_page(request):
    return render(request, "articles/sda/trie.html")

