# Requirements Document Tester

The requirements-doc-tester can be used to check if a csv requirements doc is valid.

# Running the program

Run the program using the following command `py csvParser2.py`. After doing this the program will prompt you to type in the files name. The file must be in the current directory as the csvParser2 file. 

    What are the file names you wish to test?
    > someFileName.csv

The program will run and out put the result once it is complete.

# The things it tests for

 1. Requirement ID's
	- Numbered correctly [1 - SomeNumber]
	- Requirements must in increasing order

 2. Categories
	- Follows the ordering of the settings file. [One category cannot come before another]
 3. User
 4. Requirement
	- Can test for grammar using GrammarBot
 5. Dependencies
	- Cannot be dependent on anything after itself
	- Follows dependency restrictions in settings.json file
 6. Priority
	- Follows priority restrictions in the settings.json file
 7. TimeEstimate
	- The time estimate must be some number not a string
	- Checks to see if any time estimites were given to categories that cannot have them. [Within the settings.json file]

