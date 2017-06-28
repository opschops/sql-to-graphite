# SQL-to-Graphite [![Build Status](https://travis-ci.org/opschops/sql-to-graphite.svg?branch=master)](https://travis-ci.org/opschops/sql-to-graphite)

A tool to easily send the results of SQL queries to Graphite!

## Installation

```
pip install sql-to-graphite
```

## Running

```
export S2G_DSN="mysql://username:password@host/db"
cat queries.sql | sql-to-graphite --graphite-host graphite.example.com --graphite-prefix db.metrics
```

The queries piped in should be a single query per line returning 2 columns. If there are more columns they will be ignored. The first column returned should be the metric name (minus the --graphite-prefix option) and the value.

```
SELECT "metric", 1+1;
SELECT "now", NOW();
```
