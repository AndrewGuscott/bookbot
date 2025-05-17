def get_book_text(filepath):
	with open(filepath) as f:
		words = f.read().lower()
	return words

def get_word_count(text):
	return len(text.split())

def get_letter_count(text):
	freq = {}
	for letter in text:
		if letter.isalpha():
			if letter in freq:
				freq[letter] += 1
			else:
				freq[letter] = 1
	new_list = []
	for letter in freq:
		new_dict = {"char": letter, "num":freq[letter]}
		new_list.append(new_dict)

	new_list.sort(reverse = True, key = sort_on)

	return new_list

def sort_on(dict):
	return dict["num"]

def print_report(book, words, letters):
	print("============ BOOKBOT ============")
	print(f'Analyzing book found at {book}')
	print("----------- Word Count ----------")
	print(f'Found {words} total words')
	print("-------- Character Count --------")

	for dictionary in letters:
		print(f'{dictionary["char"]}: {dictionary["num"]}')

	print("============= END =============")


