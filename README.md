# statapp_influenceurs
Contains the notebooks and additional files used in the applied statistics project 

## Detecting Influencers on Instagram

We provide here a guideline to detect influencers on instagram. 
The main prerequisit are the following :
  * chromedriver
  * selenium
  * networkx

## Methodology


To obtain influencers in a particular field, for example #GoGreen, our guideline requires that you have at least one instagram account 
identified as an influencer in that particular field.

We first scrape the follow**ers** of that account (or of several accounts) using the followers_scraping.py script. Then we construct a list
of the obtained followers and scrape their follow**ing**. The accounts generated are used to construct a graph from which several centrality measures
are applied to discriminate between accounts.
The idea here is to obtain new accounts not already identified as influencers by looking at the other important accounts that interests the community of the influencers
we are already have. We make the somehow not restrictive hypothesis that it is very unlikely that another account highly followed by the
community of a topic based influencer will be an influencer but on another topic.

*For instance let us image an account @abc which is an identified influencer for the ecologist community, we believe that it is very unlikely that if this community also
follows massively another account on instagram, its topic of predilection will differ from ecology.*

After constructing the graph we :
  * Get rid of accounts with less followers than a certain threshold
  * Produce interaction indices by scraping the number of comments and likes on their last posts
  * Produce a measure of their authenticity looking at the caption of their last posts : the more dithyrambic an account is
  regarding its picture, the less likely it is to be trully 'honest' regarding the products/location/... on their picture. Thus the
  less trustworthy : an influencer is not someone brandishing a sign on every picture.
 
 We aggregate the different indices produces, including the centrality measures (we recommand eigen vector centrality and PageRank), to get a global indice which allows to discriminate between influencers.
