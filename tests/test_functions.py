import unittest
import pandas as pd
import plotly.graph_objs as go
import os
import time
from app.data_functions import *


class Test(unittest.TestCase):

    timestr = time.strftime("%Y%m%d-%H%M%S")

    def test_get_dataframe_from_dict(self):
        my_dict = {
            "Debugging": 1,
            "Observability": 4,
            "écriture de code": 3,
            "testing": 2,
            "understanding code": 2
        }
        expected_df = pd.DataFrame({"values": [1, 4, 3, 2, 2], "keys": [
                                   "Debugging", "Observability", "écriture de code", "testing", 'understanding code']})
        result_df = get_dataframe_from_dict(my_dict)
        pd.testing.assert_frame_equal(expected_df, result_df)

    def test_generate_radar_chart_fig(self):
        test_df = pd.DataFrame({
            "keys": ["Debugging", "Observability", "écriture de code", "testing", "understanding code"],
            "values": [1, 4, 3, 2, 2]
        })
        result_fig = generate_radar_chart_fig(
            test_df, "test_id", "test_family")
        self.assertIsInstance(result_fig, go.Figure)
        self.assertEqual(len(result_fig.data), 1)
        self.assertEqual(result_fig.layout.title.text,
                         "Radar Chart de test_id, famille : test_family")

    def test_convert_fig_to_image(self):
       # Define a test fig object
        fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
        dir = 'test_files/images'
        id = 'test_id'
        family = 'test_family'
        if not os.path.exists(dir):
            os.makedirs(f'{dir}/{id}')
        img = convert_fig_to_image(fig, id, family)
        assert img is not None
        expected_file_name = f"radar_chart_{id}_{family}_{str}"
        assert any(
            expected_file_name in filename for filename in os.listdir(f'{dir}/{id}'))
        os.rmdir(dir)


if __name__ == '__main__':
    unittest.main()
