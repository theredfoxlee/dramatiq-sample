#!/usr/bin/env python3


import dramatiq


from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.results.backends import RedisBackend
from dramatiq.results import Results


# Dramatiq initialization.
rabbitmq_broker = RabbitmqBroker(host='127.0.0.1', port=5672)
result_backend = RedisBackend(host='127.0.0.1', port=6379)
rabbitmq_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor(store_results=True)
def add(x, y):
    try:
        print(f'calculating sum: {x}+{y}')
        return {'result': x + y}
    except Exception as e:
        print(e)


def main():
    req = add.send(5, 6)
    print(req.get_result(block=True))
    

if __name__ == '__main__':
    main()
