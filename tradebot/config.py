from pydantic import BaseSettings


class Setting(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class APICredentialBybit(Setting):
    API_BYBIT_TEST_API_KEY: str
    API_BYBIT_TEST_API_SECRET: str

    @property
    def API_BYBIT_API_KEY(self):
        return self.API_BYBIT_TEST_API_KEY

    @property
    def API_BYBIT_API_SECRET(self):
        return self.API_BYBIT_TEST_API_SECRET
