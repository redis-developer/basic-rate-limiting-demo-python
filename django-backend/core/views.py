import redis
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.views import View

import asyncio
from datetime import timedelta
from redis import Redis

redis = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
key = "PING"
limit = 10
period = timedelta(seconds=10)


def request_is_limited(r: Redis, k: str, lim: int, p: timedelta):
    if r.setnx(key, limit):
        r.expire(key, int(period.total_seconds()))
    bucket_val = r.get(key)
    if bucket_val and int(bucket_val) > 0:
        r.decrby(key, 1)
        return False
    return True


class GetPongView(View):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request, *args, **kwargs):
        if request_is_limited(redis, key, limit, period):
            return HttpResponse("Too many requests, please try again later.", status=429)
        return HttpResponse("PONG", status=200)

def index(request):
    context = {}
    return render(request, 'index.html', context)




