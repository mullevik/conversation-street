"""
Contents:

- Custom pipeline item for the social-auth app
    https://python-social-auth.readthedocs.io/en/latest/pipeline.html

"""
from street.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    """Update (or create) the Profile model associated with this user"""

    if backend.name == 'facebook':
        # the social service is Facebook

        profile = None
        # noinspection PyUnresolvedReferences
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            # User does not have a profile yet, create one
            profile = Profile(user=user)
        finally:
            # The profile can now be filled with some more information
            profile.display_name = response.get('name')
            profile.social_service = Profile.SOCIAL_FACEBOOK
            profile.verified = True
            profile.profile_image_link = response.get('picture')["data"]["url"]
            profile.save()
