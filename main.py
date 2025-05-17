import sys
from stats import get_book_text, get_word_count, get_letter_count, print_report

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]

	text = get_book_text(book_path)
	word_count = get_word_count(text)
	letter_counts = get_letter_count(text)
	print_report(book_path, word_count, letter_counts)

if __name__ == "__main__":
	main()
