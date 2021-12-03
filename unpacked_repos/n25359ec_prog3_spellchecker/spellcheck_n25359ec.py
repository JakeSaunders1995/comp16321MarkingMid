import argparse
import os


def get_paths():
  parser = argparse.ArgumentParser()
  parser.add_argument("english_words_file_path")
  parser.add_argument("input_folder_path")
  parser.add_argument("output_folder_path")
  args = parser.parse_args()
  english_words_file_path = args.english_words_file_path
  input_folder_path = args.input_folder_path
  output_folder_path = args.output_folder_path
  return [english_words_file_path, input_folder_path, output_folder_path]

def format_text(text: str):
  num_of_numbers_replaced = 0
  num_of_punctuation_removed = 0
  num_of_uppercase_transformed = 0
  formatted = ""
  punctuation = [".", "?", "!", ",", ":", ";", "-", "\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2015", "(", ")", "[", "]", "{", "}", "'", "\"", "\u2026"]
  index = 0
  while index < len(text):
    letter = text[index]
    if letter.isdigit():
      num_of_numbers_replaced += 1
    elif letter in punctuation:
      if(index + 2 < len(text) and text[index] == "." and text[index + 1] == "." and text[index + 2] == "."):
        index += 2
      num_of_punctuation_removed += 1
    else:
      if letter.isupper():
        num_of_uppercase_transformed += 1
      formatted += letter.lower()
    index += 1
  return [formatted, num_of_numbers_replaced, num_of_punctuation_removed, num_of_uppercase_transformed]

def main():
  
  temp = get_paths()
  words_path = temp[0]
  input_path = temp[1]
  output_path = temp[2]
  for filename in os.listdir(input_path):
    path = input_path + "/" + filename
    file = open(path, "r")
    text = file.read()
    text = text.replace("\n", " ")
    file.close()
    file = open(words_path, "r")
    dict_words = [word.replace("\n", "") for word in file.readlines()]
    formatted_info = format_text(text)
    text = formatted_info[0]
    text_words = text.split(" ")
    text_words = [word for word in text_words if not word.isspace() and word != ""]
    #text_words = [word for word in text_words if word != ""]
    correct_words = [word for word in text_words if word in dict_words]
    #t = [word for word in text_words if word not in correct_words]
    write_lines = []
    write_lines.append(f"n25359ec\n")
    write_lines.append(f"Formatting ###################\n")
    write_lines.append(f"Number of upper case letters changed: {formatted_info[3]}\n")
    write_lines.append(f"Number of punctuations removed: {formatted_info[2]}\n")
    write_lines.append(f"Number of numbers removed: {formatted_info[1]}\n")
    write_lines.append(f"Spellchecking ###################\n")
    write_lines.append(f"Number of words: {len(text_words)}\n")
    write_lines.append(f"Number of correct words: {len(correct_words)}\n")
    write_lines.append(f"Number of incorrect words: {len(text_words) - len(correct_words)}\n")
    name = "n25359ec"
    
    temp = filename.split(".")
    output_file_name = temp[0] + f"_{name}" + f".{temp[1]}"
    path = output_path + "/" + output_file_name
    if not os.path.isdir(output_path):
      cur = os.getcwd()
      os.mkdir(cur + "/" + output_path)
    file = open(path, "w")
    file.writelines(write_lines)
    file.close()
  

if __name__ == "__main__":
  main()