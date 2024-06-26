from .models import MovieDetails,MovieReviews,Category
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from .forms import CategoryForm, MovieForm



# @login_required
def profile_view(request):
    # user = request.user
    profile = Profile.objects.first()
    return render(request, 'profiles/profile_view.html', {'user': profile.user, 'profile': profile})


# @login_required
def profile_edit(request):
    if request.method == 'POST':
        # user = request.user

        profile = Profile.objects.first()

        # Update user fields
        profile.user.username = request.POST.get('username')
        profile.user.email = request.POST.get('email')

        # Update profile fields
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']


        profile.save()

        messages.success(request, 'Your profile was successfully updated!')
        return redirect('profile_view')
    else:
        # user = request.user
        profile = Profile.objects.first() # TODO:change this according to logged in user

        return render(request, 'profiles/profile_edit.html', {'user': profile.user, 'profile': profile})


def movie_list(request):
    movies = MovieDetails.objects.all().order_by('category')
    movies_by_category = {}

    for movie in movies:
        if movie.category in movies_by_category:
            movies_by_category[movie.category].append(movie)
        else:
            movies_by_category[movie.category] = [movie]

    context = {
        'movies_by_category': movies_by_category,
    }
    return render(request, 'movie/movie_list.html', context)

def add_movie(request):
    categories = Category.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        poster = request.FILES.get('poster')
        actors = request.POST.get('actors')
        trailer_link = request.POST.get('trailer_link')
        category_id = request.POST.get('category')
        release_date = request.POST.get('release_date')
        profile = Profile.objects.get(id=1)  # TODO:change this according to logged in user

        category = Category.objects.filter(id=category_id).first()

        movie = MovieDetails(
            title=title,
            description=description,
            poster=poster,
            actors=actors,
            trailer_link=trailer_link,
            created_by=profile,
            category=category,
            release_date=release_date
        )
        movie.save()
        return redirect('list')
    return render(request, 'movie/add_movie.html', {'categories': categories})
def rate_movie(request, movie_id):
    movie = get_object_or_404(MovieDetails, pk=movie_id)
    if request.method == "POST":
        review = request.POST.get('review')
        rating = request.POST.get('rating')

        movie_review = MovieReviews(
            movies=movie,
            review=review,
            rating=rating
        )
        movie_review.save()
        return redirect('list')
    return render(request, 'movie/rate_movie.html', {'movie': movie})

def admin_panel(request):
    categories = Category.objects.all()
    movies = MovieDetails.objects.all()
    profiles = Profile.objects.all()
    category_form = CategoryForm()
    movie_form = MovieForm()
    context = {
        'categories': categories,
        'movies': movies,
        'profiles': profiles,
        'category_form': category_form,
        'movie_form': movie_form,
    }
    return render(request, 'admin_panel.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return redirect('admin_panel')


def admin_add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    return redirect('admin_panel')

def delete_movie(request,movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(MovieDetails, id=movie_id)
        movie.delete()
        return redirect('admin_panel')
    return redirect('admin_panel')


def delete_profile(request,profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=profile_id)
        profile.delete()
        return redirect('admin_panel')
    return redirect('admin_panel')
