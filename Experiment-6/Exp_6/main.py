
#Question 1

# file = open('sample.txt','r')
#
# data = file.read()
#
# print(data)
#
# file.close()


#Question 2

# file = open('sample.txt','r')
# lines = file.readlines()
# file.close()
#
# ans = []
#
# for line in lines:
#     ans.append(line)
#
# print(ans)



#Question 3

# with open("sample.txt",'r') as f1,open("sample2.txt",'r') as f2,open("result.txt",'w') as f3:
#     for line1,line2 in zip(f1,f2):
#         combined_line = line1.strip() + ' ' + line2.strip() + '\n'
#         f3.write(combined_line)
#
#
# f1.close()
# f2.close()
# f3.close()

#Question 4

file_name = input("Enter file name in .txt fromat")

file = open(file_name,'r')

data = file.read()

words = data.split()
commas = data.split(',')

ans = len(words) + len(commas)

print(ans-1)

# Question-5

# import string
#
# filenames = [f"{letter}.txt" for letter in string.ascii_uppercase]
#
# for filename in filenames:
#     with open(filename, "w") as f:
#         pass

# Question-6
import string

letters_per_line = 5

alphabet = string.ascii_uppercase

alphabet_chunks = [alphabet[i:i+letters_per_line] for i in range(0, len(alphabet), letters_per_line)]

output = '\n'.join(alphabet_chunks)

with open("result.txt", "w") as f:
    f.write(output)
