# Download zap 
https://www.zaproxy.org/download/



OWASP ZAP (Zed Attack Proxy) is a powerful tool used in DevSecOps and web application security testing. Here's a complete list of what you can do with ZAP:


Feature	What It Means (Simple Explanation)
Passive Scanning	                                  Just watches the traffic (no attacking) and looks for security problems. Safe and quiet.
Active Scanning	                                      Attacks like a hacker to find things like XSS, SQL injection, etc. More powerful but not safe for production.
Spidering (Crawling)	                              ZAP goes through your website like Google does and finds all pages and links automatically.
Authentication Testing	                              Checks if login forms or authentication systems are secure. Works with login pages or HTTP logins.
Session Management Testing	                          Looks at session cookies or tokens to see if they are weak or can be stolen.
Intercepting Proxy	                                  Works like a middleman. You can see, stop, and change web traffic between your browser and your server.
Fuzzing	                                              Sends weird, random, or bad inputs to test if your app breaks or exposes security holes.
API Security Testing                                  Can test your APIs (like REST or Swagger) to check if they're secure.
Report Generation	                                  After scanning, ZAP can create reports in HTML, XML, or Markdown. Good for showing issues to your team.
Automation via Scripts	                              You can write small scripts (Python, JavaScript, etc.) to make ZAP do custom things or scan in your own way.
Command-Line Scans (CI/CD)	                          Run ZAP scans using the terminal. Perfect for adding to CI/CD pipelines like Jenkins or GitHub Actions.
Docker Support	                                      Run ZAP in Docker containers—easy, fast, and clean (no install needed on your machine).
Add-ons Marketplace	                                  Like an app store for ZAP—install new tools or features with a click.
AJAX Spidering	                                      Helps ZAP crawl modern websites that use a lot of JavaScript (like React or Angular).
Contextual Analysis                                   You can tell ZAP which roles, users, or areas to scan, so it knows what to focus on (e.g., scan only as "admin").


# docker magic

```
 sudo docker run --rm -v $(pwd):/zap/wrk softwaresecurityproject/zap-stable zap-full-scan.py -t http://172.17.0.1:5009 -r full-report.html
 
```

# allow the port
```
sudo ufw allow 5009
sudo ufw reload

```

# explain the command

```
Part	                                  Explanation
docker run	                              Tells Docker to start a container.
--rm	                Automatically removes the container after it finishes (keeps things clean).
-v $(pwd):/zap/wrk	    This mounts your current folder (from your host system) into the container's /zap/wrk folder.
So that ZAP can save the report file in your machine, not inside the container.
softwaresecurityproject/zap-stable	      This is the Docker image being used. It has ZAP and the scan scripts (zap-full-scan.py) pre-installed.
zap-full-scan.py	                      This is a ZAP script that performs an active scan (attacks your app like a real hacker would — XSS, SQLi, etc.).
-t http://localhost:5009	              This is the target of the scan (your local app). ZAP will try to crawl and attack this.
-r full-report.html	                      This tells ZAP to generate a report file named full-report.html showing all findings (vulnerabilities, warnings, etc.).
It will be saved in your current folder.
```