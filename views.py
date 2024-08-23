from django.shortcuts import render


def home(request):
    return render(request, 'fishstore/home.html')


def about(request):
    return render(request, 'fishstore/about.html')


def catalog(request):
    return render(request, 'fishstore/catalog.html')


def fish_detail(request, fish_name):
    fish_data = {
        'betta': {
            'name': 'Betta Fish',
            'description': 'Betta Fish are known for their vivid colors and long, flowing fins. They are a popular choice for fish enthusiasts.',
            'image': 'betta.avif',
            'price': 25.00
        },
        'clownfish': {
            'name': 'Clownfish',
            'description': 'Clownfish are small, brightly colored fish that live among sea anemones. They are best known from the movie Finding Nemo.',
            'image': 'clownfish.jpg',
            'price': 30.00
        },
        'angelfish': {
            'name': 'Angelfish',
            'description': 'Angelfish are a species of freshwater fish known for their unique shape and graceful swimming patterns. They are a favorite in home aquariums.',
            'image': 'angelfish.jpg',
            'price': 45.00
        }
    }
    fish = fish_data.get(fish_name, {})
    return render(request, 'fishstore/fish_detail.html', {'fish': fish})
