# coding: utf-8

import argparse
import os
import sys


def cmd_line_parser(argv=None):
    """
    CmdLine Parser
    :param argv:
    :return:
    """
    if not argv:
        argv = sys.argv
    _ = os.path.basename(argv[0])

    usage = "cli.py [options]"
    parser = argparse.ArgumentParser(prog='PyWhatWeb', usage=usage)
    parser.add_argument("-u", "--url", dest="url", help="URL")
    parser.add_argument("-f", "--input-file", dest="input_file", help="")
    parser.add_argument("--aggression", dest="aggression", help="aggression")
    parser.add_argument("--user", dest="user",
                        help="<user:password> HTTP basic authentication.")
    parser.add_argument("--cookie", dest="cookie",
                        help="name=value;name1=value;")
    parser.add_argument("--user-agent", dest="user_agent", help="Identify as AGENT")
    parser.add_argument("--proxy", dest="proxy", help="<hostname[:port]> Set proxy hostname and port. Default: 8080.")
    parser.add_argument("--proxy-user", dest="proxy_user", help="<username:password> Set proxy user and password.")
    parser.add_argument(
        "--open-timeout", dest="open_timeout", default=15, help="Time in seconds. Default: 15.")
    parser.add_argument(
        "--read-timeout", dest="read_timeout", default=30, help="ime in seconds. Default: 30")
    parser.add_argument("--max-threads", dest="max_threads", default=25, help="run threads number")
    args = parser.parse_args()

    if not any((args.url, args.input_file)):
        err_msg = "missing a mandatory option"
        err_msg += "Use -h "
        parser.error(err_msg)

    return args
