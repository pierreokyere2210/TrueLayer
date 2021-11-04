# TrueFilm
TRUEFILM
Why GoogleSheets:

Google Sheets was the data visualisation tool of choice, the reasons were as follows:\

- The information required is short-term or wanted now  - therefore ruling out the possibility of a more sophisticated UI to display the information which would be more time-consuming\

- The operator is non technical - therefore ruling out the possibility of the user calling a query using a coding language i.e. SQL\
TRUEFILM

- With Truelayer/Truefilm having a large amount of employees across Europe - the system may be seen and used by multiple employees at once , therefore I chose to display the information on google sheets as opposed to SQL, for ease of sharing.

Why Script is run periodically:

- Script is run periodically, alleviating the need for a non-technical operator to run the script - the nature of films and the industry means the ratios will not vary massively from hour to hour - therefore we\'92re okay with running the querying script daily\


ALGORITHM CHOICES:

- Used API as opposed to downloading the file since file since gz file was very large (easier) 0 values  in the budget and revenue columns have been replaced by 1, to eradicate the possibility of ZERODIVISIONERROR  and also eradicating the possibility of producing an infinity ratio value.
	- Changing from 0 to 1 has minimal impact on the ratio (especially as budgets are in the 1000s)

THINGS TO IMPROVE:

- Look into better wikipedia API - (in latest pull 944/1000) return no results of wikipedia summary(high importance)

- Better display production companies 

- Loop part of the code (low importance  - (importance low because script is run periodically)

- To make process reproducible - automating the creating of the database table based on table headers would be a next step
