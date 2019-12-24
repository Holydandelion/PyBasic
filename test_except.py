
class UserException(Exception):
    def printName(self):
        print(self)


if(__name__ == "__main__"):

    # exception of base class will be cpatured by except of derived exception
    class B(Exception):
        pass


    class C(B):
        pass


    class D(C):
        pass


    for cls in [B, C, D]:
        try:
            raise cls()

        except B:
            print("B")
        except D:
            print("D")
        except C:
            print("C")

    for cls in [B, C, D]:
        try:
            raise cls()

        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

    # exception is a class instance.
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))

            print(x/y)
            raise UserException("defined by user")
        except ZeroDivisionError:
            print("divisor can not be 0 ")

        except UserException  as e:
            e.printName()
            try:
                e.printOthers()
            except AttributeError:
                print("e has not attribute 'printOthers'")

        except:
            print("must be number")
        else:
            print("nothing wrong")
            break

        finally:
            print('finnaly, always come here.')



