from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .utils import DataMixin
from .models import *
from .forms import FeedbackForm
# Create your views here.
descr =[
    {
        'Ремонтные работы': [
            {'Строительный ремонт': 'Выполняем строительные ремонтные работы для обновления и укрепления зданий и сооружений.'},
            {'Косметический ремонт': 'Проводим косметический ремонт с акцентом на улучшение внешнего вида помещений.'},
            {'Ремонт квартир и домов': 'Осуществляем полный ремонт квартир и домов, включая все необходимые мероприятия.'}
        ]
    },
    {
        'Сантехника': [
            {'Установка сантехники': 'Производим профессиональную установку сантехнического оборудования в ваших помещениях.'},
            {'Ремонт сантехники': 'Решаем проблемы с сантехникой, обеспечивая её надежную работу.'},
            {'Обслуживание систем водоснабжения': 'Предоставляем регулярное обслуживание и ремонт систем водоснабжения для безопасности и комфорта.'}
        ]
    },
    {
        'Установка окон': [
            {'Установка пластиковых окон': 'Монтаж высококачественных пластиковых окон для эффективной теплоизоляции и звукоизоляции.'},
            {'Установка деревянных окон': 'Устанавливаем деревянные окна, придающие вашему интерьеру уют и натуральную красоту.'},
            {'Установка алюминиевых окон': 'Монтаж алюминиевых окон для современного и стильного дизайна помещений.'}
        ]
    },
    {
        'Гипсокартонные работы': [
            {'Установка перегородок из гипсокартона': 'Создаем легкие и прочные перегородки из гипсокартона для планировки пространства.'},
            {'Построение фальшстенов': 'Изготавливаем фальшстены, обеспечивая скрытие коммуникаций и декоративное оформление.'},
            {'Установка потолков из гипсокартона': 'Устанавливаем гипсокартонные потолки с различными дизайнерскими решениями.'}
        ]
    },
    {
        'Электромонтаж': [
            {'Установка и замена электропроводки': 'Проводим электромонтажные работы, включая установку и замену электропроводки.'},
            {'Установка осветительных приборов': 'Монтируем осветительные приборы для создания яркого и комфортного освещения.'},
            {'Установка электрических розеток и выключателей': 'Устанавливаем электрические розетки и выключатели для удобства использования электроприборов.'}
        ]
    },
    {
        'Внутренняя отделка': [
            {'Укладка напольных покрытий': 'Производим укладку различных напольных покрытий, включая паркет, ламинат и ковровые покрытия.'},
            {'Оклеивание обоев': 'Оформляем ваши стены с помощью профессионального оклеивания обоев.'},
            {'Покраска стен и потолков': 'Окрашиваем стены и потолки, обеспечивая им стойкость и привлекательный внешний вид.'}
        ]
    }
]
def populate_servises(data):
    for cat in data:
        print(list(cat.items()))
        (cat_name, servises) = list(cat.items())[0]
        cat_db = Categories.objects.create(cat_tag='generated', cat_name=cat_name, cat_description=cat_name)
        for servise in servises:
            (servise_name, serv_descr) = list(servise.items())[0]
            Services.objects.create(serv_cat=cat_db, serv_tag='generated', serv_name=servise_name, serv_description=serv_descr, serv_unit=Units.objects.get(pk=3), serv_unit_price=1000)

class MainPage(DataMixin, FormView):
    template_name = 'main.html'
    form_class = FeedbackForm
    def get_context_data(self, **kwargs):
        # populate_servises(descr)
        context = super().get_context_data(**kwargs)
        c_def = self.get_mixin_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ServicesPage(DataMixin, FormView, TemplateView):
    template_name = 'service.html'
    form_class = FeedbackForm
    def get_context_data(self, service_tag, **kwargs):
        print('>>>vws servisepage params:', **kwargs)
        context = super().get_context_data(**kwargs)
        c_def = self.get_mixin_context()
        context = dict(list(context.items()) + list(c_def.items()))
        context['service'] = Services.objects.get(serv_tag=service_tag)
        context['slider_images'] = [f'{url}' for url in list(str(range(10)))] #КАКИЕ КАРТИНКИ ОТКУДА БЕРЕМ БАЗА(В КАКУЮ МОДЕЛЬ ИЛИ ОТДЕЛЬНО)? ИЛИ С ДИСКА
        return context