# coding: utf-8

import sys
import os
import asyncio

try:
    import pywhatweb
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from pywhatweb.lib.cmd import cmd_line_parser
from pywhatweb.lib.option import init_options, dis_finger, formater_json
from pywhatweb.thirdparty.loguru import logger

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    init_options(cmd_line_parser().__dict__)
    get_future = asyncio.ensure_future(dis_finger())
    loop.run_until_complete(get_future)
    datas = get_future.result()
    print(datas)
    formater_json(datas)
    logger.info('pywhatweb run finish')
