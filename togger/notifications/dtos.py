from dataclasses import dataclass

from togger.calendar.models import Calendar
from togger.event.models import Event


@dataclass(frozen=True)
class MailContext:
    event: Event
    calendar: Calendar
