from wtforms import StringField,SubmitField,IntegerField,HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class ArticleFrom(FlaskForm):
    id = HiddenField('id')
    name=StringField('Name',validators=[DataRequired()])
    desc=StringField('Description')
    price=IntegerField('Price',validators=[DataRequired()])
    submit=SubmitField('Send')