

class KVA(object):
	"""KVA personality test class. takes a sequence of tuples """
	
	def __init__(self, Sequence):
		self.sequence = Sequence
		self.answers = {'K': 0,
						'V': 0,
						'A': 0 }
		self.Ptype = None
		self.__countSequence()
		self.__returnPType()


	def __countSequence(self):
		for question in self.sequence:
			if question[1] is 1:
				self.answers['K'] += 1

			elif question[1] is 2:
				self.answers['V'] += 1

			elif question[1] is 3:
				self.answers['A'] += 1

	def __returnPType(self):
		Max = 0
		# answers is only 3 elements long 
		for each in self.answers:
			if self.answers[each] > Max:
				self.Ptype = each
				Max = self.answers[each]



if __name__ == '__main__':
	testSequence = [(1,2),(2,3),(3,0),(4,1),(5,2),(6,0),(7,1),(8,3)]

	test = KVA(testSequence)
	print(test.Ptype)