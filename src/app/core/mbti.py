from itertools import islice


class MBTI:
    RED = [
        0b1111,
        0b1110,
        0b0111,
        0b0110,
    ]

    BLUE = [
        0b1011,
        0b1010,
        0b0010,
        0b0011,
    ]

    ORANGE = [
        0b1001,
        0b0001,
        0b0000,
        0b1000,
    ]

    GREEN = [
        0b1101,
        0b1100,
        0b0101,
        0b0100,
    ]

    MBTI_CODES = {
        0b1111: "ENTJ",
        0b1110: "ENTP",
        0b0111: "INTJ",
        0b0110: "INTP",

        0b1011: "ESTJ",
        0b1010: "ESTJ",
        0b0010: "ISTP",
        0b0011: "ISTJ",

        0b1001: "ESFJ",
        0b0001: "ISFJ",
        0b0000: "ISFP",
        0b1000: "ESFP",

        0b1101: "ENFJ",
        0b1100: "ENFP",
        0b0101: "INFJ",
        0b0100: "INFP",
    }

    def __init__(self, questionnaire):
        self.questionnaire = questionnaire
        self.mbti_value = None
        self.color = None
        self.mbti_key = None

        self.__compute_mbti()
        self.color = self.__color()
        self.mbti_key = self.___key()

    def __compute_mbti(self):
        EI_value = self.__compute(islice(self.questionnaire, 0, 5))
        NS_value = self.__compute(islice(self.questionnaire, 0, 5))
        TF_value = self.__compute(islice(self.questionnaire, 0, 5))
        JP_value = self.__compute(islice(self.questionnaire, 0, 5))

        mbti_value = EI_value << 3
        mbti_value += NS_value << 2
        mbti_value += TF_value << 1
        mbti_value += JP_value

        self.mbti_value = mbti_value

    def ___key(self):
        return MBTI.MBTI_CODES[self.mbti_value]

    def __color(self):
        if self.mbti_value is None:
            raise TypeError("The MBTI value is None")

        if self.mbti_value in MBTI.RED:
            return 1
        elif self.mbti_value in MBTI.BLUE:
            return 2
        elif self.mbti_value in MBTI.ORANGE:
            return 3
        elif self.mbti_value in MBTI.GREEN:
            return 4

    def __compute(self, slice):
        total = 0
        for result in slice:
            # Access the tuple then the array
            total += int(result[1][0])

        average = total / 15

        if average > 0.5:
            return 1
        if average < 0.5:
            return 0
