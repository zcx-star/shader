from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Shader(models.Model):
    SHADER_SURFACETYPE = (
    (0,'Opqaue'),
    (1,'Transparent'),
    (2,'Translucent'),
    )
    shader_name = models.CharField( max_length = 200, primary_key=True )
    shader_vertexColor = models.BooleanField()
    shader_uvSet = models.IntegerField()
    shader_surfaceType = models.IntegerField(choices = SHADER_SURFACETYPE)
    shader_complexity = models.IntegerField()
    shader_textures = models.IntegerField()
    shader_diffuseTex = models.IntegerField()
    shader_normalTex = models.IntegerField()
    shader_SMDTex = models.IntegerField()
    shader_uvTint = models.BooleanField()
    shader_maskTint = models.BooleanField()
    shader_globalDirt = models.BooleanField()
    shader_emissive = models.BooleanField()
    shader_wetness = models.BooleanField()
    shader_parallax = models.BooleanField()
    shader_retroReflect = models.BooleanField()
    def __str__(self):
        return self.shader_name