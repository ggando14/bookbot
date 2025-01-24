def main():
  with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    word_count_total = word_count(file_contents)
    char_dic= count_chars(file_contents)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count_total} words found in the document\n')
    list_of_dicts = convert_to_list_of_dicts(char_dic)
    list_of_dicts.sort(key=sort_on, reverse=True)
    for item in list_of_dicts:
      letter = item['letter']
      count = item['count']
      print(f"The '{letter}' character was found {count} times")
    print('--- End report ---')

def sort_on(dict):
  return dict['count']

def convert_to_list_of_dicts(dict):
  result = []
  for key in dict:
    if key.isalnum():
      result.append({"letter": key, "count": dict[key]})
  return result

def word_count(file):
  words = file.split()
  total = len(words)
  return total

def count_chars(text):
  result = {}
  lowered_text = text.lower()
  for char in lowered_text:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  return result

main()
