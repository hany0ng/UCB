#Create all.txt file within each of the subfolders combining to-dos included in each individual's to-do lists.
awk 1 ./Todos/Carrie/* > ./Todos/Carrie/all.txt
awk 1 ./Todos/Jennifer/* > ./Todos/Jennifer/all.txt
awk 1 ./Todos/John/* > ./Todos/John/all.txt

#Create done.txt file within each of the subfolders that includes only to-dos marked as done.
grep -i done ./Todos/Carrie/all.txt > ./Todos/Carrie/done.txt
grep -i done ./Todos/Jennifer/all.txt > ./Todos/Jennifer/done.txt
grep -i done ./Todos/John/all.txt > ./Todos/John/done.txt

#Create unfinished.txt within each of the subfolders that includes only to-dos not marked as done.
grep -iv done ./Todos/Carrie/all.txt > ./Todos/Carrie/unfinished.txt
grep -iv done ./Todos/Jennifer/all.txt > ./Todos/Jennifer/unfinished.txt
grep -iv done ./Todos/John/all.txt > ./Todos/John/unfinished.txt

#Create new file called ProductivityReport.md within the Todos folder.
touch ./Todos/ProductivityReport.md

#Specify in the ProductivityReport.md file the number of to-dos each person completed and the number they have left.
echo "Done:" > ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/Carrie/done.txt)" ; echo "Carrie: $var" >> ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/Jennifer/done.txt)" ; echo "Jennifer: $var" >> ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/John/done.txt)" ; echo -e "John: $var\n" >> ./Todos/ProductivityReport.md
echo "To Still Do:" >> ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/Carrie/unfinished.txt)" ; echo "Carrie: $var" >> ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/Jennifer/unfinished.txt)" ; echo "Jennifer: $var" >> ./Todos/ProductivityReport.md
var="$(wc -l < ./Todos/John/unfinished.txt)" ; echo "John: $var" >> ./Todos/ProductivityReport.md
