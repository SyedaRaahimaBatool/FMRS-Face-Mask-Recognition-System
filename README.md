# FMRS– Face Mask Recognition System

## Abstract
In this project, we have developed an FMRS (Face Mask Recognition System) that maintains attendance records by recognizing whether individuals are wearing masks or not. The system utilizes face recognition modules with an accuracy of approximately 99%. We have employed a CNN architecture (MobileNet V2) and trained it on approximately 5000 sample images. The model's code is then compiled with the face recognition module to detect whether a person is wearing a mask or not.

## Introduction
Facial recognition is a technology used to identify or confirm an individual's identity based on their face. It can be employed in various applications such as identifying people in photos, videos, or in real-time scenarios. Many individuals are already familiar with facial recognition technology through features like FaceID used to unlock smartphones. Facial recognition works by comparing the faces of individuals captured by special cameras with photographs of people on a watchlist. These watchlists can include pictures of both suspected individuals and non-suspected individuals, sourced from various places, including social media accounts.

## Methodology
The FMRS utilizes Python and Machine Learning models from Keras TensorFlow. For the front-end interface, we have used Tkinter. The system offers two main functionalities: Attendance Mark and Check Attendance. We implement machine learning techniques, specifically face recognition, to determine whether a person is known or unknown while wearing a mask.

## Rules of FMRS
The FMRS operates based on the following rules:
- It functions when it recognizes a face in front of the camera using OpenCV.
- It works optimally under daylight conditions.
- The system's performance is dependent on the distance between the encoded face and the known faces, with equal distances being preferable.
- The detection of a mask is based on a specific point on the nose.

## Problem Statements of Simulator
During our evaluation of existing simulators, we identified the following issues or loopholes:
- The system struggles with detecting faces wearing glasses, sometimes resulting in inaccurate detections.
- The detection block occasionally obstructs facial features.
- Night mode significantly impacts the system's detection accuracy.

## Contribution
To address the limitations mentioned above, we propose the following contributions to the FMRS:
- Incorporating additional conditions as inputs to the FMRS to provide more flexible and customizable results.
- Generating and utilizing a diverse range of data samples to enhance the FMRS's performance.

## Conclusion
In conclusion, we have developed an FMRS that automates the attendance system based on face recognition and mask detection. Our evaluation of existing FMRS systems highlighted their limitations in terms of understanding and meeting the required goals. Therefore, our FMRS system offers additional functionalities to overcome these limitations, resulting in improved efficiency and effectiveness.
