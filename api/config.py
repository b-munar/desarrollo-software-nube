class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database:5432/postgres"
    SECRET_KEY = 'La cabra 2.0'
    CELERY=dict(
        broker_url="redis://broker:6379",
        result_backend="redis://broker:6379",
        task_ignore_result=True,
    )