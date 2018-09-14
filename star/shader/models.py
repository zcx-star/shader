from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Shader(models.Model):
    shader_name = models.CharField(max_length = 200, primary_key=True)
    shader_opaque =  models.CharField(max_length = 200)
    shader_uv = models.IntegerField()
    shader_vertex = models.BooleanField()
    def __str__(self):
        return self.shader_name