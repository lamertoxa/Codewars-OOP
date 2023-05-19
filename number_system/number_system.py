def create_number_class(alphabet):
    class Number:
        length = len(alphabet)
        inverse_alphabet = {str(i): alphabet[i] for i in range(len(alphabet))}

        def __str__(self):
            return self.value

        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            instance.alphabet = {alphabet[i]: str(i) for i in range(len(alphabet))}

            return instance

        def __add__(self, other):

            result = self.value_dec + other.value_dec
            return Number(self.__convert_to(self, result))

        def __sub__(self, other):
            result = self.value_dec - other.value_dec
            return Number(self.__convert_to(self, result))

        def __mul__(self, other):
            result = self.value_dec * other.value_dec
            return Number(self.__convert_to(self, result))

        def __floordiv__(self, other):
            result = self.value_dec // other.value_dec
            return Number(self.__convert_to(self, result))

        def __init__(self, value):
            total_sum = 0

            for i in range(len(value) - 1, -1, -1):
                total_sum += int(self.alphabet[value[i]]) * self.length ** ((len(value) - i) - 1)
            self.value = value
            self.value_dec = total_sum
            self.last_result = None

        def __convert_to(self, _class, value):
            convert_num = value
            copy_num = convert_num
            new_value = ""
            while convert_num >= _class.length:
                convert_num = copy_num
                copy_num = copy_num // _class.length
                reminder_division = convert_num % _class.length

                new_value = new_value + _class.inverse_alphabet[str(reminder_division)]
            else:
                if copy_num != 0:
                    new_value += _class.inverse_alphabet[str(copy_num)]
            new_value = new_value[::-1]
            s_list = list(new_value)

            for i in range(len(s_list)):
                if s_list[i] != alphabet[0]:
                    break
            return ''.join(s_list[i:])

        def convert_to(self, _class):
            return self.__convert_to(_class, self.value_dec)

    return Number