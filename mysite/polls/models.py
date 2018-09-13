from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

@python_2_unicode_compatible
class Shader(models.Model):
    shader_name = models.CharField(max_length = 200, primary_key=True)
    shader_opaque =  models.CharField(max_length = 200)
    shader_uv = models.IntegerField()
    shader_vertex = models.BooleanField()
    def __str__(self):
        return self.shader_name