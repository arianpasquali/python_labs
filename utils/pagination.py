import numpy as np
import itertools

MASK_SHOWING_PAGE_NUMBER = "#"
MASK_HIDE_PAGE_NUMBER = "..."
# DEBUG = True

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

	def paginate(self, explain=False):

		if(explain):
			print(self)
		
		# create pages array
		pages = np.arange(0, self.total_pages, 1, dtype=np.int)		

		# adjust range values to start from one
		pages = pages + 1

		# convert to string
		pages = np.array(map(str, pages))
		
		# this auxiliary array will serve as mask
		pages_mask = pages.copy()

		# we create a mask to keep track of page numbers we want to show
		
		# . mask current page index
		current_page_idx = (self.current_page - 1)
		pages_mask[current_page_idx] = MASK_SHOWING_PAGE_NUMBER

		# . mask bounderies. mark head and the tail elements
		pages_mask[:self.boundaries] = MASK_SHOWING_PAGE_NUMBER
		pages_mask[-self.boundaries:] = MASK_SHOWING_PAGE_NUMBER

		# . mask around current page		
		next_page_idx = (self.current_page - 1) + (self.around + 1)
		previous_page_idx = (self.current_page) - (self.around + 1)

		pages_mask[current_page_idx:next_page_idx] = MASK_SHOWING_PAGE_NUMBER
		pages_mask[previous_page_idx:current_page_idx] = MASK_SHOWING_PAGE_NUMBER

		if(explain):
			print(pages_mask)
				
		# Invert mask
		# . find masked indexes
		visible_page_number_indexes = np.where(pages_mask == MASK_SHOWING_PAGE_NUMBER)
				
		# . collect page numbers we want to show
		visible_page_number_values = pages.take(visible_page_number_indexes)
		
		# . create empty list
		pagination_links = np.repeat('...', self.total_pages)
		
		# . apply mask replacing ... for page numbers
		pagination_links.put(visible_page_number_indexes[0], visible_page_number_values[0])

		if(explain):
			print(pagination_links)

		# . group repeated '...' into a single sequence
		result = [k for k, g in itertools.groupby(pagination_links)]

		if(explain):
			print(result)

		result = " ".join(result)

		return result

	def __str__(self):
		str_bf = "Paginator( total_pages={}, current_page={}, boundaries={}, around={})".format(
			self.total_pages, self.current_page, self.boundaries, self.around 
			)

		return str_bf