from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL
# dialect+driver://username:password@host:port/database
# postgressql+asyncpg://jobTracker:9646568306g@S@localhost:5434/jobtracker_db
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file= ".env")
    app_name: str = "Job Tracker 3"

    #database details
    postgres_user : str
    postgres_password : str
    postgres_db : str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    @property
    def database_url(self) -> URL:
        database_url =  URL.create(
            drivername="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db
        )
        return database_url

#read and check all settings
settings = Settings()