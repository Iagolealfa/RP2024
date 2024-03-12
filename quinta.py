def inverter_string(string):
    string_invertida = ""
    
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

string_original = "Teste"

print("String original:", string_original)
print("String invertida:", inverter_string(string_original))
