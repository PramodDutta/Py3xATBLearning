from abc import ABC, abstractmethod
class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Shubham(PyATB):

    def payFee(self):
        print("Paid")


shubham = Shubham()
shubham.enrolled()
