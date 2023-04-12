from django.db.models.signals import post_save
from django.contrib.auth.models import User
# from django.contrib.auth.models import Group


from store.models import Customer

def customer_profile(sender, instance, created, **kwargs):
	if created:
		Customer.objects.create(
			user=instance,
			name=instance.username,
			email=instance.email,
			)
		print('Profile created!')

post_save.connect(customer_profile, sender=User)