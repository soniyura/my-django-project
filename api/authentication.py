from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True  # Allow all GET requests without authentication
        # Custom authentication logic can be added here
        return super().is_authenticated(request, **kwargs)