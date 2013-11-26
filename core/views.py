from django.contrib import messages
class MessageMixin(object):
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(MessageMixin, self).delete(self, request, *args, **kwargs)

