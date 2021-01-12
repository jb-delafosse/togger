from flask import current_app

from togger.auth.auth_dao import prepare_email
from togger.auth.models import User
from togger.notifications.dtos import MailContext
from togger.notifications.interfaces.sender.gateways import INotificationSender


class MailSender(INotificationSender):
    def send_notification(self, user: User, mail_context: MailContext) -> None:
        token = user.generate_validate_token()
        url = current_app.config["APP_URL"] + "/auth/verify/" + token
        subject = "[Togger] Welcome to Togger. Verify your email"
        prepare_email(user.username, subject, url)
