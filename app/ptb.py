
import pandas as pd
FILENAME = "assets/dataset.csv"

def pivot_table_builder_func(row, col, aggr_m, aggr_a):
	df = pd.read_csv(FILENAME)

	t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:len})

	return t









