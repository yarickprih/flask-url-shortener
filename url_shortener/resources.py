from datetime import datetime

from flask import redirect, request
from flask_restful import Resource
from url_shortener import db

from .models import URL
from .schema import url_schema, urls_schema


class URLListResource(Resource):
    def get(self):
        urls = URL.query.all()
        if len(urls) == 0:
            return {"message": "There are no records yet."}
        return urls_schema.dump(urls)

    def post(self):
        new_url = URL(
            original_url=request.json["original_url"],
            expire_in=request.json["expire_in"],
        )

        if new_url.expire_in < 1 or new_url.expire_in > 365:
            return "", 404
        else:
            db.session.add(new_url)
            db.session.commit()
            return url_schema.dump(new_url)


class URLResource(Resource):
    def get(self, url_id):
        url = URL.query.get_or_404(url_id)
        return url_schema.dump(url)

    def patch(self, url_id):
        url = URL.query.get_or_404(url_id)

        if "original_url" in request.json:
            url.original_url = request.json["original_url"]
        if "expire_in" in request.json:
            url.expire_in = request.json["expire_in"]

        db.session.commit()
        return url_schema.dump(url)

    def delete(self, url_id):
        url = URL.query.get_or_404(url_id)
        db.session.delete(url)
        db.session.commit()
        return {"message": f"URL with id '{url.id}' was deleted"}


class URLRedirectResource(Resource):
    def get(self, shortened_url):
        url = URL.query.filter_by(shortened_url=shortened_url).first()
        if url_expired(url):
            db.session.delete(url)
            db.session.commit()
            return {"status": "Link was expired"}
        return redirect(url.original_url)


def url_expired(url):
    return url.expire_in < ((datetime.now() - url.created_at).total_seconds() // 60)
