from abc import ABC, abstractmethod
from typing import Callable

from togger.auth.models import User
from togger.event.models import Event
from togger.notifications.dtos import MailContext


class INotificationSender(ABC):

    @abstractmethod
    def send_notification(self, user: User, mail_context: MailContext) -> None:
        pass


# The contract for a database gateway factory
NotificationSenderFactory = Callable[[], INotificationSender]

# The database gateway factory to use to get the good implementation of the INotifSender.
# It can be set in main or tests.
NOTIFICATION_SENDER_FACTORY: NotificationSenderFactory
