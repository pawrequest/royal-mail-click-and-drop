import os
from functools import lru_cache
from pathlib import Path
from typing import Self

from loguru import logger
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from royal_mail_click_and_drop import Configuration


def load_royal_mail_settings_env():
    rm_env = Path(os.getenv('ROYAL_MAIL_ENV'))
    if not rm_env or not rm_env.exists():
        raise ValueError(f'ROYAL_MAIL_ENV ({rm_env}) incorrectly set')
    print(f'Loading RoyalMail Settings from {rm_env}')
    return rm_env


def get_env(env_name: str = 'ROYAL_MAIL_ENV') -> Path:
    env = os.getenv(env_name)
    if not env:
        raise ValueError(f'{env_name} not set')
    env_path = Path(env)
    if not env_path.exists():
        raise ValueError(f'{env_path} not a valid path')
    logger.debug(f'Loading environment from {env_path}')
    return env_path


class RoyalMailSettings(BaseSettings):
    api_key: str
    base_url: str = r'https://api.parcel.royalmail.com/api/v1'
    config: Configuration | None = None

    @classmethod
    @lru_cache
    def from_env(cls, env_name='ROYAL_MAIL_ENV') -> Self:
        return cls(_env_file=get_env(env_name))

    @classmethod
    def from_env_file(cls, env_path: Path) -> Self:
        return cls(_env_file=env_path)

    @model_validator(mode='after')
    def configuration(self) -> Self:
        if self.config is None:
            self.config = Configuration(host=self.base_url)
            self.config.api_key['Bearer'] = self.api_key
        return self

    model_config = SettingsConfigDict()

