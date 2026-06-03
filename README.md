# python_demo
Python project visualizing the value of reported gifts received by current U.S. Supreme Court justices.  Utilizes basic CSV file cleaning and dictionary manipulation to create a bar chart.

This data came from Fix the Court, a non-profit group which researched and published a google sheets (which I downloaded as a CSV) tracking the reported (and likely unreported) gifts that Supreme Court Justices accepted from 2001 to 2023. It includes a lot more data than I used in this project. 

To process my data, I compiled the lists I created from the CSV file into a dictionary, which I used to sort the Justices by highest value of gifts received.  I also introduced a new CSV file with a list of the Justices appointed by democratic presidents, which informed whether the bar representing the Justice's gift $ received was blue or red, representing democratic appointee and republican appointee.  I iterated through lists, scaled the data (twice) and used some conditional logic to determine whether Justices were on the democrats list. 

Initially, I wanted to visualize the relationship between democratic appointed Justices and republican appointed Justices and the value of the total gifts they accepted, which is  being shown in my project, but I think the story that is more striking is truly how vast Clarence Thomas's lead is over the rest of the Justices.  I believe that visual representations like this can mobilize people to hold elected officials accountable, and even Supreme Court Justices accountable, even though these days, they seem to be above the law. 
