def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	wordcount = get_wordcount(text)
	chars_dict = get_chars_dict(text)
	sorted_list = sort_on(text)
	for entry in sorted_list:
		print(f"The '{entry[0]}' character was found {entry[1]} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()
   

def get_wordcount(text):
	words = text.split()
	return len(words)


def get_chars_dict(text):
	chars = {}
	for char in text:
		if char.isalpha():
			lowered = char.lower()
			if lowered in chars:
				chars[lowered] += 1
			else:
				chars[lowered] = 1
	return chars


def sort_on(text):
	chars = get_chars_dict(text)
	sorted_list = sorted(chars.items(), key=lambda x: x[1], reverse=True)
	return sorted_list


main()