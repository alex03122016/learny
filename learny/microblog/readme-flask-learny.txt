
Pythonanywhere:
var/www
python -i wsgy.py file for debugging

https://git-scm.com/book/en/v2/Git-Tools-Submodules
https://jss367.github.io/PA-and-git.html



virtualenv
virtualenv -p /usr/bin/python2.7 venv

Git account
alex03122016
Run the server
Source venv/bin/activate
flask run –host=0.0.0.0

Deploy
One more thing: deploy!
It'd be good to see all this out and live on the Internet, right? Let's do another PythonAnywhere deploy:
Commit, and push your code up to GitHub
First off, let's see what files have changed since we last deployed (run these commands locally, not on PythonAnywhere):
command-line
$ git status
Make sure you're in the djangogirls directory and let's tell git to include all the changes in this directory:
command-line
$ git add --all .
--all means that git will also recognize if you've deleted files (by default, it only recognizes new/modified files). Also remember (from chapter 3) that . means the current directory.
Before we upload all the files, let's check what git will be uploading (all the files that git will upload should now appear in green):
command-line
$ git status
We're almost there, now it's time to tell it to save this change in its history. We're going to give it a "commit message" where we describe what we've changed. You can type anything you'd like at this stage, but it's helpful to type something descriptive so that you can remember what you've done in the future.
command-line
$ git commit -m "Changed the HTML for the site."
Make sure you use double quotes around the commit message.
Once we've done that, we upload (push) our changes up to GitHub:
command-line
$ git push
Pull your new code down to PythonAnywhere, and reload your web app
    • Open up the PythonAnywhere consoles page and go to your Bash console (or start a new one). Then, run: 
PythonAnywhere command-line
$ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
$ git pull
[...]
You'll need to substitute <your-pythonanywhere-domain> with your actual PythonAnywhere subdomain name, without the angle-brackets. Your subdomain name is normally your PythonAnywhere user name, but in some cases it might be a bit different (such as if your user name contains capital letters). So if this command doesn't work, use the ls (list files) command to find your actual subdomain/folder name, and then cd to there.
The command 
git stash
 will revert all uncommitted changes in the repository that you're in, and then you can use git pull to pull down any changes from your remote repository. 
Once you've done that, if you don't want the changes that you stashed, then you don't need to do anything more. If you want to re-apply them, then use 
git stash pop
 to re-apply the changes on top of the newly-pulled code.
Die stash änderungen müssen noch verifiziert werden in der datei selbst auskommentieren oder löschen 

git reset –hard
https://stackoverflow.com/questions/1992018/git-submodule-update-needed-only-initially/2227598#2227598
https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/
https://stackoverflow.com/questions/4161022/how-to-track-untracked-content/4162672#4162672
https://git-scm.com/book/en/v2/Git-Tools-Submodules

todo

User interface
change font size cloze test
prevent repetition in infinit verb generator and flex table
change webpage text, add explanation
(warning time flextable)
add rows wordsearch for webpage
add radio button to include exclude wordsearch (warning time)
make wordsearch faster

add named entity recognition org, pers, loc → Wer, Wen / Wo/ Wohin zuordnen
coreference resolution
→ replace pronoun with actual subject, change sentences into Hauptsätze collect information on subject
install parzu, corzu in venv
conll file as input
parzu:
docker installation
https://docs.docker.com/install/linux/docker-ce/ubuntu/
alternative coref?
https://www.opener-project.eu/documentation/coreference.html

conll
https://pypi.org/project/conllu/
https://pyconll.readthedocs.io/en/stable/pyconll/load.html

pyenv
https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/

9. You can now set the local Python version on per-project basis, for instance, if you have a project located in $HOME/python_projects/test, you can set the Python version of it using following command.
