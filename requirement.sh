#!/usr/bin/env bash
apt-get install swig cmake --yes
apt install libopenmpi-dev --yes
pip install opencv-python
pip install mpi4py
pip install baselines
pip install matplotlib
pip install visdom
pip install gym
pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl