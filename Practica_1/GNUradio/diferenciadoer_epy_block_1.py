import numpy as np
from gnuradio import gr

class blk (gr.sync_block):
	
	def __init__(self):
		gr.sync_block.__init__(
			self,
			name ='e_Diff',
			in_sig=[np.float32],
			out_sig=[np.float32]
		)
		self.acum_anterior = 0    
	def work (self, input_items, output_items):
		x = input_items[0] 
		y0 = output_items[0]
		limited_x = x[:3]
		N = len(limited_x)
		
		diff = np.cumsum (limited_x) - self.acum_anterior
		self.acum_anterior = diff[N-2]
		y0[:3] = diff

		return len (y0[:3])
