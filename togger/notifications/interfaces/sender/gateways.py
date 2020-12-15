from abc import ABC, abstractmethod
from typing import Callable

from togger.auth.models import User
from togger.event.models import Event


class INotificationSender(ABC):

    @abstractmethod
    def send_notif(self, user: User, event: Event) -> None:
        pass


# The contract for a database gateway factory
NotificationSenderFactory = Callable[[], INotificationSender]

# The database gateway factory to use to get the good implementation of the INotifSender.
# It can be set in main or tests.
NOTIFICATION_SENDER_FACTORY: NotificationSenderFactory
