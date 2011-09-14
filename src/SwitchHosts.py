# -*- coding: utf-8 -*-

u"""
本程序用于快速切换 hosts 文件

@author: oldj
@blog: http://oldj.net
@email: oldj.wu@gmail.com
@version: 0.1.1.100
"""

import os
import sys
import glob
import traceback
import wx

VERSION = "0.1.1"


def GetMondrianData():
    return "\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\
\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04gAMA\x00\x00\xaf\xc87\
\x05\x8a\xe9\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\
\x02=IDAT8\xcb\xa5\x93AK\xd4a\x10\xc6\x7f\xbb\xad\x1ad\x07MIwK\xad\xccMK\xcd\
\x83i\x14\x15D\x10\x94\x1ax0\xc2C\xa7\xbe@t\xc8Kt\xab/\xd0)*\xea\xe45\x12B\x02\
\xd3J-5w\xcd r\xb5\xd2M7SV$\xd4\xff\xff\x9dy\xdf\x0eF(E`>0\x97\xe1a`\xe67O\xc09\
\xc7f\x14\xdc\x88\xf9\xe2\xa3\xa6\xa7\xcd\xf7\xcee\xfe\xd7\x80\x96\x87\x8d\xf5\
\xbeoN\x1a\xcf\xbc[\xdb\x0f\\\xe9\xb8\xf4{\x07\xab\x16\xab\x16\x15\xdbg\xd5\xb6\
\x11\x0c^\x10#g\xc5Ht[f6\x91\xdc\x08s\x0bs$&\xc7c\xcf\xae\xbd\xa8\x01\x08\x01\
\xb4V]\xc6\xe1p\xcea\x9dcl\xf6\xe3\xd1\xf7\xc9\xd1.\xb1B\xb4\xf8\x00[3\xb3\x10\
\xb5\xa8S\xf2r\xf2X^^9|\xecF\xed\xcbW7\x07\x8e\x07\x9dsX\x1c\xd6\xd9_\xa5\xec\
\xc9\xdbKmI-\xe9\x854\x19\xa1\x0c\x8c\x08\xc6\x1a\x8c\x1a\x8c\n\xc6\x08\xc67\x19\
\x00!+\x96\x07o\xee\xa2\xa2\x04\xed\x16\xf6\xe7\x97q0r\x88\x9c\xed;\x08\xb9\x0c\
\xc6\x93\x13\xa4\xe6g\x98N\xcd\x10\xde\x19AEHL\x8c\x8f\x0c\xdc\x8a\xd7\x01\x04\
\xd6bl\xb9\xdf\x90-F\xaf\x97\x87+\xda\x8eD\xeb\x88%\x86\xe9\x89\xf5\xa8:\xdb\xd4\
\xd5\xd6\xdbQw\xb5F5d?\r\xde\x8e\x97\xfe\x95\x82\x0b\x82\r8\xe2c1\x96\xbc%\xa2E\
\xe5\xf8?\x0c^\xda\x03\xc0_\xf2\xf1\xe6\xbcut\x02\xad\xed\xcdN\x8c Fp\xe2(\xc8-d1\
\xbdHY8\xca\xbe\xa2R&\xa6\xc6\x19\x1e\x8d\x93H$8\x18\xad@\xc42484\x92h\xff\\\r\x102\
\xbe\xe1D\xf9)\xd4)j\x05\xb1\xca\\\xd6<\xf1\x0fq\x8aw\x95\x10.\x88PX\x10\xc1\x9e\xb6\
\xa8U,\x16o\xc5\xab\xda}>\xfcz\xea\xc9t]\xd0\xf8\xeb/,*,.-\x92\xfa\xfe\x8d\xe7\xbd\xdd\
\xcc\xa7\xe7\x11'\x88\x15\xc4)b\x15\x11E\x8c\x1a\x80@\xc3\x9d3N\x8c`|A\xfcUDb\xa4O<m\xf3\
\xd3\xfe\xea#\xf9\x1a\xcd\xcf\xcf\xa7\xb2\xba\x92\xe4\x97$C\xfdoc3\x9d\xb35\x7fP\xf8\x97\
\x8a\x1a#\xf5*\xda\xa5b'S\x9d\xb3\xd1\rga\xf2\xf1\xd7~5\xda\xadF+\xd7Q\xd8l\x9c\x7f\x02\
\x9f\xa4l\xb4#4\xd4~\x00\x00\x00\x00IEND\xaeB`\x82"


def GetMondrianBitmap():
    return wx.BitmapFromImage(GetMondrianImage())


def GetMondrianImage():
    import cStringIO

    stream = cStringIO.StringIO(GetMondrianData())
    return wx.ImageFromStream(stream)


def GetMondrianIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon


class TaskBarIcon(wx.TaskBarIcon):
    ID_About = wx.NewId()
    ID_Exit = wx.NewId()
    ID_MainFrame = wx.NewId()

    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        #        super(wx.TaskBarIcon, self).__init__()
        self.frame = frame
        self.SetIcon(GetMondrianIcon(), "Switch Hosts!")
        #        self.SetIcon(wx.Icon(name="arrow_switch.png", type=wx.BITMAP_TYPE_PNG), "Switch Hosts!")
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.ID_About)
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_Exit)
        self.Bind(wx.EVT_MENU, self.OnMainFrame, id=self.ID_MainFrame)

        self.current_hosts = None


    def notify(self, msg=None, title=None):
        import libs.ToasterBox as TB

        sw, sh = wx.GetDisplaySize()
        width, height = 210, 50
        px = sw - 230
        py = sh - 100

        tb = TB.ToasterBox(self.frame)
        tb.SetPopupText(msg)
        tb.SetPopupSize((width, height))
        tb.SetPopupPosition((px, py))
        tb.Play()


    def OnTaskBarLeftDClick(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    #        self.OnAbout(event)


    def OnExit(self, event):
        self.frame.Destroy()
        self.Destroy()
        sys.exit()


    def OnAbout(self, event):
    #        wx.MessageBox(u"快速切换 hosts 文件！\n\nVERSION: %s" % VERSION, u"About")
        msg = u"Switch Hosts!\n\n" +\
              u"本程序用于在多个 hosts 配置之间快速切换。\n\n" +\
              u"by oldj, oldj.wu@gmail.com\n" +\
              u"https://github.com/oldj/SwitchHosts\n" +\
              u"VERSION: %s" % VERSION

        dlg = wx.MessageDialog(self.frame, msg, "About", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


    def OnMainFrame(self, event):
        u"""显示主面板"""
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    # override
    def CreatePopupMenu(self):
        self.hosts = {}

        hosts_list = listLocalHosts()
        menu = wx.Menu()
        menu.Append(self.ID_MainFrame, u"Switch Hosts!")
        menu.AppendSeparator()

        if not self.current_hosts:
            menu.AppendRadioItem(wx.ID_ANY, u"系统默认")
        for fn in hosts_list:
            self.addHosts(menu, fn)

        menu.AppendSeparator()
        menu.Append(self.ID_About, "About")
        menu.Append(self.ID_Exit, "Exit")
        return menu


    def addHosts(self, menu, fn):
        u"""在菜单项中添加一个 hosts"""

        folder, fn2 = os.path.split(fn)
        hosts_id = wx.NewId()
        menu.AppendRadioItem(hosts_id, fn2)
        menu.Check(hosts_id, self.current_hosts == fn)
        self.hosts[hosts_id] = fn

        self.Bind(wx.EVT_MENU, self.switchHost, id=hosts_id)


    def switchHost(self, event):
        hosts_id = event.GetId()
        fn = self.hosts[hosts_id]
        #        print(dir(event))
        if not os.path.isfile(fn):
            wx.MessageBox(u"hosts 文件 '%s' 不存在！" % fn, "Error!")

        sys_hosts_fn = getSysHostsPath()
        try:
            open(sys_hosts_fn, "wb").write(open(fn, "rb").read())
            self.current_hosts = fn
            title = os.path.split(fn)[1]
            self.SetIcon(GetMondrianIcon(), "Hosts: %s" % title)
            #            wx.NotificationMessage(
            #                u"Hosts切换成功！",
            #                u"hosts 已切换为 %s" % title,
            #                self.frame).Show()
            self.notify(u"Hosts 已切换为 %s。" % title)

        except Exception:
            print(traceback.format_exc())
            wx.MessageBox(u"hosts 未能成功切换！", "Error!")

#            wx.NotificationMessage(
#                u"Hosts切换失败！",
#                u"hosts 未能成功切换！",
#                self.frame).Show()
#            self.notify(u"hosts 未能成功切换！")


class Frame(wx.Frame):

    ID_RENAME = wx.NewId()

    def __init__(
        self, parent=None, id=wx.ID_ANY, title="Switch Host!", pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
    ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self.SetIcon(GetMondrianIcon())
        self.taskbar_icon = TaskBarIcon(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem_exit = wx.MenuItem(self.m_menu1, wx.ID_EXIT, u"退出(&X)", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem_exit)

        self.m_menubar1.Append(self.m_menu1, u"文件(&F)")

        self.m_menu2 = wx.Menu()
        self.m_menuItem_about = wx.MenuItem(self.m_menu2, wx.ID_ABOUT, u"关于(&A)", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.AppendItem(self.m_menuItem_about)

        self.m_menubar1.Append(self.m_menu2, u"帮助(&H)")

        self.SetMenuBar(self.m_menubar1)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_list = wx.ListCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(160, 320),
                                       wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        bSizer5.Add(self.m_list, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE)
        bSizer6.Add(self.m_textCtrl1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel3 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_btn_apply = wx.Button(self.m_panel1, wx.ID_APPLY, u"应用", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_btn_apply, 0, wx.ALL, 5)

        self.m_btn_exit = wx.Button(self.m_panel1, wx.ID_CLOSE, u"关闭", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_btn_exit, 0, wx.ALL, 5)

        bSizer6.Add(bSizer7, 0, wx.EXPAND, 5)

        bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer4)
        self.m_panel1.Layout()
        bSizer4.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.init2()


    def init2(self):
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.taskbar_icon.OnAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_BUTTON, self.OnHide, id=wx.ID_CLOSE)

        hosts_cols = (
            (u"", wx.LIST_AUTOSIZE),
            (u"hosts", 120),
            )
        for col, (txt, width) in enumerate(hosts_cols):
            self.m_list.InsertColumn(col, txt)
            self.m_list.SetColumnWidth(col, width)
        self.updateHostsList()

        self.hosts_item_menu = wx.Menu()
        self.hosts_item_menu.Append(wx.ID_APPLY, u"切换到当前hosts")
        self.hosts_item_menu.Append(wx.ID_EDIT, u"编辑")
        self.hosts_item_menu.Append(self.ID_RENAME, u"重命名")
        self.hosts_item_menu.AppendSeparator()
        self.hosts_item_menu.Append(wx.ID_DELETE, u"删除")



    def updateHostsList(self):
        u"""更新 hosts 列表"""

        self.hosts_list_indexes = []
        hosts_list = listLocalHosts()
        hosts_list = [os.path.split(fn) for fn in hosts_list]

        for idx, (folder, fn) in enumerate(hosts_list):
            index = self.m_list.InsertStringItem(sys.maxint, "")
            self.m_list.SetStringItem(index, 1, fn)
            self.m_list.SetStringItem(index, 2, folder)
            self.hosts_list_indexes.append(index)

        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnHostsItemRClick, self.m_list)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnHostsItemBeSelected, self.m_list)


    def OnHostsItemBeSelected(self, event):
        
        print dir(event.GetItem())


    def OnHostsItemRClick(self, event):
        u""""""

        #        print dir(event)
        self.m_list.PopupMenu(self.hosts_item_menu, event.GetPosition())


    def editHost(self, event):
        u"""编辑一个 hosts 文件"""

        print(1)


    def OnHide(self, event):
        self.Hide()


    def OnIconfiy(self, event):
        wx.MessageBox("Frame has been iconized!", "Prompt")
        event.Skip()

    def OnExit(self, event):
    #        self.taskbar_icon.Destroy()
    #        self.Destroy()
    #        event.Skip()
        self.taskbar_icon.OnExit(event)

    def OnClose(self, event):
        self.Hide()
        return False


def getSysHostsPath():
    u"""取得系统 host 文件的路径"""

    if os.name == "nt":
        path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    else:
        path = "/etc/hosts"

    return path if os.path.isfile(path) else None


def listLocalHosts():
    u"""列出指定目录下的 host 文件列表"""

    global g_local_hosts_dir

    fns = [fn for fn in glob.glob(os.path.join(g_local_hosts_dir, "*")) if\
           os.path.isfile(fn) and not fn.startswith(".")\
           and not fn.startswith("_")
    ]

    return fns


def init():
    global g_local_hosts_dir

    base_dir = os.getcwd()
    g_local_hosts_dir = os.path.join(base_dir, "hosts")
    if not os.path.isdir(g_local_hosts_dir):
        os.makedirs(g_local_hosts_dir)


def main():
    init()
    app = wx.PySimpleApp()
    frame = Frame(size=(640, 480))
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()


