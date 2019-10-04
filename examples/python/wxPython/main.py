#!/usr/bin/env python3

import wx
import tgui #my wxPython gui
import urllib3
import xml.etree.ElementTree as ET

# Implementing MainFrame
class pdoProxyMainFrame( tgui.MainFrame ):

	def __init__( self, parent ):
		tgui.MainFrame.__init__( self, parent )
		self.txtSql.SetValue("select * from contacts")

	def Warn(parent, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()


	def runClicked(self,e):
		print("Clicked")
		self.grid.ClearGrid()
		if self.grid.GetNumberRows()>0: self.grid.DeleteRows(0, self.grid.GetNumberRows())
		if self.grid.GetNumberCols()>0: self.grid.DeleteCols(0,self.grid.GetNumberCols())

		self.runSql()

	def runSql(self):
		sql=self.txtSql.GetValue()
		#Download xml
		http = urllib3.PoolManager()
		r = http.request(
		     'POST',
		     'http://localhost:8080/read.php',
		     fields={
		            'user': 'fabio',
		            'pass': 'secret',
		            'sql' : sql
		     })
		if (r.status==200):
		    xml=r.data
		else:
			print("Error on connection...")
			self.Warn("Error on connection", 'Warning!')
			return

		#Parse xml
		root = ET.fromstring(xml)


		#Check for error
		if root.tag=="error":
			self.Warn(root.text, 'Warning!')
			return

		#print column names
		ncol=0
		for fields in root.iter('field'):
			self.grid.AppendCols(1)
			self.grid.SetColLabelValue(ncol,fields.attrib['name'])
			ncol+= 1

		#print row content
		currCell=0
		currRow=0
		if(self.grid.GetNumberRows()==0):self.grid.AppendRows(1)
		for record in root.findall('./records/record/cell'):
			self.grid.SetCellValue(currRow,currCell, record.text)
			currCell+=1
			if (currCell==ncol):
				self.grid.AppendRows(1)
				currCell=0
				currRow+=1

		#delete last row (always blank)
		self.grid.DeleteRows(self.grid.GetNumberRows()-1,1)





if __name__ == '__main__' :

	app = wx.App()
	window = pdoProxyMainFrame(None)
	window.Show(True)
	app.MainLoop()
