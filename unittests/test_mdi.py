import imp_unittest, unittest
import wtc
import wx

#---------------------------------------------------------------------------

class mdi_Tests(wtc.WidgetTestCase):

    def test_mdiParentFrame1(self):
        f = wx.MDIParentFrame(None, title="MDI Parent")
        f.Close()
        
    def test_mdiParentFrame2(self):
        f = wx.MDIParentFrame()
        f.Create(None, title="MDI Parent")
        f.Close()

    def test_mdiClientWindow(self):
        f = wx.MDIParentFrame(None, title="MDI Parent")
        cw = f.GetClientWindow()
        self.assertTrue(isinstance(cw, wx.MDIClientWindow))
        f.Close()
        
        
    def test_mdiChildFrame1(self):
        f = wx.MDIParentFrame(None, title="MDI Parent")
        c = wx.MDIChildFrame(f, title="MDI Child")
        f.Close()
        
    def test_mdiChildFrame2(self):
        f = wx.MDIParentFrame(None, title="MDI Parent")
        c = wx.MDIChildFrame()
        c.Create(f, title="MDI Child")
        f.Close()


#---------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()