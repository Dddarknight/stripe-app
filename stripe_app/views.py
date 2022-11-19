from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class SuccessView(generic.TemplateView):
    template_name = 'success.html'


class CancelView(generic.TemplateView):
    template_name = 'cancel.html'
