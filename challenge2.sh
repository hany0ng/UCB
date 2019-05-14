#Make folder called Allrecords
mkdir AllRecords

#Copy all records from 2012-2017 into AllRecords folder.
find ./OrderRecords -type f -iname *order_records* -exec cp {} AllRecords \;

#Create VIPCustomerOrders folder within AllRecords folder.
mkdir AllRecords/VIPCustomerOrders

#Find all orders from VIP Customers Michael Davis or Michael Campbell and copy to michael_campbbell_orders.output and michael_davis_orders.output nested within VIPCustomerOrders folder.
grep -ri --exclude-dir=VIPCustomerOrders campbell.michael AllRecords/* > AllRecords/VIPCustomerOrders/michael_campbell_orders.output
grep -ri --exclude-dir=VIPCustomerOrders davis.michael AllRecords/* > AllRecords/VIPCustomerOrders/michael_davis_orders.output

#Creating file VIPCustomerDetails.md that details how many orders each of the two users made.
var="$(awk -F, '{sum += $5} END {print sum}' AllRecords/VIPCustomerOrders/michael_campbell_orders.output)" ; echo "Michael Campbell placed $var orders." > VIPCustomerDetails.md
var="$(awk -F, '{sum += $5} END {print sum}' AllRecords/VIPCustomerOrders/michael_davis_orders.output)" ; echo "Michael Davis placed $var orders." >> VIPCustomerDetails.md
