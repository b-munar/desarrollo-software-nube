class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@database:5432/postgres"
    SECRET_KEY = 'La cabra 2.0'
    CELERY_BROKER_URL = "redis://broker:6379"
    CELERY_RESULT_BACKEND ="redis://broker:6379"
    CELERY_TASK_IGNORE_RESULT = True