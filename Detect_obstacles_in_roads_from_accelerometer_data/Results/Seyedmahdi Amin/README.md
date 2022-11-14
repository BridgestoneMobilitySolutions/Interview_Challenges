# Description

After searching a little bit I decided to solve this challenge by using **unsupervised learning** Algorithms.

I follow the steps below to solve this challenge. 

1. Data Preprocessing 
2. EDA
3. Detecting anomalies in the accelerometer data list
4. Clustering this anomalies with **DTW (Dynamic time warping)** 
5. Labelling to this clusters to use in the future. (By getting some information from Engineering team)

---
After watching this video I found out, obstacles on the road most affected the **acc_z**.
The speed afected the **acc_y**.
Turning right and left afected the **acc_x**.

![Car_axis](https://www.mdpi.com/sensors/sensors-17-00633/article_deploy/html/images/sensors-17-00633-g006-550.jpg) 

After whatching this video I decided to use acc_z to extract anomalies.

[![Automated Synchronization of Driving Data: Video, Audio, IMU, and Telemetry](https://img.youtube.com/vi/a96PO823veM/0.jpg)](http://www.youtube.com/watch?v=a96PO823veM "Automated Synchronization of Driving Data: Video, Audio, IMU, and Telemetry")

---

## DTW (Dynamic time warping)

In time series analysis, dynamic time warping (DTW) is an algorithm for measuring similarity between two temporal sequences, which may vary in speed.

<img src="https://www.databricks.com/wp-content/uploads/2019/04/Euclidean_vs_DTW.jpg" height="500px" >
