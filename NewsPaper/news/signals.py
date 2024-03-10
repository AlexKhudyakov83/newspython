
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory



def send_motifications(preview, pk, title, subscribes, instance):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'http://127.0.0.1:8000/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(subject=title,
                                 body='',
                                 from_email= "askhudyakov83@yandex.ru",
                                 to=subscribes,
                                 )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribes_emails = []

        for cat in categories:
            subscribes = cat.subscribes.all()
            subscribes_emails += [s.email for s in subscribes]

        send_motifications(instance.preview(), instance.pk,
                           instance.title, subscribes_emails)



    # emails = User.objects.filter(
    #     subscriptions__category=instance.category
    # ).values_list('email', flat=True)
    #
    # subject = f'В интересующей вас категории {instance.category} новый контент'
    #
    # text_content = (
    #     f'Тема: {instance.title}\n'
    #     f'Можете ознакомиться по ссылке: http://127.0.0.1:8000{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Тема: {instance.title}<br>'
    #     f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    #     f'Ссылка для перехода</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()