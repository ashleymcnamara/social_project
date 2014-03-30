from allaccess.views import *
from apps.user.models import *
import unicodedata


class AdditionalUserInfoCallback(OAuthCallback):
    def get_or_create_user(self, provider, access, info):
        "Create a shell auth.User."
        digest = hashlib.sha1(smart_bytes(access)).digest()
        # Base 64 encode to get below 30 characters
        # Removed padding characters
        username = force_text(base64.urlsafe_b64encode(digest)).replace('=', '')
        User = get_user_model()

        kwargs = {
            User.USERNAME_FIELD: username,
            'email': info.get('email'),
            'first_name': info.get('first_name'),
            'last_name': info.get('last_name'),
            'password': None
        }
        user = User.objects.create_user(**kwargs)
        api = access.api_client
        url = "https://graph.Twitter.com/" + info.get('username') + "/picture"
        avatar = api.request('get', url)
        userProfile = UserProfile()
        userProfile.user = user

        userProfile.avatar = unicodedata.normalize('NFKD', avatar.url).encode('ascii', 'ignore')
        UserProfile.save(userProfile)
        return user
