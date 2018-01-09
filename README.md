Code labs
==============================


Pagination string generator
---------------------------

Simple exercise. Flexible pagination string generator.

## Test

In order to run the test suite and follow results, enable standard output.

	> pytest -s

## Usage

	from utils.pagination import Paginator

	current_page = 5
	total_pages = 10
	boundaries = 2
	around = 1

	paginator = Paginator(total_pages, current_page, boundaries, around)
	
	result = paginator.paginate() 
	print(result)

	> 1 2 ... 4 5 6 ... 9 10	
