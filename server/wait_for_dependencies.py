import psycopg2

from talos.env import env


# Check connect to Postgres
config_db = env.db('TALOS_DATABASE_URL')
conn = psycopg2.connect(
    "dbname='{NAME}' user='{USER}' host='{HOST}' password='{PASSWORD}' connect_timeout=5".format(**config_db)
)
conn.close()
