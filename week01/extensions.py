filename = input('File name: ').strip().split('.')

if filename[-1].lower() in ['jpg', 'jpeg']:
    new = 'image/jpeg'
elif filename[-1].lower() in ['gif', 'png']:
    new = 'image/' + filename[-1]
elif filename[-1].lower() in ['pdf', 'zip']:
    new = 'application/' + filename[-1].lower()
elif filename[-1].lower() == 'txt':
    new = 'text/plain'
else:
    new = 'application/octet-stream'

print(new)
