import sys,os

def hexDecrypt(cipherText):
    characters = cipherText.split()
    return "".join([chr(int(hexCode,16)) for hexCode in characters]).lower()

def caeThreeDecrypt(cipherText):
    characters = list(cipherText.lower())
    plainText = [chr(((ord(character)-99)%26)+96) if 97 <= ord(character) < 123 else character for character in characters]
    for character in range(len(plainText)):
        if plainText[character] == "`":
            plainText[character] = "z"
    return "".join(plainText)
    
def getMorseCharacter(character):
    morseTree = {
        "/":{
            " ":" "
        },
        ".":{
            " ":"e",
            ".":{
                " ":"i",
                ".":{
                    " ":"s",
                    ".":{
                        " ":"h",
                        ".":{
                            " ":"5"
                        },
                        "-":{
                            " ":"4"
                        }
                    },
                    "-":{
                        " ":"v",
                        "-":{
                            " ":"3"
                        }
                    }
                },
                "-":{
                    " ":"u",
                    ".":{
                        " ":"f"
                    },
                    "-":{
                        ".":{
                            ".":{
                                " ":"?"
                            }
                        },
                        "-":{
                            " ":"2"
                        }
                    }
                }
            },
            "-":{
                " ":"a",
                ".":{
                    " ":"r",
                    ".":{
                        " ":"l",
                        ".":{
                            " ":"&"
                        },
                        "-":{
                            ".":{
                                " ":"\""
                            }
                        }
                    },
                    "-":{
                        ".":{
                            " ":"+",
                            "-":{
                                " ":"."
                            }
                        }
                    }
                },
                "-":{
                    " ":"w",
                    ".":{
                        " ":"p",
                        "-":{
                            ".":{
                                " ":"@"
                            }
                        }
                    },
                    "-":{
                        " ":"j",
                        "-":{
                            " ":"1",
                            ".":{
                                " ":"'"
                            }
                        }
                    }
                }
            }
        },
        "-":{
            " ":"t",
            ".":{
                " ":"n",
                ".":{
                    " ":"d",
                    ".":{
                        " ":"b",
                        ".":{
                            " ":"6",
                            "-":{
                                " ":"-"
                            }
                        },
                        "-":{
                            " ":"="
                        }
                    },
                    "-":{
                        " ":"x",
                        ".":{
                            " ":"/"
                        }
                    }
                },
                "-":{
                    " ":"k",
                    ".":{
                        " ":"c",
                        "-":{
                            "-":{
                                " ":"!"
                            }
                        }
                    },
                    "-":{
                        " ":"y",
                        ".":{
                            " ":"(",
                            "-":{
                                " ":")"
                            }
                        }
                    }
                }
            },
            "-":{
                " ":"m",
                ".":{
                    " ":"g",
                    ".":{
                        " ":"z",
                        ".":{
                            " ":"7"
                        },
                        "-":{
                            "-":{
                                " ":","
                            }
                        }
                    },
                    "-":{
                        " ":"q"
                    }
                },
                "-":{
                    " ":"o",
                    ".":{
                        ".":{
                            " ":"8",
                            ".":{
                                " ":":"
                            }
                        }
                    },
                    "-":{
                        ".":{
                            " ":"9"
                        },
                        "-":{
                            " ":"0"
                        }
                    }
                }
            }
        }
    }
    character += " "
    for code in character:
        morseTree = morseTree[code]
    return morseTree

def morseDecrypt(cipherText):
    characters = cipherText.split()
    return "".join([getMorseCharacter(character) for character in characters])

arguments = sys.argv

for filename in os.listdir(arguments[1]):
    if arguments[1][-1] != "/":
        source = arguments[1]+"/"+filename
    else:
        source = arguments[1]+filename
    with open(source) as sourceFile:
        sourceText = sourceFile.read()

    typeAndCipher = sourceText.split(":")
    type, cipherText = typeAndCipher[0],typeAndCipher[1]

    if type[0] == "H":
        plainText = hexDecrypt(cipherText)
    elif type[0] == "C":
        plainText = caeThreeDecrypt(cipherText)
    else:
        plainText = morseDecrypt(cipherText)
    if arguments[2][-1] != "/":
        outputName = arguments[2]+"/"+filename[:-4]+"_t28107tj.txt"
    else:
        outputName = arguments[2]+filename[:-4]+"_t28107tj.txt"

    with open(outputName,"w") as outputFile:
        outputFile.write(plainText)