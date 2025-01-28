class PAGovernor(object):
    class __OnlyOne:
        def __init__(self):
            print(f"the governor is {repr(self)}")
            self.policy = None

        def __str__(self):
            return repr(self) + self.policy
    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not PAGovernor.instance:
            print("an election occurred")
            PAGovernor.instance = PAGovernor.__OnlyOne()
        print("trying to instantiate a new governor, but the elected on is in place")
        return PAGovernor.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)


x = PAGovernor()
x.policy = 'infrastructure'
print(x)
y = PAGovernor()
y.policy = 'health care'
print(y)
z = PAGovernor()
z.policy = 'economy'
print(z)
print(x)
print(y)
