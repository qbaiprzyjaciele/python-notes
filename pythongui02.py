import wx

class EditFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))
		self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
		self.Show(True)

app = wx.App(False)
frame = EditFrame(None,'Tiny editor')
app.MainLoop()
