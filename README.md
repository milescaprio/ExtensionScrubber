A little CLI program to delete any files with a certain file extension. Needed to create this for multiple occasions
I needed to clear out files.

Uses https://github.com/AnthonyBloomer/python-cli-template for CLI.

CAREFUL: THIS PROGRAM IS PROVIDED AS-IS. DO NOT TRUST OR RELY ON IT. THERE ARE NO CURRENT KNOWN ISSUES IN THIS PROGRAM, 
BUT COULD HAVE ERRORS THAT COULD RESULT IN DATA LOSS. IT DELETES FILES IN A NONRIGOROUS PROGRAM ENVIRONMENT. WITHOUT CONFIRMING, 
OR WITH UNEXPECTED INPUT, THIS PROGRAM CAN IRREVERSIBLY DELETE EXCESSIVE AMOUNTS OF DATA.

Running:
Copy quickdel.bat into a folder in your PATH (e.g. \ or \Users\youruser\). Edit this file and put the location this program folder is 
stored in place of "thisfolder". 
Then, you can run in the command line, with the extension as an argument.

```
quickdel cpp
```

will delete all cpp files in the current working directory AND below (recursive).

Not recommended: pass the -y switch to disable confirm.

Not polished.

Last modified August 2022, Later uploaded to GitHub
