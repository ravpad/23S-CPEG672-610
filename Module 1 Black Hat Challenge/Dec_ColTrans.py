####################################################################################################
# Dec_ColTrans.py
# Columnar Transposition decryption functions
# Written by - Ravi Padma
####################################################################################################

ciphertext = "mrlsehdsolmmnoilvtelonraesdieuntuetearbfuadeerifeoenultmiemitnnltspttahinneesyumtetaauietoieehematytodcntdlsooaresogrsasnlrspsgnletssocasdtholhhlasiguueonrrserhtirnstslsynrptmienmnrtemundtouoiteslmnuwadtrptieeitgadnayasrdesimtedthgyutpeeurveanmasuomheahmbuamdfweeueognenaatcerisacevrsfsiiayentndteiiretsnfonretotfohehidptfenootrsohodbstansitgennwrrmfeshveoibueldtvrraanwetoanweeaftealcyssdtlgvnanetufwfehmtsatfsraitrhdirsfuosliwiydhisruntiyemeiertnmasvlotimmnewvttedheotdtpytdlwetohrafdthstrnartefocpnoisehnpifoanunrunilyrenomrbdefuwatulowentospaooirshoouefdetandnthonceeoesectaexfslrdtahiaensgoahugy"

key_length = 8
#column_order = [6,7,3,5,1,0,4,2]
#column_order = [5,4,0,1,6,7,2,3]
column_order = [5,4,7,2,6,3,0,1]

num_columns = key_length
print (num_columns)
num_rows = -(-len(ciphertext) // num_columns)  # Round up division
print (num_rows)
padding_needed = num_columns * num_rows - len(ciphertext)
print (padding_needed)
ciphertext_padded = ciphertext + " " * padding_needed  # Pad with spaces

plaintext_matrix = [["" for _ in range(num_columns)] for _ in range(num_rows)]
for i, char in enumerate(ciphertext_padded):
    row = i % num_rows
    col = i // num_rows
    plaintext_matrix[row][col] = char
print (num_rows, ' ', plaintext_matrix)

plaintext = ""
for row in range(num_rows):
    for col in column_order:
        plaintext += plaintext_matrix[row][col]
        #print (plaintext)
#for col in column_order:
 #   for row in range(num_rows):
  #      plaintext += plaintext_matrix[row][col]

print(plaintext)
