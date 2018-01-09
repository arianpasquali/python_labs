from utils.pagination import *
import pytest

# Enable to explain string generation

def pprint_result(paginator, result):
	print("")
	# print(paginator)
	print(result)
	print("=" * 55)

	

def test_case_1():
	
	current_page = 3
	total_pages = 5
	boundaries = 1
	around = 0

	
	current_page = 3
	total_pages = 5
	boundaries = 1
	around = 0

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()


	pprint_result(paginator,result)
	
	assert result == "1 ... 3 ... 5"


def test_case_2():
	current_page = 4
	total_pages = 5
	boundaries = 1
	around = 0

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 ... 4 5"

def test_case_3():
	current_page = 4
	total_pages = 10
	boundaries = 3
	around = 0

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 ... 8 9 10"

def test_case_4():
	current_page = 4
	total_pages = 10
	boundaries = 2
	around = 2

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 6 ... 9 10"	

def test_case_5():
	current_page = 5
	total_pages = 20
	boundaries = 2
	around = 2

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 6 7 ... 19 20"

def test_case_6():
	current_page = 5
	total_pages = 20
	boundaries = 2
	around = 3

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 6 7 8 ... 19 20"	


def test_case_7():
	current_page = 10
	total_pages = 20
	boundaries = 5
	around = 1

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 ... 9 10 11 ... 16 17 18 19 20"


def test_case_8():
	current_page = 10
	total_pages = 20
	boundaries = 5
	around = 2

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 ... 8 9 10 11 12 ... 16 17 18 19 20"	


def test_case_9():
	current_page = 11
	total_pages = 30
	boundaries = 7
	around = 2

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 6 7 ... 9 10 11 12 13 ... 24 25 26 27 28 29 30"

def test_case_10():
	current_page = 5
	total_pages = 10
	boundaries = 2
	around = 1

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 ... 4 5 6 ... 9 10"

def test_case_11():
	'Test default values'

	current_page = 1
	total_pages = 10
	boundaries = 1
	around = 0

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 ... 10"	

def test_case_12():
	'Test large values'

	paginator = Paginator(1000000,50000,1,3)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 ... 49997 49998 49999 50000 50001 50002 50003 ... 1000000"		

def test_case_13():
	'Test large values'

	paginator = Paginator(2500000000,1500000000,1,3)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 ... 1499999997 1499999998 1499999999 1500000000 1500000001 1500000002 1500000003 ... 2500000000"


def test_case_14():
	'Test wierd values'

	paginator = Paginator(100,3,10,2)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "1 2 3 4 5 6 7 8 9 10 ... 91 92 93 94 95 96 97 98 99 100"

def test_case_15():
	'Test zero values'
	current_page = 4
	total_pages = 5
	boundaries = 0
	around = 0

	paginator = Paginator(total_pages, current_page, boundaries, around)
	result = paginator.paginate()

	pprint_result(paginator,result)

	assert result == "... 4 ..."

def test_case_16():
	'Large values'

	paginator = Paginator(2147483647,147483647,3,3)
	result = paginator.paginate()

	pprint_result(paginator,result)
	
	assert result == "1 2 3 ... 147483644 147483645 147483646 147483647 147483648 147483649 147483650 ... 2147483645 2147483646 2147483647"

def test_case_invalid_inputs_0():
	'Test invalid input. Zero values.'

	current_page = 0
	total_pages = 0
	boundaries = 0
	around = 0

	with pytest.raises(Exception) as e_info:
		paginator = Paginator(total_pages, current_page, boundaries, around)
		result = paginator.paginate()	


def test_case_invalid_inputs_1():
	'Test invalid input. Negative values.'

	current_page = -4
	total_pages = 10
	boundaries = -1
	around = -1

	with pytest.raises(Exception) as e_info:
		paginator = Paginator(total_pages, current_page, boundaries, around)
		result = paginator.paginate()		

def test_case_invalid_inputs_2():
	'Test invalid input. Current page higher than total_pages.'

	current_page = 6
	total_pages = 5
	boundaries = -1
	around = -1

	with pytest.raises(Exception) as e_info:
		paginator = Paginator(total_pages, current_page, boundaries, around)
		result = paginator.paginate()	


def test_case_invalid_inputs_3():
	'Test invalid input. Negative values.'

	current_page = 5
	total_pages = 10
	boundaries = -1
	around = -1

	with pytest.raises(Exception) as e_info:
		paginator = Paginator(total_pages, current_page, boundaries, around)
		result = paginator.paginate()