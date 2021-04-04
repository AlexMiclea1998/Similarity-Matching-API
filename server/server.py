#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource
from xml.etree import ElementTree as ET
import re
from fuzzywuzzy import fuzz



app = Flask(__name__)
api = Api(app)


class Similarity(Resource):

    def get(self, urlP1, urlP2):
        lableP1 = []
        tree = ET.parse(urlP1)
        root = tree.getroot()
        for nodes in root:
            for node in nodes:
                name = node.get('name')
                lableP1.append(name)

        for elem in lableP1:
            lableP1.remove(None)

        lableP2 = []
        tree2 = ET.parse(urlP2)
        root2 = tree2.getroot()
        for nodes in root2:
            for node in nodes:
                name = node.get('name')
                lableP2.append(name)

        for elem in lableP2:
            lableP2.remove(None)

         # Compare Similarity between String Lists

        p1 = ' '
        for elem in lableP1:
            p1 = p1 + elem + ' '

        p2 = ' '
        for elem in lableP2:
            p2 = p2 + elem + ' '
        
       
    
        Token_Set_Ratio = fuzz.token_set_ratio(p1,p2)
        Token_Sort_Ratio = fuzz.token_sort_ratio(p2, p1)
        Partial_Token_Sort_Ratio = fuzz.partial_token_set_ratio(p1,p2)
        WRatio = fuzz.WRatio(p1,p2)

        final = (Token_Set_Ratio + Token_Sort_Ratio + Partial_Token_Sort_Ratio + WRatio)/4
        

        print()
        print("Process 1 : ",p1)
        print()
        print("Process 2 : ",p2)
        print()
      
 
        return {'Similarity ': final }

    def post(self):
        return {'data': 'posted'}

api.add_resource(Similarity, '/similarity/<string:urlP1>/<string:urlP2>'
                 )

if __name__ == '__main__':
    app.run(debug=True)


			