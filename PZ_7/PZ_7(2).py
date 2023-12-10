# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2.

def rep(S, S1, S2):
        index = S.find(S1)

        result = S[:index] + S2 + S[index + len(S1):]
        return result

S = "Hello World, Hello Universe"
S1 = "Hello"
S2 = "Hi"

result = rep(S, S1, S2)
print(result)