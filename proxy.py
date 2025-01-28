# Proxy.py
# Simple demonstration of the Proxy pattern.

class Implementation2:
    lock = True
    hog = 0

    def next_data(self, masked_password):
        masked_expected_pass = '12345'
        if masked_password == masked_expected_pass:
            return "I just got data using the password"
        else:
            return "invalid password"

    def nextpotentiallylockeddata(self):
        print('This function could be called multiple times while locked')

    def mycustomfunc(self):
        print("running Implementation2.myCustomFunc")

    def secretfunction1(self):
        print('secret')

    def secret_function2(self):
        print('secret')

    def defaultBehavior(self):
        print("attribute not found")

    def resourceHog(self):
        self.hog = self.hog+1
        print("running the hog")

    def resourceProtection(self):
        print("too many resources to run the hog")

    def lock_protection(self):
        return "this resource is locked and we are handling it"


class Proxy2:
    def __init__(self):
        self.__implementation = Implementation2()

    def __getattr__(self, name):
        if name == 'nextData':
            return getattr(self.__implementation, name)("12345")
        elif name == 'nextpotentiallylockeddata':
            if getattr(self.__implementation, 'lock'):
                return getattr(self.__implementation, 'lockProtection')()
            else:
                return getattr(self.__implementation, name)()
        elif name == 'resourceHog':
            if getattr(self.__implementation, 'hog') < 2:
                return getattr(self.__implementation, name)
            else:
                return getattr(self.__implementation, 'resourceProtection')
        elif name[0:6] != 'secret':
            return getattr(self.__implementation, name)
        return getattr(self.__implementation, 'defaultBehavior')


p = Proxy2()
print(p.nextData)
p.mycustomfunc()
p.secretFunction1()
p.secretFunction2()
p.resourceHog()
p.resourceHog()
p.resourceHog()
print(p.nextpotentiallylockeddata)
