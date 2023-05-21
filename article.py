from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from blog.models.article_tag import article_tag_association_table


class Article(db.Model):

    tags = relationship(
    "Tag",
    secondary=article_tag_association_table,
    back_populates="articles",

        title=Column(String(200), nullable=False,
                     default="", server_default="")
        body=Column(Text, nullable=False, default="", server_default="")
        dt_created=Column(DateTime, default=datetime.utcnow,
                          server_default=func.now())
        dt_updated=Column(DateTime, default=datetime.utcnow,
                          onupdate=datetime.utcnow)
    )


class CreateArticleForm(FlaskForm):

    title = StringField(
    "Title",
    [validators.DataRequired()],
)
    body = TextAreaField(
    "Body",
    [validators.DataRequired()],
)
    submit = SubmitField("Publish")
