 Language-Detection

========================================================================================
===================== Repository structure==============================================
========================================================================================

1. Dataset: This folder contains all of the input files and data for the model.
    it contains all the .csv file created for the pourpose of the project
    |
    -->Language Detection.csv-> original dataset downloaded from Kaggle 
    |    (https://www.kaggle.com/datasets/basilb2s/language-detection)
    |
    -->Lang_det_parsed.csv-> parsed dataset. Removal of punctuations, numbers and extra chars.
        The columns are: 
        Text: string phrase 
        Language: the language of the Text phrase
        Class: 1 italian, 0 not italian
        Number of words: numbero of words present in the Text column
    |    Number of spaces: number of spaces present in the Text column 
    |
    |
    --> Language-Detection\Dataset\words.csv -> this is a general vocbolary which contains all the words present in the dataset.
        The columns are:
        Word: single word in string format
        Where: integer embedded as follow [0: word in not_italian phrase, 1: word in italain phrase, 2: word in both italian and not italian]
        Counts_ita: number of times the word appear in an italain phrase
        Counts_other: number of times the word appear in an not_italain phrase
    |
    |
    --> Language-Detection\Dataset\Dataset_agumented1[2-3].csv-> dataset created after agumenting the original dataset 
        using the logic described in  Language-Detection\notebooks\Agumentation\Agumentation.ipynb.
        It has the same columns as the Lang_det_parsed.csv
    |
    |
    --> Language-Detection\Dataset\words_after_agum.csv-> same as words.csv but after agumentation
        
        
2. notes: This folder contains general inforamtion about the project such as refereneces to useful URLs used

3. src: it contains all the .py files:
    |
    |
    --> app.py-> python file for building the app to deploy
    |
    |
    -->parser_request.py-> python class to parse the user input
    |
    |
    -->templates
        |
        |
        -->index.html: basic html file for the user interaction and for the visualizaiont of the output of the model give the user
                      input
        

4. models: it contains the .pkl binary files of both the model and embeddings

5. notebooks: This folder contains all .ipynb files used for parsing, profiling, agumenting, model selection and error analysis
    |
    |
    -->Agumentation: notebooks used for agumenting the dataset
    |
    |
    -->Error_analysis:
        | 
        |
        -->error_anaytics.ipynb: notebook used to create .txt files for analysis of error made by the model
        |
        |
        -->DOCS: this folder contains .csv and .txt files contining data used for error analysis

    |
    |
    -->Model_selection: notebooks used to select the best model for the given task
    |
    |
    -->Profiling: notebooks used to profile both the original and agumented dataset and apply cleaning and parsing logic
    
==================================================================================================================
==================================================================================================================


=================================================================================================================
=============================NOTES==============================================================================
================================================================================================================
In the bottom part of each notebook there are notes related to the solutions used in the implementation of the model.
The notes describe the decision process and critical issues related to model selection, agumentation, oversampling and embedding method selected for the system.

================================================================================================================
================================================================================================================



===============================================================================================================
================================EXERCISE 2====================================================================
==============================================================================================================




Question 1) What kind of model would you use to implement a Machine Translation system? Describe its main features

ANSWER

 There are different models that can be used to implement a Machine Translation system for example RNN's and Transformers.
 The first one could be use in scenarios where the lenght of the input is not that big and the number of languages that is trained to translate is limited. This is because RNN's are known to be difficult to train and handle poorly long input text.
 Transformers on the other hand are, could be used in Machine translation as an encoder-decoder architecture to translate text from one language to another.
 A high level overview of the possible way transformers could be used for this task is the following:
 1)Data collection: collecting pairs of sentences in source and target languages (the relation between source and target is bidirectional). These could be stored in parallel text files or TMX files.

 2)Data cleaning: Before processing the sentences, the retrieved pairs should be filtered, deleting eventual incorrect translation pairs (using different methods).

 3) Data preparation: all the sentences are tokenized into words or subwords, and appropriate preprocessing steps such as lowercasing, punctuation removal, and numerical normalization are applied.
  
 4) Model Training: It uses an encoder and a decoder to process the source and target sentences respectively. The encoder has stacked self-attention layers followed by feed-forward neural networks to capture contextual information from the source sentences. The decoder also has stacked self-attention layers followed by feed-forward neural networks, and it generates translations word by word based on the encoded source sentences.

5) Model Evaluation: The model should be evaluated using specific metrics such as BLEU or Chrf
Other aspect not mentioned is related on how the data (pairs of sentences) is stored for further training of the model.


Question 2) Imagine having to manage customers with different needs: some need the highest quality, by compromising on inference speed. Others need to scale the inference over a huge amount of data, and have time constraints (i.e., they want a translation obtained in a few milliseconds), while maintaining good quality. How would you handle the Machine Translation models in this scenario?

ANSWER

 There are many ways models could be handled in this scenario. 
 The first way is to offer different models for different requirements. For example, if a customer prioritize quality over speed, more sophisticated  models could be used, such as Transformer.
 On the other hand, customers with time constraints and the need for fast inference, i would offer smaller models like SMT or RNNs.

 Another way could be fine-tuning the models to the specific requirements of the customers.


 Question 3) How would you implement a system to monitor the quality of a Machine Translation system currently in production?
 
 ANSWER

 To monitor the quality of a Machine Translation (MT) system currently in production a human-in the loop system could be implemented. First, we must define the quality metrics to evaluate our system and collect a representative sample of translated texts from our MT system. 
 After that the human comes into play. Experts’ translators should conduct evaluations to rate translation quality based on the defined metrics. Other than human feedback automated metrics, such as BLEU, TER, METEOR, could be used.
 Finally, the system should conduct error analysis to identify common errors or patterns in the translations.
