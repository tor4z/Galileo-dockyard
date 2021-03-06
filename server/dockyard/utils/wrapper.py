from dockyard.const import APIStatus

def auth(func):
    def _exec(self, *args, **kwargs):
        if not self.user:
            return self.error(APIStatus["STAT_API_USER_LOGIN"])
        else:
            return func(self, *args, **kwargs)
    return _exec

def auth_manager(func):
    def _exec(self, *args, **kwargs):
        if not self.manager:
            return self.error(APIStatus["STAT_API_MANAGER_LOGIN"])
        else:
            return func(self, *args, **kwargs)
    return _exec