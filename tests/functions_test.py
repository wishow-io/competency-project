import unittest
import os
import zipfile
import pandas as pd
import plotly.express as px
import sys


sys.path.append("../competency_matrix")
import functions
from functions import generate_zipfile_by_family


class TestGenerateZipfile(unittest.TestCase):
    
    def setUp(self):
        self.dict = {
            "1": {
                "Debugging & Observability": {
                    "Debugging":"1",
                    "Observability":"4"
                },

                "Quality & testing": {
                    "écriture de code":"4",
                    "testing":"3"
                },

                "Software design & architecure ": {
                    "understanding code":"2"
                },
            },

            "2": {

                "Debugging & Observability": {
                    "Debugging":"3",
                    "Observability":"5"
                },

                "Quality & testing":{
                    "écriture de code":"3",
                    "testing":"2"
                },

                "Software design & architecure ": {
                    "understanding code":"2"
                },
            }
        }

    
                
    def test_create_zipfile(self):
        # Call the function
        generate_zipfile_by_family(self.dict)
        print('hello')
        
        # Check if the zipfile exists
        # self.assertTrue(os.path.exists("myzipfile1.zip"))
        # self.assertTrue(os.path.exists("myzipfile2.zip"))


    # def test_create_dataframe(self.dict):
    # def test_create_fig(self.dict):
    # def test_convert_fig_to_image(self.dict): 

if __name__ == '__main__':
    unittest.main()
