from django.shortcuts import render, redirect

from shopapp.models import slider, banner_area, Main_Category, Product


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]

    main_category = Main_Category.objects.all()
    # .order_by('-id')
    product = Product.objects.filter(section__name="Top Deals of The Day")

    context = {
        'sliders': sliders,
        'banners': banners,
        'main_category': main_category,
        'product': product,

    }
    return render(request, 'main/home.html', context)


def PRODUCT_DETAILS(request, slug):
    product = Product.objects.filter(slug=slug)
    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')

    context = {
        'product': product,
    }
    return render(request, 'product/product_detail.html', context)


def Error404(request):
    return render(request, 'errors/404.html')
