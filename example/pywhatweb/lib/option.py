# coding: utf-8

import os
from pywhatweb.lib import whatweb
from pywhatweb.thirdparty.odict.attribdict import AttribDict
from pywhatweb.thirdparty.loguru import logger

conf = AttribDict()

white_list = ['aggression', 'user', 'cookie', 'user_agent', 'proxy', 'proxy-user', 'open-timeout', 'read-timeout',
              'max-threads', 'input-file']


def init():
    logger.info('start pywhatweb dis finger module')
    conf.url = None
    conf.command = None


def init_options(input_options=AttribDict()):
    logger.info('init input options')
    init()
    command = ''
    for key in input_options:
        _key = key.replace('_', '-')
        if _key in white_list and input_options.get(key) is not None:
            # print(_key, input_options.get(key))
            if _key == 'input-file':
                assert "not code"
                # command += '--input-file %s ' % os.path.abspath(input_options.get(key))
            else:
                command += '--' + _key + '=' + str(input_options.get(key)) + ' '
        if key == 'url':
            conf.url = input_options.get(key)
    conf.command = command
    logger.info('command : %s' % conf.command)


def formater_json(content):
    pass


async def dis_finger():
    logger.info('start call whatweb run ')
    scanner = whatweb.WhatWeb()
    result = await scanner.scan(conf.url, conf.command)
    logger.info('whatweb run finish')
    return result
