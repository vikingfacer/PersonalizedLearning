class KVA:
    """KVA personality test class. takes a sequence of tuples """

    KVA_CODE = {
        3: "K",
        2: "V",
        1: "A"
    }

    def __init__(self, Sequence):
        self.sequence = Sequence
        self.answers = {1: 0,
                        2: 0,
                        3: 0}
        self.color = None
        self.key = None
        self.__countSequence()
        self.__returnPType()

    def __countSequence(self):
        for question in self.sequence:
            if question[1][0] is '1':
                self.answers[3] += 1

            elif question[1][0] is '2':
                self.answers[2] += 1

            elif question[1][0] is '3':
                self.answers[1] += 1

    def __returnPType(self):
        Max = 0
        # answers is only 3 elements long
        for each in self.answers:
            if self.answers[each] > Max:
                self.color = each
                Max = self.answers[each]
        self.key = KVA.KVA_CODE[self.color]
