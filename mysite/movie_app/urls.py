from django.urls import path, include
from .views import (UserProfileDetailAPIView, UserProfileListAPIView,CategoryListAPIView,CategoryDetailAPIView,GenreListAPIView,GenreDetailAPIView,
                    CountryListAPIView, CountryDetailAPIVew, DirectorLisAPIView,
                    DirectorDetailAPIView,ActorListAPIView,ActorDetailAPIView, ActorImageViewSet,MovieListAPIView,MovieDetailAPIView,
                    MovieFrameViewSet, MovieVideoViewSet, RatingCreateAPIView, ReviewViewSet,
                    ReviewLikeViewSet, FavoriteItemViewSet, FavoriteViewSet,HistoryViewSet, RegisterView,
                    LoginView, LogoutView)


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'review', ReviewViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'actorimage', ActorImageViewSet)
router.register(r'favoriteitems', FavoriteItemViewSet)
router.register(r'movievideo', MovieVideoViewSet)
router.register(r'movieframe', MovieFrameViewSet)
router.register(r'reviewlike', ReviewLikeViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIVew.as_view(), name='country_detail'),
    path('director/', DirectorLisAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('user/',UserProfileDetailAPIView.as_view(), name = 'user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name= 'user_detail'),
    path('rating/', RatingCreateAPIView.as_view(),name='rating_list'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
