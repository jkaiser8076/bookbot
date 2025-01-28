def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		print(file_contents)
	words = file_contents.split()
	print(f"Total word count is {len(words)}.")

main()
