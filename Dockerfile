FROM ghcr.io/aeroptimal/openfoam-base:latest

# ADD https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.9&type=binary&os=Linux&downloadFile=ParaView-5.9.0-osmesa-MPI-Linux-Python3.8-64bit.tar.gz /opt/paraview.tar.gz

# WORKDIR /opt

# RUN sudo tar -xvzf paraview.tar.gz ;\
# 	sudo mv ParaView-5.9.0-osmesa-MPI-Linux-Python3.8-64bit paraview-5.9

# RUN sudo ln -s /opt/paraview-5.9/bin/paraview /usr/bin/paraview ;\
# 	sudo ln -s /opt/paraview-5.9/lib/paraview-5.9/  /usr/lib/paraview-5.9

WORKDIR /

USER foam

RUN mkdir -p /home/foam/OpenFOAM/-7/run

COPY . .

WORKDIR /app

RUN sudo chmod -R 777 templateFolder/* \
    && pip3 install --upgrade pip \
    && sudo pip3 install -r requirements.txt

CMD ["bash","-i","job.sh"]