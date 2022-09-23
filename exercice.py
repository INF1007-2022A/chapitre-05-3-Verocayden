#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	nb_letters = 0
	for letter in text:
		if letter.isalnum():
			nb_letters += 1

	return nb_letters

def get_word_length_histogram(text):
	text_list = text.split()
	histogram = [0]
	collect_nb_letters = []

	for word in text_list: # Get number of letters for each word.
		collect_nb_letters.append(get_num_letters(word))

	for i in range(max(collect_nb_letters)): # Create list of 0.
		histogram.append(0)

	for i in collect_nb_letters: # Count the instances of the number of letters.
		histogram[i] += 1

	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"
	format_histogram = ""
	for i in range(len(histogram)):
		format_histogram += f"{i} {ROW_CHAR*histogram[i]}\n"

	return format_histogram

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	format_histogram = ""
	bottom_line = ""
	count = max(histogram)

	for i in range(len(histogram)):
		bottom_line += LINE_CHAR

	while count > 0:
		for i in histogram:
			if i >= count:
				format_histogram += BLOCK_CHAR
			else:
				format_histogram += " "
		format_histogram += "\n"
		count -= 1

	format_histogram += bottom_line

	return format_histogram


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
