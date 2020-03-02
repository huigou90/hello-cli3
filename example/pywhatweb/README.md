
指纹识别工具

核心调用whatweb

```commandline
usage: cli.py [options]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL
  -f INPUT_FILE, --input-file INPUT_FILE
  --aggression AGGRESSION
                        aggression
  --user USER           <user:password> HTTP basic authentication.
  --cookie COOKIE       name=value;name1=value;
  --user-agent USER_AGENT
                        Identify as AGENT
  --proxy PROXY         <hostname[:port]> Set proxy hostname and port.
                        Default: 8080.
  --proxy-user PROXY_USER
                        <username:password> Set proxy user and password.
  --open-timeout OPEN_TIMEOUT
                        Time in seconds. Default: 15.
  --read-timeout READ_TIMEOUT
                        ime in seconds. Default: 30
  --max-threads MAX_THREADS
                        run threads number
```



API调用方式参考example.py文件

```python
# coding: utf-8
import asyncio
from api import init_options, dis_finger

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    json_argv = {
        'url': 'http://127.0.0.1:8080/shiro',
        'open_timeout': 15,
        'read_timeout': 30,
        'max_threads': 25
    }

    init_options(json_argv)
    get_fuuture = asyncio.ensure_future(dis_finger())
    loop.run_until_complete(get_fuuture)
    datas = get_fuuture.result()
    print(datas)
```
