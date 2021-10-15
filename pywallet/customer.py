class Customer:
    def __init__(self, cpf: str) -> None:
        self.cpf = cpf

    def validateCpf(cpf) -> None:
        #Get all digits from CPF string
        numbers = [int(char) for char in cpf if char.isdigit()]

        #Check if there are 11 digits
        if len(numbers) != 11:
            raise ValueError("The informed CPF is invalid")

        """
        Check if all the numbers are the same
        This is a valid CPF with this algorithm, but it is not used
        """
        if numbers == numbers[::-1]:
            raise ValueError("The informed CPF is invalid")

        #Validate both cpf digits
        for i in range(9, 11):
            value = sum((numbers[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != numbers[i]:
                raise ValueError("The informed CPF is invalid")