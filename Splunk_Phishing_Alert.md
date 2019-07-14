# SIEMs Homework Challenge

## Background
You are investigating **phishing attacks** at buttercupgames.  Phishers often try to send emails where the **from address** uses a company's domain name.

## Facts 
The buttercupgames domain name is **buttercupgames.com** (e.g., t1578@buttercupgames.com) and the incoming IP address is **10.0.0.0/8**. 

## Your Goal 
Find possible **anomalies** that may indicate a phishing attack.

## Create the Search 
The search has three parts:
**Part 1:** 
* First, create a search where the Sender is *anyone* from @buttercupgames.com but the incoming IP address is NOT in the domain.
	source="buttercupgames_email_log.csv" sourcetype="csv" Sender="*@buttercupgames.com" incoming_address!="10.0.0.0/8"

**Part 2:** 
* Now locate emails that satisfy the criteria for suspicious emails. Here we will use the **stats** command with the *earliest* and *latest* times *by* incoming IP address. 
    source="buttercupgames_email_log.csv" sourcetype="csv" Sender="*@buttercupgames.com" incoming_address!="10.0.0.0/8" | stats earliest(time) as earliest, latest(time) as latest by incoming_address
	
    * How is the time displayed?
        In epoch time.
	* Check the earliest time value = `1483511846` at https://www.epochconverter.com/
        Wednesday, January 4, 2017 6:37:26 AM GMT
	
**Part 3:** 
* We are now in the last part of the search.  Place the output of the **stats** command in a **table** showing the `incoming IP address`, and the `earliest date/time` and `latest date/time` in human-readable form.
    source="buttercupgames_email_log.csv" sourcetype="csv" Sender="*@buttercupgames.com" incoming_address!="10.0.0.0/8" | stats earliest(time) as earliest, latest(time) as latest by incoming_address | convert ctime(earliest) as c_earliest, ctime(latest) as c_latest | table incoming_address, c_earliest, c_latest | rename incoming_address as "Incoming IP Address", c_earliest as "Earliest Time", c_latest as "Latest Time"

	* How is the time displayed?
        MM/DD/YYYY HH:MM:SS
		
Now look at the results and collect information for the incident report.
* What **incoming IP address** was used in the attack? 
    74.207.253.34
*  Who was the **Sender** in the Phishing attack?
    address15@buttercupgames.com
*  Who was the **Recipient** of the attack?
    address37@buttercupgames.com
*  What was the **Subject** of the email?
    Anonymized Phishing Subject 19
*  What is the **Time** of the event?
    Epoch Time 1485941359, (ctime Wednesday, February 1, 2017 9:29:19 AM GMT)
*  Where there any **Attachments**?
    No

## Create a Cron Alert
We can monitor for `phishing attacks` with Splunk by scheduling alerts as a `cron` job.  
Please create a `scheduled cron alert` for the phishing search **which runs every five minutes**.
* First, run the `phishing` search and select Save as `Alert`.

Configure the alert as follows:
* Title: `Phishing Alert`
* Description: `This alert runs as a cron job every five minutes.`
* Permission: `Shared App`
* Alert Type: `Scheduled`, `Run on Cron Schedule`
* Time Range: `All Time`
* Cron Expression: */5 * * * *
* Trigger Conditions: Keep defaults
* Trigger Actions: 
	* Add Actions `Add to Triggered Alert`
	* Severity = `Critical`
* `Save` the Alert	

### View the Alert
* View the Alert from the **App** bar

### Trigger the Alert
* Run the search - select `All Time`
* Check the `Activity -> Triggered Alert` list.

### Disable the Alert 
* Disable the Alert after 10 entries.