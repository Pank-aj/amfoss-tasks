This task was really intresting.I took some time to figure it out and learned more about python and json.
So basically,api returns 30 repositories at a time so I inserted   ?page='+str(page)   in a loop so that I could obtain 30repositoties per page.
Inorder to break the loop I gave len(json)==0.After collecting names and appending it to a list I used another loop to get commits using perceval.
