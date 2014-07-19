from django.dispatch import Signal

from sitters.models import UserProfile

# A new user has registered.
user_registered = Signal(providing_args=["user", "request"])

# A user has activated his or her account.
user_activated = Signal(providing_args=["user", "request"])


def user_registered_callback(sender, user, request, **kwargs):
    pass
    #profile = UserProfile(user=user)
    #profile.is_owner = bool("is_owner" in request.POST and request.POST["is_owner"])
    #profile.is_sitter = bool("is_owner" in request.POST and request.POST["is_sitter"])
    #profile.phone = request.POST['phone']
    #profile.avatar = request.POST['avatar']
    ##profile.address = request.POST['address']
    #profile.city = request.POST['city']
    #profile.state = request.POST['state']
    #profile.zip_code = request.POST['zip_code']
    #profile.tagline = request.POST['tagline']
    #profile.description = request.POST['description']
    #profile.price = request.POST['price']
    ##pets
    ##sit_cats = request.POST['']
    ##sit_dogs = request.POST['']
    ##sit_birds = request.POST['']
    ##sit_other = request.POST['']
    ##profile.qualification = request.POST['qualification']
    #profile.not_willing_to_sit = request.POST['not_willing_to_sit']
    #profile.concerns = request.POST['concerns']

    #profile.save()

user_registered.connect(user_registered_callback)
