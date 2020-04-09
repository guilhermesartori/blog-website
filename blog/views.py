from django.shortcuts import render

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2020'
	},
	{
		'author': 'JAne Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2020'
	}

]

def home(request):
	context = {
		'posts': posts,
		'title': 'Home'
	}
	return render(request, 'blog/home.html', context)

def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'blog/about.html', context)
