from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from blog.models.database import db
from blog.models import Author, Article
from blog.forms.article import CreateArticleForm

articles_app = Blueprint("articles_app", __name__)
@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)

@articles_app.route("/<int:article_id>/", endpoint="details")
@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required

def article_detals(article_id):
    form.tags.choices = [(tag.id, tag.name)
                         for tag in Tag.query.order_by("name")]
    
    if request.method == "POST" and form.validate_on_submit():
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    article = Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags)  
    ).one_or_none()

    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)

    

