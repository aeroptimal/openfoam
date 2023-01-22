FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
	&& apt-get install -y \
		vim \
		ssh \
		sudo \
		wget \
		python3-pip \
		software-properties-common ;\
		rm -rf /var/lib/apt/lists/*

RUN useradd --user-group --create-home --shell /bin/bash foam ;\
	echo "foam ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN sudo sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -" ;\
	sudo add-apt-repository http://dl.openfoam.org/ubuntu ;\
	sudo apt-get update ;\
	sudo apt-get install -y --no-install-recommends openfoam7 ;\
	echo "source /opt/openfoam7/etc/bashrc" >> ~foam/.bashrc ;\
	echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> ~foam/.bashrc

ADD https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.9&type=binary&os=Linux&downloadFile=ParaView-5.9.0-osmesa-MPI-Linux-Python3.8-64bit.tar.gz /opt/paraview.tar.gz

WORKDIR /opt

RUN sudo tar -xvzf paraview.tar.gz ;\
	sudo mv ParaView-5.9.0-osmesa-MPI-Linux-Python3.8-64bit paraview-5.9

RUN sudo ln -s /opt/paraview-5.9/bin/paraview /usr/bin/paraview ;\
	sudo ln -s /opt/paraview-5.9/lib/paraview-5.9/  /usr/lib/paraview-5.9

USER foam

RUN mkdir -p /home/foam/OpenFOAM/-7/run

WORKDIR /

COPY . .

RUN sudo chmod -R 777 templateFolder/*
RUN sudo pip3 install -r requirements.txt

CMD ["bash","-i","job.sh"]