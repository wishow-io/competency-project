import unittest
import pandas as pd
import plotly.express as px
import sys

sys.path.append("../competency_matrix")
from ..competency_matrix.functions import *
from ..competency_matrix.mock_data.user_score import *


def test_get_dataframe_from_dict():
    my_dict = user_level
    expected_df = pd.DataFrame({'values': [1, 4, 3, 2], 'keys': ['Debugging', 'Observability', 'écriture de code','testing','understanding code']})
    result_df = get_dataframe_from_dict(my_dict)
    pd.testing.assert_frame_equal(expected_df, result_df)

test_get_dataframe_from_dict()

if __name__ == '__main__':
    unittest.main()
