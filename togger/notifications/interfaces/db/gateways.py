from abc import ABC, abstractmethod
from datetime import datetime
from typing import Callable, List

from togger.auth.models import User
from togger.event.models import Event


class IToggerDatabase(ABC):
    @abstractmethod
    def get_events(self, start: datetime, end: datetime) -> List[Event]:
        pass

    @abstractmethod
    def get_all_verified_users(self) -> List[User]:
        pass


# The contract for a database gateway factory
ToggerDatabaseFactory = Callable[[], IToggerDatabase]

# The database gateway factory to use to get the good implementation of the IToggerDatabase.
# It can be set in main or tests.
TOGGER_DATABASE_FACTORY: ToggerDatabaseFactory
