import numpy as np
import itertools

MASK_SHOWING_PAGE_NUMBER = "#"
MASK_HIDE_PAGE_NUMBER = "..."

class Paginator(object):

	def __init__(self, total_pages, current_page=1, boundaries=1, around=0):
		
		self.boundaries = boundaries
		self.around = around
		self.total_pages = total_pages
		self.current_page = current_page

		# check basic restrictions
		if(self.boundaries <= 0):
			raise ValueError('boundaries accepts only positive values and different than zero. %f is invalid' % (self.boundaries))

		if(self.around < 0):
			raise ValueError('around accepts only positive values. %f is invalid' % (self.around))
		
		if(self.current_page > total_pages):
			raise ValueError('current_page cannot be higher than total_pages. %f is invalid as current_page' % (self.current_page))

		if(self.current_page <= 0):
			raise ValueError('current_page accepts only positive values. %f is invalid' % (self.current_page))


	def __create_sequence(self):
		'create pagination sequence'

		# create pages array
		pages = np.arange(0, self.total_pages, 1, dtype=np.int)		

		# adjust range values to start from one
		pages = pages + 1

		# convert to string
		pages = np.array(map(str, pages))

		return pages
	
	
	def __build_mask(self, pages):
		' we create a mask to keep track of page numbers we want to show '

		# this auxiliary array will serve as mask
		pages_mask = pages.copy()

		# . mask current page index
		current_page_idx = (self.current_page - 1)
		pages_mask[current_page_idx] = MASK_SHOWING_PAGE_NUMBER

		# . mask bounderies. mark head and the tail elements
		pages_mask[:self.boundaries] = MASK_SHOWING_PAGE_NUMBER
		pages_mask[-self.boundaries:] = MASK_SHOWING_PAGE_NUMBER

		# . mask around current page		
		next_page_idx = (self.current_page) + (self.around)
		previous_page_idx = (self.current_page) - (self.around + 1)

		pages_mask[current_page_idx:next_page_idx] = MASK_SHOWING_PAGE_NUMBER
		pages_mask[previous_page_idx:current_page_idx] = MASK_SHOWING_PAGE_NUMBER

		return pages_mask


	def __apply_mask(self, pages_mask, pages):
		# Invert mask
		# . find masked indexes
		visible_page_number_indexes = np.where(pages_mask == MASK_SHOWING_PAGE_NUMBER)
				
		# . collect page numbers we want to show
		visible_page_number_values = pages.take(visible_page_number_indexes)
		
		# . create empty list, default value is '...'
		pagination_links = np.repeat('...', self.total_pages)
		
		# . apply mask replacing '...' for page numbers we want to show
		pagination_links.put(visible_page_number_indexes[0], visible_page_number_values[0])

		return pagination_links
	

	def paginate(self, explain=False):
		'generate pagination string'

		pages = self.__create_sequence()
		
		# mark intervals we want to hide
		pages_mask = self.__build_mask(pages)

		# apply mask
		pagination_links = self.__apply_mask(pages_mask, pages)

		# . ignore repeated '...' and group them into a single sequence
		result = [k for k, g in itertools.groupby(pagination_links)]
		
		# explain each step
		if(explain): 
			print(self)
			print(pages_mask)
			print(pagination_links)
			print(result)

		result = " ".join(result)

		return result

	def __str__(self):
		str_bf = "Paginator( total_pages={}, current_page={}, boundaries={}, around={})".format(
			self.total_pages, self.current_page, self.boundaries, self.around 
			)

		return str_bf