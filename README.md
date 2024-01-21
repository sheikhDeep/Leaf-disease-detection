# Leaf Disease Detection

# Motive
  [](https://github.com/sheikhDeep/Leaf-disease-detection/blob/main/reference-images/hugg.png)
  The purpose of this project is to create an application that can detect various kinds of leaf diseases. This app can detect the name of the leaf. It can also detect if the leaf is diseased or not and will also tell the disease name. It can detect seven kinds of leafs and their diseases.
  The leaves are - `Banana`, `Cucumber`, `Mango`, `Maple`, `Pepper`, `Rose`, `Tomato`. The diseases are - `Sigatoka`, `Powdery-mildew`, `Anthracnose`, `Leaf-spot`. 

# Data Collection
  I collected my data manually. I tried to collect data automatically with the help of tools like selenium but it was not giving me accurate images. So I choose to collect data manually by Google search.

# Data Preprocessing and Image Augmentation
  Healthy images were available on the internet but there were not many images available of the diseased leaves. As my dataset is small I had to augment images for increasing the number of images. 

# Model Training
  For better performance and time effect I choose 'Fastai' and 'Pytorch'. 
  For training, I tried two models `resnet-34` and `resnet-18`, and saved the best-performing model for future use. Both models gave `99%` accuracy. `restenet-18` was faster than `restnet-34` so I selected `restnet-18`. 

# Final Model Selection
  As I used 2 types of models here are their best results.<br>  
   |   Model       |     Accuracy|   F1_score | Precision |  Time  |
  |---------------|-------------|-------------|-----------|--------|
  | Resnet18      |    0.998834 |   0.928576	|  0.930272 |  01:38 |
  | Resnet34      |     0.999863|	0.932688		| 0.932644	|  02:11 | 

   As `resnet34` and `resnet18` both reach `99%` Accuracy, another score is way close, but `resnet18` is a little bit faster. So I chose `resnet18` for further work.

# Model size Compression
  Model compression is very essential. By compressing the models with ONNX, you can achieve smaller model sizes, faster inference times, and reduced memory requirements. Model compression code can be found in the `notebook
  /leaf-disease-detection.ipynb` file.

# Deployment
  I deployed my project in `HuggingFace`. You can see this from [here](https://huggingface.co/spaces/sheikhDeep/leaf-disease-detection).

# Interface
  I also deployed the app on `render.com`. The UI of the application is simple. Here is the [link](https://leaf-disease-detection.onrender.com)

 # Conclusion
   There are many areas to improve.
   1. More correct disease images can be added in the future to make the model more accurate and versatile.
   2. Will try different models in the future.
   3. Will improve the UI of the deployed application.
