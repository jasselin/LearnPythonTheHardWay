import ex25_import

sentence = "All good things come to those who wait."
words = ex25_import.break_words(sentence)
print words

sorted_words = ex25_import.sort_words(words)
print sorted_words

ex25_import.print_first_word(words)
ex25_import.print_last_word(words)

print words

ex25_import.print_first_word(sorted_words)
ex25_import.print_last_word(sorted_words)

print sorted_words

sorted_words = ex25_import.sort_sentence(sentence)
print sorted_words

ex25_import.print_first_and_last(sentence)
ex25_import.print_first_and_last_sorted(sentence)