# SQL-to-Graphite

A tool to easily send the results of SQL queries to Graphite!

## Installation

```
pip install sql-to-graphite
```

## Running

```
export S2G_DSN="mysq://username:password@host/db"
cat queries.sql | sql-to-graphite --graphite-host graphite.example.com --graphite-prefix db.metrics
```
