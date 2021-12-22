plaintext ← read(‘Plaintext:’)
cipherTest ← “ ”
alphabet ← “XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC”
plaintextPosition ← 0
while (plaintextPosition < length(plaintext)) do
plaintextChar ← plaintext[plaintextPosition]
alphabetPosition ← 3
while plaintextChar 6= alphabet[alphabetPosition] do
alphabetPosition ← alphabetPosition + 1
end while
alphabetPosition ← alphabetPosition - 3
cipherText ← cipherText + alphabet[alphabetPosition]
plaintextPosition ← plaintextPosition + 1
end while
display(cipherText)
