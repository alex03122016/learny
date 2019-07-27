

kivy tutorial
=================================================================
  some ressources
  ----------------------------------------------------------------------
    -  https://pythonprogramming.net/kivy-application-development-tutorial/ #has some errors?
    -  https://pythonprogramming.net/kivy-widgets-labels/?completed=/kivy-application-development-tutorial/
    -  https://techwithtim.net/tutorials/kivy-tutorial/object-properties/ #the best one!


  -----------------------------------------------------------------------
	install kivy instructions:
	https://kivy.org/doc/stable/installation/installation-linux.html

  create a pakage for android:
  -----------------------------------------------

    # buildozer android debug deploy run
    - requiers cython installation: Kivy 1.11.0 -> Cython==0.29.9,code: pip install -U --force-reinstall Cython==<version>
    - requieres openjdk8 #code: sudo apt-get install openjdk-8-jdk
    - change name of app in .spec file, Make sure that the relative path you specify on Line 13 of your buildozer.spec points to where your main.py is located
    - ressources: https://kivy.org/doc/stable/guide/packaging-android.html

  kv
  -------------------------------------------------------------
    - file name has to be lowercase version of main app
    - https://kivy.org/doc/stable/api-kivy.core.text.markup.html

  plyer
  -------------------------------------------------

    - URL: https://pypi.org/project/plyer/
    - code: pip install plyer, from plyer import battery , battery.status["percentage"]
    - list of supported api: https://github.com/kivy/plyer/blob/master/README.md
    - read the docs


  install android studio:
  ---------------------------------------------------------------
    - https://developer.android.com/studio/install
    - https://askubuntu.com/questions/25347/what-command-do-i-need-to-unzip-extract-a-tar-gz-file
