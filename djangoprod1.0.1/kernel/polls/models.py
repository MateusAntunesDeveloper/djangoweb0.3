from django.db import models


class PostGree(models.Model):
        user = models.CharField(max_length=45)
        body = models.TextField()
        create_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            
            return self.user, self.body, self.create_at


#models test 