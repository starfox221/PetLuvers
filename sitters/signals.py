from registration.signals import user_registered

def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.is_owner = bool(request.POST["is_owner"])
    profile.is_sitter = bool(request.POST["is_sitter"])
    profile.save()

user_registered.connect(user_registered_callback)
