#!/usr/bin/env python2

import ROOT as rt
from array import *

#from smsPlotABS
def setStyle():
    # canvas style
    rt.gStyle.SetOptStat(0)
    rt.gStyle.SetOptTitle(0)

# from smsPlotXSec.py
def setStyleCOLZ():
    # define the palette for z axis
    NRGBs = 5
    NCont = 255
    stops = array("d",[0.00, 0.34, 0.61, 0.84, 1.00])
    red= array("d",[0.50, 0.50, 1.00, 1.00, 1.00])
    green = array("d",[ 0.50, 1.00, 1.00, 0.60, 0.50])
    blue = array("d",[1.00, 1.00, 0.50, 0.40, 0.50])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
    rt.gStyle.SetNumberContours(NCont)

def post_process(scan):
    fname=scan+"XSEC"
    f=rt.TFile(fname+".root","r")
    c=f.Get("cCONT_XSEC")
    f.Close()
    c.Draw()
    c.cd()

    if scan=="GGM":
        ax,ay=.18,.32
        ex,ey=.31,.15
    elif scan=="T5gg":
        ax,ay=.54,.25
        ex,ey=.20,.36
    elif scan=="T5Wg":
        ax,ay=.31,.16
        ex,ey=.28,.44
    l=rt.TLatex()
    l.SetNDC(True)
    l.SetTextSize(.04)
    l.SetTextFont(52)
    l.SetTextAngle(45)
    l.DrawLatex(ex,ey,"excluded")
    l.DrawLatex(ax,ay,"allowed")
    # raw_input("...")
    c.SaveAs(fname+".pdf")

if __name__=="__main__":
    setStyle()
    setStyleCOLZ()
    post_process("GGM")
    post_process("T5gg")
    post_process("T5Wg")
