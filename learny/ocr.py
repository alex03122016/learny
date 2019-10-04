import os
#import ocrmypdf
dir_path = os.path.join(os.path.expanduser('~'),'Dokumente', 'schule-2019')




for filename in os.listdir(dir_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(dir_path, filename)
        print(file_path)
        #ocrmypdf.ocr(dir_path, file_path+'text.pdf', deskew=True)


        continue
    else:
        continue



# hello.py
import click

@click.command()
@click.option('--name', default='', help='Your name')
def say_hello(name):
    click.echo("ocrmypdf {} {}".format(name))

if __name__ == '__main__':
	for filename in os.listdir(dir_path):
	    if filename.endswith(".pdf"):
	        file_path = os.path.join(dir_path, filename)
	        print(file_path)
	        say_hello("supi")
	        #ocrmypdf.ocr(dir_path, file_path+'text.pdf', deskew=True)


	        continue
	    else:
	        continue
