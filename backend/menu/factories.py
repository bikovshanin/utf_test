
from factory import Faker, Iterator, django, fuzzy

from menu.models import Food, FoodCategory


class FoodCategoryFactory(django.DjangoModelFactory):
    """
    Фабрик для создания трёх категорий блюд.
    К категории Алкоголь не будет принадлежать ни одно блюдо.
    """
    class Meta:
        model = FoodCategory

    name_ru = Iterator(
        (
            'Напитки',
            'Выпечка',
            'Алкоголь',
        ),
    )


class DrinkFactory(django.DjangoModelFactory):
    """
    Фабрик для создания напитков.
    Все три напитка будут принадлежать категории Напитки.
    Поле is_publish будет всегда True.
    """
    class Meta:
        model = Food

    category = fuzzy.FuzzyChoice(
        FoodCategory.objects.filter(name_ru='Напитки'))
    code = Iterator(
        (
            1,
            2,
            3,
        )
    )
    internal_code = Iterator(
        (
            100,
            200,
            300,
        )
    )
    name_ru = Iterator(
        (
            'чай',
            'кофе',
            'кола',
        )
    )
    description_ru = Iterator(
        (
            'Чай 100 гр',
            'кофе',
            'кола',
        )
    )
    cost = '123.00'


class FoodFactory(django.DjangoModelFactory):
    """
    Фабрика по созданию выпечки.
    Все три блюда будут принадлежать к категории Выпечка.
    Поле is_publish может принимать случайное значение True/False,
    с вероятностью 50/50.
    """
    class Meta:
        model = Food

    is_publish = Faker('boolean', chance_of_getting_true=50)
    category = fuzzy.FuzzyChoice(
        FoodCategory.objects.filter(name_ru='Выпечка')
    )
    code = Iterator(
        (
            4,
            5,
            6,
        )
    )
    internal_code = Iterator(
        (
            400,
            500,
            600,
        )
    )
    name_ru = Iterator(
        (
            'Слойка',
            'Маффин',
            'Торт',
        )
    )
    description_ru = Iterator(
        (
            'Слойка',
            'Маффин',
            'Торт',
        )
    )
    cost = '123.00'
