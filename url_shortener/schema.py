from url_shortener import ma


class URLSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "original_url",
            "shortened_url",
            "created_at",
            "expire_in",
        )


url_schema = URLSchema()
urls_schema = URLSchema(many=True)
