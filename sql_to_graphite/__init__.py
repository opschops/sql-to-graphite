import argparse
import os
import socket
import sys
import time

import sqlalchemy

def get_executor(dsn):
    engine = sqlalchemy.create_engine(dsn, isolation_level='READ UNCOMMITTED')
    connection = engine.connect()
    return connection.execute

def get_info():
    parser = argparse.ArgumentParser(description='Send SQL results to Graphite')
    parser.add_argument('--graphite-host', metavar='graphite-host', type=str, nargs=1, default=None, help='Host to send metrics to')
    parser.add_argument('--graphite-port', metavar='graphite-port', type=int, nargs=1, default=2003, help='Graphite port to send metrics to')
    parser.add_argument('--graphite-prefix', metavar='graphite-prefix', type=str, nargs=1, default=['db'], help='Prefix for metrics')
    return parser.parse_args()

def run(graphite_host, graphite_port, graphite_prefix, queries, executor):
    data = []
    now = time.time()
    sock = _socket_for_host_port(graphite_host, graphite_port)
    data = map(executor, queries)
    for result in data:
        for line in result:
            metric, value = line[:2]
            metric = '{0}.{1} {2} {3}\n'.format(graphite_prefix, metric, value, now)
            print metric,
            sock.sendall(metric)
    sock.close()

def _socket_for_host_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    sock.settimeout(None)
    return sock


def main():
    dsn = os.environ.get('S2G_DSN')
    if dsn is None:
        print 'You must set your DSN in the environment variable `S2G_DSN`'
        sys.exit(1)

    queries = sys.stdin.readlines()
    args = get_info()
    run(
        args.graphite_host[0],
        args.graphite_port,
        args.graphite_prefix[0],
        queries,
        get_executor(dsn),
    )

if __name__ == '__main__':
    main()
