from rest_auth.views import LoginView


###############################################################
### Added by:SHIFULLAH
### For Login
###############################################################
class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response() 
        return orginal_response 
