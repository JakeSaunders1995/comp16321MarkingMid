import os
import sys

folder_path_input = sys.argv[1]
folder_path_output = sys.argv[2]
list_of_files = os.listdir(folder_path_input)


for file_name in list_of_files:
     x = file_name.find(".", 1)
     output_file_name = file_name[:x] + "_v26161ns" + file_name[x:] 
     full_path_input = os.path.abspath(os.path.join(folder_path_input, file_name))
     full_path_output = os.path.abspath(os.path.join(folder_path_output, output_file_name))

     with open(full_path_input, "r") as rf:

          size_to_read = 3
          list_score = []
          rf_contents = rf.read(size_to_read).strip()
          while len(rf_contents) > 0:
               list_score.append(rf_contents)
               rf_contents = rf.read(size_to_read).strip()

     team_1_points = 0
     team_2_points = 0

     for i in list_score:
          if i[1] == "1":
               if "t" in i[2] or "T" in i[2]:
                    team_1_points += 5

               elif "p" in i[2] or "P" in i[2] or "d" in i[2] or "D" in i[2]:
                    team_1_points += 3

               else:
                    team_1_points += 2


          elif i[1] == "2":
               if "t" in i[2] or "T" in i[2]:
                    team_2_points += 5

               elif "p" in i[2] or "P" in i[2] or "d" in i[2] or "D" in i[2]:
                    team_2_points += 3

               else:
                    team_2_points += 2

     with open(full_path_output, "w") as wf:
          wf.write(str(team_1_points) + ":" + str(team_2_points))