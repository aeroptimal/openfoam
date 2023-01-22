from repos import MeshGen
from conf import settings

import os
import json

def get_message():
	messages = settings.AWS_CLIENT.receive_message(
		QueueUrl=settings.OPENFOAM_QUEUE_URL,
		MaxNumberOfMessages=1
	)
	if not messages.get('Messages'):
		return
	receipthandle=messages['Messages'][0]['ReceiptHandle']
	settings.AWS_CLIENT.delete_message(QueueUrl=settings.OPENFOAM_QUEUE_URL, ReceiptHandle=receipthandle)
	return json.loads(messages['Messages'][0]['Body'])

def process_message(response):      
	DomainHeight        = response['DomainHeight']
	WakeLength          = response['WakeLength']
	firstLayerHeight    = response['firstLayerHeight']
	growthRate          = response['growthRate']	
	MaxCellSize         = response['MaxCellSize']

	#%These Values can be played with to improve mesh quality
	BLHeight            = response['BLHeight']
	LeadingEdgeGrading  = response['LeadingEdgeGrading']
	TrailingEdgeGrading = response['TrailingEdgeGrading']
	inletGradingFactor  = response['inletGradingFactor']
	TrailingBlockAngle  = response['TrailingBlockAngle']

	file = response['file']
	id = response['id']

	os.system(f"cp -R templateFolder/* /home/foam/OpenFOAM/-7/run/")  

	Mesh = MeshGen.Create(file, DomainHeight, WakeLength, firstLayerHeight, growthRate, MaxCellSize, BLHeight, LeadingEdgeGrading, TrailingEdgeGrading, inletGradingFactor, TrailingBlockAngle)
	Mesh.CreateFile()
	f = open('/home/foam/OpenFOAM/-7/run/request.dat','w')
	f.write(id)
	f.close()

if __name__ == '__main__':
	response = get_message()
	if response: process_message(response)