from url_shortener import api

from .resources import URLListResource, URLRedirectResource, URLResource

api.add_resource(URLRedirectResource, "/<string:shortened_url>")
api.add_resource(URLListResource, "/urls")
api.add_resource(URLResource, "/urls/<int:url_id>")
