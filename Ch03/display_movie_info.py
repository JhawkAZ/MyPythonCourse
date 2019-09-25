import sys
program_name = sys.argv[0]
print('original name \t\t', program_name)
print('upper case \t\t', program_name.upper())
print('original name \t\t', program_name)
print('removed under \t\t', program_name.replace('_',' '))
program_name = program_name.replace('.\\','')
print('removed .\\\t\t', program_name)
program_name = program_name.replace('.py','')
print('remove .py \t\t',program_name)
program_name=program_name.upper()
print('upper\t\t',program_name)
print('length is \t\t',len(program_name))


welcome_message='Welcome to {}'
welcome_message = welcome_message.format(program_name)
print(welcome_message)
welcome_message = welcome_message.center(len(welcome_message)*3,'*')
print(welcome_message)
good_year = False
while not good_year:
    year = input("What year is your favorite movie from? ")
    if year.isdecimal():
        good_year=True
    else:
        print('Please enter a valid year')
movie=input("what is your favorite move? ")
message ="In {}, the move {} debuted"
print(message.format(year,movie))
movie = movie.strip()
print(movie)
