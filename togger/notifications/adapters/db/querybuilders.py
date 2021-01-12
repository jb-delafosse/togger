from datetime import datetime
from typing import List

from togger.auth.models import User
from togger.event.event_dao import get_recur_events
from togger.event.models import Event
from togger.notifications.interfaces.db.gateways import IToggerDatabase


class SqlToggerDatabase(IToggerDatabase):
    def get_events(self, start: datetime, end: datetime) -> List[Event]:
        events = (
            Event.query.filter(Event.start <= end)
                .filter(Event.end >= start)
                .all()
        )
        recur_events_unboxed = list(
            filter(lambda event: event.recur_id is not None, events)
        )
        events.extend(get_recur_events(start, end, recur_events_unboxed))
        events = list(filter(lambda event: event.hide is not True, events))
        return events

    def get_all_verified_users(self) -> List[User]:
        users = User.query.filter(User.is_verified).all()
        return users
