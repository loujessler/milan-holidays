from django.shortcuts import render
from django.utils import translation
from django.utils.html  import strip_tags
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import get_connection, send_mail, EmailMultiAlternatives
# from django.utils.translation import ugettext as _
from .telegram import send_message
from django.template import RequestContext
from django.views.generic.list import ListView
from home.models import  Order, Car, Questions
from .forms import OrderForm


def orders(request):
    form = OrderForm(request.POST)
    car_class = Car.objects.all()
    last_car = Car.objects.last().id
    if request.method == "POST" and form.is_valid():
        form.save()
        last_order = Order.objects.last();
        #send message TELEGRAM for us
        message_for_us = "*ЗАКАЗ С MILAN-HOLIDAYS*:" + str(last_order.id) + "\n" + "*ИМЯ*: " +str(last_order.name) + "\n" + "*ТЕЛЕФОН*: " + str(last_order.phone) + "\n" + "*ОТКУДА*: " + str(last_order.from_transfer) + "\n" + "*ВРЕМЯ*: " + str(last_order.time_from) + "\n" + "*КУДА*: " + str(last_order.to_transfer)  + "\n" + "*КЛАСС*: " + str(last_order.class_transport) + "\n" + "*ПАССАЖИРОВ*: " + str(last_order.passenger)
        send_message(message_for_us)

        text = get_template('email/email.txt')
        html = get_template('email/email.html')

        #connections to yandex
        connection = get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_ssl=True
        )
        #send message for consumer
        subject, from_email, to = 'Ваш заказ Milan holidays', settings.EMAIL_HOST_USER, Order.objects.last().email
        text_content = text.render({'last_order': last_order})
        html_content = html.render({'last_order': last_order})
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return render(request, 'landing/completeOrder.html', locals())
        if not form.is_valid():
            raise forms.ValidationError('Some field is blank')
    return render(request, 'landing/orders.html', locals())


def main(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    car_class = Car.objects.all()
    return render(request, 'landing/index.html', locals())


def questions(request):
    questions = Questions.objects.all()
    return render(request, 'landing/questions.html', locals())


def confidential(request):

    return render(request, 'landing/confidential.html', locals())


def oferta(request):

    return render(request, 'landing/oferta.html', locals())

# social sites
def telegram(request):
    return HttpResponseRedirect('https://telegram.me/milan_holidays_bot')
def instagram(request):
    return HttpResponseRedirect('https://instagram.com/milan_holidays/')
    # return render(requests.get('https://telegram.me/milan_holidays_bot'))

def email(request):
    id = Order.objects.last().id
    name = Order.objects.last().name
    phone = Order.objects.last().phone
    email = Order.objects.last().email
    from_transfer = Order.objects.last().from_transfer
    time_from = Order.objects.last().time_from
    to_transfer = Order.objects.last().to_transfer
    class_transport = Order.objects.last().class_transport
    passenger = Order.objects.last().passenger
    children = Order.objects.last().children
    return_transfer = Order.objects.last().return_transfer
    time_return_transfer = Order.objects.last().time_return_transfer
    children_passenger = Order.objects.last().children_passenger
    chair_small = Order.objects.last().chair_small
    chair_middle = Order.objects.last().chair_middle
    chair_large = Order.objects.last().chair_large
    comment = Order.objects.last().comment
    created = Order.objects.last().created
    return render(request, 'email/email.html', locals())



# def e_handler404(request, exception, template_name="errors/error404.html"):
#     response = render_to_response("errors/error404.html")
#     response.status_code = 404
#     return response


# def e_handler404(request, *args, **argv):
#     response = render_to_response('errors/error404.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# def e_handler500(request, *args, **argv):
#     response = render_to_response('errors/error500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response
