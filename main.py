from stats import word_count
import sys



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


first_book = sys.argv[1]

def main(book):
    with open(book) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents


def character_count(contents):
    lowered_contents = contents.lower()
    character_dict = {}
    for lowered_content in lowered_contents:
        if lowered_content in character_dict:
            character_dict[lowered_content] +=1
        else:
            character_dict[lowered_content] = 1
    return character_dict

def converterfilter(char_dict):
    char_list = []
    for key in char_dict:
        if key.isalpha():
            key = {
                "name":key,
                "num":char_dict.get(key)
                }
            char_list.append(key)
    return char_list

def sort_on(dict):
    return dict["num"]

def print_letters(filtered_dicts):
    for x in filtered_dicts:
        name = x.get("name")
        num = x.get("num")
        print (f"{name}: {num}")

first_results = main(first_book)

char_dict = character_count(first_results)

filtered_dicts = converterfilter(char_dict)
filtered_dicts.sort(reverse=True, key=sort_on)



print (f"--- Begin report of {first_book} ---")
print (f"{word_count(first_results)} words found in the document")
print ("")
#print(character_count(first_results))
print_letters(filtered_dicts)
print ("--- End report ---")