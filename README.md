# phonedict

Phonedict is a tool written in python that can generate a dictionary of all possible mobile numbers of a specific area. It comes handy during WPA Handshake cracking as mobile phone numbers are commonly used as passwords. It can also be used for other modes of hashcat or any other password cracker. Alternatively, the possible permutations of a 10 digit mobile code are 10,000,000,000 but with phonedict, you can target a region say Delhi with only 122,000,000 possible mobile phone numbers. A decrease of 98.78%. Moreover, it can also be used to find common info like the carrier, region, etc of a mobile number. This tool can:

  - Generate a custom dictionary based on an area.
  - Reverse lookup a number for info like the carrier, region, etc.
  - Generate a combined dictionary of multiple areas.
  - Works with command-line options for advanced users.
  - Simple wizard interface for beginners to guide through the process.
  - Install dependencies automatically on Windows and Linux.
  - It comes with preloaded data but can also scrap data dynamically to generate dictionary and lookup numbers.



## Screenshots 

![Screenshot](https://i.ibb.co/SNb9cKc/phonedict.png)

### Installation

Phonedict requires Python3 and pip3 installed to work. Apart from these two, the rest of the packages like Pandas and Psutil can be installed by this tool itself. To do so, run:

```
phonedict.py -i
```

### Usage

For help info run:
```
phonedict.py -h
```

Usage Examples:
```
phonedict.py -m 1 -t 0 -c india -o C:\Users\home-pc\Desktop\dict.txt
phonedict.py -m 0 -t 1 -c india -n 1234567890
phonedict.py --wizard
phonedict.py -h
```
### Options
-m,--mode 
The mode to work in offline=0 and online=1. In offline mode, it works with preloaded data and in online mode, it scraps the data dynamically from the source.

-t,--task 
The task to be done i.e. Create a dictionary or search a number. 
-t 0 to create a dictionary and -t 1 to search a number.

-c,--country
The country of your choice.

-o,--output
Location and name of output file. Only .txt format is accepted. 
i.e. C:\Users\home-pc\Desktop\dict.txt 
i.e. /home/homepc/Desktop/dict.txt

-n,--number 
The number for which to search info like location, telecom, etc. Used with -t 1

-w,--wizard
User-friendly interface to guide through the process.

-h,--help 
Prints help info to the screen.

-i,--install
Checks for Python version 3 and pip3. Installs the necessary packages. (Pandas and Psutil)

### Development

Want to contribute? Great!

At present, this tool supports only India so, modules can be added for other countries as well. To add new modules:
1. Add the entry in the countries_supported variable of the config file.
2. Add two modules in /lib/country/. One to search number and one to generate dictionary.
3. The dictionary generator module should be in the following format: <country>.generator.py similarly, the search module should be in the <country>.search.py
4. Inside the generator file, add 3 methods:
  * offline() -Add the preloaded data in the /data/ folder in the following format: <country>.html or <country>.csv from where, this method will fetch it.
  * online() -To scrap the data dynamically. If any of the methods is not available simply print the info and exit. Each of the methods returns 2 tables:
    * Telecom operator table (To be printed as it is to take user input regarding area)
    * Data table with the following columns ['code', 'telecom','state'] which contains all the possible mobile prefixes.
 * chooser() -Asks user to choose the area and generates a final list of mobile prefixes. Returns a final list to the print method in /lib/core/diskwrite named dict_create() which manages the rest like determining the length of suffix, disk free space, calculating file size, progress monitor, etc.
 
5. Inside the search file, only one method find() to find the matching prefix of mobile code from the user-provided input.

Finally, the module is ready.

### Todos

 - Add more countries.

License
----

MIT
