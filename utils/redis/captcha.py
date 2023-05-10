#!.usr/bin/env python
# -*- coding: utf-8 -*-

import redis


pool = redis.ConnectionPool(host='192.168.2.15', port=6379,
                            password='foobared', encoding='utf-8', max_connections=1000)
conn = redis.Redis(connection_pool=pool)

conn.set('13485679617', 9999, ex=10)

value = conn.get('13485679617')
print(value)
