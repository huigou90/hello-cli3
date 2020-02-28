

指纹识别

exe_search_path指定whatweb的路径

```python
import asyncio
import whatweb


async def main():
    scanner = whatweb.WhatWeb(exe_search_path=('/Users/huigou/pentest/WhatWeb/whatweb',))
    result = await scanner.scan("http://127.0.0.1:7001")
    print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

```