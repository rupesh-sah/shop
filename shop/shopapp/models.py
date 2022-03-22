from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save


class slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS', 'HOT DEALS'),
        ('New Arraivels', 'New Arraivels'),

    )

    Image = models.ImageField(upload_to='media/silder_img')
    DISCOUNT_DEAL = models.CharField(choices=DISCOUNT_DEAL, max_length=1000)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=2000)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=2000)

    def __str__(self):
        return self.Brand_Name


class banner_area(models.Model):
    image = models.ImageField(upload_to='media/banner_img')
    Discount_Deal = models.CharField(max_length=1000)
    Quality = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.Quality


class Main_Category(models.Model):
    name = models.CharField(max_length=120000)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name + "--" + self.main_category.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.category.main_category.name + "--" + self.category.name + "--" + self.name


class Section(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.CharField(max_length=500)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    Discount = models.IntegerField()
    # Product_Information = models.TextField()
    model_Name = models.CharField(max_length=100)
    Categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100)
    # Description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    Product_information = RichTextField(null=True)
    Description = RichTextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, Product)


class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Image_url = models.CharField(max_length=300)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)