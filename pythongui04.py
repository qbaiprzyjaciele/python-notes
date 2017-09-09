import wx

class EditFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))
		self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)

		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Info")
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Close program")	
		
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File")
		
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
		self.Bind(wx.EVT_MENU,self.OnExit,menuExit)
		self.Show(True)
					
	def OnAbout(self,e):
		dialog = wx.MessageDialog(self,"Anitka","Anitka2",wx.OK)
		dialog.ShowModal()
		dialog.Destroy()
	
	def OnExit(self,e):
		self.Close(True)

app = wx.App(False)
frame = EditFrame(None,'Tiny editor')
app.MainLoop()
