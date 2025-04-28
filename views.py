#from django.shortcuts import render
#from watchlist_app.models import Movie
#from django.http import JsonResponse

#def movie_list(request):
 #   movies = Movie.objects.all()
  #  data = {
   #     'movies' : list(movies.values()),
    #}
    #return JsonResponse(data)
#def movie_details(request,pk):
 #   details = Movie.objects.get(pk=pk)
  #  data = {
   #     'movie name': details.name,
    #    'movie description': details.description 
    #}
    #return JsonResponse(data)