

class KVA(object):
	"""KVA personality test class. takes a sequence of tuples """

	def __init__(self, Sequence):
		self.sequence = Sequence
		self.answers = { 1: 0,
						 2: 0,
						 3: 0 }
		self.color = None
		self.__countSequence()
		self.__returnPType()


	def __countSequence(self):
		for question in self.sequence:
			if question[1] is 1:
				self.answers[1] += 1

			elif question[1] is 2:
				self.answers[2] += 1

			elif question[1] is 3:
				self.answers[3] += 1

	def __returnPType(self):
		Max = 0
		# answers is only 3 elements long
		for each in self.answers:
			if self.answers[each] > Max:
				self.color = each
				Max = self.answers[each]



if __name__ == '__main__':
	testSequence = [(1,2),(2,3),(3,1),(4,1),(5,2),(6,2),(7,3),(8,3),(9,1)]

	test = KVA(testSequence)
	print(test.color)