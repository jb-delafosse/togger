import itertools
from datetime import datetime, timedelta
from togger.notifications.interfaces import db
from togger.notifications.interfaces import sender


class NotifyUsecase:
    def __init__(self):
        self._db = db.gateways.TOGGER_DATABASE_FACTORY()
        self._notif_sender = sender.gateways.NOTIFICATION_SENDER_FACTORY()

    def notify_users(self, date: datetime):
        # get all users
        users = self._db.get_all_verified_users()

        # get all events that occurs in less than 3 days
        events = self._db.get_events(start=date, end=date + timedelta(days=3))
        for event, user in itertools.product(events, users):
            if not event.shifts:
                self._notif_sender.send_notif(user=user, event=event)

