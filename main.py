#here is some wordle stuff i guess

from english_words import english_words_lower_alpha_set

english = list(english_words_lower_alpha_set)
list1 = []
list2 = []
list3 = []
list4 = []
newword = []

for i in range(25463):
  if len(english[i]) == 5:
    newword = [english[i]]
    list1.extend(newword)
    newword = []

print(len(list1))

print(list1[780:782])

firstword = str(input('wut wuz da first word: '))
firstoutput = [int(a) for a in str(input('wut was the output '))]

if firstoutput[0] == 2:
  for i in range(3213):
    if (list1[i])[0] == firstword[0]:
      newword = [list1[i]]
      list2.extend(newword)
      newword = []

if firstoutput[0] == 1:
  for i in range(len(list2)):
    if firstoutput[0] in list2[i] == True and (list2[i])[0] != firstword[0]:
      newword = list2[i]
      list3.extend(newword)

print(list1)