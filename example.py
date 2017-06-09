from entity_uploader import UploadEntity

with open('example_entities.txt', 'r') as readfile:
    for obj in readfile.read().split('\n'):
        if obj.strip() != '':
            e = UploadEntity(name=obj)
            print(e.to_dict())
