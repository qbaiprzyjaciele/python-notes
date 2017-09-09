import wx
import wx.grid as gridlib
class EditFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))

		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Info")
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Close program")	
		panel = wx.Panel(self)		
		grid = gridlib.Grid(panel)
		grid.CreateGrid(12,8)
		grid.SetCellValue(0,0,"Lol");
		grid.SetCellBackgroundColour(0,0,wx.GREEN)		
		grid.SetCellBackgroundColour(1,1,wx.Colour(250,180,30))
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(grid,1,wx.EXPAND)
		panel.SetSizer(sizer)
			
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





