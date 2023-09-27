import json
import datetime
import ast

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'myfile.json'
    __objects = dict()

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update(
            {obj['id']: {
            "Firstname":obj['first_name'], 
            "Lastname":obj['last_name']
            }}
            )
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def incr(self, id):
        """Increments attendance number
        for each student after scanning QR Code
        Returns:
            _type_: None
        """
        if id:
            if id in self.all():
                if 'att' not in self.all()[id]:
                    now = datetime.datetime.now().isoformat()
                    print('attendance not found')
                    print('Creating Attendance Record')
                    self.all()[id]['att'] = 1
                    self.all()[id]['last_scan'] = now
                    self.all()[id]['next_scan'] = self.get_n_days_after_date().isoformat()
                print('found attendance')
                if not datetime.datetime.now() < datetime.datetime.strptime(self.all()[id]['next_scan'], '%Y-%m-%dT%H:%M:%S.%f'):
                    self.all()[id]['att'] += 1
                    nnow = datetime.datetime.now()
                    self.all()[id]['last_scan'] = nnow
                    self.all()[id]['next_scan'] = self.get_n_days_after_date().isoformat()
                    print('Attendance Updated')
                print('Attendance Already Updated Dont Try Again')
                

            else:
                print('STUDENT ID NOT FOUND')
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
                for key in jo:
                    self.all()[key] = jo[key]
        except:
            pass

    def get_n_days_after_date(self, date_format="%d %B %Y"):
        date_n_days_after = datetime.datetime.now() + datetime.timedelta(days=7)
        return date_n_days_after
        
    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = dict()
        for key in self.all():
            json_objects[key] = self.all()[key]
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)