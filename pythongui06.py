import wx
import wx.grid as gridlib
import sqlite3

class RequestDao():
	def __init__(self,_connection):
		self.connection = _connection
	
	def findAll():
		c = self.connection.cursor()	
		return c.execute("SELECT * FROM REQUESTS")

	def countAll():
		c = self.connection.cursor()
		return int(c.execute("SELECT count(*) FROM REQUESTS").fetchone()[0]);
		

class Request():
	def __init__(self,args):
		self.date = args[0]
		self.domain = args[1]
		self.ip = args[2]
		self.host = args[3]
	
		

class EditFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))

		filemenu = wx.Menu()
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Info")
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Close program")	
		panel = wx.Panel(self)		
		connection = sqlite3.connect('scanner.db')	
		requestDao = RequestDao(connection)
	
		allRequestsFetched = []
		for req in connection.cursor().execute("SELECT * FROM REQUESTS"): 
			allRequestsFetched.append(Request(req))
			
		grid = gridlib.Grid(panel)
		grid.CreateGrid(len(allRequestsFetched),8)
		grid.SetCellValue(0,0,"Lol");
		grid.SetCellBackgroundColour(0,0,wx.GREEN)		
		grid.SetCellBackgroundColour(1,1,wx.Colour(250,180,30))
		i = 0
		for req in allRequestsFetched:
			grid.SetCellValue(i,0,req.domain)
			grid.SetCellBackgroundColour(i,0,wx.GREEN)
			grid.SetCellValue(i,1,req.ip)		
			grid.SetCellBackgroundColour(i,1,wx.Color(250,180.30))
			i+=1
				
		
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





