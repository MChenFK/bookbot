def get_word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def get_character_count(file_contents):
    character_count = {}
    lowered_file_contents = file_contents.lower()
    for character in lowered_file_contents:
        if character in character_count.keys():
            character_count.update({character: character_count[character] + 1})
        elif character.isalpha():
            character_count[character] = 1
    
    return character_count

def sort_by_count(dict):
    return dict["count"]

def print_report(path_to_file, word_count, character_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    list_of_character_counts = []
    for character, count in character_count.items():
        list_of_character_counts.append({"character": character, "count": count})
    
    list_of_character_counts.sort(reverse=True, key=sort_by_count)

    for pair in list_of_character_counts:
        print(f"The '{pair["character"]}' character was found {pair["count"]} times")

    print(f"--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    print_report(path_to_file, word_count, character_count)

main()