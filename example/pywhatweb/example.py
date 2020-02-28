# -*- encoding: utf-8 -*-
# @ModuleName: example
# @Function: 
# @Author: huigou
# @Time: 2020/1/9 上午11:31

import asyncio
import whatweb
import json
import sys

async def main():
    scanner = whatweb.WhatWeb(exe_search_path=('/Users/huigou/pentest/WhatWeb/whatweb',))
    result = await scanner.scan(sys.argv[1])
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
