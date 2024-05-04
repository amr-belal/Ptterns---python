# # product example 1

# class ConcreteProductA :
    
#     def __init__(self):
#         self.name = 'ConcreteProductA'
        
# class ConcreteProductB :
    
#     def __init__(self):
#         self.name = 'ConcreteProductB'
        
# class ConcreteProductC :
#     def __init__(self):
#         self.name = 'ConcreteProductC'
        
# class CreateObject(object):
    
#     @staticmethod 
#     def create_object(Property):
#         if Property == "a":
#             return ConcreteProductA()
        
#         if Property=="b" :
#             return ConcreteProductB()
        
#         if Property=="c" :
#             return ConcreteProductC()
#         return None
        
# Product = CreateObject()
# Product=CreateObject.create_object("a")
# print(Product.name)


# =============================================================================


# Example 2 : Assign role (of student or teacher) depending on input given 

class SetStudent:
    def __init__(self):
        self.rule = " I am student"

class SetTeacher: 
    
    def __init__(self):
        self.rule = " I am teacher"
        
class InputRole : 
    @staticmethod
    def giveRole (Role):
        if Role == "student": 
            return SetStudent()
        if Role == "teacher": 
            return SetTeacher()
        return None

if __name__ =="__main__" : 
    GetRule = input(" what is you state? \n")
    person =InputRole.giveRole(GetRule)
    print(person.rule)
    
    
# =============================================================================


# factory example 3 advaned 
"""Imagine an application that needs to convert a Song object into its string representation using 
a specified format. Converting an object to a different representation is often called serializing. 
You will often see these requirements implemented in a single function or method"""


# In serializer_demo.py

# import json
# import xml.etree.ElementTree as et

# class Song:
#     def __init__(self, song_id, title, artist):
#         self.song_id = song_id
#         self.title = title
#         self.artist = artist


# class SongSerializer:
#     def serialize(self, song, format):
#         if format == 'JSON':
#             song_info = {
#                 'id': song.song_id,
#                 'title': song.title,
#                 'artist': song.artist
#             }
#             return json.dumps(song_info)
#         elif format == 'XML':
#             song_info = et.Element('song', attrib={'id': song.song_id})
#             title = et.SubElement(song_info, 'title')
#             title.text = song.title
#             artist = et.SubElement(song_info, 'artist')
#             artist.text = song.artist
#             return et.tostring(song_info, encoding='unicode')
#         else:
#             raise ValueError(format)
"""In the example above, you have a basic Song class to represent a song and a SongSerializer class that can convert a song object 
into its string representation according to the value of the format parameter.

The .serialize() method supports two different formats: JSON and XML.
Any other format specified is not supported, so a ValueError exception is raised.

"""

#Let's use the Python interactive shell to see how the code works:
# >>> import serializer_demo as sd
# >>> song = sd.Song('1', 'Water of Love', 'Dire Straits')
# >>> serializer = sd.SongSerializer()

# >>> serializer.serialize(song, 'JSON')
# '{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

# >>> serializer.serialize(song, 'XML')
# '<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

# >>> serializer.serialize(song, 'YAML')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "./serializer_demo.py", line 30, in serialize
#     raise ValueError(format)
# ValueError: YAML


# =================================================================================================

class 