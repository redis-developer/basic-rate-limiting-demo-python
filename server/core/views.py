from datetime import timedelta

import asyncio
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.views import View
from ipware import get_client_ip
from redis import Redis

if settings.REDIS_URL:
    redis_default = Redis.from_url(url=settings.REDIS_URL)
else:
    redis_default = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        db=settings.REDIS_DB
    )
key = 'PING'
limit = 10
period = timedelta(seconds=10)


def request_is_limited(red: Redis, redis_key: str, redis_limit: int, redis_period: timedelta):
    if red.setnx(redis_key, 0):
        red.expire(redis_key, int(redis_period.total_seconds()))
    bucket_val = red.incrby(redis_key, 1)
    return bucket_val and int(bucket_val) > redis_limit


class GetPongView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        ip, is_routable = get_client_ip(request)
        if request_is_limited(redis_default,  '%s:%s' % (ip, key), limit, period):
            return HttpResponse("Too many requests, please try again later.", status=429)
        return HttpResponse("PONG", status=200)


def index(request):
    context = {}
    return render(request, 'index.html', context)
