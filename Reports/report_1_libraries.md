<a id="index"></a>




## Index
1. [Environment Setup](#env)
    1. [Endeavour OS](#endeavour)
    2. [Python 3.12](#py3.12)
    3. [Kate](#kate)
    4. [pip 24.2](#pip2.42)
    5. [SolidPython 2](#solid2)

2. [Experiments Methodology](#methodology)
    1. [Libraries](#lib)
        1. [Open3D](#open3d)
        2. [SolidPython](#solid_python)
        3. [PyVista](#pyvista)
        4. [VPython](#vpython)
        5. [blender3d](#blender3d)
        6. [Pytorch 3D (Version 0.7.6)](pytorch3d)
        7. [Numpy STL (Version 3.1.2)](numpy-stl)
    2. [Tests](#tests)
        1. [Import Success](#import)
        2. [3d Model creation Successful](#create)
        3. [3d View Successful](#view)
3. [Results](#results)
4. [Citations](#citations)


<a id="env"></a>




## Environment Setup




<a id="endeavour"></a>




### [Endeavour OS](https://endeavouros.com/news/our-fifth-anniversary-the-return-of-arm-and-the-endeavour-release-with-plasma-6-1-is-here/)




Endeavour OS provides an Arch-based user-friendly Linux experience.




<a id="py3.12"></a>




### [Python 3.12](https://www.python.org/downloads/release/python-3120/)




Python 3.12 introduces significant enhancements aimed at performance and usability.




<a id="kate"></a>




### [Kate](https://kate-editor.org/get-it/)




 Kate serves as a versatile text editor ideal for coding tasks.




 <a id="pip2.42"></a>




### [pip 24.2](https://pypi.org/project/pip/24.2/)




 pip version 24.2 improves package management efficiency in Python projects.




 <a id="solid2"></a>




### [SolidPython 2](https://pypi.org/project/solidpython2/2.1.0/)




SolidPython version 2 enhances parametric modeling capabilities using OpenSCAD syntax within Python.






<a id="methodology"></a>




##  Experiments Methodology




We searched through google search engine for libraries which supported 3d modelling in python and gathered these libraries.

1. [Open3D](#open3d)
2. [SolidPython](#solid_python)
3. [PyVista](#pyvista)
4. [VPython](#vpython)
5. [blender3d](#blender3d)
6. [Pytorch 3D (Version 0.7.6)](pytorch3d)
7. [Numpy STL (Version 3.1.2)](numpy-stl)

From these we then tried [Solidpython 2](#solid2) and performed 3 tests:

1. [Import](#import)
2. [Model creation](#create)
3. [Model View](#view)



<a id="lib"></a>




### Libraries





There are several Python libraries and tools that support 3D modeling. Here's a breakdown of some notable options:





<a id="open3d"></a>





#### 1. [Open3D (Version 0.18.0)](https://pypi.org/project/open3d/0.18.0/)





Open3D is an open-source library designed for efficient and easy processing of 3D data. It provides a wide range of functionalities including 3D data structures, processing algorithms, scene reconstruction, surface alignment, 3D visualization with physically-based rendering (PBR), and support for 3D machine learning with PyTorch and TensorFlow. Open3D is available in both C++ and Python versions, offering GPU acceleration for core 3D operations .





<a id="solid_python"></a>





#### 2. [SolidPython 2](https://pypi.org/project/solidpython2/2.1.0/)





SolidPython is a rich modeling library that allows for the creation of 3D scenes in a format similar to OpenSCAD. It generates OpenSCAD code that can be edited or directly saved to STL files. This library is particularly useful for creating complex 3D models and performing operations like moving, rotating, merging, and subtracting shapes .





<a id="pyvista"></a>




#### 3. [PyVista](https://pypi.org/project/pyvista/0.44.1/)





PyVista is a Python library for 3D plotting and mesh analysis, providing a streamlined interface for the Visualization Toolkit (VTK). It facilitates the visualization of depth maps and meshes from STL files among other features. PyVista is suitable for those who need advanced visualization capabilities alongside 3D modeling .






<a id="vpython"></a>





#### 4. [VPython](https://pypi.org/project/vpython/7.6.5/)





Mentioned as a recommendation for developing a basic 3D modeling tool, VPython is known for its built-in mouse support and convenience functions for translating mouse-space coordinates to 3D world space. While it might not offer the same level of complexity as some other options, it could be a good starting point for simpler applications .






<a id="blender3d"></a>





#### 5. [Blender 3D](https://www.blender.org/)





Although not a Python library per se, Blender 3D is an open-source 3D modeling tool written in Python. It features an OpenGL viewport responsive to mouse events and has extensive 3D modeling capabilities. Blender serves as an inspiration for those looking to develop custom 3D modeling tools .






<a id="pytorch3d"></a>




#### 6. [Pytorch 3D (Version 0.7.6)](https://pypi.org/project/pipablepytorch3d/0.7.6/)




PyTorch3D is designed to integrate smoothly with deep learning methods for predicting and manipulating 3D data.




<a id="numpy-stl"></a>




#### 7. [Numpy STL (Version 3.1.2)](https://pypi.org/project/numpy-stl/3.1.2/)





Simple library to make working with STL files (and 3D objects in general) fast and easy.





<a id="tests"></a>




### Tests




<a id="import"></a>





#### Import Success





solidpython2 was first installed through





``` pip install solidpython2 ```





Then imported as




```




import solid2





```




This test was Successful.





<a id="create"></a>





#### 3d Model creation Successful





A model can be created in solidpython2 simply by writing the name of the shape and its perimeters.

This model can then be saved as a scad file and viewed in Openscad or any other online scad file viewer.

The name of the scad file is same as that of the python file which saved that model.




```




from solid2 import *


d = cube(5) + sphere(5).right(5) - cylinder(r=2, h=6)

d.save_as_scad()




```




<a id="view"></a>




#### 3d View Successful





We viewed the file in an online scad viewer





<a id="citations"></a>






## Citations:





1. [Open3D setup for parallelization](https://www.open3d.org/#:~:text=Open3D%20is%20an%20open%2Dsource,is%20set%20up%20for%20parallelization)
2. [Best Modules to develop a simple windowed 3D modeling application](https://stackoverflow.com/questions/410941/best-modules-to-develop-a-simple-windowed-3d-modeling-application)
3. [Top python libraries for 3D machine learning](https://analyticsindiamag.com/ai-mysteries/top-python-libraries-for-3d-machine-learning/)
4. [3D modelling with python](https://medium.com/@alexeyyurasov/3d-modeling-with-python-c21296756db2)
5. [Best language and library for rapid 3D model prototyping](https://stackoverflow.com/questions/8510209/best-language-library-for-creating-3d-models-for-rapid-prototyping)
6. [Pyslm](https://github.com/drlukeparry/pyslm)
7. [Software to generate Python codes while designing 3D model](https://www.quora.com/Is-there-a-software-that-can-be-used-to-generate-Python-codes-while-designing-a-3D-model)
8. [Python 3D modeling at sourceforge.net](https://sourceforge.net/directory/3d-modeling/python/)
9. [Python libraries for mesh and point cloud visualization part 1](https://towardsdatascience.com/python-libraries-for-mesh-and-point-cloud-visualization-part-1-daa2af36de30)
10. [What is the best gui library for python](https://www.reddit.com/r/Python/comments/wedvzi/what_is_the_best_gui_library_for_python/)
11. [Endeavour OS](https://endeavouros.com/news/our-fifth-anniversary-the-return-of-arm-and-the-endeavour-release-with-plasma-6-1-is-here/)
12. [Python 3.12](https://www.python.org/downloads/release/python-3120/)
13. [Kate](https://kate-editor.org/get-it/)
14. [pip 24.2](https://pypi.org/project/pip/24.2/)
15. [SolidPython 2](https://pypi.org/project/solidpython2/2.1.0/)
16. [Open3D](https://pypi.org/project/open3d/0.18.0/)
18. [PyVista](https://pypi.org/project/pyvista/0.44.1/)
19. [VPython](https://pypi.org/project/vpython/7.6.5/)
20. [Blender 3D](https://www.blender.org/)
21. [Pytorch 3D (Version 0.7.6)](https://pypi.org/project/pipablepytorch3d/0.7.6/)
22. [Numpy STL (Version 3.1.2)](https://pypi.org/project/numpy-stl/3.1.2/)
