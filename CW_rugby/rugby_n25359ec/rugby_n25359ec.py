import argparse
import os

def get_input_and_output_folder_paths():
  parser = argparse.ArgumentParser()
  parser.add_argument("input_folder_path")
  parser.add_argument("output_folder_path")
  args = parser.parse_args()
  input_folder_path = args.input_folder_path
  output_folder_path = args.output_folder_path
  return [input_folder_path, output_folder_path]

def output_result(team1_score, team2_score):
  if(team1_score > team2_score):
    print("Team 1 Won!")
  elif(team1_score < team2_score):
    print("Team 2 Won!")
  else:
    print("Draw")

def main():
  temp = get_input_and_output_folder_paths()
  input_path = temp[0]
  output_path = temp[1]
  for filename in os.listdir(input_path):
    path = input_path + "/" + filename
    file = open(path, "r")
    line = file.read()
    line = line.replace("\n", "")
    file.close()
    points_tokens = {
      "t": 5,
      "c": 2,
      "p": 3,
      "d": 3
    }
    team1_score = 0
    team2_score = 0
    line = line.replace("\n", "")
    line = line.replace(" ", "")
    for i in range(0, len(line), 3):
      team_string = line[i] + line[i + 1]
      point_token = line[i + 2]
      points_gained = points_tokens.get(point_token)
      if team_string == "T1":
        team1_score += points_gained
      elif team_string == "T2":
        team2_score += points_gained
    name = "n25359ec"
    temp = filename.split(".")
    output_file_name = temp[0] + f"_{name}" + f".{temp[1]}"
    path = output_path + "/" + output_file_name
    if not os.path.isdir(output_path):
      cur = os.getcwd()
      os.mkdir(cur + "/" + output_path)
    file = open(path, "w")
    file.write(f"{team1_score}:{team2_score}")
    file.close()
  

if __name__ == "__main__":
  main()