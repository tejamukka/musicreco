import os
from config import settings

def load_collection(tags, dataset_dir):
    lst = []
    for tag in tags:
        for subdir, dirs, files in os.walk(os.path.join(dataset_dir, tag)):
          for file in files:
              if "ipynb" in file:
                continue
              filepath = os.path.join(dataset_dir, tag) + "/" + file
              lst.append((filepath, file, tag))

    return lst

def load_test_collection(tags):
	dataset_dir = settings['test_dataset']
	lst = []
	for tag in tags:
		for subdir, dirs, files in os.walk(os.path.join(dataset_dir, tag)):
			for file in files:
				
				filepath = os.path.join(dataset_dir, tag) + "/" + file
				lst.append((filepath, file, tag))

	return lst
