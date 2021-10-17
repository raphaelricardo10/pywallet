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
            Customer.validateDocument(value)
        except:
            raise

        self._document = value

    def validateDocument(document: str) -> None:
        #Get all digits from CPF string
        numbers = [int(char) for char in document if char.isdigit()]

        #Check if there are 11 digits
        if len(numbers) != 11:
            raise Customer.InvalidDocumentError

        """
        Check if all the numbers are the same
        This is a valid CPF with this algorithm, but it is not used
        """
        if numbers == numbers[::-1]:
            raise Customer.InvalidDocumentError

        #Validate both document digits
        for i in range(9, 11):
            value = sum((numbers[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != numbers[i]:
                raise Customer.InvalidDocumentError