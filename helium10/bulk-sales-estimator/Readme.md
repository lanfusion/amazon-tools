# Helium10 - Bulk Sales Estimator	
This tool will pull Helium10 monthly sales estimations in bulk from a list of Amazon ASINs. 

## Requirements
* [Paid Helium10 Account (Platinum or higher)](https://www.helium10.com/)
* [Python 3](https://www.python.org/downloads/)
* [Get cookies.txt LOCALLY Chrome Extension](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/)

## Disable Size Values in Exported Cookie.
In a latest version of the Get_Cookies.txt Chrome Extension, it adds a size value to the exported cookie file which results in `ValueError: to many values to unpack` while running the script. After installing the extension, __and__ before exporting the cookie file:
1. Click the extension in the top right corner of your browser. 
2. In the popup window, click the gear icon in the top right corner of the popup.
3. In the Settings window, make sure that `Include Cookie Size Values` in unchecked or disabled.

## Setup Instructions
1. Clone this git repo.
2. Download and Install Python 3 (**make sure pip is selected during install options**) or install it manually from [here](https://pip.pypa.io/en/stable/installation/).
3. Open command prompt/powershell/terminal, etc.
4. Run the command `pip install requests` to install the requests library. 
5. Add the Get cookies.txt extension to your Chrome browser.
6. Login to your Helium10 account on the same Chrome browser. 
7. After you reach the dashboard, click on the Get cookies.txt extension in the top right of your browser and you should see _Get cookies.txt for members.helium10.com_ with an **Export** button. Click **Export**.
8. Copy the `accountid=` number from the URL in the browser.
9. Move the downloaded `helium10.com_cookies.txt` file into the same directory as `helium.py` and `asins.txt`. 
10. Open `asins.txt` in a text editor and add/modify ASINs you want data on, one row at a time. 
11. Open `helium.py` in a text editor and locate line 44, starting with `__base_url__`, replace `accountId=<accountid>` with the account ID number in step 8. Replace `marketplaceid=` with the Amazon marketplace you want to search. A full list of IDs is located [here](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids). Make sure to remove the < and > from before and after the IDs.
12. Open command prompt/powershell/terminal, etc. Navigate to the directory where `helium.py` is located and run `python helium.py`. When the app finishes, the results will be stored in asins.csv in the same folder. Results will be ASIN, # of Monthly Sales, and the HTTP code (for information). 

## FAQ
Q: I am getting `No module named 'requests'`, when I start the script<br>
A: _The Python module, requests, is not found. Make sure you performed step 4. If that does not work, reinstall Python._

Q: I am getting error 400, Limit exceeded. How do fix this?<br>
A: _There is a hard cap on the max searches you can do per day from H10, try again tomorrow. If you need more, buy another Helium10 account and repeat the steps from 5-11 with the separate account._

Q: I am getting error 404 on some of my ASINs.<br>
A: _Either the ASIN does not exist (check by entering the ASIN in the respective marketplace) or Helium10 has no data about the ASIN._

Q: I am getting error 401 Unauthorized.<br>
A: _Your cookie is invalid, make sure you followed steps 5-11 in the Setup Instructions._

Q: It runs a bit slow, is there a way to make it faster?<br>
A: _This is not officially supported, as such you may or may not have issues gathering data from Helium10 by adjusting the sleep timer. You can change line 75 on `helium.py` from `2 + random.randint(1, 3)` to a fixed value like `0` or `1` or whatever works for you. Use at your own risk._

Q: How do I use this with multiple accounts?<br>
A: _Perform Step 1, in separate folder, for every account you own. Then repeat all the steps starting from 6 for each account in its own folder._
