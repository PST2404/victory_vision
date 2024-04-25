My Website Link : [IPL The Victory Vision](https://victory-vision.streamlit.app/)


# Film Fusion

Introduction:
The movie recommender system project aimed to develop a personalized recommendation system for movies.

Methodology:
The recommender system utilized content based filtering technique to generate recommendations based on user preferences and similarities with other users. Python programming language and relevant libraries were employed for implementation.

Data Collection and Preprocessing:
Preprocessing steps involved handling missing values and performing feature engineering to extract relevant information from the dataset.

Implementation:
The implementation of the movie recommender system involved several key steps, including data preprocessing, text vectorization, similarity computation using bag-of-words (BoW), and cosine similarity.

* Data Collection and Data Preprocessing :
   - The datasets used for training the recommender systems are movies and credits provided by TMDB. Dataset Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
   - The dataset containing movie descriptions or reviews was preprocessed to handle any inconsistencies, missing values, or noise. 
   - Text data was cleaned by removing special characters, punctuation, and stopwords to ensure better vectorization.

* Text Vectorization :
   - The preprocessed text data was transformed into numerical vectors using text vectorization techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) or CountVectorizer.
   - This step converted each movie description or review into a numerical representation, facilitating similarity computation.

* Similarity Computation using Bag-of-Words (BoW) :
   - Bag-of-Words (BoW) methodology was employed to represent each movie as a vector of word occurrences, disregarding grammar and word order.
   - BoW vectors were generated for each movie based on the frequency of words in their descriptions or reviews.

* Cosine Similarity Calculation :
   - Cosine similarity was utilized to measure the similarity between pairs of movie vectors.
   - For each user, their preferences were represented as a vector based on the movies they liked or rated.
   - Cosine similarity scores were computed between the user preference vector and the BoW vectors of all movies in the dataset.
   - The movies with the highest cosine similarity scores to the user preference vector were recommended as top recommendations.

* Building Webpage :
   - The webpage was builded using Pycharm and Frontend tool Streamlit
  

* Deployment and User Interaction:
   - The trained recommender system was deployed in a user-friendly interface Streamlit Cloud, allowing users to input their preferences or interact with the system through the website.


The implementation of the movie recommender system leveraged text vectorization techniques and cosine similarity to generate personalized movie recommendations based on user preferences and movie descriptions. This approach facilitated efficient recommendation generation while ensuring relevance and accuracy in the recommendations provided to users.


