# :thumbsup: :thumbsdown: Review-Helpfulness-Prediction

# Abstract
The aim of this MA project was to develop a machine learning model able to predict helpfulness of customer reviews posted on the Steam platform, an online video game store. 
To that end, various classification as well as regression algorithms and two different helpfulness scores were tested. The impact of linguistic characteristics of a review content (lexical
units, length, polarity, etc.) and metadata information available on Steam (e.g., number of games a reviewer owns) on the helpfulness prediction was examined. Overall, classification models based on votes up and hybrid sets of review- as well as reviewer-related features were found to be the most efficient. In particular, combining metadata with lexical units or with values reflecting readability, length, polarity, the number of comparative expressions a review contains allowed to achieve the highest predictive accuracy of about 74% for the helpful category. Furthermore, the findings reveal that lexical units, readability, length and a year (when a review was posted on Steam) are the most influential determinants of helpfulness. Finally, the empirical results provide evidence that the use of metadata information is crucial for boosting the model performance, especially with respect to the prediction of helpful reviews.

The MA thesis is available [here](https://drive.google.com/file/d/1Hqo493xVEOy4VuxHNv67WbLjj-VQnbyh/view?usp=sharing).

# Dataset
37788 user reviews collected from Steam through API. For the review collection, 27 different games were chosen. The games is listed in the table below.
<br /> 

<details>
  <summary>  List of games </summary>

|**Game**                       |      **Release date**                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|No Man’s Sky                   | 12.08.2016               |
|Dark Souls III                 | 11.04.2016               |
|Fallout 4                      | 12.11.2015               |
|Pay Day 2                      | 13.08.2013               |
|Day Z                          | 13.12.2018               |
|Life is Strange                | 30.01.2015               |
|Euro Truck Simulator 2         | 18.10.2012               |
|ARK: Survival Evolved          | 27.08.2017               |
|Subnautica                     | 23.01.2018               |
|The Forest                     | 30.04.2018               |
|Arma 3                         | 12.09.2013               |
|PlayerUnknown’s Battlegrounds  | 21.12.2017               |
|Red Dead Redemption 2          | 05.12.2019               |
|Divinity: Original Sin 2       | 12.09.2017               |
|Sekiro: Shadows Die Twice      | 21.03.2019               |
|Wallpaper Engine               | 16.11.2018               |
|Don’t Starve Together          | 21.03.2016               |
|Portal 2                       | 19.03.2011               |
|Left 4 Dead 2                  | 17.11.2009               |
|Dying Light                    | 26.01.2015               |
|The Binding of Isaac: Rebirth  | 04.11.2014               |
|Sid Meier’s Civilization VI    | 21.10.2016               |
|Mount & Blade II: Bannerlord   | 30.03.2020               |
|Rust                           | 08.02.2018               |
|Stardew Valley                 | 26.02.2016               |
|Grand Theft Auto V             | 14.03.2015               |
|Monster Hunter: Worldvote score| 09.08.2018               |                                                                                                                                                                                

</details>

<br />

# Features and response variables

|**Feature variable**          |      **Description**                                                                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|Lexical units	               |   TF-IDF weighted *n*-grams and word2vec embeddings. For the letter, both embeddings obtained from the basiline (trained on Steam corpus) model and from the pre-trained Google’s word2vec were utilized.  |
|Length                        |  <ul><li> Total number of characters, words, sentences, paragraphs;</li><li>the average sentence length (number of words divided by the number of sentences).</li></ul>                                    |                                                       
|Readability            	   |  <ul><li>Flesch Reading Ease;</li><li>Automated Readability Index;</li><li>Gunning Fog Index</li></ul>.                                                                                                    |
|Polarity    	               |  <ul><li>Positive, neutral and negative polarity scores produced by VADER;</li><li>User recommendation: Recommend (positive)/Not recommend (negative).</li></ul>                                           |
|Grammatical Categories	       |   Percentage of nouns, verbs and adjectives per review.                                                                                                                                                    |
|Comparative Expressions       |   Number of comparative and superlative adjectives/adverbs per review.                                                                                                                                     |
|Date           	           |   Day, month and year when an review was posted on Steam.                                                                                                                                                  |
|Playtime                      |   Total time a reviewer played a game.                                                                                                                                                                     |
|Number of games owned         |   Total number of games owned by a reviewer.                                                                                                                                                               |
|Number of reviews	           |   Total number of reviews written by a reviewer.                                                                                                                                                           |


|**Response variables**        |      **Description**                                                                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|Weighted vote score	       |  An helpfulness average value that tales into account fake helpfulness votes. Steam developers do not provide information with respect to the score is computed.|
|Votes Up                      |  Number of users rated a review as helpful.                                                                                                                     |                                                                                       

