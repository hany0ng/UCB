#Create 3 folders, 'JPG', 'PNG', 'TIFF'.
mkdir JPG PNG TIFF

#Locate all .jpg files in 'Pictures' folder & copy into 'JPG' folder. 
find ./Pictures -type f -iname *.jpg -exec cp {} ./JPG \;

#Locate all .png files in 'Pictures' folder & copy into 'PNG' folder.
find ./Pictures -type f -iname *.png -exec cp {} ./PNG \;

#Locate all .tiff files in 'Pictures' folder & copy into 'TIFF' folder.
find ./Pictures -type f -iname *.tiff -exec cp {} ./TIFF \;

#Create new file called 'PictureCounts.md'
touch PictureCounts.md

#Count how many .jpg files occur & log results into 'PictureCounts.md'
var="$(find . -type f -iname *.jpg | wc -l)" ; echo "JPG file count in Pictures folder is $var" >> PictureCounts.md

#Count how many .png files occur & log results into 'PictureCounts.md'
var="$(find . -type f -iname *.png | wc -l)" ; echo "PNG file count in Pictures folder is $var" >> PictureCounts.md

#Count how many .tiff files occur & log results into 'PictureCounts.md'
var="$(find . -type f -iname *.tiff | wc -l)" ; echo "TIFF file count in Pictures folder is $var" >> PictureCounts.md
