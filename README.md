# CM_ACT-R
Python script for Cognitive Modelling Lab Assignment 3 

Solving Tower of Hanoi using ACT-R

Authors: Valeria Rezan, Matiss Kalnare, Catherine Smeyers, Beyza Celep

# Prerequisites
The code is compatible with Python 2.7 only!

Conda is required to create a Conda environment!

# Installation Steps
1. Clone the CCMSuite Repository found here:

https://github.com/sterlingsomers/ccmsuite

2. Set up a Python 2.7 Environment
 - Option A: Using Conda (RECOMMENDED)
   
   Step 1: in terminal/command prompt/Anaconda prompt
   
       conda create -n ccm_env python=2.7
   
   Step 2: Activate the Conda environment
     On macOS/Linux
       source activate ccm_env
   
     On Windows
       activate ccm_env
   
- Option B: Using venv
  NOTE: Python's built-in 'venv' module does not support Python 2.7, so  instead use 'virtualenv'.
  
  Step 1: install 'virtualenv'
  
        pip install virtualenv

  Step 2: Navigate to the cloned repository:
  
       cd ccmsuite

  Step 3: Create a virtual environment named venv using Python 2.7
  
        virtualenv -p /usr/bin/pyhton2.7 venv
  
    NOTE: Replace /usr/bin/pyhton2.7 with the path to your Python 2.7     executable if it's different.

  Step 4: Activate the virtual environment:
  
  On macOS/Linux
  
       source venv/bin/activate

  On Windows:
  
       venv\Scripts\activate

3. Clone this repository or download hanoi_final.py
   
4. Place Python script 'hanoi_final.py' into the ccmsuite directory
   
5. Ensure you are in ccmsuite directory and the environment is activated
   
       cd path/to/directory
   
7. Run Our Script
   
       python hanoi_final.py

Alternatively, open ccmsuite folder as a project in your IDE, and as the interpreter select the created Conda environment. 
    
