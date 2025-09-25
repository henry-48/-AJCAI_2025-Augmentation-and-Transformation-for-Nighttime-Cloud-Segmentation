# [AJCAI_2025] Augmentation and Transformation for Nighttime Cloud Segmentation in All-Sky Camera Images

Official implementation for the AJCAI 2025 paper "Augmentation and Transformation for Nighttime Cloud Segmentation". This research explores advanced data augmentation techniques to improve cloud segmentation performance in nighttime all-sky camera imagery.

📖 Abstract

For ground-based optical telescopes, automated planning and control
systems play a vital role in ensuring efficient acquisition of scientific data. These
systems rely on All-Sky Cameras (ASC) to capture real-time sky conditions, in-
cluding sky obscuration and lunar position. We address the task of assessing sky
conditions under ambient nighttime illumination and in the presence optical arti-
facts such as lens flares. Seeking to develop a solution based on a neural network
model, we are faced with a lack of real nighttime cloud segmentation bench-
mark datasets. To address this, we propose an Augmentation and Transformation
for Nighttime Cloud Segmentation in All-Sky Camera Images (AT-NCS) that
converts existing daytime and dusk cloud segmentation datasets into a synthetic
benchmark simulating realistic nighttime observing conditions. Our approach in-
corporates key challenges such as night sky glow, and optical artifacts (e.g., lens
flare), thereby providing a training and evaluation framework for ASC-based ob-
servation systems. This work aims to enhance the reliability and value of au-
tonomous observatory operations under diverse nighttime environments.

In this repoitory, we has list three model used to verificate the useof the augmentation and transformation pipeline. Each of them are adopted for the cloud segmentation task.

The detail of the implementation of each augmentaiton technique is list in Augmentation Implementations.

The day-to-night style transfer is created by viraj kadam from kaggle on city day-to-night task. I adopted it to the cloud day-to-night.
