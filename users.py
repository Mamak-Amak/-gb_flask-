from blog.models import User
from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template

users_app = Blueprint("users_app", __name__)
USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}
@users_app.route("/")
def users_list():
    return render_template("users/list.html", users=USERS)


@users_app.route("/", endpoint="list")
@users_app.route("/<int:user_id>/", endpoint="details")


@users_app.route("/<int:user_id>/")

def user_details(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id, user_name=user_name)


users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)

@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template("users/details.html", user=user)
