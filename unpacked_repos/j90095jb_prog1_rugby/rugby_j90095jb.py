import os, argparse

t1 = 0
t2 = 0
USER_NAME = "j90095jb"

def GetAllFilesAtPath(dir) -> "list[str]":
    paths = []
    for path in os.listdir(dir):
        if path.endswith(".txt"):
            paths.append(os.path.join(dir, path))
    return paths

def GetOutputPath(path: str, outdir: str):
    return f"{os.path.join(outdir, os.path.splitext(os.path.basename(path))[0])}_{USER_NAME}.txt"

def ReadFile(path):
    file = open(path)
    data = file.readline()
    records = []
    for record in [data[i:i+3] for i in range(0, len(data), 3)]:
        records.append(record)
    file.close()
    return records

def RecordValue(record) -> int:
    if record[2] == "t":
        return 5
    elif record[2] == "c":
        return 2
    elif record[2] == "p":
        return 3
    elif record[2] == "d":
        return 3
    #else:
    #    raise ValueError("Your input was incorrectly formatted!")
    
def RecordTeam(record) -> int:
    if record[0:2] == "T1":
        return 1
    elif record[0:2] == "T2":
        return 2
    #else:
    #    raise ValueError("Your input was incorrectly formatted!")

def AddRecord(record):
    global t1, t2
    if RecordTeam(record) == 1:
        t1 += RecordValue(record)
    elif RecordTeam(record) == 2:
        t2 += RecordValue(record)

def WriteScores(outputPath, team1, team2):
    out = open(outputPath, "w")
    out.write(f"{team1}:{team2}")
    out.close()

def Main(inDir, outDir):
    global t1, t2
    for filename in GetAllFilesAtPath(inDir):
        t1, t2 = 0
        records = ReadFile(filename)
        for record in records:
            AddRecord(record)
        WriteScores(GetOutputPath(filename, outDir), t1, t2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Input")
    parser.add_argument("Output")
    args = parser.parse_args()
    Main(args.Input, args.Output)