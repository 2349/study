from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from nomadgram.users import models as user_models


class TimeStampeModel(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Image(TimeStampeModel):

	""" Image Model """

	file = models.ImageField()
	location = models.CharField(max_length=140)
	caption = models.TextField()
	creator = models.ForeignKey(user_models.User, null=True, related_name='images', on_delete=models.PROTECT)

	@property
	def like_count(self):
		return self.likes.all().count()

	@property
	def comment_count(self):
		return self.comments.all().count()

	def __str__(self):
		return '{} - {}'.format(self.location, self.caption)

	class Meta:
		ordering = ['-created_at']


@python_2_unicode_compatible
class Comment(TimeStampeModel):

	""" Comment Model """

	message = models.TextField()
	creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
	image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='comments')

	def __str__(self):
		return self.message


@python_2_unicode_compatible
class Like(TimeStampeModel):

	""" Like Model """

	creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
	image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='likes')

	def __str__(self):
		return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)