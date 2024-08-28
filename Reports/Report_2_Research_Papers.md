<a id="index"></a>




## Index
1. [Environment Setup](#env)
    1. [Endeavour OS](#endeavour)
    2. [Python 3.12](#py3.12)
    3. [Kate](#kate)
    4. [pip 24.2](#pip2.42)

2. [Experiments Methodology](#methodology)
    1. [Research Papers](#papers)
        1. [Nerf](#nerf)
        2. [Advances in 3D Generation: A Survey](#gen_survey)
        3. [Rapid 3D Model Generation with Intuitive 3D Input](#vr3d)
        4. [GPT4PoinT](#gpt4point)
3. [Results](#results)
4. [Future Steps](#fsteps)
5. [References](#citations)






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










<a id="methodology"></a>




##  Experiments Methodology




We searched through google search engine for research papers which supported 3d model generation.




<a id="papers"></a>




### Research Papers




<a id="nerf"></a>




### [NeRF](https://www.matthewtancik.com/nerf)




For training, a batch of observations in the format of pixel RGBs and rays is fed. The corresponding scene code is randomly initialized and optimized by minimizing both the rendering loss and the diffusion loss, and model parameters ϕ, ψ are also updated along the way.


During training, SSDNeRF jointly learns triplane features of individual scenes, a shared NeRF decoder, and a triplane diffusion prior. During testing, it can perform (a) unconditional generation, (b) single-view reconstruction, as well as multi-view reconstruction.


Excerpts taken from [here - Single-Stage Diffusion NeRF: A Unified Approach to 3D Generation and Reconstruction](https://lakonik.github.io/ssdnerf/)




<a id="gen_survey"></a>





### [Advances in 3D Generation: A Survey](https://arxiv.org/pdf/2401.17807)





This research paper outlines research conducted till January 2024 in the field of 3d Content generation.







<a id="vr3d"></a>





### [Rapid 3D Model Generation with Intuitive 3D Input](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Rapid_3D_Model_Generation_with_Intuitive_3D_Input_CVPR_2024_paper.pdf)




Since beginners can effortlessly sketch 3D paths in the air using AR/VR 3D sketching tools, the model presented in this paper enables easier 3D model generation.


Excerpt taken from [here](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Rapid_3D_Model_Generation_with_Intuitive_3D_Input_CVPR_2024_paper.pdf) and edited to suit the tone of this report.




<a id = "gpt4point"></a>




### [GPT4PoinT](https://github.com/Pointcept/GPT4Point)
<a id="results"></a>




Text based 3D model generation.






<a id="results"></a>





## Results





Insert result here




<a id="fsteps"></a>




## Future steps




Insert future steps here




<a id="citations"></a>






## References:




Insert references here

