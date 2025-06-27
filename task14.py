file_name = input('File nomini kiriting: ')

a = 'File turi:'

if file_name.endswith('.pdf'):
    print(a, 'pdf')
elif file_name.endswith('.docx'):
    print(a, 'docx')
elif file_name.endswith('.txt'):
    print(a, 'txt')
else:
    print("No'malim file turi")

