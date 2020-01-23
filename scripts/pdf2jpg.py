'''
This script converts pages from a pdf file to jpeg images. Requires poppler and the pdf2image wrapper to be installed.
'''

from pdf2image import convert_from_path

filename = input('Enter the name of the file you wish to convert: ')
first = int(input('First page to convert: '))
last = int(input('Last page to convert: '))

# Setup which pages to convert
pages = convert_from_path(filename, last_page=last, first_page=first)

# Name the pages and save as jpeg
for i in range(len(pages)):
    pages[i].save('page' + str(i + 1) + '.jpg', 'JPEG')

print('All done!')
