from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.article import ArticleList, ArticleDetail


def init_api(app):
    api = Api(app)
    api.route(TagList, "tag_list", "/api/tags/")

    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
    return api


def create_api_spec_plugin(app):

    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
    }
)
    return api_spec_plugin


def init_api(app):

    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(
        app,
        plugins=[
            api_spec_plugin,
    ],
)

    def init_api(app):
        event_plugin = EventPlugin()
        api_spec_plugin = create_api_spec_plugin(app)
        permission_plugin = PermissionPlugin(strict=False)
        api = Api(
            app,
            plugins=[
                event_plugin,
                api_spec_plugin,
                permission_plugin,
    ],
)
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail",
            "/api/authors/<int:id>/", tag="Author")
