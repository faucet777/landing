from .models import *


class DataMixin:

    def get_mixin_context(self, **kwargs):
        context = kwargs
        context['aside_data'] = {}
        cats = Categories.objects.all()
        for cat in cats:
            services = Services.objects.filter(serv_cat=cat)
            context['aside_data'][cat] = list(services)
        print('utls mix_cont aside_data',context['aside_data'])
        return context
