from django.db import models

class BugPic(models.Model):
    user = models.CharField(max_length = 30)
    img = models.ImageField(upload_to='whereYouAre')
    time = models.DateTimeField()
    vote_problem = models.IntegerField(default=0)
    vote_useful = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%d' % (self.id)