from celery import shared_task
import time

from NewsPaper.news.signals import send_motifications


@shared_task
def create_post():
    new_post = send_motifications()
    return new_post

