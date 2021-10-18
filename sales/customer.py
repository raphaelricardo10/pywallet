class Customer:

    def __init__(self, name: str, document: str) -> None:
        self.name = name
        self.document = document

    class Error(Exception):
        """Base class for errors"""
        pass

    class InvalidDocumentError(Error):
        """Raised when the input CPF is invalid"""
        pass

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        try:
            self._document = Customer.validateDocument(value)
        except:
            raise

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The customer name cannot be in blank")

        self._name = value

    def validateDocument(document: str) -> str:
        numberLst = []
        digits = ""

        # Transform all the digits of string in a list for better handling
        for char in document:
            if char.isdigit():
                numberLst.append(int(char))
                digits += char

        # Check if there are 11 digits
        if len(numberLst) != 11:
            raise Customer.InvalidDocumentError

        """
        Check if all the numbers are the same
        This is a valid CPF with this algorithm, but it is not used
        """
        if numberLst == numberLst[::-1]:
            raise Customer.InvalidDocumentError

        # Validate both document digits
        for i in range(9, 11):
            value = sum((numberLst[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != numberLst[i]:
                raise Customer.InvalidDocumentError

        return digits