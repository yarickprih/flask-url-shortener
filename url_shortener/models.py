from random import choices
from datetime import datetime
import string

from url_shortener import db


class URL(db.Model):
    """URL Model description"""

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    shortened_url = db.Column(db.String(5), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.today())
    expire_in = db.Column(db.Integer, default=90)

    def __init__(self, original_url, expire_in, shortened_url=None, created_at=None):
        self.original_url = original_url
        self.created_at = datetime.today()
        if expire_in is None:
            self.expire_in = 90
        else:
            self.expire_in = expire_in
        self.shortened_url = self.generate_short_url()

    def generate_short_url(self):
        """Generates shortend url part"""

        # URL-allowed characters
        characters = string.digits + string.ascii_letters + "$-_.+!*'(),"

        # Random string of URL-allowed characters of length 5
        # Quantity of available variations of random strings would be
        # 2706784157 (77^5)
        shortened_url = "".join(choices(characters, k=5))

        # Returns True if such random string already exists
        exists = self.query.filter_by(shortened_url=shortened_url).first()

        if exists:
            pass
        return shortened_url
