from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,length,DataRequired
from flask_wtf.file import FileField,file_allowed

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class UploadPitch(FlaskForm):
    category=SelectField('Select Category',validators=[DataRequired()],choices=[('Interview Pitch','Interview Pitch'),
                                                    ('Products Pitch','Products Pitch'),
                                                    ('Tech Pitch','Tech Pitch'),
                                                    ('Political Pitch','Political Pitch'),
                                                    ('Religious Pitch','Religious Pitch'),
                                                    ('Pickup Lines','Pickup Lines'),
                                                    ('Others','None of the above')])
    pitch=TextAreaField('Write Pitch:',validators=[DataRequired()])
    submit=SubmitField('Post Pitch')
  
class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')