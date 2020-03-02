# -*- encoding: utf-8 -*-
# @ModuleName: whatweb
# @Function:
# @Author: huigou
# @Time: 2020/1/9 上午11:15
import asyncio
import collections
import json
import re
import shlex
import odf.script
import os

_VersionInfo = collections.namedtuple(
    "WhatWebVersion", ['major', 'minor', 'micro'])

byo_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'./WhatWeb/whatweb')

_whatweb_search_path = (
    byo_path, 'whatweb', '/usr/bin/whatweb', '/usr/local/bin/whatweb')

regex_warning = re.compile('^Warning: .*', re.IGNORECASE)
regex_whatweb_banner = re.compile(
    'WhatWeb version ([0-9]+)\.([0-9]+)(?:\.([0-9])+)[^ ]* \( https?://.* \)')


class WhatWeb(object):
    def __init__(self, exe_search_path=_whatweb_search_path):
        self._search_path = exe_search_path
        self._version_info = None
        self._whatweb_path = None

    @asyncio.coroutine
    def _ensure_path_and_version(self):
        if self._whatweb_path:
            return
        is_found = False

        for whatweb_path in self._search_path:
            proc = None
            try:
                proc = yield from asyncio.create_subprocess_exec(whatweb_path, '--version',
                                                                 stdout=asyncio.subprocess.PIPE)
                while True:
                    line = yield from proc.stdout.readline()
                    line = line.decode('utf8')
                    match_info = regex_whatweb_banner.match(line)
                    if match_info is None:
                        continue
                    is_found = True
                    self._whatweb_path = whatweb_path

                    versions = match_info.groups()
                    if len(versions) == 2:
                        self._version_info = _VersionInfo(
                            major=int(versions[0]), minor=int(versions[1]))
                    else:
                        self._version_info = _VersionInfo(major=int(versions[0]), minor=int(versions[1]),
                                                          micro=int(versions[2]))
                    break
                    if proc.stdout.at_eof():
                        break
            except:
                pass
            else:
                if is_found:
                    break
            finally:
                if proc:
                    try:
                        proc.terminate()
                    except ProcessLookupError:
                        pass
                    yield from proc.wait()
        if not is_found:
            raise WhatWebError('whatweb was not found in path')

    @asyncio.coroutine
    def version(self):
        yield from self._ensure_path_and_version()
        return self._version_info

    @asyncio.coroutine
    def scan(self, targets, arguments=None):
        yield from self._ensure_path_and_version()
        args = self._get_scan_args(targets, arguments)
        return (yield from self._scan_proc(args))

    @asyncio.coroutine
    def _scan_proc(self, args):
        proc = None
        try:
            proc = yield from asyncio.create_subprocess_exec(self._whatweb_path, *args, stdout=asyncio.subprocess.PIPE,
                                                             stderr=asyncio.subprocess.PIPE)
            whatweb_output, whatweb_err = yield from proc.communicate()
        except:
            raise
        finally:
            if proc:
                try:
                    proc.terminate()
                except ProcessLookupError:
                    pass
                yield from proc.wait()
        if whatweb_output:
            try:
                whatweb_output = whatweb_output.decode('utf8')
                return json.loads(whatweb_output, encoding='utf-8')
            except:
                if whatweb_err:
                    raise WhatWebError(whatweb_err.decode('utf8'))
                else:
                    raise
        elif whatweb_err:
            raise WhatWebError(whatweb_err.decode('utf8'))

    def _get_scan_args(self, targets, arguments):
        assert isinstance(targets, (
            str, collections.Iterable)), 'Wrong type for [hosts], should be a string or Iterable [was {0}]'.format(
            type(targets))
        assert isinstance(arguments,
                          (str, type(None))), 'Wrong type for [arguments], should be a string [was {0}]'.format(
            type(arguments))  # noqa

        if not isinstance(targets, str):
            targets = ' '.join(targets)
        if arguments:
            assert all(_ not in arguments for _ in (
                '--log-json',)), 'can set log option'
            scan_args = shlex.split(arguments)
        else:
            scan_args = []
        targets_args = shlex.split(targets)
        return ['--log-json=-', '-q'] + targets_args + scan_args


class WhatWebError(Exception):
    """
    Exception error class for WhatWeb class
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return 'WhatWebError exception {0}'.format(self.value)
