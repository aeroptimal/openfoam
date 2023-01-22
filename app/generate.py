from repos import MeshGen
from conf import settings

import base64
import os
from zipfile import ZipFile
import requests

def write_zip(zipobj : ZipFile,current_folder,foldername):
    dir_list = os.listdir(current_folder+foldername)
    for dir in dir_list:
        if not os.path.isdir(current_folder+foldername+dir):
            zipobj.write(current_folder+foldername+dir,foldername+dir)
        else:
            write_zip(zipobj,current_folder,foldername+dir+'/')

def write_files():
	os.chdir('/home/foam/OpenFOAM/-7/run/'  )
	zipobj = ZipFile('/home/foam/OpenFOAM/-7/run/Mesh.zip', 'w')
	write_zip(zipobj,'/home/foam/OpenFOAM/-7/run/' ,'0/')
	write_zip(zipobj,'/home/foam/OpenFOAM/-7/run/' ,'system/')
	write_zip(zipobj,'/home/foam/OpenFOAM/-7/run/' ,'constant/')
	zipobj.write('/home/foam/OpenFOAM/-7/run/case.foam',arcname='case.foam')

	zipobj = ZipFile('/home/foam/OpenFOAM/-7/run/VTK.zip', 'w')
	zipobj.write('/home/foam/OpenFOAM/-7/run/VTK/run_0.vtk',arcname='run_0.vtk')

	zipobj = ZipFile('/home/foam/OpenFOAM/-7/run/msh.zip', 'w')
	zipobj.write('/home/foam/OpenFOAM/-7/run/fluentInterface/run.msh',arcname='run.msh')

	zipobj = ZipFile('/home/foam/OpenFOAM/-7/run/su2.zip', 'w')
	zipobj.write('/home/foam/OpenFOAM/-7/run/Mesh.su2',arcname='Mesh.su2')


def get_request():
	import time
	t0 = time.time()
	MeshGen.MeshPreview()
	print(f"Elapsed time: {t0 - time.time()}")
	params = MeshGen.GetMeshParams()
	print(f"Elapsed time: {t0 - time.time()}")
	MeshGen.Convert2Su2()
	print(f"Elapsed time: {t0 - time.time()}")

	data = {
		"status":True,
		"params":params,
	}

	return data

def post_request(data):
	f = open('/home/foam/OpenFOAM/-7/run/request.dat','r')
	id = f.read()
	f.close()

	file1 = open('/home/foam/OpenFOAM/-7/run/msh.zip','rb')
	file2 = open('/home/foam/OpenFOAM/-7/run/VTK.zip','rb')
	file3 = open('/home/foam/OpenFOAM/-7/run/su2.zip','rb')
	file4 = open('/home/foam/OpenFOAM/-7/run/Mesh.zip','rb')
	file5 = open('/home/foam/OpenFOAM/-7/run/cercana.png','rb')
	file6 = open('/home/foam/OpenFOAM/-7/run/lejana.png','rb')

	data['files'] = {
		"msh": base64.b64encode(file1.read()).decode("utf-8"),
		"vtk": base64.b64encode(file2.read()).decode("utf-8"),
		"su2": base64.b64encode(file3.read()).decode("utf-8"),
		"foam": base64.b64encode(file4.read()).decode("utf-8"),
		"cercana": base64.b64encode(file5.read()).decode("utf-8"),
		"lejana": base64.b64encode(file6.read()).decode("utf-8"),
	}

	requests.post(f"{settings.HOST}/mesh/result/{id}",
		json=data,
	)

	file1.close()
	file2.close()
	file3.close()
	file4.close()
	file5.close()
	file6.close()

if __name__ == '__main__':
	data = get_request()
	write_files()
	post_request(data)
	print('done')