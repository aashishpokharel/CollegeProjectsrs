# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating
#
# from django.db import models
#
#
# class Foo(models.Model):
#     bar = models.CharField(max_length=100)
#     ratings = GenericRelation(Rating, related_query_name='foos')
#
# Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')