## Devanagari Handwriting Recognition : A Major Project
It's includes following steps:

<ul>
  <li>Data collection and Datasets Generation</li>
  <li>Train and Testing model</li>
</ul>

### 1. Data collection and Datasets Generation
<ul>
<li>We have visited more than 30 schools with in the Pokhara valley.</li>
<li>About 2000 students are involved directly during dataset collection.</li>
  
![data_collection_1_](https://user-images.githubusercontent.com/39429615/134664277-64a2f741-276d-4d32-83d2-cf57485d2c7d.PNG)
  
<li>We provided students empty A4 paper and they write down characters accordingly.</li>

![data_collection_3](https://user-images.githubusercontent.com/39429615/134663616-cf8c2986-8d50-4e1e-8af4-d22ae0a41995.PNG)
  
<li>All A4 paper are scanned and converted to .tif image form.</li>
<li>Image are pre-processed and characters are generated in following approach:<a href="https://github.com/np-n/Devanagari-Handwriting-Recognition/blob/master/Dataset%20Generation/Box%20as%20contour/approach1/image_render.py"> Python implementation here </a></li>

![data_collection_4](https://user-images.githubusercontent.com/39429615/134664758-53ce038a-3fd7-42bf-8c20-b4779726ab9c.PNG)

</ul>

### 2. Train and Testing model
<ul>
  <li>Data preprocessing: We already have preprocesse data during dataset generation.</li>
  <li>Convolutional Neural Network is used to train our dataset.<a href="https://github.com/np-n/Devanagari-Handwriting-Recognition/blob/master/Train-Test/02-%20New%20Datasets%20Train-Test/01.%20Devanagari_Character_Recognition_36chars_train-test.ipynb"> Notebook-1here</a></li>
  
![model_training_cnn](https://user-images.githubusercontent.com/39429615/134666567-3fbd43ab-abae-4064-a482-f8149ecdae5d.PNG)

  <li>About 99% training accuracy and 93% validation accuracy has been obtained.</li>
  
  ![classifcation_matrix](https://user-images.githubusercontent.com/39429615/134667362-90fcd654-981d-4828-b09f-c0ddea1caee6.png)


  <li>Model is overfitted,so I applied BatchNormalization and Dropout. But result is not promising.<a href="https://github.com/np-n/Devanagari-Handwriting-Recognition/blob/master/Train-Test/02-%20New%20Datasets%20Train-Test/00.%20Devanagari_Character_Recognition_36chars_train-test.ipynb">Notebook 2 here</a></li>
  <li>Further works need to be done in the area of hyperparameter tuning since the model is overfitted.</li>
  <li>Word and line recognition will be further research area.</li>
  </ul>
