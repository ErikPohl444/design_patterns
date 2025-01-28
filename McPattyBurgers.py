class McPattyBurgers:
    def __init__(self):
        self._apps = Apps('Quesadillas')
        self._frozenpatty = FrozenPatty()
        self._prepackagedbun = PrepackagedBun()

    def homemadeburger(self):
        self._apps.microwave()
        self._frozenpatty.zap()
        self._frozenpatty.slatherwith('ketchup')
        self._frozenpatty.slatherwith('mustard')
        self._prepackagedbun.fillandserve()


class Apps:
    def __init__(self, typeofapps):
        self.typeofapps = typeofapps

    def microwave(self):
        print("putting the ", self.typeofapps, " in the radiation box for 6 minutes")


class FrozenPatty:
    def zap(self):
        print("zap a frozen beef patty in the microwave")

    def slatherwith(self, condiment):
        print("smear some ", condiment, " on it")


class PrepackagedBun:
    def fillandserve(self):
        print("put everything but the apps in one of these buns from a plastic bag and serve")


def main():
    franchise = McPattyBurgers()
    franchise.homemadeburger()


if __name__ == '__main__':
    main()
