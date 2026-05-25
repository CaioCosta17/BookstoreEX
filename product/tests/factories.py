import factory
from product.models.category import Category
from product.models.product import Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('text')
    active = True

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    description = factory.Faker('text')
    price = 49.90
    active = True

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)