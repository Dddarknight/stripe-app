from django.views import generic


class SuccessView(generic.TemplateView):
    template_name = 'success.html'


class CancelView(generic.TemplateView):
    template_name = 'cancel.html'
