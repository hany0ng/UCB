# OWASP Top 10 - A Primer

This document explores the 10 vulnerability classes discussed in [OWASP Top 10 - 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf).

## Vulnerabilities

### A1:2017 - Injections

#### Definition / Description
Injections occur when untrusted, hostile data is sent through an interpreter as part of a command or query, resulting in the interpreter being tricked into executing unintended commands or accessing unauthorized data.  Generally a result of poor sanitation, lack of whitelisting, or developer oversight, these attacks are relatively common due to their ease of exploitation, but are also easy to detect.  Injection attacks will vary in degrees of severity dependent on whether it is data being stolen or if the host is completely compromised to the will of the attacker.  The attacker may use injections for data exfiltration or sabotage.

#### How it Works
Attackers can first assess for injection flaws using fuzzers or scanners such as sqlmap, after which they can then construction injection payloads using their understanding of whichever language or application is vulnerable to execute commands not authorized by the web application.  An example of a SQLi into a form field within DVWA<SQLi can include the original query, followed by **' and '1'='1'**, e.g. **tom'%20or%20'1'='1'**, which will return a list of all users because of the latter statement, which will always return True.

#### Scenario
In the following URL: <http://ptl-f99df351-3bdd4c8f.libcurl.so/cat.php?id=1%20UNION%20SELECT%201,concat(login,%27:%27,password),3,4%20FROM%20users>, the intended SQL query would have originally pulled images from the database, but the injection allowed for the attacker to pull login information using a UNION operator to combine two queries, one with the original query <http://ptl-f99df351-3bdd4c8f.libcurl.so/cat.php?id=1> and the other with **SELECT 1,concat(login,':',password),3,4 FROM users**, which dumps the administrator's username and password hash, concatenated with a colon.  Two methods to patch this vulnerability are to white-list input validation to allow for only certain characters to be passed through the query, or using a LIMIT statement in SQL to limit the amount of data returned based on the limit value.

While SQL injections and command injections both allow for the attacker to exfiltrate data and run unauthorized commands, command injections in contrast to SQL injections, allow for the attacker to execute operating system commands on the host rather than a server via a vulnerable web application.  An example of this is on DVWA<Command Injection, whereupon we can deliver a command injection payload with **8.8.8.8 && ls -l**, which would first ping 8.8.8.8 and then return a list of items in the currently directory.  

---

### A2:2017 - Broken Authentication

#### Definition / Description
Broken Authentication occurs when application functions related to authentication and session management are implemented incorrectly, allowing for attackers to compromise credentials, cookies, or session tokens to assume other users' identities.  Some examples of broken authentication are theft of session cookies, passwords, and secret keys.  Prevalence is relatively common due to the design and implementation of most identity and access controls and ease of exploitation being easy.  As attackers only have to gain access to a few accounts, or just one admin account to compromise the system, it has the potential to cause a lot of damage for the end-users as they become victims of identity theft, social security fraud, or blackmail.  Some countermeasures include session isolation, idle session timeouts, and multi-factor authentication to secure each session, as well as enforcing stronger passwords.

#### How it Works
Attackers can detect broken authentication using manual means and exploit them using automated tools such as password lists and dictionary attacks.  Brute Force in DVWA qualifies as a Broken Authentication vulnerability because attackers can steal the credentials of a user due to insufficient countermeasures.

#### Scenario
1. Submit arbitrary request into username and password fields and intercept request to login form located at DVWA<Vulnerabilities<Bruce Force
2. Send intercepted request to BURP Intruder
3. Set positions around username and password and select Cluster Bomb attack type.
4. Provide a list of usernames and passwords to test in Payloads.
---
##### Raw Request
```
GET /dvwa/vulnerabilities/brute/?username=admin&password=admin&Login=Login HTTP/1.1
```
##### Intruder Request
```
GET /dvwa/vulnerabilities/brute/?username=§admin§&password=§admin§&Login=Login
```
##### Valid Response(s)
```
<p>Welcome to the password protected area admin</p>
```
##### Mitigation

To mitigate brute force attacks, one may implement a method to lock out accounts after a certain number of failed login attempts.  Another countermeasure is to implement CAPTCHAs into the webpage, which is a completely automated Turing test to tell computers and humans apart.

---

### A3:2017 - Sensitive Data Exposure

#### Definition / Description
Sensitive Data Exposure results from sensitive information such as passwords, credit cards, health records, personal information, and business secrets being exfiltrated.  These issues usually result from insufficient of lack of encryption.  It is moderately difficult to exploit and detect, but is extremely common in prevalence.  As sensitive data is being involved, this is considered to be of high criticality/severity in terms of impact.  To mitigate such risks, companies should encrypt all sensitive data with sufficient cryptographic methods, disable caching for responses, and not store sensitive data unnecessarily.

#### How it Works
LFI (Local File Inclusion) allows for attackers to trick the application into exposing or running files on the server.  Normally, a user should only have specific privileges, but a LFI vulnerability would allow for the attacker to upload script into the server, from which they can run any server-side malicious code, such as looking into the contents of `/etc/passwd/`.  Thus, it qualifies as Sensitive Data Exposure vulnerability due to attackers being able to gain access to sensitive data.

#### Scenario
TODO: Explain the LFI vulnerability you explored on the DVWA **File Inclusion** page.

Specifically, explain
- How you perform the attack
  - **Note**: Include the URL you use to demonstrate the LFI, and provide a screenshot of the output it generates.
- Why the attack works
- How the server could be configured to prevent this attack

---

### A4:2017 - XML External Entities (XXE)

#### Definition / Description
XML External Entities (XXE) is a vulnerability that occurs when: applications accept XML directly or XML uploads, XML processors or SOAP based web services have document type definitions enabled, the application uses SAML for identity processing within federated security or single sign on purposes, or XML entitites are being passed to SOAP framework in a version prior to v1.2.  XXE has a moderate amount of difficulty to exploit, are relatively common but easy to detect.  XXE is considered to have high severity as vulnerability can be used for data exfiltration, execute remote requests from server, perform recon, perform DoS, and other types of attacks.  XXE can be mitigated by using less complex data formats such as JSON, avoiding serialization of sensitive data, ensuring XML processors and libraries are up to date, disable XML external entity and DND processing, and implement whitelisting in server-side input validation.

#### How it Works
XML is a metalanguage that allows users to define their own customized markup languages, especially to display documents on the Internet.  Web applications use XML to format documents and share them on the internet, but they are susceptible to attacks using XML uploads as misconfigured XML parsers can lead to exploits such as remote code executions and data exfiltration.
TODO: Explain the following:
  - What XML is
  - How web applications use XML
  - Why web applications can be attacked via XML uploads
  - Ways that XXE payloads can be delivered

#### Scenario
Below, I will explain what each of the payloads does.

##### Payload 1
```xml
<?xml version="1.0" encoding="ISO-8859-1"?> <!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]> <foo>&xxe;</foo>
 ```
In the above scenario, an attacker can use this payload to extract data from the server that contains user info and encrypted passwords, along with their privileges within the system.  If this succeeds, it also ties into Injections, Sensitive Data Exposure, and Broken Access Control.
 
##### Payload 2
```xml
<!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>
 ```
In the above scenario, an attacker can use this payload to probe a server's private network.  If this succeeds, it also ties into Injections and Broken Access Control.

##### Payload 3
```xml
<!ENTITY xxe SYSTEM "file:///dev/random" >]>
 ```
In the above scenario, an external entity declaration is made to URI `file:///dev/random`.  External entitites will force the XML parser to access the sources specified by the URI, but this puts the application at risk to DoS attacks, such as the one indicated.  Thus, this can crash the server if the XML parser attempts to substitute the entity with the contents of the /dev/random file.

---

### A5:2017 - Broken Access Control

#### Definition / Description
Broken Access Control occurs when users can act outside of their intended permissions, leading to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside of the limits of the user.  It has a moderate difficulty in regards to exploitability and detection, and is considered to be relatively common.  It has a high severity categorization because attackers can act as users or administrators, which gives them complete power over a system.  It can be mitigated by enforcing server-side code or server-less API, where the attacker cannot modify the access control check or metadata.

#### How it Works
LFI (Local File Inclusion) qualifies as a Broken Access Control vulnerability because an attacker can use it to trick the application into exposing or running files on the server.  Normally, a user should only have specific privileges, but a LFI vulnerability would allow for the attacker to upload script into the server, from which they can run any server-side malicious code, taking on the role of an server administrator when they shouldn't have that access.

#### Scenario
In an example, if user `jane` logs into an application and gets redirected to `https://example.site/userProfile.php?user=jane`, but can see Bob's profile by navigating to `https://example.site/userProfile.php?user=bob`, this is an example of Insecure Direct Object Reference (IDOR).  IDOR is when an application provides access to objects based on user-supplied input simply by someone modifying the value of a parameter.

---

### A6:2017 - Security Misconfiguration

#### Definition / Description
Security Misconfigurations are the most commonly observed issue, resulting from insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP heads, and verbose error messages containing sensitive information.  Security misconfigurations can occur at any level of an application stack, and thus can be missed unless identified by experts or hackers.  Automated scanners can be used to detect misconfigurations, use of default accounts or configurations, unnecessary services, and legacy options.  It is considered to be easy to exploit due to attack vectors being prevalent across each level in the application stack, and thus is extremely common, yet easy to detect.  As any system can be misconfigured, the scope of impact includes both businesses as well as the end-user.  In terms of impact, it varies from business to business, but these misconfigurations may lead to unauthorized access to some system data or functionality.  If an attacker gained root access using default credentials, for example, they can completely compromise the system for their own use.  Examples of security misconfigurations are default passwords, default scripts stored in servers, default directories, and default error messages.

#### How it Works
One example of security misconfiguration are file inclusion vulnerabilities, the two types being local file inclusion (LFI) and remote file inclusions (RFI).  In order for a RFI to be successful with PHP, [allow_url_include](http://php.net/manual/en/filesystem.configuration.php) and [allow_url_fopen]() both need to be "on".  **allow_url_include**, necessary since PHP 5.2.0, allows for the use of URL-aware fopen wrappers with the following functions: include, include_once, require, require_once.  **allow_url_fopen**, necessary for PHP 4.3.4 and earlier versions, enables URL-aware fopen wrappers that enable accessing URL object like files.  The PHP language has a directive that allows for filesystem functions to use an URL to retrieve data from remote locations.  RFI on DVWA qualifies as Security Misconfiguration because the user input is not validated, allowing for the attacker to pass through commands

#### Scenario
```php
// TODO: Disables allow_url_fopen
nano /var/www/html/dvwa/php.ini
allow_url_fopen = off

// TODO: Disables allow_url_include
nano /var/www/html/dvwa/php.ini
allow_url_include = off
```
---

### A7:2017 - Cross-Site Scripting (XSS)

#### Definition / Description
XSS occurs when an attacker inserts untrusted data or scripts in a new web page without proper validation or escaping, or updates.  XSS is split into three types: reflected, stored, and DOM-based, with the differences between the three being how the payload arrives at the server.  Reflected XSS involves the attacker submitting his payload as a part of the request sent to the web server, which is then echoed back onto the page in a way that the HTTP response includes the payload from the HTTP request..   Stored, or Persistent XSS involves the attacker injecting malicious script into the target application, where it is permanently stored by the target application, for example within a database.  For example, an attacker may inject malicious script into a user input field such as a blog comment.  DOM-based XSS is an advanced XSS attack that exploits the client-side script via manipulation of the DOM (Document Object Model).  XSS will allow for the attacker to execute scripts in the victim's browser to hijack user sessions, deface websites, or redirect the user to malicious sites.  It is considered easy to exploit, and is considered the second most prevalent among the OWASP Top 10, found in about two-thirds of all applications.  It is considered easy to detect.  The impact for XSS is moderate for reflected/DOM XSS and severe for stored XSS.  XSS attacks typically target the end-user and are used in attacks to redirect end users to malicious websites, steal credentials or sessions, or deliver malware to the victim.  Some countermeasures include output encoding and escaped untrusted HTTP request data, as well as enabling a Content Security Policy (CSP).

#### How it Works
User input from forms are often sent to servers via GET query parameters, from which the server will use those query parameters to generate the HTML page it sends back.  Reflected XSS payloads will use this method of echoing queries back onto the HTML page by inputting in script such as Javascript into the query, so that when the HTML page tries to echo back the script in the form of a query, it will echo back the script and execute upon arrival to the client.

#### Scenario
In DVWA, reflected XSS works by the attacker providing an input into the form field.  Upon realization that the page echoes back "Hello < user input >", the attacker can test for vulnerabilities by using javascript syntax to reflect output such as an alert using the below payload.
```
GET /dvwa/vulnerabilities/xss_r/?name=%3Cscript%3Ealert(%221%22)%3C%2Fscript%3E HTTP/1.1
```

---

### A8:2017 - Insecure Deserialization

#### Definition / Description
Insecure Deserializations result from attackers deserializing applications and APIs, and are difficult to exploit, but are still relatively common in regards to prevalence and can be detected with a moderate amount of difficulty.  Serialization converts an object into a format which can be persisted to disk (such as saving to a file), sent through streams (such as stdout), or sent over a network.  The format can be either binary or structured text (like JSON or XML).  Deserialization is the opposite of serialization, thus converting serialized data into an object.  Web Applications use serialization and deserialization for databases, cache servers, file systems, HTTP cookies, HTML form parameters, API authentication tokens, wire protocols, web services, message brokers, and RPC/IPC.  The issue occurs when deserializing untrusted user input, and can be used in attacks that abuse an application's logic, inflict a DoS attack, or RCE (Remote Code Execution).  Thus, the impact of insecure deserialization cannot be understated as RCE attacks are among the most severe attacks possible.  To mitigate the risk for insecure deserialization, it is recommended not to accept serialized objects from untrusted sources or to use serialized mediums that only permit primitive data types.  Other alternatives include implementing integrity checks, isolating deserialization to low privilege environments, logging and monitoring deserialization, and restricting network traffic.

#### How it Works / Scenario
In the RCE example provided in the [Acutenix article](https://www.acunetix.com/blog/articles/what-is-insecure-deserialization/), the attacker prepares an exploit with a "whoami" command, serializes it, then has the application insecurely deserialize the attacker's serialized data.  In this scenario, the attacker uses Python's native serialization format, pickle, to serialize the RCE, then deserialize the output and returns it back to the attacker.

---

### A9:2017 - Using Components with Known Vulnerabilities

#### Definition / Description
Using Components with Known Vulnerabilities result from unpatched or outdated software.  Vulnerable Components are moderate in regards to difficulty to exploit and detection, but have a widespread prevalence.  While these usually lead to minor impacts, some of the largest breaches have relied on exploiting known vulnerabilities in components, such as WannaCry ransomware with the EternalBlue exploit.  To mitigate such risks, there should be a patch management process in place to remote unused dependencies, unnecessary features, components, files and documentation, while continuously inventoring the versions of client-side and service-side components.  The administrator should also monitor for libaries and components that are unmaintained or do not create security patches for older versions, and only obtain components from official sources over secure links.

#### How it Works
In [this article](https://news.thomasnet.com/featured/new-nist-framework-focuses-on-supply-chain-security/), the author writes that supply chain risk is important as nearly all companies utilize supply chain.  Supply chain will not be more secure simply by banning foreign suppliers, because it ultimately does not matter due to globalization being more utilized..  All companies should adopt the NIST Cybersecurity Framework, which discusses how to perform self-asessments, provide details on supply chain risk management methods, and provide insight on interactions with supply chain stakeholders.  Each organization should identify responsible third-party suppliers by identifying and assessing them routinely and addressing untrustworthy partnerships which can be seen through poor manufacturing, counterfeiting, tampering, and malicious code.

#### Scenario
In the [leftpad incident](https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/), Azer Koculu unpublished more than 250 of his modules from NPM (a popular package manager used by Javascript projects to install dependencies), with one of those dependencies was left-pad, which pads the lefthand-side of strings with zeroes or spaces.  Thousands of projects worldwide include Node and Babel relied on left-pad, so when Koculu pulled it from NPM, applications and widely used bits of open-source infrastructure were unable to obtain the dependency, and fell over during development and deployment.  It resembled an accidental DoS attack because it left many companies with broken builds/installations after they failed to obtain the left-pad dependency, thus making them unable to operate.

---

### A10:2017 - Insufficient Logging & Monitoring

#### Definition / Description
Insufficient Logging and Monitoring occur when: auditable events are not logged, warnings/errors generate no, insufficient, or unclear messages, logs are not monitored for suspicious activity, logs are stored locally, appropriate alerting thresholds are not in place, pen testing and scans do not trigger alerts, or the application is unable to detect, escalate or alert for active attacks in real time.  These are moderate in regards to difficulty to exploit, but are difficult to detect and have a widespread prevalence.  They have a moderate impact, as most successful attacks begin with vulnerability probing, thus, allowing for a probe to continue will lead to a successful exploit.  Risks can be mitigated by ensuring logging is sufficient, in real time, consistently monitored, and can detect suspicious events as they occur.

#### How it Works / Scenario
An example scenario in which insufficient logging and monitoring hindered forensic or defensive efforts is when logging is sufficient, but SOC professionals experience log/alert fatigue and ignore the alarms set in place, thus having insufficient monitoring.  A real-life example of this was the Target data breach of 2013.