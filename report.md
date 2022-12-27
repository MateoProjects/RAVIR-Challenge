# RAVIR challenge

## Introduction

RAVIR: A Dataset and Methodology for the Semantic Segmentation and Quantitative Analysis of Retinal Arteries and Veins in Infrared Reflectance Imaging Challenge.

The original dataset only contains 23 images. Applying Data Augmentation I increased the dataset to 92 images adding 69 images more.

For this practice I trained a different AI with the architecture of Unet. The parameters estudied for see if exists any improvements are Optimizer and Batchsize.

To load images and avoid problems with memory I used a Data Generator for load images during the training, not before and the image size used for train model and test is 512x512.

For test better and see if model has enought data I made a data augmentation rotating age image 90 and 180 degrees for see if exists any improvement with more data. An example is provided below.


Original           |  Rotated 90 | Rotated 180
:-------------------------:|:-------------------------:|:-------------------------:
![](RAVIR_Dataset\train\training_images\IR_Case_011.png)  |  ![](RAVIR_Dataset_DA\training_images\IR_Case_011_90.png) |  ![](RAVIR_Dataset_DA\training_images\IR_Case_011_180.png)

**Mask**

Original           |  Rotated 90 | Rotated 180
:-------------------------:|:-------------------------:|:-------------------------:
![](RAVIR_Dataset\train\training_masks\IR_Case_011.png)  |  ![](RAVIR_Dataset_DA\training_masks\IR_Case_011_90.png) |  ![](RAVIR_Dataset_DA\training_masks\IR_Case_011_180.png)


## Test and metrics

A differents tests was made. The results during the training can see on the following plots that are below. The plots show was de accuracy and the loss during the training. The diferent test executed was changing first the optimitzer. Two optimizers was tested, first RMSPROP and second Adam without data augmentation and the second test was changing the batchsize.

### **RMSPROP Without Data Augmentation Batchsize 4**


Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\rmsprop_4_no_da_acc.png)  |  ![](report_results\rmsprop_4_no_da_loss.png) 

### **Adam Without Data Augmentation Batchsize 4**


Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\adam_4_no_da_acc.png)  |  ![](report_results\adam_4_no_da_loss.png)) 



### **RMSPROP Without Data Augmentation Batchsize 8**


Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\rmsprop_8_no_da_acc.png)  |  ![](report_results\rmsprop_8_no_da_loss.png)) 



### **Adam Without Data Augmentation Batchsize 8**

Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\adam_8_no_da_acc.png)  |  ![](report_results\adam_8_no_da_loss.png) 



### **RMSPROP Data Augmentation Batchsize 8**

Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\rmsprop_8_da_acc.png)  |  ![](report_results\rmsprop_8_da_loss.png)



### **Adam Data Augmentation Batchsize 8**

Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\adam_8_da_acc.png)  |  ![](report_results\adam_8_da_loss.png)

### **RMSPROP Data Augmentation Batchsize 16**

Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\rmsprop_16_da_acc.png)  |  ![](report_results\rmsprop_16_da_loss.png)



### **Adam Data Augmentation Batchsize 16**

Accuracy          |  Loss
:-------------------------:|:-------------------------:
![](report_results\adam_16_da_acc.png)  |  ![](report_results\adam_16_da_loss.png)



## Metrics

|Name                          |Sensitivity       |Specificity       |Accuracy          |jaccard           |dice_val          |
|------------------------------|------------------|------------------|------------------|------------------|------------------|
|adam_bat4_15_epoc_noDA.h5     |**0.3907**|0.665|0.6388|0.0876|0.159|
|adam_bat8_15_epoc_noDA.h5      |0.0009|0.9974|0.8998|0.0009|0.0019|
|adam_bat8_15_epoc_DA.h5    |5.265e-05|0.999|0.9046|5.257e-05|0.0001|
|adam_bat16_15_epoc_DA.h5    |0.0005|**0.9998**|0.9046|0.0005|0.001|
|rmsprop_bat4_15_epoch_noDA.h5 |0.00039|0.9991|0.9018|0.00038|0.0007|
|rmsprop_bat8_15_epoc_noDA.h5   |0.00138 |0.9979|0.8999|0.0013|0.0027|
|rmsprop_bat8_15_epoch_DA.h5    |0.278| 0.997|**0.929**|**0.269**|**0.4139**|
|rmsprop_bat16_15_epoch_DA.h5   |0.0007 |0.999| 0.903|0.0007|0.0014|


## Examples of results of predictions


RMSPROP 8 no DA | RMSPROP 8 DA
:-------------------------:|:-------------------------:
![](report_results\results_rmsprop_8_no_da.png)  |  ![](report_results\results_rmsprop_8_2_da.png)

Adam 4 no DA | Adam 8 no DA
:-------------------------:|:-------------------------:
![](report_results\results_adam_4_no_da.png)  |  ![](report_results\results_adam_8_no_da.png)


## Conclusions and future work

When I trined Unet with images I experimented with different parameters and I found that training with the same parameters again give me different results and in some cases a good results. One of the examples is RMSPROP 8 DA that predicts good the mask image. This was achieved training again a lot of times with same parameters so here we have a problem that is that the initial weights can affect to the results. 

The main conclusion is that Unet it's not a good architecture for this challenge. I achieved a good results with RMSPROP 8 DA but the results are not good enough. I think that the problem is that the images are not enough to train the network. I think that the best solution is to use a network that is pretrained with a lot of images and then fine tune the network with the images of this challenge.

