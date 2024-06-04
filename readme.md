# FileChecker
**Powered by 3DSurveyGroup|DABC|Politecnico di Milano**
***
### Introduction
_The tools for preparing training set for Object detection job_

This easy software is design to help us collect annoataion of images. Other availble softwares are too much complicated with unneccesary functions, and cannot be customed to our need. Therefore we use this one.

What you can expect:
- You can annotate the image files from scrath
- You can edit already provided annotation, change the classification and cancel them.
- **This software will automatically generate the txt file that records your annotation, please send back to us these files.**

### Interface OverView
![Interface_main_initial](docs/image.png)
The interface is giving you a frame of $640 \times 640$ on the left. One the right we have a board that gives the list of annotated instances (indicated by the red arrow) and the a log board at the bottom right (indicated by the blue arrow). From the log board some suggestions will be made to guide your operation. 


### Getting started
In order to start you have to:
1. Click **[File]** - **[Open]** to load **the folder of the images and txt files**.
    ![Interface_main_open](docs/image-5.png)
2. Click '**Show && Edit Annotation**' to show the annotation of the current image.
    You can double click an existing box to edit previous annotation.
    ![alt text](docs/image-7.png)
3. You can also drag a box and click **[+]** to add new annotation.
   ==Notice that the new annotation will not be added if the overlap is over 0.5.==
   ![alt text](docs/image-6.png)
   It's prefered that you annotate with smaller and continuous bounding boxes for objects that takes the diagonal area of the corresponding area. In this way, it's possible also to annotate the part that is left.
   ![Interface_annoationMode](docs/image-4.png)
   After clicking **[+]** buttom, you will be able to access to the annotation window.
   ![Interface_annotationbox](docs/image-2.png)    
   In the list you can choose the predefined categories. You can also opt to delete the current annotation.  
   ![Interface_annotation_list](docs/image-3.png)
4. You can also double click the existing box to edit current annotation.
5. Click **[Accept]** or **[Abort]** to save or cancel the modification.
    ==Note that if you don't do that, the software will not allow you to go to other images.==
6. Click '**Next**' or '**Previous**' to switch to the next or previous image.

### Contact Information
If you happened to be encountering any problem, you can contact: ` kai.zhang@polimi.it` 
We will be happy to recieve your comment and suggestion.

<!--

### Features and Functionality
### Advanced
### Troubleshooting
### To be Undated
- [ ] currently no


### How to export the soft ware
[Download QtDesigner](https://build-system.fman.io/qt-designer-download)

[Export to macos](https://pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/)

[Export to exe](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)
> Note: run this in the console: `pyinstaller --onefile --noconsole --icon=Checker.ico  --name "fileChecker" fileChecker_roi.py`

-->