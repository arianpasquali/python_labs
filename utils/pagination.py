import numpy as np
import itertools

class Paginator(object):

	def __init__(self, total_pages, current_page=1, boundaries=0, around=0):
		
		self.boundaries = boundaries
		self.around = around
		self.total_pages = total_pages
		self.current_page = current_page

		# check basic restrictions
		if(self.boundaries < 0):
			raise ValueError('boundaries accepts only positive values. %f is invalid' % (self.boundaries))

		if(self.around < 0):
			raise ValueError('around accepts only positive values. %f is invalid' % (self.around))
		
		if(self.current_page > total_pages):
			raise ValueError('current_page cannot be higher than total_pages. %f is invalid as current_page' % (self.current_page))

		if(self.current_page <= 0):
			raise ValueError('current_page accepts only positive values. %f is invalid' % (self.current_page))

	def __handle_sequence_intervals(self,sequence,following_sequence):
		if(len(sequence) > 0 and len(following_sequence) > 0):
			if((sequence[-1] + 1) < following_sequence[0]):
				# interval symbol
				sequence += "."
		sequence += following_sequence
		return sequence

	def paginate(self):
		
		head = []
		mid = []
		tail = []
		sequence = []
		
		# head
		if(self.boundaries > 0):
			head = range(1,self.boundaries + 1)
		
		# tail
		tail = range(self.total_pages - self.boundaries + 1, self.total_pages + 1)

		# around current_page
		if(self.around > 0):
			start_mid = self.current_page - (self.around)
			end_mid = self.current_page + (self.around + 1)

			mid = range(start_mid,end_mid)
		else:
			mid = [self.current_page]
		
		# ignore intersection
		mid = set(mid) - set(head)
		mid = sorted(list(mid))
		
		# ignore intersection
		tail = set(tail) - set(mid)
		tail = sorted(list(tail))

		# concatenate final integer sequence
		sequence += head

		# handle sequences and intervals
		# head to midle
		sequence = self.__handle_sequence_intervals(sequence, mid)
		# midle to tail
		sequence = self.__handle_sequence_intervals(sequence, tail)
		
		# in the end, handle symbols for zero boundaries
		if(self.boundaries == 0):
			# start sequence with symbol
		 	if(self.current_page - self.around > 1):
				sequence = ["."] + sequence

		 	# end sequence with symbol
		 	if (self.current_page + self.around < self.total_pages):
				sequence += "."

		# make sure all values are string
		sequence = map(str,sequence)

		# build final string sequence
		result = " ".join(sequence)

		# '...' may be treated as [".",".","."]
		# fixing "." as "..." in the end 
		result = result.replace(".","...")

		return result

	def __str__(self):
		str_bf = "Paginator( total_pages={}, current_page={}, boundaries={}, around={})".format(
			self.total_pages, self.current_page, self.boundaries, self.around 
			)

		return str_bf
