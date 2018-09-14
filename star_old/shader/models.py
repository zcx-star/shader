from django.db import models

class Shader(models.Model):
    shader_name = models.CharField(max_length = 255, primary_key=True)
    shader_info = models.CharField(max_length = 255)
    shader_url = models.CharField(max_length = 255)
    shader_p4 = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.shader_name