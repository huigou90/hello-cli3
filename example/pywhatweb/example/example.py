# coding: utf-8

import sys
import os
import asyncio

try:
    import pywhatweb
except ImportError:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from pywhatweb.api import init_options, dis_finger

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    json_argv = {
        'url': 'http://www.baidu.com',
        'open_timeout': 15,
        'read_timeout': 30,
        'max_threads': 25
    }
    
    init_options(json_argv)

    get_fuuture = asyncio.ensure_future(dis_finger())
    loop.run_until_complete(get_fuuture)
    datas = get_fuuture.result()
    print(datas)
