from blog.models.tag import Tag
from blog.models import User
from blog.models.user import User


__all__ = [
    "User",
]


@app.cli.command("init-db")
def init_db():

    db.create_all()
    print("done!")
    
@app.cli.command("create-users")
def create_users():
    
    admin = User(username="admin", is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)


__all__ = [
    "User",
    "Author",
    "Article",
    "Tag",
]
