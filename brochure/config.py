import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = u'postgresql+psycopg2://{}:{}@{}/{}'.format(
        os.environ['POSTGRES_USER'],
        os.environ['POSTGRES_PASS'],
        os.environ.get('POSTGRES_HOST', 'postgresql'),
        os.environ['POSTGRES_DB']
    )
