<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

### Description

This is a program to get data about restaurants in Bandung City from [pergikuliner.com](http://pergikuliner.com). 

### Specification

This program does data scraping to get certain data or information from a website without using API. The data collected from the scraper will be stored in a file with JSON format, and the file have to be preprocessed beforehand. There is also a Makefile provided to easily build, clean, and run the program. 

### How to Use

Run the makefile with the command __mingw32-make__ in the command prompt.

### JSON Structure

Each tuple of restaurant data contains information about:
```
1. The Name of the Restaurant
2. The Region of the Restaurant's Location
3. A List of the Restaurant's Cuisine(s)
4. The Overall Rating of the Restaurant
5. The Rating of the Restaurant's Food's Flavor
6. The Price Range of the Food Sold by the Restaurant
```

### Screenshots

![screenshot1](https://github.com/michelleliza/Seleksi-2018/blob/master/Tugas1/screenshots/screenshot1.PNG)
<br>
![screenshot2](https://github.com/michelleliza/Seleksi-2018/blob/master/Tugas1/screenshots/screenshot2.PNG)
<br>
![screenshot3](https://github.com/michelleliza/Seleksi-2018/blob/master/Tugas1/screenshots/screenshot3.PNG)

### References

The libraries used in this program are:
```
1. BeautifulSoup4 - for the data scraping
2. JSON, copy, os - to convert the data to a JSON file
3. urllib - to open links from the internet
4. time - to make delays between each request
```

<p align="center">
  <br>
  Michelle Eliza Gananjaya - 13516015
  <br>
  <br>
</p>
