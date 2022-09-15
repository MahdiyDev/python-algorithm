from re import sub


arr = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']

# arr = list(zip(*arr))

# p = (sub("!|@|#|$|%|&", "\s", i, 1) for i in arr)

# print(p)
text = "This is Matrix#  %!"

text = sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', " ", text)

print(text)