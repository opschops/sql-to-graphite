import argparse
import os
import socket
import sys
import time

import sqlalchemy

def get_executor(dsn):
    engine = sqlalchemy.create_engine(dsn)
    connection = engine.connect()
    return connection.execute

def get_info():
    parser = argparse.ArgumentParser(description='Send Klout scores to Graphite')
    parser.add_argument('--graphite-host', metavar='graphite-host', type=str, nargs=1, default=None, help='Host to send metrics to')
    parser.add_argument('--graphite-port', metavar='graphite-port', type=int, nargs=1, default=2003, help='Graphite port to send metrics to')
    parser.add_argument('--graphite-prefix', metavar='graphite-prefix', type=str, nargs=1, default='klout', help='Prefix for metrics')
    return parser.parse_args()


def main():
    dsn = os.environ.get('S2G_DSN')
    if key is None:
        print 'You must set your DSN in the environment variable `S2G_DSN`'
        sys.exit(1)

